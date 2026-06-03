"""
ContaEC - Schemas de Proforma
Pydantic models for request/response validation
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# ============================================
# Detalle schemas
# ============================================

class ProformaDetalleCreate(BaseModel):
    """Schema para crear un detalle de proforma"""
    product_id: Optional[str] = None
    codigo_principal: str
    codigo_auxiliar: Optional[str] = None
    descripcion: str
    cantidad: Decimal = Field(gt=0)
    unidad_medida: str = "Unidad"
    precio_unitario: Decimal = Field(ge=0)
    descuento: Decimal = Field(ge=0, default=Decimal("0"))
    iva_codigo: str = "0"
    iva_porcentaje: Decimal = Field(ge=0, default=Decimal("0"))
    ice_codigo: Optional[str] = None
    ice_porcentaje: Optional[Decimal] = None


class ProformaDetalleResponse(BaseModel):
    """Schema de respuesta para un detalle de proforma"""
    id: str
    product_id: Optional[str] = None
    codigo_principal: str
    codigo_auxiliar: Optional[str] = None
    descripcion: str
    cantidad: Decimal
    unidad_medida: str
    precio_unitario: Decimal
    descuento: Decimal
    precio_total_sin_impuestos: Decimal
    iva_codigo: str
    iva_porcentaje: Decimal
    iva_valor: Decimal
    ice_codigo: Optional[str] = None
    ice_porcentaje: Optional[Decimal] = None
    ice_valor: Optional[Decimal] = None

    model_config = {"from_attributes": True}


# ============================================
# Proforma schemas
# ============================================

class ProformaCreate(BaseModel):
    """Schema para crear una proforma"""
    company_id: str
    client_id: Optional[str] = None
    detalles: list[ProformaDetalleCreate] = Field(min_length=1)
    observaciones: Optional[str] = None
    forma_pago: Optional[str] = "01"
    fecha_validez: Optional[str] = None  # ISO date string
    info_adicional: Optional[dict[str, str]] = None


class ProformaUpdate(BaseModel):
    """Schema para actualizar una proforma (solo BORRADOR)"""
    client_id: Optional[str] = None
    detalles: Optional[list[ProformaDetalleCreate]] = None
    observaciones: Optional[str] = None
    forma_pago: Optional[str] = None
    fecha_validez: Optional[str] = None
    info_adicional: Optional[dict[str, str]] = None


class ProformaResponse(BaseModel):
    """Schema de respuesta completa de una proforma"""
    id: str
    company_id: str
    client_id: Optional[str] = None
    secuencial: str
    fecha_emision: datetime
    fecha_validez: Optional[datetime] = None
    estado: str
    cliente_tipo_identificacion: str
    cliente_identificacion: str
    cliente_razon_social: str
    cliente_direccion: Optional[str] = None
    cliente_email: Optional[str] = None
    cliente_telefono: Optional[str] = None
    subtotal_sin_impuestos: Decimal
    total_iva: Decimal
    total_ice: Decimal
    total_descuento: Decimal
    total_con_impuestos: Decimal
    forma_pago: Optional[str] = None
    observaciones: Optional[str] = None
    comprobante_convertido_id: Optional[str] = None
    detalles: list[ProformaDetalleResponse] = []
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProformaListResponse(BaseModel):
    """Schema de respuesta resumida para listado de proformas"""
    id: str
    secuencial: str
    fecha_emision: datetime
    fecha_validez: Optional[datetime] = None
    estado: str
    cliente_razon_social: str
    total_con_impuestos: Decimal
    comprobante_convertido_id: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class ProformaStatsResponse(BaseModel):
    """Schema de estadísticas de proformas"""
    total: int
    borrador: int
    enviada: int
    aceptada: int
    rechazada: int
    convertida: int
