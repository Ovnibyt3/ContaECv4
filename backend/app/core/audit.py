"""
ContaEC - Utilidades de Auditoría
Función helper para registrar acciones en el log de auditoría
"""
import json
import logging
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.audit_log import AuditLog

logger = logging.getLogger(__name__)


async def log_action(
    db: AsyncSession,
    user_id: str,
    user_email: str,
    action: str,
    entity_type: str,
    entity_id: Optional[str] = None,
    description: str = "",
    ip_address: Optional[str] = None,
    old_values: Optional[dict] = None,
    new_values: Optional[dict] = None,
) -> AuditLog:
    """
    Registra una acción en el log de auditoría.

    Args:
        db: Sesión de base de datos asíncrona
        user_id: ID del usuario que realizó la acción
        user_email: Correo electrónico del usuario
        action: Tipo de acción (CREATE, UPDATE, DELETE, LOGIN, LOGOUT, SIGN, SEND, AUTHORIZE, etc.)
        entity_type: Tipo de entidad afectada (user, company, client, product, comprobante, etc.)
        entity_id: ID de la entidad afectada (opcional)
        description: Descripción legible de la acción
        ip_address: Dirección IP del cliente (opcional)
        old_values: Diccionario con valores anteriores (opcional)
        new_values: Diccionario con valores nuevos (opcional)

    Returns:
        El objeto AuditLog creado
    """
    audit_log = AuditLog(
        user_id=user_id,
        user_email=user_email,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        description=description,
        ip_address=ip_address,
        old_values=json.dumps(old_values, default=str) if old_values else None,
        new_values=json.dumps(new_values, default=str) if new_values else None,
    )
    db.add(audit_log)
    await db.flush()

    logger.info(
        f"Audit: user={user_email}, action={action}, "
        f"entity={entity_type}/{entity_id}, desc={description}"
    )

    return audit_log
