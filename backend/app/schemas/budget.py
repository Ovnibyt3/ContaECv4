"""
ContaEC - Esquemas Pydantic de Presupuestos y Control Presupuestario
Schemas para presupuestos anuales, cuentas presupuestarias,
ejecución mensual, alertas y comparativos presupuestarios
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# ==========================================
# Presupuesto Cuenta (Create / Response)
# ==========================================

class PresupuestoCuentaCreate(BaseModel):
    """Esquema para crear una cuenta presupuestaria"""
    cuenta_codigo: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Código de cuenta contable (ej: 1.1.1.01, 5.1.1.01)",
        examples=["5.1.1.01"],
    )
    cuenta_nombre: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre de la cuenta contable",
        examples=["Servicios Básicos"],
    )
    cuenta_tipo: str = Field(
        ...,
        description="Tipo de cuenta: ingreso o egreso",
        examples=["egreso"],
    )
    monto_anual: Decimal = Field(
        ...,
        gt=0,
        description="Monto anual presupuestado",
        examples=["12000.00"],
    )
    distribucion_mensual: Optional[list[Decimal]] = Field(
        None,
        description="Lista de 12 montos mensuales. Si no se proporciona, se distribuye equitativamente.",
        examples=[["1000.00"] * 12],
    )


class PresupuestoEjecucionMensualResponse(BaseModel):
    """Esquema de respuesta para ejecución mensual"""
    id: str = Field(..., description="ID único del registro")
    presupuesto_cuenta_id: str = Field(..., description="ID de la cuenta presupuestaria")
    mes: int = Field(..., description="Mes (1-12)")
    monto_presupuestado: Decimal = Field(..., description="Monto presupuestado para el mes")
    monto_ejecutado: Decimal = Field(..., description="Monto ejecutado en el mes")
    monto_disponible: Decimal = Field(..., description="Monto disponible en el mes")
    porcentaje_ejecucion: Decimal = Field(..., description="Porcentaje de ejecución mensual")
    observaciones: Optional[str] = Field(None, description="Observaciones")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class PresupuestoAlertaResponse(BaseModel):
    """Esquema de respuesta para alerta presupuestaria"""
    id: str = Field(..., description="ID único de la alerta")
    company_id: str = Field(..., description="ID de la empresa")
    presupuesto_cuenta_id: str = Field(..., description="ID de la cuenta presupuestaria")
    tipo_alerta: str = Field(..., description="Tipo de alerta")
    mensaje: Optional[str] = Field(None, description="Mensaje descriptivo")
    monto_presupuestado: Decimal = Field(..., description="Monto presupuestado al momento de la alerta")
    monto_ejecutado: Decimal = Field(..., description="Monto ejecutado al momento de la alerta")
    monto_sobregiro: Decimal = Field(..., description="Monto de sobregiro")
    porcentaje_ejecucion: Decimal = Field(..., description="Porcentaje de ejecución")
    is_leida: bool = Field(..., description="Si la alerta ha sido leída")
    is_resuelta: bool = Field(..., description="Si la alerta ha sido resuelta")
    created_at: datetime = Field(..., description="Fecha de creación")

    model_config = {"from_attributes": True}


class PresupuestoCuentaResponse(BaseModel):
    """Esquema de respuesta para cuenta presupuestaria"""
    id: str = Field(..., description="ID único de la cuenta presupuestaria")
    presupuesto_id: str = Field(..., description="ID del presupuesto anual")
    cuenta_codigo: str = Field(..., description="Código de cuenta contable")
    cuenta_nombre: str = Field(..., description="Nombre de la cuenta")
    cuenta_tipo: str = Field(..., description="Tipo de cuenta (ingreso/egreso)")
    monto_anual: Decimal = Field(..., description="Monto anual presupuestado")
    monto_ejecutado: Decimal = Field(..., description="Monto ejecutado acumulado")
    monto_disponible: Decimal = Field(..., description="Monto disponible")
    porcentaje_ejecucion: Decimal = Field(..., description="Porcentaje de ejecución")
    is_active: bool = Field(..., description="Está activa")
    ejecuciones_mensuales: list[PresupuestoEjecucionMensualResponse] = Field(
        default_factory=list,
        description="Ejecuciones mensuales",
    )
    alertas: list[PresupuestoAlertaResponse] = Field(
        default_factory=list,
        description="Alertas de la cuenta",
    )
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Presupuesto Anual (Create / Update / Response)
# ==========================================

class PresupuestoAnualCreate(BaseModel):
    """Esquema para crear un nuevo presupuesto anual"""
    company_id: str = Field(
        ...,
        description="ID de la empresa",
    )
    anio: int = Field(
        ...,
        ge=2020,
        le=2050,
        description="Año fiscal del presupuesto",
        examples=[2024],
    )
    nombre: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nombre descriptivo del presupuesto",
        examples=["Presupuesto Anual 2024"],
    )
    descripcion: Optional[str] = Field(
        None,
        description="Descripción detallada del presupuesto",
    )
    cuentas: list[PresupuestoCuentaCreate] = Field(
        ...,
        min_length=1,
        description="Lista de cuentas presupuestarias",
    )


class PresupuestoAnualUpdate(BaseModel):
    """Esquema para actualizar un presupuesto anual"""
    nombre: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nombre descriptivo del presupuesto",
    )
    descripcion: Optional[str] = Field(
        None,
        description="Descripción detallada",
    )


class PresupuestoAnualResponse(BaseModel):
    """Esquema de respuesta para un presupuesto anual"""
    id: str = Field(..., description="ID único del presupuesto")
    company_id: str = Field(..., description="ID de la empresa")
    user_id: str = Field(..., description="ID del usuario creador")
    anio: int = Field(..., description="Año fiscal")
    nombre: str = Field(..., description="Nombre del presupuesto")
    descripcion: Optional[str] = Field(None, description="Descripción")
    estado: str = Field(..., description="Estado del presupuesto")
    total_ingresos_presupuestado: Decimal = Field(..., description="Total ingresos presupuestados")
    total_egresos_presupuestado: Decimal = Field(..., description="Total egresos presupuestados")
    total_ingresos_ejecutado: Decimal = Field(..., description="Total ingresos ejecutados")
    total_egresos_ejecutado: Decimal = Field(..., description="Total egresos ejecutados")
    is_active: bool = Field(..., description="Está activo")
    cuentas: list[PresupuestoCuentaResponse] = Field(
        default_factory=list,
        description="Cuentas presupuestarias",
    )
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Ejecución Mensual (Create / Update)
# ==========================================

class EjecucionMensualCreate(BaseModel):
    """Esquema para registrar ejecución mensual"""
    monto_ejecutado: Decimal = Field(
        ...,
        ge=0,
        description="Monto ejecutado en el mes",
        examples=["1500.00"],
    )
    observaciones: Optional[str] = Field(
        None,
        description="Observaciones sobre la ejecución",
    )


class EjecucionMensualUpdate(BaseModel):
    """Esquema para actualizar una ejecución mensual"""
    monto_ejecutado: Decimal = Field(
        ...,
        ge=0,
        description="Nuevo monto ejecutado",
    )
    observaciones: Optional[str] = Field(
        None,
        description="Observaciones actualizadas",
    )


# ==========================================
# Cuenta Update (para modificar monto_anual)
# ==========================================

class PresupuestoCuentaUpdate(BaseModel):
    """Esquema para actualizar monto de una cuenta presupuestaria"""
    monto_anual: Optional[Decimal] = Field(
        None,
        gt=0,
        description="Nuevo monto anual presupuestado",
    )
    cuenta_nombre: Optional[str] = Field(
        None,
        min_length=1,
        max_length=200,
        description="Nuevo nombre de la cuenta",
    )


# ==========================================
# Comparativo Presupuestario
# ==========================================

class ComparativoPresupuestario(BaseModel):
    """Comparación presupuestado vs ejecutado por cuenta"""
    cuenta_codigo: str = Field(..., description="Código de cuenta")
    cuenta_nombre: str = Field(..., description="Nombre de la cuenta")
    cuenta_tipo: str = Field(..., description="Tipo de cuenta (ingreso/egreso)")
    monto_presupuestado: Decimal = Field(..., description="Monto presupuestado anual")
    monto_ejecutado: Decimal = Field(..., description="Monto ejecutado acumulado")
    monto_disponible: Decimal = Field(..., description="Monto disponible")
    porcentaje_ejecucion: Decimal = Field(..., description="Porcentaje de ejecución")
    variacion: Decimal = Field(..., description="Variación absoluta (presupuestado - ejecutado)")
    variacion_porcentaje: Decimal = Field(..., description="Variación porcentual")
    alerta_tipo: Optional[str] = Field(None, description="Tipo de alerta activa, si existe")


class ComparativoGeneralResponse(BaseModel):
    """Comparativo general presupuestario"""
    anio: int = Field(..., description="Año fiscal")
    total_ingresos_presupuestado: Decimal = Field(..., description="Total ingresos presupuestados")
    total_ingresos_ejecutado: Decimal = Field(..., description="Total ingresos ejecutados")
    total_egresos_presupuestado: Decimal = Field(..., description="Total egresos presupuestados")
    total_egresos_ejecutado: Decimal = Field(..., description="Total egresos ejecutados")
    resultado_presupuestario: Decimal = Field(
        ..., description="Resultado presupuestario (ingresos - egresos presupuestado)"
    )
    resultado_real: Decimal = Field(
        ..., description="Resultado real (ingresos - egresos ejecutado)"
    )
    cuentas: list[ComparativoPresupuestario] = Field(
        default_factory=list,
        description="Comparativo por cuenta",
    )


# ==========================================
# Estadísticas de Presupuestos
# ==========================================

class PresupuestoStatsResponse(BaseModel):
    """Estadísticas generales de presupuestos"""
    total_presupuestos: int = Field(..., description="Total de presupuestos")
    presupuestos_borrador: int = Field(..., description="Presupuestos en borrador")
    presupuestos_aprobados: int = Field(..., description="Presupuestos aprobados")
    presupuestos_cerrados: int = Field(..., description="Presupuestos cerrados")
    total_cuentas_con_alerta: int = Field(..., description="Cuentas con alertas activas")
    total_sobregiros: int = Field(..., description="Total de sobregiros")
