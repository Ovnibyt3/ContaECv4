"""
ContaEC - Módulo de escaneo de malware
ClamAV (escaneo local vía clamd) + VirusTotal (escaneo en la nube, opcional)
Soporta degradación graceful cuando los servicios no están disponibles

NOTA: Las operaciones síncronas (pyclamd) se ejecutan en un executor
para no bloquear el event loop de asyncio.
"""
import asyncio
import logging
import tempfile
import os
from functools import partial
from typing import Optional

import aiofiles

from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


class ScanResult:
    """Resultado del escaneo de malware"""
    def __init__(
        self,
        is_clean: bool,
        scanner: str = "none",
        threat: Optional[str] = None,
        details: Optional[str] = None,
    ):
        self.is_clean = is_clean
        self.scanner = scanner
        self.threat = threat
        self.details = details

    def to_dict(self) -> dict:
        return {
            "is_clean": self.is_clean,
            "scanner": self.scanner,
            "threat": self.threat,
            "details": self.details,
        }


class ClamAVScanner:
    """
    Escáner ClamAV vía clamd (demonio local).
    
    Soporta dos modos de conexión:
    - Unix socket (predeterminado): /var/run/clamav/clamd.ctl
    - TCP: host:port (127.0.0.1:3310)
    
    Si ClamAV no está disponible, devuelve un resultado "limpio"
    con una advertencia en los logs.
    """

    def __init__(self):
        self._available: Optional[bool] = None
        self._cd = None

    def _try_connect(self) -> bool:
        """Intenta conectar al demonio ClamAV"""
        if self._available is not None:
            return self._available

        try:
            import pyclamd

            # Intentar primero vía Unix socket
            try:
                self._cd = pyclamd.ClamdUnixSocket(
                    path=settings.CLAMAV_SOCKET
                )
                self._cd.ping()
                self._available = True
                logger.info("ClamAV conectado vía Unix socket")
                return True
            except Exception:
                pass

            # Intentar vía TCP
            try:
                self._cd = pyclamd.ClamdNetworkSocket(
                    host=settings.CLAMAV_HOST,
                    port=settings.CLAMAV_PORT,
                )
                self._cd.ping()
                self._available = True
                logger.info("ClamAV conectado vía TCP")
                return True
            except Exception:
                pass

            self._available = False
            logger.warning(
                "ClamAV no disponible. Los archivos NO serán escaneados localmente. "
                "Instale y configure ClamAV para protección completa."
            )
            return False

        except ImportError:
            self._available = False
            logger.warning("pyclamd no instalado. ClamAV no disponible.")
            return False

    def _scan_file_sync(self, file_path: str) -> ScanResult:
        """Escaneo síncrono de archivo con ClamAV (para ejecutar en executor)."""
        if not self._try_connect():
            return ScanResult(
                is_clean=True,
                scanner="clamav",
                details="ClamAV no disponible - escaneo omitido",
            )

        try:
            result = self._cd.scan_file(file_path)

            if result is None:
                return ScanResult(
                    is_clean=True,
                    scanner="clamav",
                    details="Archivo limpio",
                )

            for filename, (status, threat_name) in result.items():
                if status == "FOUND":
                    logger.warning(
                        f"⚠️ MALWARE DETECTADO por ClamAV: {threat_name} en {filename}"
                    )
                    return ScanResult(
                        is_clean=False,
                        scanner="clamav",
                        threat=threat_name,
                        details=f"Amenaza detectada: {threat_name}",
                    )

            return ScanResult(
                is_clean=True,
                scanner="clamav",
                details="Archivo limpio",
            )

        except Exception as e:
            logger.error(f"Error escaneando con ClamAV: {e}")
            return ScanResult(
                is_clean=True,  # No bloquear si falla el escáner
                scanner="clamav",
                details=f"Error en escaneo: {str(e)}",
            )

    async def scan_file(self, file_path: str) -> ScanResult:
        """
        Escanea un archivo con ClamAV.
        Ejecuta el escaneo en un executor para no bloquear el event loop.
        """
        if not settings.CLAMAV_ENABLED:
            return ScanResult(
                is_clean=True,
                scanner="clamav",
                details="ClamAV deshabilitado en configuración",
            )

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, partial(self._scan_file_sync, file_path)
        )

    def _scan_bytes_sync(self, content: bytes) -> ScanResult:
        """Escaneo síncrono de bytes con ClamAV (para ejecutar en executor)."""
        if not self._try_connect():
            return ScanResult(
                is_clean=True,
                scanner="clamav",
                details="ClamAV no disponible - escaneo omitido",
            )

        try:
            result = self._cd.scan_stream(content)

            if result is None:
                return ScanResult(
                    is_clean=True,
                    scanner="clamav",
                    details="Archivo limpio",
                )

            for stream, (status, threat_name) in result.items():
                if status == "FOUND":
                    logger.warning(
                        f"⚠️ MALWARE DETECTADO por ClamAV (stream): {threat_name}"
                    )
                    return ScanResult(
                        is_clean=False,
                        scanner="clamav",
                        threat=threat_name,
                        details=f"Amenaza detectada: {threat_name}",
                    )

            return ScanResult(
                is_clean=True,
                scanner="clamav",
                details="Archivo limpio",
            )

        except Exception as e:
            logger.error(f"Error escaneando stream con ClamAV: {e}")
            return ScanResult(
                is_clean=True,
                scanner="clamav",
                details=f"Error en escaneo: {str(e)}",
            )

    async def scan_bytes(self, content: bytes) -> ScanResult:
        """
        Escanea contenido en memoria con ClamAV.
        Ejecuta el escaneo en un executor para no bloquear el event loop.
        """
        if not settings.CLAMAV_ENABLED:
            return ScanResult(
                is_clean=True,
                scanner="clamav",
                details="ClamAV deshabilitado en configuración",
            )

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, partial(self._scan_bytes_sync, content)
        )


class VirusTotalScanner:
    """
    Escáner VirusTotal vía API v3.
    
    Requiere una API key válida. Es opcional y se activa por usuario.
    Nota: La API gratuita tiene un límite de 4 requests/minuto.
    """

    def __init__(self):
        self._api_key = settings.VIRUSTOTAL_API_KEY

    async def scan_file(self, file_path: str) -> ScanResult:
        """
        Escanea un archivo con VirusTotal.
        
        Args:
            file_path: Ruta del archivo a escanear
            
        Returns:
            ScanResult con el resultado del escaneo
        """
        if not self._api_key:
            return ScanResult(
                is_clean=True,
                scanner="virustotal",
                details="API key de VirusTotal no configurada",
            )

        try:
            import vt

            async with vt.Client(self._api_key) as client:
                # Calcular hash del archivo
                import hashlib

                with open(file_path, "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()

                # Primero intentar consultar por hash (más rápido, no consume cuota)
                try:
                    file_report = await client.get_object(f"/files/{file_hash}")
                    stats = file_report.last_analysis_stats

                    malicious = stats.get("malicious", 0)
                    total = sum(stats.values())

                    if malicious > 0:
                        # Obtener detalles de las detecciones
                        threats = []
                        results = file_report.last_analysis_results
                        for engine, result in results.items():
                            if result.get("category") == "malicious":
                                threats.append(
                                    f"{engine}: {result.get('result', 'unknown')}"
                                )

                        threat_list = "; ".join(threats[:5])
                        logger.warning(
                            f"⚠️ VirusTotal: {malicious}/{total} motores detectaron amenaza"
                        )
                        return ScanResult(
                            is_clean=False,
                            scanner="virustotal",
                            threat=f"{malicious}/{total} detecciones",
                            details=threat_list,
                        )

                    return ScanResult(
                        is_clean=True,
                        scanner="virustotal",
                        details=f"Archivo limpio ({total} motores)",
                    )

                except vt.error.APIError as e:
                    if e.code == "NotFoundError":
                        # Archivo no conocido - subir para análisis
                        with open(file_path, "rb") as f:
                            analysis = await client.scan_file(f, wait_for_completion=True)

                        stats = analysis.stats
                        malicious = stats.get("malicious", 0)

                        if malicious > 0:
                            return ScanResult(
                                is_clean=False,
                                scanner="virustotal",
                                threat=f"{malicious} detecciones",
                                details="Archivo subido y analizado",
                            )

                        return ScanResult(
                            is_clean=True,
                            scanner="virustotal",
                            details="Archivo limpio (recién analizado)",
                        )
                    raise

        except ImportError:
            logger.warning("vt-py no instalado. VirusTotal no disponible.")
            return ScanResult(
                is_clean=True,
                scanner="virustotal",
                details="Librería vt-py no disponible",
            )
        except Exception as e:
            logger.error(f"Error escaneando con VirusTotal: {e}")
            return ScanResult(
                is_clean=True,  # No bloquear si falla
                scanner="virustotal",
                details=f"Error en escaneo: {str(e)}",
            )

    async def scan_bytes(self, content: bytes, filename: str = "upload") -> ScanResult:
        """
        Escanea contenido en memoria con VirusTotal.
        Escribe a archivo temporal y escanea.
        
        Args:
            content: Bytes del archivo a escanear
            filename: Nombre del archivo (para logging)
            
        Returns:
            ScanResult con el resultado del escaneo
        """
        # VirusTotal requiere un archivo físico para escaneo
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{filename}") as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        try:
            return await self.scan_file(tmp_path)
        finally:
            os.unlink(tmp_path)


# Instancias singleton
clamav_scanner = ClamAVScanner()
virustotal_scanner = VirusTotalScanner()


async def scan_upload(
    content: bytes,
    filename: str,
    use_virustotal: bool = False,
) -> list[ScanResult]:
    """
    Escanea un archivo subido con todos los escáneres disponibles.
    
    Args:
        content: Contenido del archivo en bytes
        filename: Nombre del archivo original
        use_virustotal: Si se debe usar VirusTotal (configurable por usuario)
        
    Returns:
        Lista de ScanResult, uno por cada escáner utilizado
    """
    results = []

    # 1. Escaneo ClamAV (siempre si está habilitado)
    clamav_result = await clamav_scanner.scan_bytes(content)
    results.append(clamav_result)

    # 2. Escaneo VirusTotal (opcional, activable por usuario)
    if use_virustotal and settings.VIRUSTOTAL_ENABLED:
        vt_result = await virustotal_scanner.scan_bytes(content, filename)
        results.append(vt_result)

    return results


def is_any_threat_found(results: list[ScanResult]) -> bool:
    """Verifica si algún escáner detectó una amenaza"""
    return any(not r.is_clean for r in results)
