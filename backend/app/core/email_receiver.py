"""
ContaEC - Servicio de Recepción de Correos Electrónicos
Recepción de correos vía IMAP y POP3 para procesamiento
de comprobantes electrónicos recibidos de proveedores

NOTA: Todas las operaciones síncronas (imaplib, poplib) se ejecutan
en un executor para no bloquear el event loop de asyncio.
"""
import asyncio
import email
import imaplib
import logging
import poplib
from email.header import decode_header
from functools import partial
from typing import Optional

logger = logging.getLogger(__name__)


class EmailReceiverError(Exception):
    """Error en el servicio de recepción de correos"""
    pass


def _decode_str(value: Optional[bytes | str]) -> str:
    """Decodifica un valor de encabezado de correo electrónico"""
    if value is None:
        return ""
    if isinstance(value, bytes):
        try:
            return value.decode("utf-8")
        except UnicodeDecodeError:
            try:
                return value.decode("latin-1")
            except UnicodeDecodeError:
                return value.decode("utf-8", errors="replace")
    return str(value)


def _decode_header_value(header_value: str) -> str:
    """Decodifica un encabezado de correo electrónico (Subject, From, etc.)"""
    if not header_value:
        return ""
    decoded_parts = decode_header(header_value)
    result_parts = []
    for part, charset in decoded_parts:
        if isinstance(part, bytes):
            charset = charset or "utf-8"
            try:
                result_parts.append(part.decode(charset))
            except (UnicodeDecodeError, LookupError):
                result_parts.append(part.decode("utf-8", errors="replace"))
        else:
            result_parts.append(part)
    return "".join(result_parts)


def _extract_attachments(msg: email.message.Message) -> list[dict]:
    """Extrae información de los adjuntos de un mensaje de correo"""
    attachments = []
    for part in msg.walk():
        content_disposition = part.get_content_disposition()
        if content_disposition in ("attachment", "inline"):
            filename = part.get_filename()
            if filename:
                filename = _decode_header_value(filename)
                content_type = part.get_content_type()
                size = len(part.get_payload(decode=True) or b"")
                attachments.append({
                    "filename": filename,
                    "content_type": content_type,
                    "size": size,
                    "index": len(attachments),
                })
    return attachments


def _receive_emails_imap_sync(
    host: str,
    port: int,
    user: str,
    password: str,
    ssl: bool = True,
    folder: str = "INBOX",
    limit: int = 50,
) -> list[dict]:
    """Función síncrona para recibir correos vía IMAP (se ejecuta en executor)."""
    try:
        if ssl:
            mail = imaplib.IMAP4_SSL(host, port)
        else:
            mail = imaplib.IMAP4(host, port)

        mail.login(user, password)
        mail.select(folder)

        # Buscar todos los mensajes
        status, message_ids = mail.search(None, "ALL")
        if status != "OK":
            return []

        id_list = message_ids[0].split()
        # Limitar a los más recientes
        id_list = id_list[-limit:] if len(id_list) > limit else id_list
        id_list = list(reversed(id_list))  # Más recientes primero

        emails = []
        for msg_id in id_list:
            status, msg_data = mail.fetch(msg_id, "(RFC822)")
            if status != "OK":
                continue

            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            email_info = {
                "id": _decode_str(msg_id),
                "subject": _decode_header_value(msg.get("Subject", "")),
                "from": _decode_header_value(msg.get("From", "")),
                "to": _decode_header_value(msg.get("To", "")),
                "date": msg.get("Date", ""),
                "attachments": _extract_attachments(msg),
            }
            emails.append(email_info)

        mail.logout()
        logger.info(f"Recibidos {len(emails)} correos vía IMAP de {user}@{host}")
        return emails

    except imaplib.IMAP4.error as e:
        raise EmailReceiverError(f"Error IMAP: {str(e)}")
    except Exception as e:
        raise EmailReceiverError(f"Error al recibir correos vía IMAP: {str(e)}")


def _receive_emails_pop3_sync(
    host: str,
    port: int,
    user: str,
    password: str,
    ssl: bool = True,
    limit: int = 50,
) -> list[dict]:
    """Función síncrona para recibir correos vía POP3 (se ejecuta en executor)."""
    try:
        if ssl:
            mail = poplib.POP3_SSL(host, port)
        else:
            mail = poplib.POP3(host, port)

        mail.user(user)
        mail.pass_(password)

        # Obtener lista de mensajes
        msg_count, _ = mail.stat()
        start = max(1, msg_count - limit + 1)
        msg_ids = list(range(msg_count, start - 1, -1))

        emails = []
        for msg_id in msg_ids:
            _, msg_lines, _ = mail.retr(msg_id)
            raw_email = b"\r\n".join(msg_lines)
            msg = email.message_from_bytes(raw_email)

            email_info = {
                "id": str(msg_id),
                "subject": _decode_header_value(msg.get("Subject", "")),
                "from": _decode_header_value(msg.get("From", "")),
                "to": _decode_header_value(msg.get("To", "")),
                "date": msg.get("Date", ""),
                "attachments": _extract_attachments(msg),
            }
            emails.append(email_info)

        mail.quit()
        logger.info(f"Recibidos {len(emails)} correos vía POP3 de {user}@{host}")
        return emails

    except poplib.error_proto as e:
        raise EmailReceiverError(f"Error POP3: {str(e)}")
    except Exception as e:
        raise EmailReceiverError(f"Error al recibir correos vía POP3: {str(e)}")


async def receive_emails_imap(
    host: str,
    port: int,
    user: str,
    password: str,
    ssl: bool = True,
    folder: str = "INBOX",
    limit: int = 50,
) -> list[dict]:
    """
    Recibe correos electrónicos vía IMAP.
    Ejecuta la operación en un executor para no bloquear el event loop.
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,
        partial(
            _receive_emails_imap_sync,
            host=host, port=port, user=user, password=password,
            ssl=ssl, folder=folder, limit=limit,
        )
    )


async def receive_emails_pop3(
    host: str,
    port: int,
    user: str,
    password: str,
    ssl: bool = True,
    limit: int = 50,
) -> list[dict]:
    """
    Recibe correos electrónicos vía POP3.
    Ejecuta la operación en un executor para no bloquear el event loop.
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,
        partial(
            _receive_emails_pop3_sync,
            host=host, port=port, user=user, password=password,
            ssl=ssl, limit=limit,
        )
    )


def _download_attachment_sync(
    host: str,
    port: int,
    user: str,
    password: str,
    email_id: str,
    attachment_index: int,
    protocol: str = "IMAP",
    ssl: bool = True,
    folder: str = "INBOX",
) -> bytes:
    """Función síncrona para descargar adjunto (se ejecuta en executor)."""
    try:
        if protocol.upper() == "IMAP":
            if ssl:
                mail = imaplib.IMAP4_SSL(host, port)
            else:
                mail = imaplib.IMAP4(host, port)

            mail.login(user, password)
            mail.select(folder)

            status, msg_data = mail.fetch(email_id.encode(), "(RFC822)")
            mail.logout()

            if status != "OK":
                raise EmailReceiverError("No se pudo obtener el correo")

            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

        elif protocol.upper() == "POP3":
            if ssl:
                mail = poplib.POP3_SSL(host, port)
            else:
                mail = poplib.POP3(host, port)

            mail.user(user)
            mail.pass_(password)

            _, msg_lines, _ = mail.retr(int(email_id))
            mail.quit()

            raw_email = b"\r\n".join(msg_lines)
            msg = email.message_from_bytes(raw_email)

        else:
            raise EmailReceiverError(f"Protocolo no soportado: {protocol}")

        # Buscar el adjunto por índice
        current_index = 0
        for part in msg.walk():
            content_disposition = part.get_content_disposition()
            if content_disposition in ("attachment", "inline"):
                filename = part.get_filename()
                if filename:
                    if current_index == attachment_index:
                        payload = part.get_payload(decode=True)
                        if payload is None:
                            raise EmailReceiverError("No se pudo decodificar el adjunto")
                        return payload
                    current_index += 1

        raise EmailReceiverError(
            f"Adjunto con índice {attachment_index} no encontrado en el correo"
        )

    except EmailReceiverError:
        raise
    except Exception as e:
        raise EmailReceiverError(f"Error al descargar adjunto: {str(e)}")


async def download_attachment(
    host: str,
    port: int,
    user: str,
    password: str,
    email_id: str,
    attachment_index: int,
    protocol: str = "IMAP",
    ssl: bool = True,
    folder: str = "INBOX",
) -> bytes:
    """
    Descarga un adjunto específico de un correo electrónico.
    Ejecuta la operación en un executor para no bloquear el event loop.
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,
        partial(
            _download_attachment_sync,
            host=host, port=port, user=user, password=password,
            email_id=email_id, attachment_index=attachment_index,
            protocol=protocol, ssl=ssl, folder=folder,
        )
    )
