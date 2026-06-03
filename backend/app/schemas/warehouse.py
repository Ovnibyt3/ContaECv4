"""
ContaEC - Esquemas Pydantic de Multi-Almacén y Logística
Schemas para almacenes, ubicaciones, transferencias y stock
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ==========================================
# Almacén (Warehouse)
# ==========================================

class WarehouseCreate(BaseModel):
    """Esquema para crear un nuevo almacén"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    nombre: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre del almacén",
        examples=["Bodega Principal"],
    )
    codigo: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Código del almacén (ej: BOD-001), único por empresa",
        examples=["BOD-001"],
    )
    direccion: Optional[str] = Field(
        None,
        max_length=500,
        description="Dirección del almacén",
    )
    ciudad: Optional[str] = Field(
        None,
        max_length=100,
        description="Ciudad donde se ubica el almacén",
    )
    responsable: Optional[str] = Field(
        None,
        max_length=200,
        description="Persona responsable del almacén",
    )
    telefono: Optional[str] = Field(
        None,
        max_length=50,
        description="Teléfono del almacén",
    )
    is_principal: bool = Field(
        default=False,
        description="Indica si es el almacén principal (solo uno por empresa)",
    )


class WarehouseUpdate(BaseModel):
    """Esquema para actualizar un almacén"""
    nombre: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nombre del almacén",
    )
    codigo: Optional[str] = Field(
        None,
        min_length=1,
        max_length=20,
        description="Código del almacén",
    )
    direccion: Optional[str] = Field(
        None,
        max_length=500,
        description="Dirección del almacén",
    )
    ciudad: Optional[str] = Field(
        None,
        max_length=100,
        description="Ciudad",
    )
    responsable: Optional[str] = Field(
        None,
        max_length=200,
        description="Responsable",
    )
    telefono: Optional[str] = Field(
        None,
        max_length=50,
        description="Teléfono",
    )
    is_principal: Optional[bool] = Field(
        None,
        description="¿Es almacén principal?",
    )


class WarehouseResponse(BaseModel):
    """Esquema de respuesta para un almacén"""
    id: str = Field(..., description="ID único del almacén")
    company_id: str = Field(..., description="ID de la empresa")
    nombre: str = Field(..., description="Nombre del almacén")
    codigo: str = Field(..., description="Código del almacén")
    direccion: Optional[str] = Field(None, description="Dirección")
    ciudad: Optional[str] = Field(None, description="Ciudad")
    responsable: Optional[str] = Field(None, description="Responsable")
    telefono: Optional[str] = Field(None, description="Teléfono")
    is_principal: bool = Field(..., description="¿Es almacén principal?")
    is_active: bool = Field(..., description="¿Está activo?")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Ubicación de Almacén (WarehouseLocation)
# ==========================================

class WarehouseLocationCreate(BaseModel):
    """Esquema para crear una ubicación dentro de un almacén"""
    producto_id: Optional[str] = Field(
        None,
        description="ID del producto asignado a esta ubicación (opcional)",
    )
    zona: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Zona del almacén (ej: A, B, C)",
        examples=["A"],
    )
    rack: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Rack dentro de la zona (ej: R1, R2)",
        examples=["R1"],
    )
    estante: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Estante o nivel del rack (ej: E1, E2)",
        examples=["E1"],
    )
    nivel: Optional[str] = Field(
        None,
        max_length=50,
        description="Posición dentro del estante (opcional)",
    )
    capacidad_maxima: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Capacidad máxima de la ubicación",
    )
    cantidad_actual: Decimal = Field(
        default=Decimal("0"),
        ge=0,
        description="Cantidad actual en la ubicación",
    )


class WarehouseLocationUpdate(BaseModel):
    """Esquema para actualizar una ubicación de almacén"""
    producto_id: Optional[str] = Field(
        None,
        description="ID del producto asignado",
    )
    zona: Optional[str] = Field(
        None,
        max_length=50,
        description="Zona del almacén",
    )
    rack: Optional[str] = Field(
        None,
        max_length=50,
        description="Rack",
    )
    estante: Optional[str] = Field(
        None,
        max_length=50,
        description="Estante",
    )
    nivel: Optional[str] = Field(
        None,
        max_length=50,
        description="Nivel/posición",
    )
    capacidad_maxima: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Capacidad máxima",
    )
    cantidad_actual: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Cantidad actual",
    )


class WarehouseLocationResponse(BaseModel):
    """Esquema de respuesta para una ubicación de almacén"""
    id: str = Field(..., description="ID único de la ubicación")
    warehouse_id: str = Field(..., description="ID del almacén")
    producto_id: Optional[str] = Field(None, description="ID del producto")
    zona: str = Field(..., description="Zona")
    rack: str = Field(..., description="Rack")
    estante: str = Field(..., description="Estante")
    nivel: Optional[str] = Field(None, description="Nivel/posición")
    codigo_ubicacion: str = Field(..., description="Código de ubicación (ej: A-R1-E1)")
    capacidad_maxima: Optional[Decimal] = Field(None, description="Capacidad máxima")
    cantidad_actual: Decimal = Field(..., description="Cantidad actual")
    is_active: bool = Field(..., description="¿Está activa?")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Transferencia entre Almacenes
# ==========================================

class WarehouseTransferDetalleCreate(BaseModel):
    """Esquema para crear una línea de detalle de transferencia"""
    product_id: str = Field(
        ...,
        description="ID del producto a transferir",
    )
    cantidad: Decimal = Field(
        ...,
        gt=0,
        description="Cantidad a transferir",
    )
    costo_unitario: Decimal = Field(
        ...,
        ge=0,
        description="Costo unitario del producto",
    )
    ubicacion_origen_id: Optional[str] = Field(
        None,
        description="ID de la ubicación de origen dentro del almacén origen",
    )
    ubicacion_destino_id: Optional[str] = Field(
        None,
        description="ID de la ubicación de destino dentro del almacén destino",
    )


class WarehouseTransferDetalleResponse(BaseModel):
    """Esquema de respuesta para una línea de detalle de transferencia"""
    id: str = Field(..., description="ID único del detalle")
    transferencia_id: str = Field(..., description="ID de la transferencia")
    product_id: str = Field(..., description="ID del producto")
    cantidad: Decimal = Field(..., description="Cantidad transferida")
    costo_unitario: Decimal = Field(..., description="Costo unitario")
    costo_total: Decimal = Field(..., description="Costo total")
    ubicacion_origen_id: Optional[str] = Field(None, description="ID ubicación origen")
    ubicacion_destino_id: Optional[str] = Field(None, description="ID ubicación destino")
    created_at: datetime = Field(..., description="Fecha de creación")

    model_config = {"from_attributes": True}


class WarehouseTransferCreate(BaseModel):
    """Esquema para crear una nueva transferencia entre almacenes"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    warehouse_origen_id: str = Field(
        ...,
        description="ID del almacén de origen",
    )
    warehouse_destino_id: str = Field(
        ...,
        description="ID del almacén de destino",
    )
    detalles: list[WarehouseTransferDetalleCreate] = Field(
        ...,
        min_length=1,
        description="Lista de líneas de detalle",
    )
    motivo: Optional[str] = Field(
        None,
        max_length=500,
        description="Motivo de la transferencia",
    )
    observaciones: Optional[str] = Field(
        None,
        description="Observaciones adicionales",
    )

    @field_validator("warehouse_destino_id")
    @classmethod
    def validate_destino_diferente(cls, v: str, values) -> str:
        """Valida que el almacén de destino sea diferente al de origen"""
        origen = values.data.get("warehouse_origen_id")
        if origen and v == origen:
            raise ValueError("El almacén de destino debe ser diferente al de origen")
        return v


class WarehouseTransferResponse(BaseModel):
    """Esquema de respuesta para una transferencia entre almacenes"""
    id: str = Field(..., description="ID único de la transferencia")
    company_id: str = Field(..., description="ID de la empresa")
    numero: str = Field(..., description="Número de transferencia")
    warehouse_origen_id: str = Field(..., description="ID almacén origen")
    warehouse_destino_id: str = Field(..., description="ID almacén destino")
    estado: str = Field(..., description="Estado: pendiente, en_transito, recibida, anulada")
    motivo: Optional[str] = Field(None, description="Motivo")
    observaciones: Optional[str] = Field(None, description="Observaciones")
    user_id: str = Field(..., description="ID del usuario creador")
    fecha_envio: Optional[datetime] = Field(None, description="Fecha de envío")
    fecha_recepcion: Optional[datetime] = Field(None, description="Fecha de recepción")
    detalles: list[WarehouseTransferDetalleResponse] = Field(
        default_factory=list,
        description="Líneas de detalle",
    )
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Stock de Almacén
# ==========================================

class WarehouseStockResponse(BaseModel):
    """Esquema de respuesta para el stock de un producto en un almacén"""
    product_id: str = Field(..., description="ID del producto")
    producto_codigo: str = Field(..., description="Código principal del producto")
    producto_descripcion: str = Field(..., description="Descripción del producto")
    saldo_cantidad: Decimal = Field(default=Decimal("0"), description="Cantidad en stock")
    saldo_valor: Decimal = Field(default=Decimal("0"), description="Valor en stock")
    costo_promedio: Decimal = Field(default=Decimal("0"), description="Costo promedio ponderado")

    model_config = {"from_attributes": True}


# ==========================================
# Kardex Detallado con información de almacén
# ==========================================

class KardexDetalladoResponse(BaseModel):
    """Esquema de respuesta para un movimiento de kardex con información de almacén"""
    id: str = Field(..., description="ID único del movimiento")
    company_id: str = Field(..., description="ID de la empresa")
    product_id: str = Field(..., description="ID del producto")
    warehouse_id: Optional[str] = Field(None, description="ID del almacén")
    warehouse_nombre: Optional[str] = Field(None, description="Nombre del almacén")
    tipo_movimiento: str = Field(..., description="Tipo de movimiento")
    cantidad: Decimal = Field(..., description="Cantidad del movimiento")
    costo_unitario: Decimal = Field(..., description="Costo unitario")
    costo_total: Decimal = Field(..., description="Costo total del movimiento")
    saldo_cantidad: Decimal = Field(..., description="Saldo de cantidad acumulado")
    saldo_valor: Decimal = Field(..., description="Saldo de valor acumulado")
    referencia_tipo: Optional[str] = Field(None, description="Tipo de referencia")
    referencia_id: Optional[str] = Field(None, description="ID de referencia")
    referencia_secuencial: Optional[str] = Field(None, description="Secuencial de referencia")
    detalle: Optional[str] = Field(None, description="Detalle del movimiento")
    fecha_movimiento: datetime = Field(..., description="Fecha del movimiento")
    user_id: str = Field(..., description="ID del usuario")
    is_active: bool = Field(..., description="¿Está activo?")
    created_at: datetime = Field(..., description="Fecha de creación")

    model_config = {"from_attributes": True}
