"""
ContaEC - Endpoints de Empresas
CRUD de empresas, establecimientos, auto-completado RUC desde SRI
"""
import logging
import os
import uuid
from uuid import UUID
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.company import Company, Establishment
from app.models.client import Client, TipoIdentificacion
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate,
    EstablishmentCreate,
    EstablishmentResponse,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/companies", tags=["Empresas"])


# _ensure_consumidor_final movido a app.core.utils para evitar duplicación
from app.core.utils import ensure_consumidor_final


@router.post("", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
async def create_company(
    company_data: CompanyCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Crear una nueva empresa para el usuario actual"""
    # Verificar que el RUC no exista ya para este usuario
    result = await db.execute(
        select(Company).where(
            Company.user_id == current_user.id,
            Company.ruc == company_data.ruc
        )
    )
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya tiene una empresa registrada con este RUC."
        )

    company = Company(
        user_id=current_user.id,
        **company_data.model_dump(),
    )
    db.add(company)
    await db.flush()

    # Crear cliente Consumidor Final por defecto
    await ensure_consumidor_final(db, str(company.id))

    logger.info(f"Nueva empresa creada: {company.ruc} - {company.razon_social}")
    return CompanyResponse.model_validate(company)


@router.get("", response_model=list[CompanyResponse])
async def list_companies(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar todas las empresas del usuario actual"""
    result = await db.execute(
        select(Company).where(Company.user_id == current_user.id)
    )
    companies = result.scalars().all()
    return [CompanyResponse.model_validate(c) for c in companies]


@router.get("/{company_id}", response_model=CompanyResponse)
async def get_company(
    company_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Obtener detalles de una empresa específica"""
    result = await db.execute(
        select(Company).where(
            Company.id == company_id,
            Company.user_id == current_user.id,
        )
    )
    company = result.scalars().first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return CompanyResponse.model_validate(company)


@router.put("/{company_id}", response_model=CompanyResponse)
async def update_company(
    company_id: UUID,
    company_data: CompanyUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Actualizar datos de una empresa"""
    result = await db.execute(
        select(Company).where(
            Company.id == company_id,
            Company.user_id == current_user.id,
        )
    )
    company = result.scalars().first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    update_data = company_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(company, field, value)

    await db.flush()
    return CompanyResponse.model_validate(company)


@router.delete("/{company_id}")
async def delete_company(
    company_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Desactivar una empresa (eliminación lógica)"""
    result = await db.execute(
        select(Company).where(
            Company.id == company_id,
            Company.user_id == current_user.id,
        )
    )
    company = result.scalars().first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    company.is_active = False
    await db.flush()
    return {"message": "Empresa desactivada exitosamente."}


@router.get("/ruc/{ruc}", response_model=dict)
async def lookup_ruc(
    ruc: str,
    current_user: User = Depends(get_current_user),
):
    """
    Consultar datos de una empresa por RUC desde el SRI.
    Auto-completa los campos de la empresa basado en la información del SRI.
    """
    from app.core.config import get_settings
    settings = get_settings()

    # Validar formato de RUC (13 dígitos)
    if not ruc.isdigit() or len(ruc) != 13:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="RUC inválido. Debe tener 13 dígitos numéricos."
        )

    # Modo sandbox: retornar datos simulados (solo desarrollo)
    if settings.SRI_RUC_SANDBOX and settings.is_development:
        logger.info(f"Sandbox mode: returning mock data for RUC {ruc}")
        return {
            "ruc": ruc,
            "razon_social": f"EMPRESA DE PRUEBA {ruc[-4:]} C.A.",
            "nombre_comercial": f"Comercial {ruc[-4:]}",
            "dir_matriz": "AV. PRINCIPAL 123 Y CALLE SECUNDARIA",
            "obligado_contabilidad": "SI",
            "contribuyente_especial": "",
            "agente_retencion": "",
            "contribuyente_rimpe": "REGIMEN RIMPE",
            "message": "Datos de prueba (sandbox). Verifique con el SRI.",
        }

    try:
        # Intentar consultar el SRI con reintentos
        import httpx
        last_error = None
        for attempt in range(3):
            try:
                timeout = httpx.Timeout(connect=10.0, read=20.0, total=30.0)
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.get(
                        f"https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsultaRuc/obtenerDatosRuc",
                        params={"ruc": ruc},
                        headers={"User-Agent": "ContaEC/4.0"},
                    )
                    if response.status_code == 200:
                        data = response.json()
                        if data.get("razonSocial"):
                            return {
                                "ruc": ruc,
                                "razon_social": data.get("razonSocial", ""),
                                "nombre_comercial": data.get("nombreComercial", ""),
                                "dir_matriz": data.get("dirMatriz", ""),
                                "obligado_contabilidad": data.get("obligadoContabilidad", "NO"),
                                "contribuyente_especial": data.get("contribuyenteEspecial", ""),
                                "agente_retencion": data.get("agenteRetencion", ""),
                                "contribuyente_rimpe": data.get("contribuyenteRimpe", ""),
                            }
                        else:
                            logger.warning(f"SRI no encontro datos para RUC {ruc}: {data}")
                            return {
                                "ruc": ruc,
                                "message": "RUC no encontrado en el SRI. Verifique el numero e intente nuevamente.",
                                "razon_social": "",
                                "nombre_comercial": "",
                                "dir_matriz": "",
                            }
                    else:
                        logger.warning(f"SRI respondio con status {response.status_code} para RUC {ruc}")
                        last_error = f"El SRI respondio con status {response.status_code}"
                        break  # Non-200 status, don't retry
            except httpx.TimeoutException:
                last_error = "El servicio del SRI no responde (timeout)"
                logger.warning(f"SRI timeout en intento {attempt+1} para RUC {ruc}")
                if attempt < 2:
                    import asyncio
                    await asyncio.sleep(2)
                continue
            except httpx.ConnectError:
                last_error = "No se puede conectar con el servicio del SRI"
                logger.warning(f"SRI connection error en intento {attempt+1} para RUC {ruc}")
                if attempt < 2:
                    import asyncio
                    await asyncio.sleep(2)
                continue

        logger.warning(f"Error consultando RUC {ruc} en SRI despues de reintentos: {last_error}")
    except Exception as e:
        logger.warning(f"Error inesperado consultando RUC {ruc} en SRI: {e}")

    # Fallback: retornar datos basicos
    return {
        "ruc": ruc,
        "message": "El servicio del SRI no esta disponible en este momento. Complete los datos manualmente.",
        "razon_social": "",
        "nombre_comercial": "",
        "dir_matriz": "",
    }


# ==================== ESTABLECIMIENTOS ====================

@router.post("/{company_id}/establishments", response_model=EstablishmentResponse, status_code=status.HTTP_201_CREATED)
async def create_establishment(
    company_id: UUID,
    establishment_data: EstablishmentCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Crear un establecimiento para una empresa"""
    # Verificar que la empresa pertenece al usuario
    result = await db.execute(
        select(Company).where(
            Company.id == company_id,
            Company.user_id == current_user.id,
        )
    )
    if not result.scalars().first():
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    establishment = Establishment(
        company_id=company_id,
        **establishment_data.model_dump(),
    )
    db.add(establishment)
    await db.flush()

    return EstablishmentResponse.model_validate(establishment)


@router.get("/{company_id}/establishments", response_model=list[EstablishmentResponse])
async def list_establishments(
    company_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar establecimientos de una empresa"""
    result = await db.execute(
        select(Company).where(
            Company.id == company_id,
            Company.user_id == current_user.id,
        )
    )
    if not result.scalars().first():
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    result = await db.execute(
        select(Establishment).where(Establishment.company_id == company_id)
    )
    establishments = result.scalars().all()
    return [EstablishmentResponse.model_validate(e) for e in establishments]


# ==================== CLIENTES ====================

@router.get("/{company_id}/clients")
async def list_clients(
    company_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar clientes de una empresa"""
    # Verificar que la empresa pertenece al usuario
    result = await db.execute(
        select(Company).where(
            Company.id == company_id,
            Company.user_id == current_user.id,
        )
    )
    if not result.scalars().first():
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    result = await db.execute(
        select(Client).where(Client.company_id == company_id)
    )
    clients = result.scalars().all()

    # Asegurar que exista Consumidor Final
    has_consumer = any(c.is_default_consumer for c in clients)
    if not has_consumer:
        consumer = await ensure_consumidor_final(db, str(company_id))
        clients = [consumer] + list(clients)

    return [
        {
            "id": str(c.id),
            "tipo_identificacion": c.tipo_identificacion,
            "identificacion": c.identificacion,
            "razon_social": c.razon_social,
            "direccion": c.direccion,
            "email": c.email,
            "telefono": c.telefono,
            "is_default_consumer": c.is_default_consumer,
            "is_active": c.is_active,
        }
        for c in clients
    ]


@router.post("/upload/{upload_type}")
async def upload_company_file(
    upload_type: str,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    """
    Subir archivos de empresa: logo o firma electronica.
    
    upload_type: "logo" o "firma"
    Retorna la ruta del archivo guardado.
    """
    if upload_type not in ("logo", "firma"):
        raise HTTPException(status_code=400, detail="Tipo de archivo invalido. Use 'logo' o 'firma'")

    settings = get_settings()
    upload_dir = Path(settings.upload_dir) / "companies"
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Validar extension
    filename = file.filename or ""
    if upload_type == "logo":
        if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
            raise HTTPException(status_code=400, detail="Solo se permiten imagenes (png, jpg, jpeg, gif, svg, webp)")
    else:  # firma
        if not filename.lower().endswith((".p12", ".pfx")):
            raise HTTPException(status_code=400, detail="Solo se permiten archivos .p12 o .pfx")

    # Generar nombre unico
    ext = Path(filename).suffix
    unique_name = f"{uuid.uuid4().hex}{ext}"
    file_path = upload_dir / unique_name

    content = await file.read()
    file_path.write_bytes(content)

    relative_path = f"/uploads/companies/{unique_name}"

    logger.info(f"Archivo {upload_type} subido por {current_user.email}: {relative_path}")

    return {
        "file_path": relative_path,
        "filename": filename,
        "upload_type": upload_type,
    }
