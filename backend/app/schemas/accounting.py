"""
ContaEC - Schemas de Contabilidad Core
Plan de Cuentas, Asientos Contables, Cuentas por Cobrar, Pagos, Períodos Fiscales
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# ==========================================
# Plan de Cuentas
# ==========================================

class CuentaContableCreate(BaseModel):
    """Schema para crear una cuenta contable"""
    codigo: str = Field(..., max_length=20, description="Código de la cuenta (ej: 1.1.01.01)")
    nombre: str = Field(..., max_length=255, description="Nombre de la cuenta")
    tipo: str = Field(..., description="Tipo: activo, pasivo, patrimonio, ingreso, gasto, costo")
    naturaleza: str = Field(..., description="Naturaleza: deudora o acreedora")
    nivel: int = Field(default=1, description="Nivel jerárquico")
    cuenta_padre_id: Optional[str] = None
    es_cuenta_movimiento: bool = True
    es_imputable: bool = True
    saldo_inicial: Decimal = Decimal("0")
    descripcion: Optional[str] = None
    etiqueta: Optional[str] = None
    cuenta_contrapartida_id: Optional[str] = None


class CuentaContableUpdate(BaseModel):
    """Schema para actualizar una cuenta contable"""
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    naturaleza: Optional[str] = None
    nivel: Optional[int] = None
    cuenta_padre_id: Optional[str] = None
    es_cuenta_movimiento: Optional[bool] = None
    es_imputable: Optional[bool] = None
    saldo_inicial: Optional[Decimal] = None
    descripcion: Optional[str] = None
    etiqueta: Optional[str] = None
    cuenta_contrapartida_id: Optional[str] = None
    is_active: Optional[bool] = None


class CuentaContableResponse(BaseModel):
    """Schema de respuesta de cuenta contable"""
    id: str
    company_id: str
    codigo: str
    nombre: str
    tipo: str
    naturaleza: str
    nivel: int
    cuenta_padre_id: Optional[str] = None
    es_cuenta_movimiento: bool
    es_imputable: bool
    saldo_inicial: Decimal
    saldo_actual: Decimal
    total_debitos: Decimal
    total_creditos: Decimal
    descripcion: Optional[str] = None
    etiqueta: Optional[str] = None
    cuenta_contrapartida_id: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # Computed
    codigo_nombre: Optional[str] = None

    class Config:
        from_attributes = True


# ==========================================
# Asientos Contables
# ==========================================

class AsientoDetalleCreate(BaseModel):
    """Schema para crear un detalle de asiento"""
    cuenta_contable_id: str
    debito: Decimal = Decimal("0")
    credito: Decimal = Decimal("0")
    descripcion: Optional[str] = None
    referencia_tipo: Optional[str] = None
    referencia_id: Optional[str] = None


class AsientoDetalleResponse(BaseModel):
    """Schema de respuesta de detalle de asiento"""
    id: str
    asiento_id: str
    cuenta_contable_id: str
    debito: Decimal
    credito: Decimal
    descripcion: Optional[str] = None
    referencia_tipo: Optional[str] = None
    referencia_id: Optional[str] = None
    created_at: datetime
    # Cuenta contable info
    cuenta_codigo: Optional[str] = None
    cuenta_nombre: Optional[str] = None

    class Config:
        from_attributes = True


class AsientoContableCreate(BaseModel):
    """Schema para crear un asiento contable"""
    fecha: datetime
    tipo: str = Field(default="ordinario", description="Tipo: apertura, ordinario, cierre, ajuste, estimacion, reclasificacion")
    concepto: str = Field(..., max_length=500, description="Concepto del asiento")
    referencia_tipo: Optional[str] = None
    referencia_id: Optional[str] = None
    referencia_secuencial: Optional[str] = None
    observaciones: Optional[str] = None
    detalles: list[AsientoDetalleCreate] = Field(..., min_length=2, description="Al menos 2 líneas (débito y crédito)")
    periodo_fiscal_id: Optional[str] = None


class AsientoContableUpdate(BaseModel):
    """Schema para actualizar un asiento contable (solo en borrador)"""
    concepto: Optional[str] = None
    observaciones: Optional[str] = None
    detalles: Optional[list[AsientoDetalleCreate]] = None


class AsientoContableResponse(BaseModel):
    """Schema de respuesta de asiento contable"""
    id: str
    company_id: str
    user_id: str
    periodo_fiscal_id: Optional[str] = None
    numero: str
    fecha: datetime
    tipo: str
    estado: str
    total_debitos: Decimal
    total_creditos: Decimal
    concepto: str
    referencia_tipo: Optional[str] = None
    referencia_id: Optional[str] = None
    referencia_secuencial: Optional[str] = None
    observaciones: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    detalles: list[AsientoDetalleResponse] = []
    is_cuadrado: Optional[bool] = None

    class Config:
        from_attributes = True


# ==========================================
# Cuentas por Cobrar
# ==========================================

class CuentaPorCobrarCreate(BaseModel):
    """Schema para crear una cuenta por cobrar"""
    client_id: Optional[str] = None
    comprobante_id: Optional[str] = None
    numero_factura: Optional[str] = None
    fecha_emision: datetime
    fecha_vencimiento: Optional[datetime] = None
    monto_total: Decimal
    dias_credito: int = 30
    cliente_nombre: Optional[str] = None
    cliente_identificacion: Optional[str] = None
    observaciones: Optional[str] = None


class CuentaPorCobrarUpdate(BaseModel):
    """Schema para actualizar una cuenta por cobrar"""
    fecha_vencimiento: Optional[datetime] = None
    dias_credito: Optional[int] = None
    observaciones: Optional[str] = None
    estado: Optional[str] = None


class CuentaPorCobrarResponse(BaseModel):
    """Schema de respuesta de cuenta por cobrar"""
    id: str
    company_id: str
    client_id: Optional[str] = None
    comprobante_id: Optional[str] = None
    numero_factura: Optional[str] = None
    fecha_emision: datetime
    fecha_vencimiento: Optional[datetime] = None
    monto_total: Decimal
    monto_pagado: Decimal
    monto_pendiente: Decimal
    estado: str
    dias_credito: int
    dias_vencida: int
    cliente_nombre: Optional[str] = None
    cliente_identificacion: Optional[str] = None
    observaciones: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    rango_vencimiento: Optional[str] = None

    class Config:
        from_attributes = True


# ==========================================
# Pagos / Cobros
# ==========================================

class PagoCreate(BaseModel):
    """Schema para crear un pago/cobro"""
    tipo: str = Field(..., description="Tipo: cobro, pago, otro")
    fecha: datetime
    monto: Decimal
    forma_pago: str = "01"
    referencia: Optional[str] = None
    cuenta_bancaria_id: Optional[str] = None
    cuenta_por_cobrar_id: Optional[str] = None
    cuenta_por_pagar_id: Optional[str] = None
    tercero_nombre: Optional[str] = None
    tercero_identificacion: Optional[str] = None
    observaciones: Optional[str] = None


class PagoUpdate(BaseModel):
    """Schema para actualizar un pago"""
    forma_pago: Optional[str] = None
    referencia: Optional[str] = None
    observaciones: Optional[str] = None
    estado: Optional[str] = None


class PagoResponse(BaseModel):
    """Schema de respuesta de pago"""
    id: str
    company_id: str
    user_id: str
    tipo: str
    numero: str
    fecha: datetime
    monto: Decimal
    forma_pago: str
    referencia: Optional[str] = None
    cuenta_bancaria_id: Optional[str] = None
    cuenta_por_cobrar_id: Optional[str] = None
    cuenta_por_pagar_id: Optional[str] = None
    tercero_nombre: Optional[str] = None
    tercero_identificacion: Optional[str] = None
    estado: str
    observaciones: Optional[str] = None
    asiento_id: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==========================================
# Períodos Fiscales
# ==========================================

class PeriodoFiscalCreate(BaseModel):
    """Schema para crear un período fiscal"""
    nombre: str = Field(..., max_length=100, description="Nombre del período")
    anio: int = Field(..., description="Año fiscal")
    mes: Optional[int] = Field(None, ge=1, le=12, description="Mes (1-12, None para anual)")
    tipo_periodo: str = Field(default="mensual", description="Tipo: mensual, trimestral, semestral, anual")
    fecha_inicio: datetime
    fecha_fin: datetime
    observaciones: Optional[str] = None


class PeriodoFiscalUpdate(BaseModel):
    """Schema para actualizar un período fiscal"""
    nombre: Optional[str] = None
    observaciones: Optional[str] = None


class PeriodoFiscalResponse(BaseModel):
    """Schema de respuesta de período fiscal"""
    id: str
    company_id: str
    nombre: str
    anio: int
    mes: Optional[int] = None
    tipo_periodo: str
    fecha_inicio: datetime
    fecha_fin: datetime
    estado: str
    fecha_cierre: Optional[datetime] = None
    cerrado_por: Optional[str] = None
    total_debitos: Decimal
    total_creditos: Decimal
    total_asientos: int
    observaciones: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==========================================
# Reportes Contables
# ==========================================

class BalanceComprobacionItem(BaseModel):
    """Item del Balance de Comprobación"""
    codigo: str
    nombre: str
    tipo: str
    nivel: int
    saldo_deudor: Decimal = Decimal("0")
    saldo_acreedor: Decimal = Decimal("0")
    total_debitos: Decimal = Decimal("0")
    total_creditos: Decimal = Decimal("0")


class BalanceComprobacionResponse(BaseModel):
    """Respuesta del Balance de Comprobación"""
    items: list[BalanceComprobacionItem] = []
    total_debitos: Decimal = Decimal("0")
    total_creditos: Decimal = Decimal("0")
    total_saldo_deudor: Decimal = Decimal("0")
    total_saldo_acreedor: Decimal = Decimal("0")
    periodo: Optional[str] = None
    fecha_generacion: datetime = Field(default_factory=datetime.now)


class LibroDiarioItem(BaseModel):
    """Item del Libro Diario"""
    asiento_numero: str
    asiento_fecha: datetime
    asiento_concepto: str
    asiento_tipo: str
    asiento_estado: str
    cuenta_codigo: str
    cuenta_nombre: str
    debito: Decimal = Decimal("0")
    credito: Decimal = Decimal("0")
    descripcion: Optional[str] = None


class LibroMayorItem(BaseModel):
    """Item del Libro Mayor"""
    cuenta_codigo: str
    cuenta_nombre: str
    cuenta_tipo: str
    saldo_inicial: Decimal = Decimal("0")
    movimientos: list[dict] = []
    total_debitos: Decimal = Decimal("0")
    total_creditos: Decimal = Decimal("0")
    saldo_final: Decimal = Decimal("0")


class EnvejecimientoCarteraItem(BaseModel):
    """Item del envejecimiento de cartera (CxC)"""
    cliente_id: Optional[str] = None
    cliente_nombre: str
    cliente_identificacion: Optional[str] = None
    total: Decimal = Decimal("0")
    vigente: Decimal = Decimal("0")
    dias_1_30: Decimal = Decimal("0")
    dias_31_60: Decimal = Decimal("0")
    dias_61_90: Decimal = Decimal("0")
    dias_91_180: Decimal = Decimal("0")
    dias_mas_180: Decimal = Decimal("0")


class EnvejecimientoCarteraResponse(BaseModel):
    """Respuesta del envejecimiento de cartera"""
    items: list[EnvejecimientoCarteraItem] = []
    total_general: Decimal = Decimal("0")
    total_vigente: Decimal = Decimal("0")
    total_1_30: Decimal = Decimal("0")
    total_31_60: Decimal = Decimal("0")
    total_61_90: Decimal = Decimal("0")
    total_91_180: Decimal = Decimal("0")
    total_mas_180: Decimal = Decimal("0")


class ContabilidadStats(BaseModel):
    """Estadísticas del módulo contable"""
    total_cuentas: int = 0
    total_cuentas_activas: int = 0
    total_asientos: int = 0
    total_asientos_aprobados: int = 0
    total_cxc: int = 0
    total_cxc_pendiente: Decimal = Decimal("0")
    total_cxp_pendiente: Decimal = Decimal("0")
    total_cobros_mes: Decimal = Decimal("0")
    total_pagos_mes: Decimal = Decimal("0")
    periodos_abiertos: int = 0
    periodo_actual: Optional[str] = None
