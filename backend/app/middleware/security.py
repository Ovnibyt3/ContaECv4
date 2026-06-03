"""
ContaEC - Middleware de seguridad
Rate limiting, sanitización de entradas, y protección general
"""
import re
import time
import logging
from typing import Callable

from fastapi import Request, Response, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware de limitación de tasa por IP"""
    
    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self._requests: dict[str, list[float]] = {}
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        client_ip = request.client.host if request.client else "unknown"
        current_time = time.time()
        
        # Limpiar solicitudes antiguas
        if client_ip in self._requests:
            self._requests[client_ip] = [
                t for t in self._requests[client_ip]
                if current_time - t < 60
            ]
        else:
            self._requests[client_ip] = []
        
        # Verificar límite
        if len(self._requests[client_ip]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=429,
                detail="Demasiadas solicitudes. Intente nuevamente en un momento."
            )
        
        self._requests[client_ip].append(current_time)
        response = await call_next(request)
        return response


class InputSanitizationMiddleware(BaseHTTPMiddleware):
    """Middleware de sanitización de entradas para prevenir inyecciones"""
    
    # Patrones peligrosos
    SQL_INJECTION_PATTERNS = [
        r"(?i)(\b(union|select|insert|update|delete|drop|alter|create|exec)\b.*\b(from|table|into|where|set)\b)",
        r"(?i)(\b(or|and)\b\s+.*[=<>])",
        r"(?i)(;\s*(drop|delete|update|insert|alter))",
        r"(?i)(xp_|sp_)\w+",
    ]
    
    XSS_PATTERNS = [
        r"<\s*script[^>]*>.*?<\s*/\s*script\s*>",
        r"javascript\s*:",
        r"on\w+\s*=",
        r"<\s*iframe[^>]*>",
        r"<\s*object[^>]*>",
        r"<\s*embed[^>]*>",
    ]
    
    PATH_TRAVERSAL_PATTERNS = [
        r"\.\./",
        r"\.\.\\",
        r"%2e%2e%2f",
        r"%2e%2e/",
        r"..%2f",
        r"..%5c",
    ]
    
    # Rutas que no deben ser validadas en body (contienen XML, firmas, uploads, etc.)
    SKIP_BODY_VALIDATION_PATHS = {
        "/api/v1/uploads",
        "/api/v1/comprobantes/sign",
        "/api/v1/comprobantes/xml",
        "/api/v1/backup",
        "/api/v1/config/signature",
        "/docs",
        "/redoc",
        "/openapi.json",
        "/api/v1/comprobantes",
        "/api/v1/accounting",
    }

    def _check_patterns(self, value: str, source: str, client_ip: str) -> None:
        """Valida un string contra todos los patrones peligrosos."""
        # SQL Injection
        for pattern in self.SQL_INJECTION_PATTERNS:
            if re.search(pattern, value):
                logger.warning(
                    f"SQL Injection detectado desde {client_ip} en {source}: "
                    f"{value[:200]}"
                )
                raise HTTPException(status_code=400, detail="Solicitud inválida")
        
        # XSS
        for pattern in self.XSS_PATTERNS:
            if re.search(pattern, value, re.IGNORECASE | re.DOTALL):
                logger.warning(
                    f"XSS detectado desde {client_ip} en {source}: "
                    f"{value[:200]}"
                )
                raise HTTPException(status_code=400, detail="Solicitud inválida")
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        client_ip = request.client.host if request.client else "unknown"
        
        # 1. Verificar path traversal en la URL
        path = str(request.url.path)
        for pattern in self.PATH_TRAVERSAL_PATTERNS:
            if re.search(pattern, path, re.IGNORECASE):
                logger.warning(f"Path traversal detectado desde {client_ip}: {path}")
                raise HTTPException(status_code=400, detail="Solicitud inválida")
        
        # 2. Verificar query parameters
        query_string = str(request.url.query) if request.url.query else ""
        if query_string:
            self._check_patterns(query_string, "query_params", client_ip)
        
        # 3. Verificar body de la petición (excepto rutas excluidas)
        should_skip = any(
            path.startswith(skip_path) for skip_path in self.SKIP_BODY_VALIDATION_PATHS
        )
        
        if not should_skip and request.method in ("POST", "PUT", "PATCH"):
            try:
                body_bytes = await request.body()
                if body_bytes:
                    body_str = body_bytes.decode("utf-8", errors="replace")
                    # Solo validar si es texto (JSON, form data, etc.)
                    content_type = request.headers.get("content-type", "")
                    if any(ct in content_type for ct in ("json", "form", "text")):
                        self._check_patterns(body_str, "request_body", client_ip)
            except HTTPException:
                raise
            except Exception:
                # Si no se puede leer el body, continuar sin validar
                pass
        
        response = await call_next(request)
        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Middleware para añadir headers de seguridad"""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        return response
