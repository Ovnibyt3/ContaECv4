"""
ContaEC - Utilidades de cifrado
Cifrado simétrico Fernet para configuraciones sensibles del usuario
(firma digital, contraseñas SMTP, claves de respaldo, etc.)
"""
import base64
import json
from typing import Any, Dict

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from app.core.config import get_settings

settings = get_settings()


def _derive_fernet_key(key: str) -> bytes:
    """
    Deriva una clave Fernet de 32 bytes a partir de una cadena de texto.
    Utiliza PBKDF2HMAC con SHA-256 para derivar la clave.
    
    Args:
        key: Cadena de texto base para derivar la clave
    
    Returns:
        Clave de 32 bytes codificada en base64url para Fernet
    """
    # Usar el SECRET_KEY de la aplicación como salt adicional
    salt = settings.SECRET_KEY.encode("utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480_000,
    )
    derived_key = kdf.derive(key.encode("utf-8"))
    return base64.urlsafe_b64encode(derived_key)


def _get_fernet(key: str) -> Fernet:
    """
    Obtiene una instancia de Fernet con la clave derivada.
    
    Args:
        key: Clave de cifrado en texto plano
    
    Returns:
        Instancia de Fernet configurada
    """
    fernet_key = _derive_fernet_key(key)
    return Fernet(fernet_key)


def encrypt_user_config(data: Dict[str, Any], key: str) -> str:
    """
    Cifra un diccionario de configuración del usuario.
    
    Utiliza cifrado simétrico Fernet (AES-128-CBC con HMAC-SHA256).
    Los datos se serializan a JSON antes de cifrar.
    
    Args:
        data: Diccionario con los datos a cifrar
        key: Clave de cifrado (generalmente la clave de respaldo del usuario)
    
    Returns:
        Cadena cifrada codificada en base64
    
    Example:
        >>> config = {"smtp_password": "secret123", "signature_pass": "pass"}
        >>> encrypted = encrypt_user_config(config, "user-encryption-key")
        >>> isinstance(encrypted, str)
        True
    """
    fernet = _get_fernet(key)
    json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
    encrypted_bytes = fernet.encrypt(json_data)
    return encrypted_bytes.decode("utf-8")


def decrypt_user_config(encrypted: str, key: str) -> Dict[str, Any]:
    """
    Descifra una cadena cifrada y la deserializa a un diccionario.
    
    Args:
        encrypted: Cadena cifrada codificada en base64
        key: Clave de cifrado (la misma usada para cifrar)
    
    Returns:
        Diccionario con los datos descifrados
    
    Raises:
        ValueError: Si la clave es incorrecta o los datos están corruptos
    
    Example:
        >>> config = {"smtp_password": "secret123"}
        >>> encrypted = encrypt_user_config(config, "user-key")
        >>> decrypted = decrypt_user_config(encrypted, "user-key")
        >>> decrypted == config
        True
    """
    try:
        fernet = _get_fernet(key)
        decrypted_bytes = fernet.decrypt(encrypted.encode("utf-8"))
        json_str = decrypted_bytes.decode("utf-8")
        return json.loads(json_str)
    except InvalidToken:
        raise ValueError(
            "No se pudo descifrar la configuración. "
            "La clave de cifrado es incorrecta o los datos están corruptos."
        )
    except json.JSONDecodeError:
        raise ValueError(
            "Los datos descifrados no son un JSON válido. "
            "El cifrado puede estar corrupto."
        )


def generate_encryption_key() -> str:
    """
    Genera una nueva clave de cifrado Fernet aleatoria.
    Útil para crear claves de respaldo de usuarios.
    
    Returns:
        Clave de cifrado Fernet codificada en base64url
    """
    return Fernet.generate_key().decode("utf-8")


def encrypt_field(value: str, key: str) -> str:
    """
    Cifra un campo individual (por ejemplo, una contraseña SMTP).
    
    Args:
        value: Valor en texto plano a cifrar
        key: Clave de cifrado
    
    Returns:
        Valor cifrado codificado en base64
    """
    fernet = _get_fernet(key)
    encrypted_bytes = fernet.encrypt(value.encode("utf-8"))
    return encrypted_bytes.decode("utf-8")


def decrypt_field(encrypted: str, key: str) -> str:
    """
    Descifra un campo individual cifrado.
    
    Args:
        encrypted: Valor cifrado codificado en base64
        key: Clave de cifrado
    
    Returns:
        Valor en texto plano
    
    Raises:
        ValueError: Si la clave es incorrecta o los datos están corruptos
    """
    try:
        fernet = _get_fernet(key)
        decrypted_bytes = fernet.decrypt(encrypted.encode("utf-8"))
        return decrypted_bytes.decode("utf-8")
    except InvalidToken:
        raise ValueError(
            "No se pudo descifrar el campo. "
            "La clave de cifrado es incorrecta o los datos están corruptos."
        )
