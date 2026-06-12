"""
ContaEC - Configuración de la base de datos
Soporte asíncrono para SQLite (aiosqlite) y PostgreSQL (asyncpg)
Detección automática del tipo de base de datos según la URL configurada
"""
from datetime import datetime
from typing import AsyncGenerator
from uuid import uuid4

from sqlalchemy import MetaData, event
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import get_settings

# Convención de nombres para restricciones (compatible con Alembic)
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)


class Base(DeclarativeBase):
    """Clase base declarativa para todos los modelos SQLAlchemy"""
    metadata = metadata


# Configuración del engine asíncrono
settings = get_settings()

# Parámetros específicos según el tipo de base de datos
engine_kwargs: dict = {}
if settings.database_url_async.startswith("sqlite"):
    # SQLite requiere check_same_thread=False en modo asíncrono
    engine_kwargs["connect_args"] = {"check_same_thread": False}
else:
    # PostgreSQL - pool de conexiones optimizado
    engine_kwargs["pool_size"] = 20
    engine_kwargs["max_overflow"] = 10
    engine_kwargs["pool_pre_ping"] = True
    engine_kwargs["pool_recycle"] = 3600

engine = create_async_engine(
    settings.database_url_async,
    echo=settings.DEBUG,
    **engine_kwargs,
)

# Configuración específica para SQLite: habilitar Foreign Keys
if settings.database_url_async.startswith("sqlite"):
    @event.listens_for(engine.sync_engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        """Habilitar Foreign Keys en SQLite"""
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA busy_timeout=5000")
        cursor.close()

# Fábrica de sesiones asíncronas
async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependencia de FastAPI que proporciona una sesión de base de datos asíncrona.
    Utiliza el patrón `async with` para garantizar el cierre de la sesión.

    NOTA ARQUITECTURAL: Este generador realiza un commit implícito al finalizar
    exitosamente la petición. Esto es un acoplamiento que debe ser refactorizado
    en el futuro: los endpoints deberían llamar a `await db.commit()` explícitamente.

    Si se elimina el commit automático, todos los endpoints de escritura que solo
    llaman a `await db.flush()` dejarán de persistir datos silenciosamente.
    Hay ~218 instancias de `await db.flush()` sin `await db.commit()` en los endpoints.

    Uso:
        @app.get("/items")
        async def get_items(db: AsyncSession = Depends(get_db)):
            ...
    """
    async with async_session_factory() as session:
        try:
            yield session
            # TODO: Remove implicit commit - requires auditing ~218 flush()-only endpoints
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        # session.close() is handled by async with context manager


async def init_db() -> None:
    """
    Inicializa la base de datos creando todas las tablas.
    Se debe llamar al iniciar la aplicación.
    
    Para PostgreSQL en producción, se recomienda usar Alembic
    para migraciones en lugar de create_all.
    """
    async with engine.begin() as conn:
        # Importar todos los modelos para que Base.metadata los conozca
        import app.models  # noqa: F401

        await conn.run_sync(Base.metadata.create_all)


async def close_db() -> None:
    """
    Cierra la conexión a la base de datos.
    Se debe llamar al detener la aplicación.
    """
    await engine.dispose()
