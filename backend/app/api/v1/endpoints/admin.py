"""
ContaEC - Endpoints de Administración
Dashboard, gestión de usuarios, licencias, seguridad
"""
import logging
import platform
import os
from datetime import datetime, timezone, timedelta
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user, get_current_active_admin, get_password_hash
from app.core.config import get_settings
from app.models.user import User, UserConfig, LicenseType
from app.models.company import Company
from app.models.client import Client
from app.schemas.auth import UserResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/admin", tags=["Administración"])

# Track application start time for uptime calculation
_startup_time = datetime.now(timezone.utc)


@router.get("/dashboard")
async def admin_dashboard(
    current_user: User = Depends(get_current_active_admin),
    db: AsyncSession = Depends(get_db),
):
    """Dashboard general del administrador con resumen completo del sistema"""
    # Total usuarios
    total_users = await db.scalar(select(func.count(User.id)))
    active_users = await db.scalar(select(func.count(User.id)).where(User.is_active == True))
    
    # Total empresas
    total_companies = await db.scalar(select(func.count(Company.id)))
    
    # Total clientes
    total_clients = await db.scalar(select(func.count(Client.id)))
    
    # Licencias por vencer (próximos 30 días)
    now = datetime.now(timezone.utc)
    thirty_days = now + timedelta(days=30)
    expiring_licenses = await db.scalar(
        select(func.count(User.id)).where(
            and_(
                User.license_end_date != None,
                User.license_end_date <= thirty_days,
                User.license_end_date >= now,
            )
        )
    )
    
    # Licencias expiradas
    expired_licenses = await db.scalar(
        select(func.count(User.id)).where(
            and_(
                User.license_end_date != None,
                User.license_end_date < now,
            )
        )
    )
    
    # Usuarios por tipo de licencia
    license_distribution = {}
    for lt in LicenseType:
        count = await db.scalar(
            select(func.count(User.id)).where(User.license_type == lt)
        )
        license_distribution[lt.value] = count
    
    return {
        "total_users": total_users,
        "active_users": active_users,
        "inactive_users": (total_users or 0) - (active_users or 0),
        "total_companies": total_companies,
        "total_clients": total_clients,
        "expiring_licenses": expiring_licenses,
        "expired_licenses": expired_licenses,
        "license_distribution": license_distribution,
    }


@router.get("/system-health")
async def system_health(
    current_user: User = Depends(get_current_active_admin),
    db: AsyncSession = Depends(get_db),
):
    """Dashboard detallado de salud del sistema"""
    settings = get_settings()

    # System information with psutil
    try:
        import psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        # Cross-platform disk usage
        disk = psutil.disk_usage('/')
        system_info = {
            "cpu_percent": cpu_percent,
            "memory_total_mb": round(memory.total / (1024 * 1024), 2),
            "memory_used_mb": round(memory.used / (1024 * 1024), 2),
            "memory_percent": memory.percent,
            "disk_total_gb": round(disk.total / (1024 ** 3), 2),
            "disk_used_gb": round(disk.used / (1024 ** 3), 2),
            "disk_percent": disk.percent,
        }
    except ImportError:
        # Fallback without psutil - use basic OS commands
        system_info = {
            "cpu_percent": "N/A (instalar psutil)",
            "memory_percent": "N/A (instalar psutil)",
            "disk_percent": "N/A (instalar psutil)",
        }

    # Database stats
    total_users = await db.scalar(select(func.count(User.id)))
    total_companies = await db.scalar(select(func.count(Company.id)))
    total_clients = await db.scalar(select(func.count(Client.id)))

    # Calculate uptime
    now = datetime.now(timezone.utc)
    uptime_delta = now - _startup_time
    uptime_seconds = int(uptime_delta.total_seconds())
    if uptime_seconds < 3600:
        uptime_str = f"{uptime_seconds // 60} min"
    elif uptime_seconds < 86400:
        uptime_str = f"{uptime_seconds // 3600}h {uptime_seconds % 3600 // 60}m"
    else:
        uptime_str = f"{uptime_seconds // 86400}d {uptime_seconds % 86400 // 3600}h"

    return {
        "system": system_info,
        "database": {
            "total_users": total_users,
            "total_companies": total_companies,
            "total_clients": total_clients,
        },
        "application": {
            "name": "ContaEC",
            "version": settings.APP_VERSION,
            "environment": settings.APP_ENV,
            "uptime": uptime_str,
            "python_version": platform.python_version(),
            "system": platform.system(),
        },
        "environment_toggle_available": True,
    }


@router.post("/environment/toggle")
async def toggle_environment(
    current_user: User = Depends(get_current_active_admin),
):
    """
    Cambiar entre ambiente de desarrollo y producción.
    Nota: Esto solo cambia la variable APP_ENV en memoria.
    Para un cambio permanente, se debe actualizar el archivo .env.
    """
    settings = get_settings()
    current_env = settings.APP_ENV

    if current_env.lower() == "production":
        new_env = "development"
    else:
        new_env = "production"

    # Note: We cannot modify pydantic-settings at runtime directly.
    # We return the target environment so the frontend can show it.
    # For a permanent change, the admin should update the .env file.
    return {
        "current_environment": current_env,
        "target_environment": new_env,
        "message": f"Para cambiar permanentemente, actualice APP_ENV={new_env} en el archivo .env y reinicie el servidor.",
        "is_production": current_env.lower() == "production",
    }


@router.put("/environment")
async def update_environment_config(
    app_env: str = Query(..., description="Nuevo ambiente: 'production' o 'development'"),
    current_user: User = Depends(get_current_active_admin),
):
    """
    Actualizar configuración de ambiente.
    Retorna la nueva configuración para que el frontend la refleje.
    Nota: El cambio real requiere actualizar .env y reiniciar.
    """
    if app_env.lower() not in ("production", "development"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="APP_ENV debe ser 'production' o 'development'."
        )

    settings = get_settings()
    return {
        "current_environment": settings.APP_ENV,
        "requested_environment": app_env.lower(),
        "message": f"Para aplicar el cambio, actualice APP_ENV={app_env.lower()} en el archivo .env y reinicie el servidor.",
        "is_production": app_env.lower() == "production",
    }


@router.get("/users", response_model=list[UserResponse])
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    current_user: User = Depends(get_current_active_admin),
    db: AsyncSession = Depends(get_db),
):
    """Listar todos los usuarios con su información de licencia"""
    result = await db.execute(
        select(User).offset(skip).limit(limit).order_by(User.created_at.desc())
    )
    users = result.scalars().all()
    return [UserResponse.model_validate(u) for u in users]


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    current_user: User = Depends(get_current_active_admin),
    db: AsyncSession = Depends(get_db),
):
    """Obtener detalles de un usuario específico"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UserResponse.model_validate(user)


@router.put("/users/{user_id}/license")
async def update_user_license(
    user_id: UUID,
    license_type: LicenseType,
    current_user: User = Depends(get_current_active_admin),
    db: AsyncSession = Depends(get_db),
):
    """Modificar el licenciamiento de un usuario"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    now = datetime.now(timezone.utc)
    user.license_type = license_type
    user.is_active = True
    
    # Calcular nueva fecha de expiración
    duration_map = {
        LicenseType.MENSUAL: timedelta(days=30),
        LicenseType.TRIMESTRAL: timedelta(days=90),
        LicenseType.SEMESTRAL: timedelta(days=180),
        LicenseType.ANUAL: timedelta(days=365),
    }
    
    # Si la licencia actual no ha expirado, extender desde la fecha actual
    base_date = user.license_end_date if user.license_end_date and user.license_end_date > now else now
    user.license_start_date = now
    user.license_end_date = base_date + duration_map[license_type]
    
    await db.flush()
    
    return {
        "message": f"Licencia actualizada a {license_type.value}",
        "user_id": str(user.id),
        "license_type": license_type.value,
        "license_end_date": user.license_end_date.isoformat(),
    }


@router.put("/users/{user_id}/active")
async def toggle_user_active(
    user_id: UUID,
    is_active: bool = Query(..., description="Nuevo estado activo del usuario"),
    current_user: User = Depends(get_current_active_admin),
    db: AsyncSession = Depends(get_db),
):
    """Activar o desactivar un usuario"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # No permitir desactivar al propio administrador
    if str(user.id) == str(current_user.id) and not is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No puede desactivar su propia cuenta."
        )
    
    user.is_active = is_active
    await db.flush()
    
    action = "activado" if is_active else "desactivado"
    logger.info(f"Usuario {user.email} {action} por {current_user.email}")
    
    return {
        "message": f"Usuario {action} exitosamente.",
        "user_id": str(user.id),
        "is_active": user.is_active,
    }


@router.get("/security-issues")
async def security_issues(
    current_user: User = Depends(get_current_active_admin),
    db: AsyncSession = Depends(get_db),
):
    """Dashboard detallado de problemas de seguridad por usuario"""
    now = datetime.now(timezone.utc)
    
    # Usuarios con licencia expirada pero aún activos
    expired_active = await db.execute(
        select(User).where(
            and_(
                User.license_end_date != None,
                User.license_end_date < now,
                User.is_active == True,
            )
        )
    )
    expired_active_users = expired_active.scalars().all()
    
    # Usuarios sin configuración
    users_without_config = await db.execute(
        select(User).where(
            ~User.id.in_(select(UserConfig.user_id))
        )
    )
    users_no_config = users_without_config.scalars().all()
    
    return {
        "expired_active_licenses": [
            {
                "user_id": str(u.id),
                "email": u.email,
                "full_name": u.full_name,
                "license_end_date": u.license_end_date.isoformat() if u.license_end_date else None,
                "days_expired": (now - u.license_end_date).days if u.license_end_date else None,
            }
            for u in expired_active_users
        ],
        "users_without_config": [
            {
                "user_id": str(u.id),
                "email": u.email,
                "full_name": u.full_name,
            }
            for u in users_no_config
        ],
    }
