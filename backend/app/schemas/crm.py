"""
ContaEC - Esquemas Pydantic de CRM (Customer Relationship Management)
Schemas para pipelines, etapas, leads, oportunidades, actividades, segmentos y automatizaciones
"""
from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from pydantic import BaseModel, Field


# ==========================================
# CRM Pipeline schemas
# ==========================================

class CRMPipelineCreate(BaseModel):
    """Esquema para crear un pipeline de ventas"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre del pipeline",
        examples=["Pipeline de Ventas Principal"],
    )
    description: Optional[str] = Field(
        None,
        description="Descripción del pipeline",
    )
    is_default: Optional[bool] = Field(
        None,
        description="Si es el pipeline por defecto de la empresa",
    )
    order: Optional[int] = Field(
        None,
        ge=0,
        description="Posición de orden del pipeline",
    )


class CRMPipelineUpdate(BaseModel):
    """Esquema para actualizar un pipeline"""
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nombre del pipeline",
    )
    description: Optional[str] = Field(
        None,
        description="Descripción del pipeline",
    )
    is_default: Optional[bool] = Field(
        None,
        description="Si es el pipeline por defecto",
    )
    order: Optional[int] = Field(
        None,
        ge=0,
        description="Posición de orden",
    )


class CRMPipelineStageResponse(BaseModel):
    """Esquema de respuesta para etapa de pipeline"""
    id: str = Field(..., description="ID único de la etapa")
    pipeline_id: str = Field(..., description="ID del pipeline")
    name: str = Field(..., description="Nombre de la etapa")
    order: int = Field(..., description="Posición de orden")
    probability_percentage: int = Field(..., description="Porcentaje de probabilidad")
    color: Optional[str] = Field(None, description="Color hex")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class CRMPipelineResponse(BaseModel):
    """Esquema de respuesta para pipeline"""
    id: str = Field(..., description="ID único del pipeline")
    company_id: str = Field(..., description="ID de la empresa")
    name: str = Field(..., description="Nombre del pipeline")
    description: Optional[str] = Field(None, description="Descripción")
    is_default: bool = Field(..., description="Es pipeline por defecto")
    order: int = Field(..., description="Posición de orden")
    stages: list[CRMPipelineStageResponse] = Field(
        default_factory=list,
        description="Etapas del pipeline",
    )
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class PipelineWithStages(CRMPipelineResponse):
    """Pipeline con sus etapas (alias para claridad)"""
    pass


# ==========================================
# CRM Pipeline Stage schemas
# ==========================================

class CRMPipelineStageCreate(BaseModel):
    """Esquema para crear una etapa de pipeline"""
    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre de la etapa",
        examples=["Prospecto"],
    )
    order: Optional[int] = Field(
        None,
        ge=0,
        description="Posición de orden dentro del pipeline",
    )
    probability_percentage: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Porcentaje de probabilidad de cierre (0-100)",
        examples=[10],
    )
    color: Optional[str] = Field(
        None,
        max_length=7,
        description="Color hex de la etapa (ej: #FF5733)",
    )


class CRMPipelineStageUpdate(BaseModel):
    """Esquema para actualizar una etapa de pipeline"""
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nombre de la etapa",
    )
    order: Optional[int] = Field(
        None,
        ge=0,
        description="Posición de orden",
    )
    probability_percentage: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Porcentaje de probabilidad",
    )
    color: Optional[str] = Field(
        None,
        max_length=7,
        description="Color hex",
    )


# ==========================================
# CRM Lead schemas
# ==========================================

class CRMLeadCreate(BaseModel):
    """Esquema para crear un lead"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    client_id: Optional[str] = Field(
        None,
        description="ID del cliente asociado (opcional)",
    )
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nombre del lead",
        examples=["Juan"],
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Apellido del lead",
        examples=["Pérez"],
    )
    email: Optional[str] = Field(
        None,
        max_length=255,
        description="Correo electrónico del lead",
    )
    phone: Optional[str] = Field(
        None,
        max_length=50,
        description="Teléfono del lead",
    )
    source: Optional[str] = Field(
        None,
        description="Fuente: website, referral, social, ad, event, other",
        examples=["website"],
    )
    status: Optional[str] = Field(
        None,
        description="Estado: nuevo, contactado, cualificado, propuesta, negociacion, ganado, perdido",
        examples=["nuevo"],
    )
    assigned_to: Optional[str] = Field(
        None,
        description="ID del usuario asignado",
    )
    estimated_value: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Valor estimado del lead",
    )
    notes: Optional[str] = Field(
        None,
        description="Notas adicionales",
    )
    last_contact_date: Optional[datetime] = Field(
        None,
        description="Fecha del último contacto",
    )
    next_follow_up: Optional[datetime] = Field(
        None,
        description="Fecha del próximo seguimiento",
    )


class CRMLeadUpdate(BaseModel):
    """Esquema para actualizar un lead"""
    client_id: Optional[str] = Field(
        None,
        description="ID del cliente asociado",
    )
    first_name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="Nombre del lead",
    )
    last_name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="Apellido del lead",
    )
    email: Optional[str] = Field(
        None,
        max_length=255,
        description="Correo electrónico",
    )
    phone: Optional[str] = Field(
        None,
        max_length=50,
        description="Teléfono",
    )
    source: Optional[str] = Field(
        None,
        description="Fuente del lead",
    )
    status: Optional[str] = Field(
        None,
        description="Estado del lead",
    )
    assigned_to: Optional[str] = Field(
        None,
        description="ID del usuario asignado",
    )
    estimated_value: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Valor estimado",
    )
    notes: Optional[str] = Field(
        None,
        description="Notas adicionales",
    )
    last_contact_date: Optional[datetime] = Field(
        None,
        description="Fecha del último contacto",
    )
    next_follow_up: Optional[datetime] = Field(
        None,
        description="Fecha del próximo seguimiento",
    )


class CRMLeadResponse(BaseModel):
    """Esquema de respuesta para lead"""
    id: str = Field(..., description="ID único del lead")
    company_id: str = Field(..., description="ID de la empresa")
    client_id: Optional[str] = Field(None, description="ID del cliente asociado")
    first_name: str = Field(..., description="Nombre del lead")
    last_name: str = Field(..., description="Apellido del lead")
    email: Optional[str] = Field(None, description="Correo electrónico")
    phone: Optional[str] = Field(None, description="Teléfono")
    source: str = Field(..., description="Fuente del lead")
    status: str = Field(..., description="Estado del lead")
    assigned_to: Optional[str] = Field(None, description="ID del usuario asignado")
    estimated_value: Decimal = Field(..., description="Valor estimado")
    notes: Optional[str] = Field(None, description="Notas")
    last_contact_date: Optional[datetime] = Field(None, description="Último contacto")
    next_follow_up: Optional[datetime] = Field(None, description="Próximo seguimiento")
    converted_to_opportunity: bool = Field(..., description="Convertido a oportunidad")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# CRM Opportunity schemas
# ==========================================

class CRMOpportunityCreate(BaseModel):
    """Esquema para crear una oportunidad"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    lead_id: Optional[str] = Field(
        None,
        description="ID del lead origen (opcional)",
    )
    client_id: Optional[str] = Field(
        None,
        description="ID del cliente asociado (opcional)",
    )
    pipeline_id: str = Field(
        ...,
        description="ID del pipeline",
    )
    stage_id: str = Field(
        ...,
        description="ID de la etapa actual del pipeline",
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre de la oportunidad",
        examples=["Venta de Software ERP"],
    )
    description: Optional[str] = Field(
        None,
        description="Descripción de la oportunidad",
    )
    estimated_amount: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Monto estimado de la oportunidad",
    )
    probability: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Probabilidad de cierre (0-100)",
    )
    expected_close_date: Optional[datetime] = Field(
        None,
        description="Fecha esperada de cierre",
    )
    status: Optional[str] = Field(
        None,
        description="Estado: abierta, ganada, perdida",
        examples=["abierta"],
    )
    assigned_to: Optional[str] = Field(
        None,
        description="ID del usuario asignado",
    )


class CRMOpportunityUpdate(BaseModel):
    """Esquema para actualizar una oportunidad"""
    lead_id: Optional[str] = Field(
        None,
        description="ID del lead origen",
    )
    client_id: Optional[str] = Field(
        None,
        description="ID del cliente asociado",
    )
    pipeline_id: Optional[str] = Field(
        None,
        description="ID del pipeline",
    )
    stage_id: Optional[str] = Field(
        None,
        description="ID de la etapa actual",
    )
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nombre de la oportunidad",
    )
    description: Optional[str] = Field(
        None,
        description="Descripción",
    )
    estimated_amount: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Monto estimado",
    )
    probability: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Probabilidad de cierre",
    )
    expected_close_date: Optional[datetime] = Field(
        None,
        description="Fecha esperada de cierre",
    )
    actual_close_date: Optional[datetime] = Field(
        None,
        description="Fecha real de cierre",
    )
    status: Optional[str] = Field(
        None,
        description="Estado de la oportunidad",
    )
    assigned_to: Optional[str] = Field(
        None,
        description="ID del usuario asignado",
    )
    lost_reason: Optional[str] = Field(
        None,
        description="Razón de pérdida",
    )


class CRMOpportunityResponse(BaseModel):
    """Esquema de respuesta para oportunidad"""
    id: str = Field(..., description="ID único de la oportunidad")
    company_id: str = Field(..., description="ID de la empresa")
    lead_id: Optional[str] = Field(None, description="ID del lead origen")
    client_id: Optional[str] = Field(None, description="ID del cliente asociado")
    pipeline_id: str = Field(..., description="ID del pipeline")
    stage_id: str = Field(..., description="ID de la etapa actual")
    name: str = Field(..., description="Nombre de la oportunidad")
    description: Optional[str] = Field(None, description="Descripción")
    estimated_amount: Decimal = Field(..., description="Monto estimado")
    probability: int = Field(..., description="Probabilidad de cierre")
    expected_close_date: Optional[datetime] = Field(None, description="Fecha esperada de cierre")
    actual_close_date: Optional[datetime] = Field(None, description="Fecha real de cierre")
    status: str = Field(..., description="Estado")
    assigned_to: Optional[str] = Field(None, description="ID del usuario asignado")
    lost_reason: Optional[str] = Field(None, description="Razón de pérdida")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class OpportunityWithDetails(CRMOpportunityResponse):
    """Oportunidad con información adicional del lead, cliente y etapa"""
    lead_name: Optional[str] = Field(None, description="Nombre del lead asociado")
    client_name: Optional[str] = Field(None, description="Nombre del cliente asociado")
    stage_name: Optional[str] = Field(None, description="Nombre de la etapa actual")
    stage_color: Optional[str] = Field(None, description="Color de la etapa")
    pipeline_name: Optional[str] = Field(None, description="Nombre del pipeline")
    weighted_amount: Optional[Decimal] = Field(None, description="Monto ponderado (estimated_amount * probability / 100)")


class OpportunityStageChange(BaseModel):
    """Esquema para mover una oportunidad a otra etapa"""
    stage_id: str = Field(
        ...,
        description="ID de la nueva etapa del pipeline",
    )


# ==========================================
# CRM Activity schemas
# ==========================================

class CRMActivityCreate(BaseModel):
    """Esquema para crear una actividad"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    opportunity_id: Optional[str] = Field(
        None,
        description="ID de la oportunidad asociada (opcional)",
    )
    lead_id: Optional[str] = Field(
        None,
        description="ID del lead asociado (opcional)",
    )
    type: str = Field(
        ...,
        description="Tipo: llamada, email, reunion, tarea, nota",
        examples=["llamada"],
    )
    subject: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Asunto de la actividad",
        examples=["Primera llamada de seguimiento"],
    )
    description: Optional[str] = Field(
        None,
        description="Descripción de la actividad",
    )
    scheduled_at: Optional[datetime] = Field(
        None,
        description="Fecha programada de la actividad",
    )
    status: Optional[str] = Field(
        None,
        description="Estado: pendiente, completada, cancelada",
        examples=["pendiente"],
    )
    result: Optional[str] = Field(
        None,
        description="Resultado de la actividad",
    )


class CRMActivityUpdate(BaseModel):
    """Esquema para actualizar una actividad"""
    opportunity_id: Optional[str] = Field(
        None,
        description="ID de la oportunidad asociada",
    )
    lead_id: Optional[str] = Field(
        None,
        description="ID del lead asociado",
    )
    type: Optional[str] = Field(
        None,
        description="Tipo de actividad",
    )
    subject: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Asunto",
    )
    description: Optional[str] = Field(
        None,
        description="Descripción",
    )
    scheduled_at: Optional[datetime] = Field(
        None,
        description="Fecha programada",
    )
    completed_at: Optional[datetime] = Field(
        None,
        description="Fecha de completación",
    )
    status: Optional[str] = Field(
        None,
        description="Estado de la actividad",
    )
    result: Optional[str] = Field(
        None,
        description="Resultado de la actividad",
    )


class CRMActivityResponse(BaseModel):
    """Esquema de respuesta para actividad"""
    id: str = Field(..., description="ID único de la actividad")
    company_id: str = Field(..., description="ID de la empresa")
    opportunity_id: Optional[str] = Field(None, description="ID de la oportunidad")
    lead_id: Optional[str] = Field(None, description="ID del lead")
    user_id: str = Field(..., description="ID del usuario")
    type: str = Field(..., description="Tipo de actividad")
    subject: str = Field(..., description="Asunto")
    description: Optional[str] = Field(None, description="Descripción")
    scheduled_at: Optional[datetime] = Field(None, description="Fecha programada")
    completed_at: Optional[datetime] = Field(None, description="Fecha completada")
    status: str = Field(..., description="Estado")
    result: Optional[str] = Field(None, description="Resultado")
    created_at: datetime = Field(..., description="Fecha de creación")

    model_config = {"from_attributes": True}


# ==========================================
# CRM Contact Segment schemas
# ==========================================

class CRMContactSegmentCreate(BaseModel):
    """Esquema para crear un segmento de contactos"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre del segmento",
        examples=["Clientes VIP"],
    )
    description: Optional[str] = Field(
        None,
        description="Descripción del segmento",
    )
    type: Optional[str] = Field(
        None,
        description="Tipo: manual, regla, rfm",
        examples=["manual"],
    )
    rules: Optional[Any] = Field(
        None,
        description="Reglas JSON para segmentos basados en reglas",
    )
    rfm_score: Optional[Any] = Field(
        None,
        description="Configuración RFM JSON para segmentos RFM",
    )
    color: Optional[str] = Field(
        None,
        max_length=7,
        description="Color hex del segmento (ej: #3498DB)",
    )


class CRMContactSegmentUpdate(BaseModel):
    """Esquema para actualizar un segmento"""
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nombre del segmento",
    )
    description: Optional[str] = Field(
        None,
        description="Descripción",
    )
    type: Optional[str] = Field(
        None,
        description="Tipo de segmento",
    )
    rules: Optional[Any] = Field(
        None,
        description="Reglas JSON",
    )
    rfm_score: Optional[Any] = Field(
        None,
        description="Configuración RFM JSON",
    )
    color: Optional[str] = Field(
        None,
        max_length=7,
        description="Color hex",
    )
    is_active: Optional[bool] = Field(
        None,
        description="Si el segmento está activo",
    )


class CRMContactSegmentMemberResponse(BaseModel):
    """Esquema de respuesta para miembro de segmento"""
    id: str = Field(..., description="ID único del miembro")
    segment_id: str = Field(..., description="ID del segmento")
    client_id: str = Field(..., description="ID del cliente")
    created_at: datetime = Field(..., description="Fecha de adición")

    model_config = {"from_attributes": True}


class CRMContactSegmentResponse(BaseModel):
    """Esquema de respuesta para segmento de contactos"""
    id: str = Field(..., description="ID único del segmento")
    company_id: str = Field(..., description="ID de la empresa")
    name: str = Field(..., description="Nombre del segmento")
    description: Optional[str] = Field(None, description="Descripción")
    type: str = Field(..., description="Tipo de segmento")
    rules: Optional[str] = Field(None, description="Reglas JSON")
    rfm_score: Optional[str] = Field(None, description="Configuración RFM JSON")
    color: Optional[str] = Field(None, description="Color hex")
    is_active: bool = Field(..., description="Está activo")
    client_members: list[CRMContactSegmentMemberResponse] = Field(
        default_factory=list,
        description="Miembros del segmento",
    )
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class SegmentAddClientsRequest(BaseModel):
    """Esquema para agregar clientes a un segmento"""
    client_ids: list[str] = Field(
        ...,
        min_length=1,
        description="Lista de IDs de clientes a agregar al segmento",
    )


# ==========================================
# CRM Automation schemas
# ==========================================

class CRMAutomationCreate(BaseModel):
    """Esquema para crear una automatización"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre de la automatización",
        examples=["Notificar al crear lead"],
    )
    trigger_type: str = Field(
        ...,
        description="Tipo de disparador: lead_creado, oportunidad_ganada, oportunidad_perdida, stage_changed, client_creado",
        examples=["lead_creado"],
    )
    trigger_conditions: Optional[Any] = Field(
        None,
        description="Condiciones del disparador en JSON",
    )
    actions: Optional[Any] = Field(
        None,
        description="Lista de acciones en JSON: send_email, create_task, notify_user, change_stage, assign_user",
    )
    is_active: Optional[bool] = Field(
        None,
        description="Si la automatización está activa",
    )


class CRMAutomationUpdate(BaseModel):
    """Esquema para actualizar una automatización"""
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nombre de la automatización",
    )
    trigger_type: Optional[str] = Field(
        None,
        description="Tipo de disparador",
    )
    trigger_conditions: Optional[Any] = Field(
        None,
        description="Condiciones del disparador",
    )
    actions: Optional[Any] = Field(
        None,
        description="Lista de acciones",
    )
    is_active: Optional[bool] = Field(
        None,
        description="Si la automatización está activa",
    )


class CRMAutomationResponse(BaseModel):
    """Esquema de respuesta para automatización"""
    id: str = Field(..., description="ID único de la automatización")
    company_id: str = Field(..., description="ID de la empresa")
    name: str = Field(..., description="Nombre de la automatización")
    trigger_type: str = Field(..., description="Tipo de disparador")
    trigger_conditions: Optional[str] = Field(None, description="Condiciones JSON")
    actions: Optional[str] = Field(None, description="Acciones JSON")
    is_active: bool = Field(..., description="Está activa")
    last_triggered_at: Optional[datetime] = Field(None, description="Última ejecución")
    trigger_count: int = Field(..., description="Número de ejecuciones")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# CRM Stats schema
# ==========================================

class CRMStats(BaseModel):
    """Estadísticas generales del CRM"""
    total_leads: int = Field(..., description="Total de leads")
    total_opportunities: int = Field(..., description="Total de oportunidades")
    won_opportunities: int = Field(..., description="Oportunidades ganadas")
    lost_opportunities: int = Field(..., description="Oportunidades perdidas")
    conversion_rate: Decimal = Field(..., description="Tasa de conversión (%)")
    pipeline_value: Decimal = Field(..., description="Valor total del pipeline")
    weighted_pipeline: Decimal = Field(..., description="Valor ponderado del pipeline")
