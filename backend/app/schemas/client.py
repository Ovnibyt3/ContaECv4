"""
ContaEC - Esquemas Pydantic de Cliente
Schemas para creación, actualización y respuesta de clientes
con tipos de identificación según catálogos del SRI (Tabla 7)
"""
import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class ClientCreate(BaseModel):
    """Esquema para crear un nuevo cliente"""
    company_id: str = Field(
        ...,
        description="ID de la empresa a la que pertenece el cliente",
    )
    tipo_identificacion: str = Field(
        ...,
        max_length=2,
        description="Tipo de identificación SRI: 04=RUC, 05=Cédula, 06=Pasaporte, 07=Consumidor Final, 08=Exterior",
        examples=["05"],
    )
    identificacion: str = Field(
        ...,
        max_length=20,
        description="Número de identificación (RUC, cédula, pasaporte, etc.)",
        examples=["1712345678"],
    )
    razon_social: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Razón social o nombre completo del cliente",
        examples=["JUAN PÉREZ"],
    )
    direccion: Optional[str] = Field(
        None,
        max_length=500,
        description="Dirección del cliente",
    )
    email: Optional[str] = Field(
        None,
        max_length=255,
        description="Correo electrónico del cliente",
    )
    telefono: Optional[str] = Field(
        None,
        max_length=20,
        description="Número de teléfono del cliente",
    )

    @field_validator("tipo_identificacion")
    @classmethod
    def validate_tipo_identificacion(cls, v: str) -> str:
        """Valida que el tipo de identificación sea válido según Tabla 7 del SRI"""
        validos = {"04", "05", "06", "07", "08"}
        if v not in validos:
            raise ValueError(
                f"Tipo de identificación inválido: {v}. "
                f"Válidos: 04 (RUC), 05 (Cédula), 06 (Pasaporte), 07 (Consumidor Final), 08 (Exterior)"
            )
        return v

    @field_validator("identificacion")
    @classmethod
    def validate_identificacion(cls, v: str) -> str:
        """Validación básica del número de identificación"""
        v = v.strip()
        if not v:
            raise ValueError("La identificación no puede estar vacía")
        return v

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        """Validación básica del formato de correo electrónico"""
        if v is not None and v.strip():
            # Validación simple de formato de email
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", v.strip()):
                raise ValueError("Formato de correo electrónico inválido")
            return v.strip()
        return v


class ClientUpdate(BaseModel):
    """Esquema para actualizar un cliente"""
    tipo_identificacion: Optional[str] = Field(
        None,
        max_length=2,
        description="Tipo de identificación SRI",
    )
    identificacion: Optional[str] = Field(
        None,
        max_length=20,
        description="Número de identificación",
    )
    razon_social: Optional[str] = Field(
        None,
        min_length=1,
        max_length=255,
        description="Razón social o nombre completo",
    )
    direccion: Optional[str] = Field(
        None,
        max_length=500,
        description="Dirección del cliente",
    )
    email: Optional[str] = Field(
        None,
        max_length=255,
        description="Correo electrónico",
    )
    telefono: Optional[str] = Field(
        None,
        max_length=20,
        description="Número de teléfono",
    )
    is_active: Optional[bool] = Field(
        None,
        description="Indica si el cliente está activo",
    )

    @field_validator("tipo_identificacion")
    @classmethod
    def validate_tipo_identificacion(cls, v: Optional[str]) -> Optional[str]:
        """Valida que el tipo de identificación sea válido"""
        if v is not None and v not in {"04", "05", "06", "07", "08"}:
            raise ValueError(
                f"Tipo de identificación inválido: {v}. "
                f"Válidos: 04, 05, 06, 07, 08"
            )
        return v

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        """Validación básica del formato de correo electrónico"""
        if v is not None and v.strip():
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", v.strip()):
                raise ValueError("Formato de correo electrónico inválido")
            return v.strip()
        return v


class ClientResponse(BaseModel):
    """Esquema de respuesta para un cliente"""
    id: str = Field(..., description="ID único del cliente")
    company_id: str = Field(..., description="ID de la empresa")
    tipo_identificacion: str = Field(..., description="Tipo de identificación SRI")
    identificacion: str = Field(..., description="Número de identificación")
    razon_social: str = Field(..., description="Razón social o nombre completo")
    direccion: Optional[str] = Field(None, description="Dirección del cliente")
    email: Optional[str] = Field(None, description="Correo electrónico")
    telefono: Optional[str] = Field(None, description="Número de teléfono")
    is_default_consumer: bool = Field(..., description="Indica si es Consumidor Final por defecto")
    is_active: bool = Field(..., description="Indica si está activo")
    created_at: datetime = Field(..., description="Fecha de creación")
    updated_at: datetime = Field(..., description="Fecha de actualización")

    model_config = {"from_attributes": True}
