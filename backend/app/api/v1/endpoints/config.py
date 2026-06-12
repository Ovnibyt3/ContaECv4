"""
ContaEC - Endpoints de Configuración de Usuario
Firma electrónica, SMTP, modo sandbox/producción, VirusTotal, perfil
"""
import os
import logging
import asyncio
import aiofiles
from datetime import datetime, timezone
from uuid import UUID
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user
from app.core.encryption import encrypt_field, decrypt_field
from app.core.config import get_settings
from app.core.scanner import scan_upload, is_any_threat_found
from app.models.user import User, UserConfig

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/config", tags=["Configuración"])
settings = get_settings()


@router.get("/user-config")
async def get_user_config(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Obtener la configuración completa del usuario actual"""
    result = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    config = result.scalars().first()

    if not config:
        # Crear configuración por defecto
        config = UserConfig(user_id=current_user.id, environment_mode="sandbox")
        db.add(config)
        await db.flush()

    # Estado de la firma electrónica
    signature_status = "none"
    signature_days_left = None
    if config.digital_signature_path:
        if config.signature_expiry_date:
            if config.signature_expiry_date > datetime.now(timezone.utc):
                signature_status = "valid"
                signature_days_left = (config.signature_expiry_date - datetime.now(timezone.utc)).days
            else:
                signature_status = "expired"
        else:
            signature_status = "uploaded"  # Sin info de expiración

    return {
        "id": str(config.id),
        "user_id": str(config.user_id),
        "environment_mode": config.environment_mode,
        "virustotal_enabled": config.virustotal_enabled,
        # Firma digital
        "has_digital_signature": bool(config.digital_signature_path),
        "signature_status": signature_status,
        "signature_expiry_date": config.signature_expiry_date.isoformat() if config.signature_expiry_date else None,
        "signature_days_left": signature_days_left,
        # SMTP
        "has_smtp_config": bool(config.smtp_host),
        "smtp_host": config.smtp_host,
        "smtp_port": config.smtp_port,
        "smtp_user": config.smtp_user,
        "smtp_ssl": config.smtp_ssl,
        "smtp_protocol": config.smtp_protocol,
        # Logo
        "company_logo_path": config.company_logo_path,
        # Perfil
        "user": {
            "id": str(current_user.id),
            "email": current_user.email,
            "full_name": current_user.full_name,
            "phone": current_user.phone,
            "language": current_user.language,
            "theme": current_user.theme,
            "license_type": current_user.license_type,
            "license_start_date": current_user.license_start_date.isoformat() if current_user.license_start_date else None,
            "license_end_date": current_user.license_end_date.isoformat() if current_user.license_end_date else None,
        },
        # Escáneres
        "clamav_available": settings.CLAMAV_ENABLED,
        "virustotal_available": settings.VIRUSTOTAL_ENABLED and bool(settings.VIRUSTOTAL_API_KEY),
    }


@router.post("/digital-signature")
async def upload_digital_signature(
    file: UploadFile = File(...),
    password: str = "",
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Subir firma electrónica (.p12/.pfx) y su clave.
    
    Proceso:
    1. Escaneo de malware
    2. Validación del certificado PKCS#12
    3. Extracción de fecha de expiración
    4. Almacenamiento encriptado
    """
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo debe tener un nombre.",
        )

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in (".p12", ".pfx"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo de firma electrónica debe ser formato .p12 o .pfx"
        )

    content = await file.read()

    # Verificar tamaño (máximo 5MB)
    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo no debe exceder 5MB."
        )

    # Escaneo de malware
    scan_results = await scan_upload(content=content, filename=file.filename)
    if is_any_threat_found(scan_results):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Archivo rechazado: se detectó malware en la firma electrónica.",
        )

    # Guardar archivo en ubicación segura (fuera del directorio público de uploads)
    upload_dir = os.path.join(settings.SIGNATURES_DIR, str(current_user.id))
    os.makedirs(upload_dir, exist_ok=True)

    # Eliminar firma anterior si existe
    result_config = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    old_config = result_config.scalars().first()

    file_path = os.path.join(upload_dir, f"firma_{datetime.now().strftime('%Y%m%d%H%M%S')}.p12")

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(content)

    # Validar certificado y extraer información
    expiry_date = None
    cert_info = {}
    warnings = []

    try:
        from cryptography.hazmat.primitives.serialization import pkcs12

        private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
            content, password.encode()
        )

        if certificate:
            expiry_date = certificate.not_valid_after_utc
            not_before = certificate.not_valid_before_utc
            now = datetime.now(timezone.utc)

            is_valid = not_before <= now <= expiry_date
            days_left = (expiry_date - now).days if expiry_date else None

            # Extraer nombre del sujeto
            subject_cn = ""
            issuer_cn = ""
            for attr in certificate.subject:
                if attr.oid.dotted_string == "2.5.4.3":
                    subject_cn = attr.value
            for attr in certificate.issuer:
                if attr.oid.dotted_string == "2.5.4.3":
                    issuer_cn = attr.value

            known_ec_ca = ["BANCO CENTRAL DEL ECUADOR", "SECURITY DATA", "ANF"]
            is_ec = any(ca in issuer_cn.upper() for ca in known_ec_ca)

            cert_info = {
                "subject_cn": subject_cn,
                "issuer_cn": issuer_cn,
                "is_ec_signature": is_ec,
                "not_before": not_before.isoformat(),
                "not_after": expiry_date.isoformat(),
                "days_until_expiry": days_left,
                "has_private_key": private_key is not None,
            }

            if not is_valid and now > expiry_date:
                warnings.append("La firma electrónica ha EXPIRADO. No podrá firmar comprobantes.")
            elif days_left is not None and days_left <= 30:
                warnings.append(f"La firma electrónica expirará en {days_left} días.")

            if not is_ec:
                warnings.append("El certificado no parece ser de una CA ecuatoriana (BCE, Security Data, ANF).")

            if private_key is None:
                warnings.append("No se encontró clave privada. No se podrá firmar comprobantes.")

    except ValueError as e:
        if "password" in str(e).lower() or "mac" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Contraseña incorrecta para la firma electrónica.",
            )
        logger.warning(f"Error leyendo certificado: {e}")
    except Exception as e:
        logger.warning(f"No se pudo leer el certificado: {e}")

    # Guardar configuración encriptada
    if not old_config:
        old_config = UserConfig(user_id=current_user.id)
        db.add(old_config)

    old_config.digital_signature_path = encrypt_field(file_path, settings.ENCRYPTION_KEY)
    old_config.digital_signature_password = encrypt_field(password, settings.ENCRYPTION_KEY)
    old_config.signature_expiry_date = expiry_date

    await db.flush()

    return {
        "message": "Firma electrónica cargada exitosamente.",
        "expiry_date": expiry_date.isoformat() if expiry_date else None,
        "is_valid": expiry_date > datetime.now(timezone.utc) if expiry_date else None,
        "days_until_expiry": cert_info.get("days_until_expiry"),
        "cert_info": cert_info,
        "warnings": warnings,
    }


@router.get("/signature-status")
async def get_signature_status(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Obtener el estado de la firma electrónica del usuario.
    Verifica vigencia y devuelve información detallada.
    """
    result = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    config = result.scalars().first()

    if not config or not config.digital_signature_path:
        return {
            "has_signature": False,
            "status": "none",
            "message": "No se ha cargado una firma electrónica.",
        }

    now = datetime.now(timezone.utc)
    status_str = "uploaded"  # Sin info de expiración

    if config.signature_expiry_date:
        if config.signature_expiry_date > now:
            days_left = (config.signature_expiry_date - now).days
            if days_left <= 30:
                status_str = "expiring_soon"
            else:
                status_str = "valid"
        else:
            status_str = "expired"

    return {
        "has_signature": True,
        "status": status_str,
        "expiry_date": config.signature_expiry_date.isoformat() if config.signature_expiry_date else None,
        "days_until_expiry": (config.signature_expiry_date - now).days if config.signature_expiry_date and config.signature_expiry_date > now else None,
        "is_valid": config.signature_expiry_date > now if config.signature_expiry_date else None,
        "warnings": _get_status_warnings(status_str, config.signature_expiry_date),
    }


def _get_status_warnings(status_str: str, expiry_date) -> list[str]:
    """Genera advertencias basadas en el estado de la firma"""
    warnings = []
    now = datetime.now(timezone.utc)

    if status_str == "expired":
        warnings.append("Su firma electrónica ha EXPIRADO. No puede firmar comprobantes electrónicos.")
    elif status_str == "expiring_soon":
        days = (expiry_date - now).days if expiry_date else 0
        warnings.append(f"Su firma electrónica expirará en {days} días. Renueve a tiempo.")
    elif status_str == "uploaded":
        warnings.append("No se pudo verificar la vigencia de la firma. Verifique manualmente.")

    return warnings


@router.put("/virustotal")
async def toggle_virustotal(
    enabled: bool,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Activar o desactivar VirusTotal para el escaneo de archivos del usuario"""
    if enabled and (not settings.VIRUSTOTAL_ENABLED or not settings.VIRUSTOTAL_API_KEY):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="VirusTotal no está configurado en el servidor. Contacte al administrador.",
        )

    result = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    config = result.scalars().first()
    if not config:
        config = UserConfig(user_id=current_user.id)
        db.add(config)

    config.virustotal_enabled = enabled
    await db.flush()

    return {
        "message": f"VirusTotal {'activado' if enabled else 'desactivado'} exitosamente.",
        "virustotal_enabled": enabled,
    }


class SMTPConfigRequest(BaseModel):
    """Esquema para configuración SMTP"""
    smtp_host: str
    smtp_port: int
    smtp_user: str
    smtp_password: str
    smtp_protocol: str = "SMTP"
    smtp_ssl: bool = True


@router.post("/smtp")
async def configure_smtp(
    data: SMTPConfigRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Configurar SMTP para envío de correos"""
    # Validar puerto
    if data.smtp_port < 1 or data.smtp_port > 65535:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Puerto SMTP inválido (1-65535).",
        )

    # Proveedores predefinidos
    smtp_providers = {
        "gmail": {"host": "smtp.gmail.com", "port": 465, "ssl": True},
        "zoho": {"host": "smtp.zoho.com", "port": 465, "ssl": True},
        "outlook": {"host": "smtp-mail.outlook.com", "port": 587, "ssl": False},
        "office365": {"host": "smtp.office365.com", "port": 587, "ssl": False},
    }

    # Auto-configurar si el host coincide con un proveedor conocido
    smtp_host = data.smtp_host
    smtp_port = data.smtp_port
    smtp_ssl = data.smtp_ssl
    host_lower = smtp_host.lower()
    for provider, config_data in smtp_providers.items():
        if provider in host_lower or host_lower in config_data["host"]:
            smtp_host = config_data["host"]
            smtp_port = config_data["port"]
            smtp_ssl = config_data["ssl"]
            break

    result = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    config = result.scalars().first()
    if not config:
        config = UserConfig(user_id=current_user.id)
        db.add(config)

    config.smtp_host = smtp_host
    config.smtp_port = smtp_port
    config.smtp_user = data.smtp_user
    config.smtp_password = encrypt_field(data.smtp_password, settings.ENCRYPTION_KEY)
    config.smtp_protocol = data.smtp_protocol
    config.smtp_ssl = smtp_ssl

    await db.flush()

    return {
        "message": "Configuración SMTP guardada exitosamente.",
        "smtp_host": smtp_host,
        "smtp_port": smtp_port,
        "smtp_user": data.smtp_user,
        "smtp_ssl": smtp_ssl,
    }


@router.post("/test-smtp")
async def test_smtp(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Probar la configuración SMTP enviando un correo de prueba"""
    result = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    config = result.scalars().first()

    if not config or not config.smtp_host:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No hay configuración SMTP. Configure primero el correo.",
        )

    try:
        import smtplib
        from email.mime.text import MIMEText

        smtp_password = decrypt_field(config.smtp_password, settings.ENCRYPTION_KEY)

        if config.smtp_ssl:
            server = smtplib.SMTP_SSL(config.smtp_host, config.smtp_port, timeout=10)
        else:
            server = smtplib.SMTP(config.smtp_host, config.smtp_port, timeout=10)
            server.starttls()

        server.login(config.smtp_user, smtp_password)

        msg = MIMEText("ContaEC - Prueba de configuración SMTP exitosa.\n\nSi recibió este correo, su configuración es correcta.", "plain")
        msg["Subject"] = "ContaEC - Prueba SMTP"
        msg["From"] = config.smtp_user
        msg["To"] = current_user.email

        server.sendmail(config.smtp_user, current_user.email, msg.as_string())
        server.quit()

        return {"message": "Correo de prueba enviado exitosamente."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al enviar correo de prueba: {str(e)}"
        )


@router.put("/environment-mode")
async def set_environment_mode(
    mode: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Cambiar modo de ambiente (sandbox/producción).
    
    En modo sandbox:
    - Los comprobantes se envían al SRI de pruebas
    - No tienen validez fiscal
    - Ideal para verificar configuración
    
    En modo producción:
    - Los comprobantes se envían al SRI de producción
    - Tienen validez fiscal
    - Requiere firma electrónica válida
    """
    if mode not in ("sandbox", "production"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Modo inválido. Use 'sandbox' o 'production'."
        )

    # Verificar requisitos para producción
    if mode == "production":
        result_config = await db.execute(
            select(UserConfig).where(UserConfig.user_id == current_user.id)
        )
        config = result_config.scalars().first()

        errors = []
        if not config or not config.digital_signature_path:
            errors.append("Se requiere una firma electrónica válida para operar en producción.")

        if config and config.signature_expiry_date and config.signature_expiry_date < datetime.now(timezone.utc):
            errors.append("Su firma electrónica ha expirado. Renuévela antes de cambiar a producción.")

        if errors:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "message": "No se puede cambiar a producción. Resuelva los siguientes requisitos:",
                    "errors": errors,
                },
            )

    result = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    config = result.scalars().first()
    if not config:
        config = UserConfig(user_id=current_user.id)
        db.add(config)

    config.environment_mode = mode
    await db.flush()

    return {
        "message": f"Modo cambiado a {'Producción' if mode == 'production' else 'Pruebas (Sandbox)'}.",
        "environment_mode": mode,
        "warning": "Los comprobantes emitidos en producción tienen validez fiscal." if mode == "production" else None,
    }


class ProfileUpdateRequest(BaseModel):
    """Esquema para actualización de perfil del usuario"""
    full_name: Optional[str] = None
    phone: Optional[str] = None
    language: Optional[str] = None
    theme: Optional[str] = None


@router.put("/profile")
async def update_profile(
    data: ProfileUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Actualizar datos del perfil del usuario"""
    if data.full_name is not None:
        if len(data.full_name) < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre debe tener al menos 2 caracteres.",
            )
        current_user.full_name = data.full_name

    if data.phone is not None:
        current_user.phone = data.phone

    if data.language is not None:
        if data.language not in ("es_EC", "en_US"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Idioma no soportado. Opciones: es_EC, en_US",
            )
        current_user.language = data.language

    if data.theme is not None:
        if data.theme not in ("light", "dark", "system"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tema no válido. Opciones: light, dark, system",
            )
        current_user.theme = data.theme

    await db.flush()

    return {
        "message": "Perfil actualizado exitosamente.",
        "user": {
            "id": str(current_user.id),
            "email": current_user.email,
            "full_name": current_user.full_name,
            "phone": current_user.phone,
            "language": current_user.language,
            "theme": current_user.theme,
        },
    }


class BackupKeyRequest(BaseModel):
    """Esquema para clave de encriptación de backups"""
    key: str


@router.post("/backup-key")
async def set_backup_encryption_key(
    data: BackupKeyRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Establecer la clave de encriptación de backups (se solicita una sola vez)"""
    if len(data.key) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La clave debe tener al menos 8 caracteres."
        )

    current_user.backup_encryption_key = encrypt_field(data.key, settings.ENCRYPTION_KEY)
    await db.flush()

    return {"message": "Clave de backup configurada exitosamente."}


@router.post("/company-logo")
async def upload_company_logo(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Subir logotipo de la empresa"""
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo debe ser una imagen."
        )

    content = await file.read()

    # Escaneo de malware
    scan_results = await scan_upload(content=content, filename=file.filename or "logo")
    if is_any_threat_found(scan_results):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Archivo rechazado: se detectó malware.",
        )

    upload_dir = os.path.join(settings.UPLOAD_DIR, str(current_user.id), "logos")
    os.makedirs(upload_dir, exist_ok=True)

    ext = os.path.splitext(file.filename or "logo.png")[1] if file.filename else ".png"
    file_path = os.path.join(upload_dir, f"logo_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}")

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(content)

    result = await db.execute(
        select(UserConfig).where(UserConfig.user_id == current_user.id)
    )
    config = result.scalars().first()
    if not config:
        config = UserConfig(user_id=current_user.id)
        db.add(config)

    config.company_logo_path = file_path
    await db.flush()

    return {"message": "Logotipo cargado exitosamente.", "logo_path": file_path}
