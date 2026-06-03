"""
ContaEC - Configuración de la aplicación
Lee las variables de entorno desde el archivo .env usando pydantic-settings
"""
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuración principal de la aplicación ContaEC.
    Todas las variables se cargan desde el archivo .env
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ==========================================
    # Aplicación
    # ==========================================
    APP_NAME: str = "ContaEC"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    DEBUG: bool = True
    SECRET_KEY: str = "dev-only-change-in-production-USE-ENV-VAR"
    ENCRYPTION_KEY: str = "dev-only-change-in-production-USE-ENV-VAR"

    # ==========================================
    # Base de datos
    # ==========================================
    DATABASE_URL: str = "sqlite+aiosqlite:///./contaec.db"

    # PostgreSQL (producción)
    POSTGRES_USER: str = "contaec_user"
    POSTGRES_PASSWORD: str = ""
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "contaec_db"

    # ==========================================
    # Autenticación JWT
    # ==========================================
    JWT_SECRET_KEY: str = "dev-only-change-in-production-USE-ENV-VAR"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # ==========================================
    # Credenciales Admin (pre-configuradas)
    # ==========================================
    ADMIN_EMAIL: str = "steve.mejia@tymtechnology.shop"
    # Admin password must be set via ADMIN_PASSWORD env var in production
    ADMIN_PASSWORD: str = "Vitaestcum21.."

    # ==========================================
    # Servicios Web del SRI - Pruebas (Testing)
    # ==========================================
    SRI_WS_RECEPCION_PRUEBAS: str = (
        "https://celcer.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl"
    )
    SRI_WS_AUTORIZACION_PRUEBAS: str = (
        "https://celcer.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl"
    )

    # ==========================================
    # Servicios Web del SRI - Producción
    # ==========================================
    SRI_WS_RECEPCION_PRODUCCION: str = (
        "https://cel.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl"
    )
    SRI_WS_AUTORIZACION_PRODUCCION: str = (
        "https://cel.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl"
    )

    # ==========================================
    # Servicios Web de Consulta del SRI - Pruebas
    # ==========================================
    SRI_WS_CONSULTA_PRUEBAS: str = (
        "https://celcer.sri.gob.ec/comprobantes-electronicos-ws/ConsultaComprobante?wsdl"
    )
    SRI_WS_CONSULTA_FACTURA_PRUEBAS: str = (
        "https://celcer.sri.gob.ec/comprobantes-electronicos-ws/ConsultaFactura?wsdl"
    )

    # ==========================================
    # Servicios Web de Consulta del SRI - Producción
    # ==========================================
    SRI_WS_CONSULTA_PRODUCCION: str = (
        "https://cel.sri.gob.ec/comprobantes-electronicos-ws/ConsultaComprobante?wsdl"
    )
    SRI_WS_CONSULTA_FACTURA_PRODUCCION: str = (
        "https://cel.sri.gob.ec/comprobantes-electronicos-ws/ConsultaFactura?wsdl"
    )

    # ==========================================
    # Configuración de Respaldos
    # ==========================================
    BACKUP_DIR: str = "./backups"
    BACKUP_ENCRYPTION_KEY: str = ""

    # ==========================================
    # ClamAV (Antivirus)
    # ==========================================
    CLAMAV_ENABLED: bool = False
    CLAMAV_SOCKET: str = "/var/run/clamav/clamd.ctl"
    CLAMAV_HOST: str = "127.0.0.1"
    CLAMAV_PORT: int = 3310

    # ==========================================
    # VirusTotal
    # ==========================================
    VIRUSTOTAL_ENABLED: bool = False
    VIRUSTOTAL_API_KEY: str = ""

    # ==========================================
    # CORS
    # ==========================================
    CORS_ORIGINS: str = "http://localhost:3000,https://conta.tymtechnology.shop"

    # ==========================================
    # Rate Limiting
    # ==========================================
    RATE_LIMIT_PER_MINUTE: int = 60

    # ==========================================
    # Servidor
    # ==========================================
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000

    # ==========================================
    # Almacenamiento Volátil
    # ==========================================
    TEMP_DIR: str = "./temp"
    UPLOAD_DIR: str = "./uploads"

    # ==========================================
    # Propiedades derivadas
    # ==========================================
    @property
    def is_production(self) -> bool:
        """Indica si el ambiente es producción"""
        return self.APP_ENV.lower() == "production"

    @property
    def is_development(self) -> bool:
        """Indica si el ambiente es desarrollo"""
        return self.APP_ENV.lower() == "development"

    @property
    def sri_ws_recepcion(self) -> str:
        """URL del servicio web de recepción del SRI según el ambiente"""
        if self.is_production:
            return self.SRI_WS_RECEPCION_PRODUCCION
        return self.SRI_WS_RECEPCION_PRUEBAS

    @property
    def sri_ws_autorizacion(self) -> str:
        """URL del servicio web de autorización del SRI según el ambiente"""
        if self.is_production:
            return self.SRI_WS_AUTORIZACION_PRODUCCION
        return self.SRI_WS_AUTORIZACION_PRUEBAS

    @property
    def sri_ws_consulta(self) -> str:
        """URL del servicio web de consulta del SRI según el ambiente"""
        if self.is_production:
            return self.SRI_WS_CONSULTA_PRODUCCION
        return self.SRI_WS_CONSULTA_PRUEBAS

    @property
    def sri_ws_consulta_factura(self) -> str:
        """URL del servicio web de consulta de factura del SRI según el ambiente"""
        if self.is_production:
            return self.SRI_WS_CONSULTA_FACTURA_PRODUCCION
        return self.SRI_WS_CONSULTA_FACTURA_PRUEBAS

    @property
    def database_url_async(self) -> str:
        """
        URL asíncrona de la base de datos.
        
        Prioridad:
        1. Si DATABASE_URL está configurada y apunta a PostgreSQL -> usar PostgreSQL
        2. Si DATABASE_URL está configurada y apunta a SQLite -> usar SQLite (solo desarrollo)
        3. Si APP_ENV es 'production' -> construir URL PostgreSQL desde settings individuales
        4. Fallback -> SQLite local (desarrollo)
        
        NOTA: En producción (APP_ENV=production) SOLO se permite PostgreSQL.
        SQLite NO es compatible con carga de trabajo multi-usuario concurrente
        por las siguientes razones:
        - SQLite usa locking a nivel de archivo (solo 1 escritor a la vez)
        - No soporta conexiones concurrentes de escritura
        - No tiene pool de conexiones real
        - PRAGMA foreign_keys no es persistente (debe activarse por conexión)
        - No soporta NOTIFY/LISTEN para eventos en tiempo real
        - Funciones como func.strftime son incompatibles con PostgreSQL
        - Riesgo de corrupción bajo carga concurrente
        """
        url = self.DATABASE_URL
        
        # Si la URL viene de Prisma (file:...), usar SQLite aiosqlite por defecto
        if url.startswith("file:"):
            url = "sqlite+aiosqlite:///./contaec.db"
        # Si es SQLite sincrónico, convertir a asíncrono
        elif url.startswith("sqlite:///") and "aiosqlite" not in url:
            url = url.replace("sqlite:///", "sqlite+aiosqlite:///")
        # Si es SQLite relativo sin protocolo, agregar protocolo aiosqlite
        elif url.endswith(".db") and ":///" not in url:
            url = f"sqlite+aiosqlite:///{url}"
        # Si es PostgreSQL sincrónico, convertir a asíncrono
        elif url.startswith("postgresql://") and "asyncpg" not in url:
            url = url.replace("postgresql://", "postgresql+asyncpg://")
        # Si ya tiene asyncpg, usarla directamente
        elif url.startswith("postgresql+asyncpg://"):
            pass  # Ya está en el formato correcto
        # Si es producción y no hay URL explícita, construir PostgreSQL
        elif self.is_production and not url.startswith("sqlite"):
            url = (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )
        
        # BLOQUEAR SQLite en producción
        if self.is_production and url.startswith("sqlite"):
            raise RuntimeError(
                "⛔ PRODUCCIÓN: SQLite NO está permitido en ambiente de producción. "
                "SQLite no soporta concurrencia de escritura, tiene riesgo de corrupción "
                "bajo carga, y funciones como func.strftime son incompatibles con PostgreSQL. "
                "Configure DATABASE_URL con PostgreSQL en las variables de entorno: "
                "DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/dbname"
            )
        
        return url

    @property
    def cors_origins_list(self) -> list[str]:
        """Lista de orígenes CORS permitidos"""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]
    
    def validate_production_secrets(self) -> list[str]:
        """
        Valida que los secrets no tengan valores por defecto en producción.
        Retorna una lista de advertencias (vacía si todo está bien).
        """
        warnings = []
        
        insecure_defaults = {
            "SECRET_KEY": "dev-only-change-in-production-USE-ENV-VAR",
            "ENCRYPTION_KEY": "dev-only-change-in-production-USE-ENV-VAR",
            "JWT_SECRET_KEY": "dev-only-change-in-production-USE-ENV-VAR",
        }
        
        for key, insecure_value in insecure_defaults.items():
            if getattr(self, key) == insecure_value:
                warnings.append(
                    f"⚠️  {key} tiene valor por defecto inseguro. "
                    f"Configure la variable de entorno {key} con un valor seguro."
                )
        
        if not self.ADMIN_PASSWORD:
            warnings.append(
                "⚠️  ADMIN_PASSWORD no configurada. Configure la variable de entorno "
                "ADMIN_PASSWORD con la contraseña del administrador."
            )
        
        if not self.BACKUP_ENCRYPTION_KEY:
            warnings.append(
                "⚠️  BACKUP_ENCRYPTION_KEY no configurada. Los respaldos no estarán cifrados."
            )
        
        if not self.POSTGRES_PASSWORD:
            warnings.append(
                "⚠️  POSTGRES_PASSWORD no configurada. No se podrá conectar a PostgreSQL."
            )
        
        return warnings


@lru_cache()
def get_settings() -> Settings:
    """
    Obtiene la configuración de la aplicación (caché en memoria).
    Se utiliza como dependencia en FastAPI.
    """
    return Settings()
