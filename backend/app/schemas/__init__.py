"""
ContaEC - Esquemas Pydantic
Importa todos los esquemas para facilitar el acceso
"""
from app.schemas.auth import (
    PasswordChange,
    RefreshTokenRequest,
    Token,
    TokenData,
    UserLogin,
    UserRegister,
    UserResponse,
    UserUpdate,
)
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate,
    EstablishmentCreate,
    EstablishmentResponse,
)
from app.schemas.sri import (
    IVATarifa,
    ICETarifa,
    RetencionIVA,
    RetencionRenta,
    TipoComprobante,
    TipoIdentificacion,
    FormaPago,
    EstadoComprobante,
    # Datos de catálogos
    IVA_TARIFAS,
    ICE_TARIFAS,
    RETENCION_IVA,
    RETENCION_RENTA,
    TIPOS_COMPROBANTE,
    TIPOS_IDENTIFICACION,
    FORMAS_PAGO,
    ESTADOS_COMPROBANTE,
    CONTRIBUYENTE_TIPOS,
    REGIMEN_TIPOS,
)

__all__ = [
    # Autenticación
    "UserLogin",
    "UserRegister",
    "UserResponse",
    "UserUpdate",
    "PasswordChange",
    "Token",
    "TokenData",
    "RefreshTokenRequest",
    # Empresa
    "CompanyCreate",
    "CompanyResponse",
    "CompanyUpdate",
    "EstablishmentCreate",
    "EstablishmentResponse",
    # Catálogos SRI - Esquemas
    "IVATarifa",
    "ICETarifa",
    "RetencionIVA",
    "RetencionRenta",
    "TipoComprobante",
    "TipoIdentificacion",
    "FormaPago",
    "EstadoComprobante",
    # Catálogos SRI - Datos
    "IVA_TARIFAS",
    "ICE_TARIFAS",
    "RETENCION_IVA",
    "RETENCION_RENTA",
    "TIPOS_COMPROBANTE",
    "TIPOS_IDENTIFICACION",
    "FORMAS_PAGO",
    "ESTADOS_COMPROBANTE",
    "CONTRIBUYENTE_TIPOS",
    "REGIMEN_TIPOS",
]
