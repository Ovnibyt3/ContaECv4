"""
ContaEC - Utilidades de seguridad
Hashing de contraseñas con bcrypt, creación y verificación de tokens JWT
Soporte para revocación de tokens (blacklist) y rotación de refresh tokens
"""
import secrets
from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.database import get_db
from app.core.token_blacklist import get_token_blacklist

# Esquema de autenticación OAuth2 con Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

settings = get_settings()


# ==========================================
# Funciones de hashing de contraseñas
# ==========================================

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que una contraseña en texto plano coincida con su hash.
    
    Args:
        plain_password: Contraseña en texto plano
        hashed_password: Hash bcrypt de la contraseña almacenada
    
    Returns:
        True si la contraseña coincide, False en caso contrario
    """
    if isinstance(plain_password, str):
        plain_password = plain_password.encode('utf-8')
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Genera el hash bcrypt de una contraseña.
    
    Args:
        password: Contraseña en texto plano
    
    Returns:
        Hash bcrypt de la contraseña
    """
    if isinstance(password, str):
        password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed.decode('utf-8')


# ==========================================
# Funciones de tokens JWT
# ==========================================

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None,
) -> str:
    """
    Crea un token de acceso JWT con JTI para revocación.
    
    Args:
        data: Payload del token (debe incluir 'sub' con el ID del usuario)
        expires_delta: Tiempo de expiración personalizado.
                      Si no se especifica, usa JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    
    Returns:
        Token JWT codificado como string
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({
        "exp": expire,
        "type": "access",
        "jti": secrets.token_urlsafe(16),  # Unique ID for token revocation
    })
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


def create_refresh_token(
    data: dict,
    expires_delta: Optional[timedelta] = None,
) -> str:
    """
    Crea un token de refresco JWT con JTI para rotación y revocación.
    
    Args:
        data: Payload del token (debe incluir 'sub' con el ID del usuario)
        expires_delta: Tiempo de expiración personalizado.
                      Si no se especifica, usa JWT_REFRESH_TOKEN_EXPIRE_DAYS
    
    Returns:
        Token JWT de refresco codificado como string
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS
        )
    to_encode.update({
        "exp": expire,
        "type": "refresh",
        "jti": secrets.token_urlsafe(16),  # Unique ID for rotation tracking
    })
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


def verify_token(token: str, token_type: str = "access") -> Optional[dict]:
    """
    Verifica y decodifica un token JWT.
    Comprueba que el token no esté revocado en la blacklist.
    
    Args:
        token: Token JWT codificado
        token_type: Tipo esperado del token ('access' o 'refresh')
    
    Returns:
        Payload del token decodificado, o None si el token es inválido
    
    Raises:
        HTTPException: Si el token es inválido, ha expirado, está revocado, o el tipo no coincide
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    revoked_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token revocado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        # Verificar tipo de token
        if payload.get("type") != token_type:
            raise credentials_exception

        # Verificar si el token está revocado
        jti = payload.get("jti")
        if jti:
            blacklist = get_token_blacklist()
            if blacklist.is_revoked(jti):
                raise revoked_exception

        return payload
    except JWTError:
        raise credentials_exception


def revoke_token(payload: dict) -> None:
    """
    Revoca un token JWT añadiendo su JTI a la blacklist.
    
    Args:
        payload: Payload decodificado del token a revocar
    """
    jti = payload.get("jti")
    exp = payload.get("exp")
    if jti and exp:
        blacklist = get_token_blacklist()
        blacklist.revoke_token(jti, exp)


# ==========================================
# Dependencia de usuario actual
# ==========================================

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    """
    Dependencia de FastAPI que obtiene el usuario actual a partir del token JWT.
    Verifica que el token no esté revocado.
    
    Args:
        token: Token JWT del encabezado Authorization
        db: Sesión de base de datos asíncrona
    
    Returns:
        Objeto User del usuario autenticado
    
    Raises:
        HTTPException: Si el token es inválido, revocado, o el usuario no existe
    """
    from app.models.user import User

    payload = verify_token(token, token_type="access")
    user_id: Optional[str] = payload.get("sub")
    
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudieron validar las credenciales",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Buscar por string (compatible con SQLite y PostgreSQL)
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo",
        )
    
    return user


async def get_current_active_admin(
    current_user=Depends(get_current_user),
):
    """
    Dependencia de FastAPI que verifica que el usuario actual sea administrador.
    
    Args:
        current_user: Usuario actual (inyectado por get_current_user)
    
    Returns:
        Objeto User del administrador autenticado
    
    Raises:
        HTTPException: Si el usuario no es administrador
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permisos de administrador",
        )
    return current_user
