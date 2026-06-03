"""
ContaEC - Esquemas de Empresa y Establecimiento
Pydantic schemas para creación, actualización y respuesta de empresas
"""
import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ==========================================
# Empresa (Company)
# ==========================================

class CompanyCreate(BaseModel):
    """Esquema para crear una nueva empresa"""
    ruc: str = Field(
        ...,
        min_length=13,
        max_length=13,
        description="Registro Único de Contribuyente (13 dígitos)",
        examples=["1790012345001"],
    )
    razon_social: str = Field(
        ...,
        min_length=2,
        max_length=255,
        description="Razón social de la empresa (nombre legal)",
        examples=["DISTRIBUIDORA ABC S.A."],
    )
    nombre_comercial: Optional[str] = Field(
        None,
        max_length=255,
        description="Nombre comercial de la empresa",
        examples=["ABC Distribuciones"],
    )
    dir_matriz: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Dirección de la matriz de la empresa",
        examples=["Av. Amazonas 1234 y Amazonas"],
    )
    dir_establecimiento: Optional[str] = Field(
        None,
        max_length=500,
        description="Dirección del establecimiento principal",
    )
    cod_establecimiento: str = Field(
        default="001",
        min_length=3,
        max_length=3,
        description="Código del establecimiento (3 dígitos)",
        examples=["001"],
    )
    cod_punto_emision: str = Field(
        default="001",
        min_length=3,
        max_length=3,
        description="Código del punto de emisión (3 dígitos)",
        examples=["001"],
    )
    contribuyente_especial: Optional[str] = Field(
        None,
        max_length=5,
        description="Número de resolución como contribuyente especial",
    )
    obligado_contabilidad: str = Field(
        default="NO",
        description="Obligado a llevar contabilidad (SI/NO)",
        examples=["SI"],
    )
    tipo_ambiente: str = Field(
        default="1",
        description="Tipo de ambiente: 1=Pruebas, 2=Producción",
        examples=["1"],
    )
    tipo_emision: str = Field(
        default="1",
        description="Tipo de emisión: 1=Normal",
        examples=["1"],
    )
    rise: Optional[str] = Field(
        None,
        max_length=50,
        description="Régimen Simplificado RISE",
    )
    agente_retencion: Optional[str] = Field(
        None,
        max_length=5,
        description="Número de resolución como agente de retención",
    )
    contribuyente_rimpe: Optional[str] = Field(
        None,
        max_length=50,
        description="Tipo de contribuyente RIMPE",
        examples=["RIMPE Emprendedor"],
    )
    logo_path: Optional[str] = Field(
        None,
        max_length=500,
        description="Ruta del logo de la empresa",
    )

    @field_validator("ruc")
    @classmethod
    def validate_ruc(cls, v: str) -> str:
        """Valida el formato del RUC ecuatoriano (13 dígitos)"""
        if not re.match(r"^\d{13}$", v):
            raise ValueError("El RUC debe tener exactamente 13 dígitos numéricos")
        # Validación básica del dígito verificador
        provincia = int(v[:2])
        if provincia < 1 or provincia > 24:
            raise ValueError("Código de provincia del RUC inválido (01-24)")
        return v

    @field_validator("obligado_contabilidad")
    @classmethod
    def validate_obligado_contabilidad(cls, v: str) -> str:
        """Valida que el valor sea SI o NO"""
        if v not in ("SI", "NO"):
            raise ValueError("obligado_contabilidad debe ser 'SI' o 'NO'")
        return v

    @field_validator("tipo_ambiente")
    @classmethod
    def validate_tipo_ambiente(cls, v: str) -> str:
        """Valida que el tipo de ambiente sea 1 o 2"""
        if v not in ("1", "2"):
            raise ValueError("tipo_ambiente debe ser '1' (Pruebas) o '2' (Producción)")
        return v

    @field_validator("tipo_emision")
    @classmethod
    def validate_tipo_emision(cls, v: str) -> str:
        """Valida que el tipo de emisión sea 1"""
        if v != "1":
            raise ValueError("tipo_emision debe ser '1' (Normal)")
        return v

    @field_validator("cod_establecimiento", "cod_punto_emision")
    @classmethod
    def validate_codigo_3_digitos(cls, v: str) -> str:
        """Valida que el código tenga exactamente 3 dígitos"""
        if not re.match(r"^\d{3}$", v):
            raise ValueError("El código debe tener exactamente 3 dígitos numéricos (ej: 001)")
        return v

    @field_validator("contribuyente_rimpe")
    @classmethod
    def validate_contribuyente_rimpe(cls, v: Optional[str]) -> Optional[str]:
        """Valida que el tipo de contribuyente RIMPE sea válido"""
        if v is not None:
            valid_types = {"RIMPE Emprendedor", "RIMPE Negocio Popular", ""}
            if v not in valid_types:
                raise ValueError(
                    "Tipo de contribuyente RIMPE inválido. "
                    "Opciones: RIMPE Emprendedor, RIMPE Negocio Popular"
                )
        return v


class CompanyUpdate(BaseModel):
    """Esquema para actualizar datos de una empresa"""
    razon_social: Optional[str] = Field(
        None,
        min_length=2,
        max_length=255,
        description="Razón social de la empresa",
    )
    nombre_comercial: Optional[str] = Field(
        None,
        max_length=255,
        description="Nombre comercial de la empresa",
    )
    dir_matriz: Optional[str] = Field(
        None,
        min_length=5,
        max_length=500,
        description="Dirección de la matriz",
    )
    dir_establecimiento: Optional[str] = Field(
        None,
        max_length=500,
        description="Dirección del establecimiento",
    )
    cod_establecimiento: Optional[str] = Field(None, max_length=3)
    cod_punto_emision: Optional[str] = Field(None, max_length=3)
    contribuyente_especial: Optional[str] = Field(None, max_length=5)
    obligado_contabilidad: Optional[str] = Field(None)
    tipo_ambiente: Optional[str] = Field(None)
    tipo_emision: Optional[str] = Field(None)
    rise: Optional[str] = Field(None, max_length=50)
    agente_retencion: Optional[str] = Field(None, max_length=5)
    contribuyente_rimpe: Optional[str] = Field(None, max_length=50)
    logo_path: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = Field(None, description="Estado activo de la empresa")

    @field_validator("obligado_contabilidad")
    @classmethod
    def validate_obligado_contabilidad(cls, v: Optional[str]) -> Optional[str]:
        """Valida que el valor sea SI o NO"""
        if v is not None and v not in ("SI", "NO"):
            raise ValueError("obligado_contabilidad debe ser 'SI' o 'NO'")
        return v

    @field_validator("tipo_ambiente")
    @classmethod
    def validate_tipo_ambiente(cls, v: Optional[str]) -> Optional[str]:
        """Valida que el tipo de ambiente sea 1 o 2"""
        if v is not None and v not in ("1", "2"):
            raise ValueError("tipo_ambiente debe ser '1' (Pruebas) o '2' (Producción)")
        return v


class CompanyResponse(BaseModel):
    """Esquema de respuesta con datos de la empresa"""
    id: str = Field(..., description="ID único de la empresa")
    user_id: str = Field(..., description="ID del usuario propietario")
    ruc: str = Field(..., description="RUC de la empresa")
    razon_social: str = Field(..., description="Razón social")
    nombre_comercial: Optional[str] = Field(None, description="Nombre comercial")
    dir_matriz: str = Field(..., description="Dirección de la matriz")
    dir_establecimiento: Optional[str] = Field(None, description="Dirección del establecimiento")
    cod_establecimiento: str = Field(..., description="Código del establecimiento")
    cod_punto_emision: str = Field(..., description="Código del punto de emisión")
    contribuyente_especial: Optional[str] = Field(None, description="Contribuyente especial")
    obligado_contabilidad: str = Field(..., description="Obligado a llevar contabilidad")
    tipo_ambiente: str = Field(..., description="Tipo de ambiente")
    tipo_emision: str = Field(..., description="Tipo de emisión")
    rise: Optional[str] = Field(None, description="RISE")
    agente_retencion: Optional[str] = Field(None, description="Agente de retención")
    contribuyente_rimpe: Optional[str] = Field(None, description="Contribuyente RIMPE")
    logo_path: Optional[str] = Field(None, description="Ruta del logo")
    is_active: bool = Field(..., description="Estado activo")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}


# ==========================================
# Establecimiento (Establishment)
# ==========================================

class EstablishmentCreate(BaseModel):
    """Esquema para crear un nuevo establecimiento"""
    codigo: str = Field(
        ...,
        min_length=3,
        max_length=3,
        description="Código del establecimiento (3 dígitos)",
        examples=["002"],
    )
    direccion: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Dirección del establecimiento",
        examples=["Av. 9 de Octubre 567 y Colón"],
    )

    @field_validator("codigo")
    @classmethod
    def validate_codigo(cls, v: str) -> str:
        """Valida que el código tenga exactamente 3 dígitos"""
        if not re.match(r"^\d{3}$", v):
            raise ValueError("El código debe tener exactamente 3 dígitos numéricos (ej: 001)")
        return v


class EstablishmentResponse(BaseModel):
    """Esquema de respuesta con datos del establecimiento"""
    id: str = Field(..., description="ID único del establecimiento")
    company_id: str = Field(..., description="ID de la empresa")
    codigo: str = Field(..., description="Código del establecimiento")
    direccion: str = Field(..., description="Dirección del establecimiento")
    is_active: bool = Field(..., description="Estado activo")

    model_config = {"from_attributes": True}
