"""
ContaEC - Esquemas Pydantic de RRHH (Fase 5)
Schemas para cargas familiares, evaluaciones de desempeño,
asistencia, liquidaciones laborales, utilidades e impuesto a la renta
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ==========================================
# Carga Familiar
# ==========================================

class CargaFamiliarCreate(BaseModel):
    """Esquema para crear una carga familiar"""
    employee_id: str = Field(..., description="ID del empleado")
    nombres: str = Field(..., min_length=1, max_length=200, description="Nombres de la carga familiar")
    apellidos: str = Field(..., min_length=1, max_length=200, description="Apellidos de la carga familiar")
    parentesco: str = Field(..., description="Parentesco: hijo, conyuge, otro")
    fecha_nacimiento: Optional[datetime] = Field(None, description="Fecha de nacimiento")
    identificacion: Optional[str] = Field(None, max_length=20, description="Número de identificación")
    discapacidad: bool = Field(default=False, description="Tiene discapacidad")
    es_estudiante: bool = Field(default=False, description="Es estudiante")

    @field_validator("parentesco")
    @classmethod
    def validate_parentesco(cls, v: str) -> str:
        validos = ["hijo", "conyuge", "otro"]
        if v not in validos:
            raise ValueError(f"Parentesco inválido. Válidos: {', '.join(validos)}")
        return v


class CargaFamiliarUpdate(BaseModel):
    """Esquema para actualizar una carga familiar"""
    nombres: Optional[str] = Field(None, min_length=1, max_length=200, description="Nombres")
    apellidos: Optional[str] = Field(None, min_length=1, max_length=200, description="Apellidos")
    parentesco: Optional[str] = Field(None, description="Parentesco")
    fecha_nacimiento: Optional[datetime] = Field(None, description="Fecha de nacimiento")
    identificacion: Optional[str] = Field(None, max_length=20, description="Identificación")
    discapacidad: Optional[bool] = Field(None, description="Tiene discapacidad")
    es_estudiante: Optional[bool] = Field(None, description="Es estudiante")

    @field_validator("parentesco")
    @classmethod
    def validate_parentesco(cls, v: str | None) -> str | None:
        if v is not None:
            validos = ["hijo", "conyuge", "otro"]
            if v not in validos:
                raise ValueError(f"Parentesco inválido. Válidos: {', '.join(validos)}")
        return v


class CargaFamiliarResponse(BaseModel):
    """Esquema de respuesta para carga familiar"""
    id: str = Field(..., description="ID único")
    employee_id: str = Field(..., description="ID del empleado")
    nombres: str = Field(..., description="Nombres")
    apellidos: str = Field(..., description="Apellidos")
    parentesco: str = Field(..., description="Parentesco")
    fecha_nacimiento: Optional[datetime] = Field(None, description="Fecha de nacimiento")
    identificacion: Optional[str] = Field(None, description="Identificación")
    discapacidad: bool = Field(..., description="Tiene discapacidad")
    es_estudiante: bool = Field(..., description="Es estudiante")
    is_active: bool = Field(..., description="Activo en el sistema")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Evaluación de Desempeño
# ==========================================

class EvaluacionDesempenoCreate(BaseModel):
    """Esquema para crear una evaluación de desempeño"""
    employee_id: str = Field(..., description="ID del empleado evaluado")
    evaluador_id: Optional[str] = Field(None, description="ID del evaluador")
    periodo: str = Field(..., min_length=1, max_length=10, description="Período (ej: 2024-Q1)")
    puntaje: int = Field(..., ge=0, le=100, description="Puntaje (0-100)")
    objetivos: Optional[str] = Field(None, description="Objetivos en JSON")
    comentarios: Optional[str] = Field(None, description="Comentarios")
    fortalezas: Optional[str] = Field(None, description="Fortalezas")
    areas_mejora: Optional[str] = Field(None, description="Áreas de mejora")
    plan_accion: Optional[str] = Field(None, description="Plan de acción")
    estado: str = Field(default="pendiente", description="Estado: pendiente, en_proceso, completada")
    fecha_evaluacion: Optional[datetime] = Field(None, description="Fecha de evaluación")

    @field_validator("estado")
    @classmethod
    def validate_estado(cls, v: str) -> str:
        validos = ["pendiente", "en_proceso", "completada"]
        if v not in validos:
            raise ValueError(f"Estado inválido. Válidos: {', '.join(validos)}")
        return v


class EvaluacionDesempenoUpdate(BaseModel):
    """Esquema para actualizar una evaluación de desempeño"""
    evaluador_id: Optional[str] = Field(None, description="ID del evaluador")
    periodo: Optional[str] = Field(None, max_length=10, description="Período")
    puntaje: Optional[int] = Field(None, ge=0, le=100, description="Puntaje (0-100)")
    objetivos: Optional[str] = Field(None, description="Objetivos")
    comentarios: Optional[str] = Field(None, description="Comentarios")
    fortalezas: Optional[str] = Field(None, description="Fortalezas")
    areas_mejora: Optional[str] = Field(None, description="Áreas de mejora")
    plan_accion: Optional[str] = Field(None, description="Plan de acción")
    estado: Optional[str] = Field(None, description="Estado")
    fecha_evaluacion: Optional[datetime] = Field(None, description="Fecha de evaluación")

    @field_validator("estado")
    @classmethod
    def validate_estado(cls, v: str | None) -> str | None:
        if v is not None:
            validos = ["pendiente", "en_proceso", "completada"]
            if v not in validos:
                raise ValueError(f"Estado inválido. Válidos: {', '.join(validos)}")
        return v


class EvaluacionDesempenoResponse(BaseModel):
    """Esquema de respuesta para evaluación de desempeño"""
    id: str = Field(..., description="ID único")
    employee_id: str = Field(..., description="ID del empleado")
    evaluador_id: Optional[str] = Field(None, description="ID del evaluador")
    periodo: str = Field(..., description="Período")
    puntaje: int = Field(..., description="Puntaje (0-100)")
    objetivos: Optional[str] = Field(None, description="Objetivos")
    comentarios: Optional[str] = Field(None, description="Comentarios")
    fortalezas: Optional[str] = Field(None, description="Fortalezas")
    areas_mejora: Optional[str] = Field(None, description="Áreas de mejora")
    plan_accion: Optional[str] = Field(None, description="Plan de acción")
    estado: str = Field(..., description="Estado")
    fecha_evaluacion: Optional[datetime] = Field(None, description="Fecha de evaluación")
    is_active: bool = Field(..., description="Activo en el sistema")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Asistencia
# ==========================================

class AsistenciaCreate(BaseModel):
    """Esquema para registrar asistencia"""
    employee_id: str = Field(..., description="ID del empleado")
    fecha: datetime = Field(..., description="Fecha de la asistencia")
    hora_entrada: Optional[datetime] = Field(None, description="Hora de entrada")
    hora_salida: Optional[datetime] = Field(None, description="Hora de salida")
    horas_trabajadas: Decimal = Field(default=Decimal("0.00"), decimal_places=2, description="Horas trabajadas")
    horas_extras: Decimal = Field(default=Decimal("0.00"), decimal_places=2, description="Horas extras")
    tipo: str = Field(default="normal", description="Tipo: normal, descanso, festivo, vacacion, permiso, enfermedad")
    dispositivo_entrada: Optional[str] = Field(None, max_length=100, description="Dispositivo de entrada")
    dispositivo_salida: Optional[str] = Field(None, max_length=100, description="Dispositivo de salida")
    observacion: Optional[str] = Field(None, description="Observaciones")

    @field_validator("tipo")
    @classmethod
    def validate_tipo(cls, v: str) -> str:
        validos = ["normal", "descanso", "festivo", "vacacion", "permiso", "enfermedad"]
        if v not in validos:
            raise ValueError(f"Tipo inválido. Válidos: {', '.join(validos)}")
        return v


class AsistenciaUpdate(BaseModel):
    """Esquema para actualizar asistencia"""
    hora_entrada: Optional[datetime] = Field(None, description="Hora de entrada")
    hora_salida: Optional[datetime] = Field(None, description="Hora de salida")
    horas_trabajadas: Optional[Decimal] = Field(None, decimal_places=2, description="Horas trabajadas")
    horas_extras: Optional[Decimal] = Field(None, decimal_places=2, description="Horas extras")
    tipo: Optional[str] = Field(None, description="Tipo de día")
    dispositivo_entrada: Optional[str] = Field(None, max_length=100, description="Dispositivo entrada")
    dispositivo_salida: Optional[str] = Field(None, max_length=100, description="Dispositivo salida")
    observacion: Optional[str] = Field(None, description="Observaciones")


class AsistenciaResponse(BaseModel):
    """Esquema de respuesta para asistencia"""
    id: str = Field(..., description="ID único")
    employee_id: str = Field(..., description="ID del empleado")
    fecha: datetime = Field(..., description="Fecha")
    hora_entrada: Optional[datetime] = Field(None, description="Hora de entrada")
    hora_salida: Optional[datetime] = Field(None, description="Hora de salida")
    horas_trabajadas: Decimal = Field(..., description="Horas trabajadas")
    horas_extras: Decimal = Field(..., description="Horas extras")
    tipo: str = Field(..., description="Tipo de día")
    dispositivo_entrada: Optional[str] = Field(None, description="Dispositivo entrada")
    dispositivo_salida: Optional[str] = Field(None, description="Dispositivo salida")
    observacion: Optional[str] = Field(None, description="Observaciones")
    is_active: bool = Field(..., description="Activo en el sistema")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class AsistenciaResumenResponse(BaseModel):
    """Esquema de respuesta para resumen mensual de asistencia"""
    employee_id: str = Field(..., description="ID del empleado")
    anio: int = Field(..., description="Año")
    mes: int = Field(..., description="Mes")
    dias_trabajados: int = Field(..., description="Días trabajados")
    dias_descanso: int = Field(..., description="Días de descanso")
    dias_festivo: int = Field(..., description="Días festivos trabajados")
    dias_vacacion: int = Field(..., description="Días de vacaciones")
    dias_permiso: int = Field(..., description="Días de permiso")
    dias_enfermedad: int = Field(..., description="Días de enfermedad")
    total_horas_trabajadas: Decimal = Field(..., description="Total horas trabajadas")
    total_horas_extras: Decimal = Field(..., description="Total horas extras")


# ==========================================
# Liquidación Laboral
# ==========================================

class LiquidacionLaboralCreate(BaseModel):
    """Esquema para calcular una liquidación laboral"""
    employee_id: str = Field(..., description="ID del empleado")
    company_id: str = Field(..., description="ID de la empresa")
    tipo: str = Field(..., description="Tipo: finiquito, liquidacion, despido, renuncia_voluntaria")
    fecha_fin: datetime = Field(..., description="Fecha de fin de la relación laboral")
    otros_ingresos: Decimal = Field(default=Decimal("0.00"), decimal_places=2, description="Otros ingresos")
    iess_pendiente: Decimal = Field(default=Decimal("0.00"), decimal_places=2, description="Aporte IESS pendiente")
    anticipos_pendientes: Decimal = Field(default=Decimal("0.00"), decimal_places=2, description="Anticipos pendientes")
    prestamos_pendientes: Decimal = Field(default=Decimal("0.00"), decimal_places=2, description="Préstamos pendientes")
    otros_descuentos: Decimal = Field(default=Decimal("0.00"), decimal_places=2, description="Otros descuentos")
    observaciones: Optional[str] = Field(None, description="Observaciones")

    @field_validator("tipo")
    @classmethod
    def validate_tipo(cls, v: str) -> str:
        validos = ["finiquito", "liquidacion", "despido", "renuncia_voluntaria"]
        if v not in validos:
            raise ValueError(f"Tipo inválido. Válidos: {', '.join(validos)}")
        return v


class LiquidacionLaboralUpdate(BaseModel):
    """Esquema para actualizar una liquidación laboral"""
    otros_ingresos: Optional[Decimal] = Field(None, decimal_places=2, description="Otros ingresos")
    iess_pendiente: Optional[Decimal] = Field(None, decimal_places=2, description="IESS pendiente")
    anticipos_pendientes: Optional[Decimal] = Field(None, decimal_places=2, description="Anticipos pendientes")
    prestamos_pendientes: Optional[Decimal] = Field(None, decimal_places=2, description="Préstamos pendientes")
    otros_descuentos: Optional[Decimal] = Field(None, decimal_places=2, description="Otros descuentos")
    observaciones: Optional[str] = Field(None, description="Observaciones")


class LiquidacionLaboralResponse(BaseModel):
    """Esquema de respuesta para liquidación laboral"""
    id: str = Field(..., description="ID único")
    employee_id: str = Field(..., description="ID del empleado")
    company_id: str = Field(..., description="ID de la empresa")
    tipo: str = Field(..., description="Tipo de liquidación")
    fecha_inicio: datetime = Field(..., description="Fecha inicio relación laboral")
    fecha_fin: datetime = Field(..., description="Fecha fin relación laboral")
    sueldo_pendiente: Decimal = Field(..., description="Sueldo pendiente")
    decimo_tercero_pendiente: Decimal = Field(..., description="Décimo tercero pendiente")
    decimo_cuarto_pendiente: Decimal = Field(..., description="Décimo cuarto pendiente")
    vacaciones_pendientes: Decimal = Field(..., description="Vacaciones pendientes")
    fondo_reserva_pendiente: Decimal = Field(..., description="Fondo de reserva pendiente")
    bono_desahucio: Decimal = Field(..., description="Bono de desahucio")
    indemnizacion: Decimal = Field(..., description="Indemnización")
    otros_ingresos: Decimal = Field(..., description="Otros ingresos")
    total_ingresos: Decimal = Field(..., description="Total ingresos")
    iess_pendiente: Decimal = Field(..., description="IESS pendiente")
    anticipos_pendientes: Decimal = Field(..., description="Anticipos pendientes")
    prestamos_pendientes: Decimal = Field(..., description="Préstamos pendientes")
    otros_descuentos: Decimal = Field(..., description="Otros descuentos")
    total_descuentos: Decimal = Field(..., description="Total descuentos")
    total_liquidacion: Decimal = Field(..., description="Total liquidación neta")
    estado: str = Field(..., description="Estado")
    observaciones: Optional[str] = Field(None, description="Observaciones")
    aprobado_por: Optional[str] = Field(None, description="ID del aprobador")
    fecha_aprobacion: Optional[datetime] = Field(None, description="Fecha de aprobación")
    is_active: bool = Field(..., description="Activo en el sistema")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Utilidades / Participación de Utilidades
# ==========================================

class UtilidadesParticipacionCreate(BaseModel):
    """Esquema para calcular participación de utilidades"""
    company_id: str = Field(..., description="ID de la empresa")
    anio: int = Field(..., ge=2000, le=2100, description="Año fiscal")
    total_utilidades: Decimal = Field(..., gt=0, decimal_places=2, description="Total de utilidades de la empresa")
    porcentaje_trabajadores: Decimal = Field(
        default=Decimal("15.00"),
        ge=0,
        le=100,
        decimal_places=2,
        description="Porcentaje para trabajadores (15% por defecto)",
    )


class UtilidadesParticipacionResponse(BaseModel):
    """Esquema de respuesta para participación de utilidades"""
    id: str = Field(..., description="ID único")
    company_id: str = Field(..., description="ID de la empresa")
    anio: int = Field(..., description="Año fiscal")
    total_utilidades: Decimal = Field(..., description="Total utilidades")
    porcentaje_trabajadores: Decimal = Field(..., description="Porcentaje para trabajadores")
    numero_trabajadores: int = Field(..., description="Número de trabajadores")
    monto_distribuir: Decimal = Field(..., description="Monto total a distribuir")
    estado: str = Field(..., description="Estado")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class UtilidadesDetalleResponse(BaseModel):
    """Esquema de respuesta para detalle de utilidades por empleado"""
    id: str = Field(..., description="ID único")
    utilidad_id: str = Field(..., description="ID de la participación de utilidades")
    employee_id: str = Field(..., description="ID del empleado")
    dias_trabajados: int = Field(..., description="Días trabajados en el año")
    sueldo_acumulado: Decimal = Field(..., description="Sueldo acumulado en el año")
    porcentaje_participacion: Decimal = Field(..., description="Porcentaje de participación")
    monto_asignado: Decimal = Field(..., description="Monto asignado")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


class UtilidadesParticipacionFullResponse(UtilidadesParticipacionResponse):
    """Esquema de respuesta para participación de utilidades con detalles"""
    detalles: list[UtilidadesDetalleResponse] = Field(
        default_factory=list,
        description="Detalle por empleado",
    )


# ==========================================
# Impuesto a la Renta (IR) Progresivo
# ==========================================

class IRProgressiveCalcRequest(BaseModel):
    """Esquema para calcular impuesto a la renta progresivo"""
    ingreso_gravable: Decimal = Field(
        ...,
        ge=0,
        decimal_places=2,
        description="Ingreso gravable anual (base imponible)",
    )
    periodo: str = Field(
        ...,
        description="Período de cálculo (ej: 2024)",
    )


class IRProgressiveCalcResponse(BaseModel):
    """Esquema de respuesta para cálculo de impuesto a la renta"""
    base_imponible: Decimal = Field(..., description="Base imponible (ingreso gravable - fracción básica)")
    impuesto: Decimal = Field(..., description="Impuesto a la renta calculado")
    fraccion_basica: Decimal = Field(..., description="Fracción básica aplicada")
    exceso: Decimal = Field(..., description="Exceso sobre la fracción básica")
    tasa: Decimal = Field(..., description="Tasa porcentual aplicada")
    impuesto_fraccion: Decimal = Field(..., description="Impuesto sobre la fracción básica")
    fecha: str = Field(..., description="Fecha/período de cálculo")


# ==========================================
# Exportación de Pago Bancario
# ==========================================

class BankPaymentExportRequest(BaseModel):
    """Esquema para exportar archivo de pago bancario"""
    company_id: str = Field(..., description="ID de la empresa")
    periodo: str = Field(..., description="Período de pago (ej: 2024-01)")
    formato: str = Field(default="xlsx", description="Formato de exportación: xlsx o csv")

    @field_validator("formato")
    @classmethod
    def validate_formato(cls, v: str) -> str:
        validos = ["xlsx", "csv"]
        if v not in validos:
            raise ValueError(f"Formato inválido. Válidos: {', '.join(validos)}")
        return v


class BankPaymentExportResponse(BaseModel):
    """Esquema de respuesta para exportación de pago bancario"""
    filename: str = Field(..., description="Nombre del archivo generado")
    content: str = Field(..., description="Contenido del archivo en base64")
