"""
ContaEC - Configuración de Rate Limiting con slowapi
Implementa limitación de tasa específica por ruta para proteger endpoints críticos.
"""
from slowapi import Limiter
from slowapi.util import get_remote_address

# Crear instancia del limitador con almacenamiento en memoria
# Para producción con múltiples workers, usar Redis como backend
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["60/minute"],  # Límite global por defecto
)

# Límites específicos para rutas críticas
# Estos decoradores se aplican directamente en los endpoints

# Auth endpoints - Más estrictos para prevenir fuerza bruta
AUTH_LOGIN_LIMIT = "10/minute"
AUTH_REGISTER_LIMIT = "5/minute"
AUTH_CHANGE_PASSWORD_LIMIT = "10/minute"
AUTH_REFRESH_LIMIT = "20/minute"

# Backup endpoints - Prevenir DoS por uso de CPU/memoria
BACKUP_CREATE_LIMIT = "5/hour"
BACKUP_RESTORE_LIMIT = "2/hour"

# Uploads - Prevenir spam de archivos pesados
UPLOAD_LIMIT = "30/minute"

# Comprobantes - Prevenir colapso de conexión con SRI
COMPROBANTES_SEND_LIMIT = "20/minute"
COMPROBANTES_QUERY_LIMIT = "60/minute"

# ML/AI - Prevenir sobrecarga por solicitudes pesadas
ML_AI_LIMIT = "10/minute"

# Accounting - Operaciones críticas
ACCOUNTING_WRITE_LIMIT = "30/minute"
