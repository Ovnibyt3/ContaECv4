"""
ContaEC - Esquemas Pydantic de Registro de Auditoría
Schemas para consulta y respuesta de registros de auditoría
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AuditLogResponse(BaseModel):
    """Esquema de respuesta para un registro de auditoría"""
    id: str = Field(..., description="ID único del registro")
    user_id: Optional[str] = Field(None, description="ID del usuario")
    user_email: Optional[str] = Field(None, description="Correo del usuario")
    action: str = Field(..., description="Acción realizada")
    entity_type: str = Field(..., description="Tipo de entidad afectada")
    entity_id: Optional[str] = Field(None, description="ID de la entidad afectada")
    description: str = Field(..., description="Descripción de la acción")
    ip_address: Optional[str] = Field(None, description="Dirección IP")
    user_agent: Optional[str] = Field(None, description="User-Agent del cliente")
    old_values: Optional[str] = Field(None, description="Valores anteriores (JSON)")
    new_values: Optional[str] = Field(None, description="Valores nuevos (JSON)")
    created_at: datetime = Field(..., description="Fecha y hora de la acción")

    model_config = {"from_attributes": True}


class AuditStatsResponse(BaseModel):
    """Estadísticas del registro de auditoría"""
    total_actions: int = Field(..., description="Total de acciones registradas")
    actions_by_type: dict[str, int] = Field(
        ..., description="Acciones agrupadas por tipo"
    )
    actions_by_entity: dict[str, int] = Field(
        ..., description="Acciones agrupadas por tipo de entidad"
    )
    recent_logins: int = Field(..., description="Logins en las últimas 24 horas")
