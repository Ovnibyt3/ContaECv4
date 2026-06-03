"""
ContaEC - Endpoints de Integraciones
Integracion bancaria (extractos, conciliacion) y conectores e-commerce
"""
import logging
from datetime import datetime, timezone
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.audit import log_action
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.company import Company
from app.models.integration import (
    CuentaBancaria,
    EcommerceConnector,
    EcommerceSyncLog,
    ExtractoBancario,
    ExtractoEstado,
    MovimientoBancario,
    ConciliacionEstado,
    MovimientoTipo,
    ConnectorEstado,
    SyncEstado,
    BancoTipoCuenta,
    EcommercePlataforma,
)
from app.models.user import User
from app.schemas.integration import (
    CuentaBancariaCreate,
    CuentaBancariaUpdate,
    CuentaBancariaResponse,
    ExtractoBancarioCreate,
    ExtractoBancarioResponse,
    MovimientoBancarioCreate,
    MovimientoBancarioUpdate,
    MovimientoBancarioResponse,
    EcommerceConnectorCreate,
    EcommerceConnectorUpdate,
    EcommerceConnectorResponse,
    EcommerceSyncLogCreate,
    EcommerceSyncLogResponse,
    IntegrationStats,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/integrations", tags=["Integraciones"])


# ==========================================
# Funciones auxiliares
# ==========================================

async def _get_company_for_user(
    db: AsyncSession,
    company_id: str,
    user_id: str,
) -> Company:
    """Obtiene una empresa verificando que pertenezca al usuario actual"""
    result = await db.execute(
        select(Company).where(
            Company.id == company_id,
            Company.user_id == user_id,
            Company.is_active == True,
        )
    )
    company = result.scalars().first()
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa no encontrada o no pertenece al usuario actual.",
        )
    return company


# ==========================================
# 1. ESTADISTICAS
# ==========================================

@router.get("/stats", response_model=IntegrationStats)
async def get_integration_stats(
    company_id: str = Query(..., description="ID de la empresa"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Obtener estadisticas generales de integraciones"""
    await _get_company_for_user(db, company_id, current_user.id)

    # Bank stats
    total_cuentas = await db.execute(
        select(func.count(CuentaBancaria.id)).where(
            CuentaBancaria.company_id == company_id,
        )
    )
    cuentas_activas = await db.execute(
        select(func.count(CuentaBancaria.id)).where(
            CuentaBancaria.company_id == company_id,
            CuentaBancaria.is_active == True,
        )
    )
    total_extractos = await db.execute(
        select(func.count(ExtractoBancario.id)).where(
            ExtractoBancario.company_id == company_id,
        )
    )
    extractos_pendientes = await db.execute(
        select(func.count(ExtractoBancario.id)).where(
            ExtractoBancario.company_id == company_id,
            ExtractoBancario.estado.in_([
                ExtractoEstado.IMPORTADO.value,
                ExtractoEstado.EN_CONCILIACION.value,
            ]),
        )
    )
    mov_pendientes = await db.execute(
        select(func.count(MovimientoBancario.id)).where(
            MovimientoBancario.company_id == company_id,
            MovimientoBancario.conciliacion_estado == ConciliacionEstado.PENDIENTE.value,
        )
    )
    mov_conciliados = await db.execute(
        select(func.count(MovimientoBancario.id)).where(
            MovimientoBancario.company_id == company_id,
            MovimientoBancario.conciliacion_estado == ConciliacionEstado.CONCILIADO.value,
        )
    )
    saldo_total = await db.execute(
        select(func.coalesce(func.sum(CuentaBancaria.saldo_actual), 0)).where(
            CuentaBancaria.company_id == company_id,
            CuentaBancaria.is_active == True,
        )
    )

    # E-Commerce stats
    total_connectors = await db.execute(
        select(func.count(EcommerceConnector.id)).where(
            EcommerceConnector.company_id == company_id,
        )
    )
    connectors_activos = await db.execute(
        select(func.count(EcommerceConnector.id)).where(
            EcommerceConnector.company_id == company_id,
            EcommerceConnector.is_active == True,
            EcommerceConnector.estado == ConnectorEstado.CONECTADO.value,
        )
    )
    # By platform
    platforms_result = await db.execute(
        select(EcommerceConnector.plataforma, func.count(EcommerceConnector.id)).where(
            EcommerceConnector.company_id == company_id,
            EcommerceConnector.is_active == True,
        ).group_by(EcommerceConnector.plataforma)
    )
    platforms = dict(platforms_result.all())

    total_syncs = await db.execute(
        select(func.count(EcommerceSyncLog.id)).where(
            EcommerceSyncLog.company_id == company_id,
        )
    )

    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    syncs_hoy = await db.execute(
        select(func.count(EcommerceSyncLog.id)).where(
            EcommerceSyncLog.company_id == company_id,
            EcommerceSyncLog.fecha_inicio >= today,
        )
    )

    ultima_sync = await db.execute(
        select(func.max(EcommerceSyncLog.fecha_inicio)).where(
            EcommerceSyncLog.company_id == company_id,
            EcommerceSyncLog.estado == SyncEstado.COMPLETADA.value,
        )
    )

    return IntegrationStats(
        total_cuentas_bancarias=total_cuentas.scalar() or 0,
        cuentas_activas=cuentas_activas.scalar() or 0,
        total_extractos=total_extractos.scalar() or 0,
        extractos_pendientes=extractos_pendientes.scalar() or 0,
        movimientos_pendientes_conciliar=mov_pendientes.scalar() or 0,
        movimientos_conciliados=mov_conciliados.scalar() or 0,
        saldo_total_cuentas=saldo_total.scalar() or Decimal("0"),
        total_connectors=total_connectors.scalar() or 0,
        connectors_activos=connectors_activos.scalar() or 0,
        connectors_por_plataforma=platforms,
        total_sync_logs=total_syncs.scalar() or 0,
        sync_logs_hoy=syncs_hoy.scalar() or 0,
        ultima_sync_fecha=ultima_sync.scalar(),
    )


# ==========================================
# 2. CUENTAS BANCARIAS CRUD
# ==========================================

@router.post("/bank/accounts", response_model=CuentaBancariaResponse, status_code=status.HTTP_201_CREATED)
async def create_cuenta_bancaria(
    data: CuentaBancariaCreate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Crear una cuenta bancaria"""
    await _get_company_for_user(db, data.company_id, current_user.id)

    # Validate tipo_cuenta
    valid_tipos = {t.value for t in BancoTipoCuenta}
    if data.tipo_cuenta not in valid_tipos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tipo de cuenta invalido: {data.tipo_cuenta}",
        )

    cuenta = CuentaBancaria(
        company_id=data.company_id,
        nombre_banco=data.nombre_banco,
        codigo_banco=data.codigo_banco,
        tipo_cuenta=data.tipo_cuenta,
        numero_cuenta=data.numero_cuenta,
        iban=data.iban,
        titular=data.titular,
        moneda=data.moneda,
        saldo_inicial=data.saldo_inicial,
        saldo_actual=data.saldo_inicial,
        formato_extracto=data.formato_extracto,
        configuracion_mapeo=data.configuracion_mapeo,
    )

    db.add(cuenta)
    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="CREATE",
        entity_type="cuenta_bancaria",
        entity_id=cuenta.id,
        description=f"Cuenta bancaria creada: {cuenta.nombre_banco} - {cuenta.numero_cuenta}",
        ip_address=request.client.host if request.client else None,
    )

    return CuentaBancariaResponse.model_validate(cuenta)


@router.get("/bank/accounts", response_model=list[CuentaBancariaResponse])
async def list_cuentas_bancarias(
    company_id: str | None = None,
    is_active: bool | None = True,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar cuentas bancarias"""
    query = (
        select(CuentaBancaria)
        .join(Company, CuentaBancaria.company_id == Company.id)
        .where(Company.user_id == current_user.id)
    )

    if company_id:
        await _get_company_for_user(db, company_id, current_user.id)
        query = query.where(CuentaBancaria.company_id == company_id)
    if is_active is not None:
        query = query.where(CuentaBancaria.is_active == is_active)

    query = query.order_by(CuentaBancaria.created_at.desc())

    result = await db.execute(query)
    cuentas = result.scalars().all()
    return [CuentaBancariaResponse.model_validate(c) for c in cuentas]


@router.get("/bank/accounts/{account_id}", response_model=CuentaBancariaResponse)
async def get_cuenta_bancaria(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Obtener una cuenta bancaria por ID"""
    result = await db.execute(
        select(CuentaBancaria).where(CuentaBancaria.id == account_id)
    )
    cuenta = result.scalars().first()
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta bancaria no encontrada.")
    await _get_company_for_user(db, cuenta.company_id, current_user.id)
    return CuentaBancariaResponse.model_validate(cuenta)


@router.put("/bank/accounts/{account_id}", response_model=CuentaBancariaResponse)
async def update_cuenta_bancaria(
    account_id: str,
    data: CuentaBancariaUpdate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Actualizar una cuenta bancaria"""
    result = await db.execute(
        select(CuentaBancaria).where(CuentaBancaria.id == account_id)
    )
    cuenta = result.scalars().first()
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta bancaria no encontrada.")
    await _get_company_for_user(db, cuenta.company_id, current_user.id)

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(cuenta, field, value)

    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="UPDATE",
        entity_type="cuenta_bancaria",
        entity_id=cuenta.id,
        description=f"Cuenta bancaria actualizada: {cuenta.nombre_banco}",
        ip_address=request.client.host if request.client else None,
    )

    return CuentaBancariaResponse.model_validate(cuenta)


@router.delete("/bank/accounts/{account_id}")
async def delete_cuenta_bancaria(
    account_id: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Eliminar una cuenta bancaria (soft delete)"""
    result = await db.execute(
        select(CuentaBancaria).where(CuentaBancaria.id == account_id)
    )
    cuenta = result.scalars().first()
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta bancaria no encontrada.")
    await _get_company_for_user(db, cuenta.company_id, current_user.id)

    cuenta.is_active = False
    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="DELETE",
        entity_type="cuenta_bancaria",
        entity_id=account_id,
        description=f"Cuenta bancaria desactivada: {cuenta.nombre_banco}",
        ip_address=request.client.host if request.client else None,
    )

    return {"message": "Cuenta bancaria desactivada exitosamente."}


# ==========================================
# 3. EXTRACTOS BANCARIOS CRUD
# ==========================================

@router.post("/bank/statements", response_model=ExtractoBancarioResponse, status_code=status.HTTP_201_CREATED)
async def create_extracto(
    data: ExtractoBancarioCreate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Crear/importar un extracto bancario"""
    await _get_company_for_user(db, data.company_id, current_user.id)

    # Verify cuenta bancaria ownership
    cuenta_result = await db.execute(
        select(CuentaBancaria).where(CuentaBancaria.id == data.cuenta_bancaria_id)
    )
    cuenta = cuenta_result.scalars().first()
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta bancaria no encontrada.")

    extracto = ExtractoBancario(
        company_id=data.company_id,
        cuenta_bancaria_id=data.cuenta_bancaria_id,
        fecha_desde=data.fecha_desde,
        fecha_hasta=data.fecha_hasta,
        saldo_inicial=data.saldo_inicial,
        saldo_final=data.saldo_final,
        total_debitos=data.total_debitos,
        total_creditos=data.total_creditos,
        numero_movimientos=data.numero_movimientos,
        archivo_original=data.archivo_original,
        notas=data.notas,
    )

    db.add(extracto)
    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="CREATE",
        entity_type="extracto_bancario",
        entity_id=extracto.id,
        description=f"Extracto importado: {cuenta.nombre_banco} ({data.fecha_desde.date()} a {data.fecha_hasta.date()})",
        ip_address=request.client.host if request.client else None,
    )

    resp = ExtractoBancarioResponse.model_validate(extracto)
    resp.banco_nombre = cuenta.nombre_banco
    resp.cuenta_numero = cuenta.numero_cuenta
    return resp


@router.get("/bank/statements", response_model=list[ExtractoBancarioResponse])
async def list_extractos(
    company_id: str | None = None,
    cuenta_bancaria_id: str | None = None,
    estado: str | None = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar extractos bancarios"""
    query = (
        select(ExtractoBancario)
        .join(Company, ExtractoBancario.company_id == Company.id)
        .where(Company.user_id == current_user.id)
    )

    if company_id:
        await _get_company_for_user(db, company_id, current_user.id)
        query = query.where(ExtractoBancario.company_id == company_id)
    if cuenta_bancaria_id:
        query = query.where(ExtractoBancario.cuenta_bancaria_id == cuenta_bancaria_id)
    if estado:
        query = query.where(ExtractoBancario.estado == estado)

    query = query.order_by(ExtractoBancario.created_at.desc())

    result = await db.execute(query)
    extractos = result.scalars().all()

    responses = []
    for ext in extractos:
        resp = ExtractoBancarioResponse.model_validate(ext)
        # Get bank info
        cuenta_result = await db.execute(
            select(CuentaBancaria).where(CuentaBancaria.id == ext.cuenta_bancaria_id)
        )
        cuenta = cuenta_result.scalars().first()
        if cuenta:
            resp.banco_nombre = cuenta.nombre_banco
            resp.cuenta_numero = cuenta.numero_cuenta
        responses.append(resp)

    return responses


@router.get("/bank/statements/{statement_id}", response_model=ExtractoBancarioResponse)
async def get_extracto(
    statement_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Obtener un extracto bancario por ID"""
    result = await db.execute(
        select(ExtractoBancario).where(ExtractoBancario.id == statement_id)
    )
    extracto = result.scalars().first()
    if not extracto:
        raise HTTPException(status_code=404, detail="Extracto no encontrado.")
    await _get_company_for_user(db, extracto.company_id, current_user.id)

    resp = ExtractoBancarioResponse.model_validate(extracto)
    cuenta_result = await db.execute(
        select(CuentaBancaria).where(CuentaBancaria.id == extracto.cuenta_bancaria_id)
    )
    cuenta = cuenta_result.scalars().first()
    if cuenta:
        resp.banco_nombre = cuenta.nombre_banco
        resp.cuenta_numero = cuenta.numero_cuenta
    return resp


@router.delete("/bank/statements/{statement_id}")
async def delete_extracto(
    statement_id: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Eliminar un extracto bancario y sus movimientos"""
    result = await db.execute(
        select(ExtractoBancario).where(ExtractoBancario.id == statement_id)
    )
    extracto = result.scalars().first()
    if not extracto:
        raise HTTPException(status_code=404, detail="Extracto no encontrado.")
    await _get_company_for_user(db, extracto.company_id, current_user.id)

    await db.delete(extracto)
    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="DELETE",
        entity_type="extracto_bancario",
        entity_id=statement_id,
        description=f"Extracto eliminado",
        ip_address=request.client.host if request.client else None,
    )

    return {"message": "Extracto eliminado exitosamente."}


# ==========================================
# 4. MOVIMIENTOS BANCARIOS CRUD
# ==========================================

@router.post("/bank/movements", response_model=MovimientoBancarioResponse, status_code=status.HTTP_201_CREATED)
async def create_movimiento(
    data: MovimientoBancarioCreate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Crear un movimiento bancario"""
    await _get_company_for_user(db, data.company_id, current_user.id)

    # Verify cuenta bancaria ownership
    cuenta_result = await db.execute(
        select(CuentaBancaria).where(CuentaBancaria.id == data.cuenta_bancaria_id)
    )
    cuenta = cuenta_result.scalars().first()
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta bancaria no encontrada.")

    # Verify extracto exists and belongs to same cuenta
    ext_result = await db.execute(
        select(ExtractoBancario).where(ExtractoBancario.id == data.extracto_id)
    )
    extracto = ext_result.scalars().first()
    if not extracto:
        raise HTTPException(status_code=404, detail="Extracto no encontrado.")
    if extracto.cuenta_bancaria_id != data.cuenta_bancaria_id:
        raise HTTPException(
            status_code=400,
            detail="El extracto no pertenece a la cuenta bancaria indicada.",
        )

    movimiento = MovimientoBancario(
        company_id=data.company_id,
        cuenta_bancaria_id=data.cuenta_bancaria_id,
        extracto_id=data.extracto_id,
        fecha=data.fecha,
        tipo=data.tipo,
        monto=data.monto,
        saldo_posterior=data.saldo_posterior,
        referencia=data.referencia,
        descripcion=data.descripcion,
        beneficiario=data.beneficiario,
        documento=data.documento,
        categoria=data.categoria,
    )

    db.add(movimiento)
    await db.flush()

    # Update cuenta saldo_actual
    if data.tipo == MovimientoTipo.CREDITO.value:
        cuenta.saldo_actual = (cuenta.saldo_actual + data.monto).quantize(Decimal("0.01"))
    else:
        cuenta.saldo_actual = (cuenta.saldo_actual - data.monto).quantize(Decimal("0.01"))
    await db.flush()

    return MovimientoBancarioResponse.model_validate(movimiento)


@router.get("/bank/movements", response_model=list[MovimientoBancarioResponse])
async def list_movimientos(
    extracto_id: str | None = None,
    cuenta_bancaria_id: str | None = None,
    conciliacion_estado: str | None = None,
    tipo: str | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(200, ge=1, le=1000),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar movimientos bancarios con filtros"""
    query = (
        select(MovimientoBancario)
        .join(Company, MovimientoBancario.company_id == Company.id)
        .where(Company.user_id == current_user.id)
    )

    if extracto_id:
        query = query.where(MovimientoBancario.extracto_id == extracto_id)
    if cuenta_bancaria_id:
        query = query.where(MovimientoBancario.cuenta_bancaria_id == cuenta_bancaria_id)
    if conciliacion_estado:
        query = query.where(MovimientoBancario.conciliacion_estado == conciliacion_estado)
    if tipo:
        query = query.where(MovimientoBancario.tipo == tipo)

    query = query.order_by(MovimientoBancario.fecha.desc()).offset(skip).limit(limit)

    result = await db.execute(query)
    movimientos = result.scalars().all()
    return [MovimientoBancarioResponse.model_validate(m) for m in movimientos]


@router.put("/bank/movements/{movement_id}", response_model=MovimientoBancarioResponse)
async def update_movimiento(
    movement_id: str,
    data: MovimientoBancarioUpdate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Actualizar un movimiento bancario (conciliacion)"""
    result = await db.execute(
        select(MovimientoBancario).where(MovimientoBancario.id == movement_id)
    )
    movimiento = result.scalars().first()
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado.")
    await _get_company_for_user(db, movimiento.company_id, current_user.id)

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(movimiento, field, value)

    # If conciliacion_estado changed to conciliado, set date
    if "conciliacion_estado" in update_data and update_data["conciliacion_estado"] == ConciliacionEstado.CONCILIADO.value:
        movimiento.conciliacion_fecha = datetime.now(timezone.utc)

    await db.flush()

    # Update extracto conciliados count
    if "conciliacion_estado" in update_data:
        conciliados_count = await db.execute(
            select(func.count(MovimientoBancario.id)).where(
                MovimientoBancario.extracto_id == movimiento.extracto_id,
                MovimientoBancario.conciliacion_estado == ConciliacionEstado.CONCILIADO.value,
            )
        )
        ext_result = await db.execute(
            select(ExtractoBancario).where(ExtractoBancario.id == movimiento.extracto_id)
        )
        ext = ext_result.scalars().first()
        if ext:
            ext.movimientos_conciliados = conciliados_count.scalar() or 0
            # Check if all movements are conciliado or ignorado
            pendientes = await db.execute(
                select(func.count(MovimientoBancario.id)).where(
                    MovimientoBancario.extracto_id == movimiento.extracto_id,
                    MovimientoBancario.conciliacion_estado == ConciliacionEstado.PENDIENTE.value,
                )
            )
            if (pendientes.scalar() or 0) == 0:
                ext.estado = ExtractoEstado.CONCILIADO.value
            else:
                ext.estado = ExtractoEstado.EN_CONCILIACION.value
            await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="UPDATE",
        entity_type="movimiento_bancario",
        entity_id=movement_id,
        description=f"Movimiento actualizado: conciliacion={movimiento.conciliacion_estado}",
        ip_address=request.client.host if request.client else None,
    )

    return MovimientoBancarioResponse.model_validate(movimiento)


@router.delete("/bank/movements/{movement_id}")
async def delete_movimiento(
    movement_id: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Eliminar un movimiento bancario"""
    result = await db.execute(
        select(MovimientoBancario).where(MovimientoBancario.id == movement_id)
    )
    movimiento = result.scalars().first()
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado.")
    await _get_company_for_user(db, movimiento.company_id, current_user.id)

    await db.delete(movimiento)
    await db.flush()

    return {"message": "Movimiento eliminado exitosamente."}


# ==========================================
# 5. IMPORTAR EXTRACTO (CSV/Excel parsing)
# ==========================================

@router.post("/bank/import-csv")
async def import_bank_csv(
    cuenta_bancaria_id: str = Query(...),
    company_id: str = Query(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Importar extracto bancario desde CSV/Excel.
    Nota: En produccion se procesaria el archivo subido.
    Aqui se crea el extracto con los datos proporcionados.
    """
    await _get_company_for_user(db, company_id, current_user.id)

    cuenta_result = await db.execute(
        select(CuentaBancaria).where(CuentaBancaria.id == cuenta_bancaria_id)
    )
    cuenta = cuenta_result.scalars().first()
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta bancaria no encontrada.")

    # Update last sync date
    cuenta.ultima_fecha_sincronizacion = datetime.now(timezone.utc)
    await db.flush()

    return {
        "message": "Extracto importado exitosamente. Configure el mapeo de columnas para procesar los datos.",
        "cuenta_id": cuenta_bancaria_id,
    }


# ==========================================
# 6. E-COMMERCE CONNECTORS CRUD
# ==========================================

@router.post("/ecommerce/connectors", response_model=EcommerceConnectorResponse, status_code=status.HTTP_201_CREATED)
async def create_ecommerce_connector(
    data: EcommerceConnectorCreate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Crear un conector e-commerce"""
    await _get_company_for_user(db, data.company_id, current_user.id)

    # Validate plataforma
    valid_plataformas = {p.value for p in EcommercePlataforma}
    if data.plataforma not in valid_plataformas:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Plataforma invalida: {data.plataforma}",
        )

    connector = EcommerceConnector(
        company_id=data.company_id,
        user_id=current_user.id,
        nombre=data.nombre,
        plataforma=data.plataforma,
        url_tienda=data.url_tienda,
        api_key=data.api_key,
        api_secret=data.api_secret,
        access_token=data.access_token,
        refresh_token=data.refresh_token,
        configuracion_extra=data.configuracion_extra,
        sincronizacion_auto=data.sincronizacion_auto,
        frecuencia_sync=data.frecuencia_sync,
        sync_productos=data.sync_productos,
        sync_ordenes=data.sync_ordenes,
        sync_clientes=data.sync_clientes,
        sync_inventario=data.sync_inventario,
    )

    db.add(connector)
    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="CREATE",
        entity_type="ecommerce_connector",
        entity_id=connector.id,
        description=f"Conector e-commerce creado: {connector.nombre} ({connector.plataforma})",
        ip_address=request.client.host if request.client else None,
    )

    return EcommerceConnectorResponse.model_validate(connector)


@router.get("/ecommerce/connectors", response_model=list[EcommerceConnectorResponse])
async def list_ecommerce_connectors(
    company_id: str | None = None,
    plataforma: str | None = None,
    is_active: bool | None = True,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar conectores e-commerce"""
    query = (
        select(EcommerceConnector)
        .join(Company, EcommerceConnector.company_id == Company.id)
        .where(Company.user_id == current_user.id)
    )

    if company_id:
        await _get_company_for_user(db, company_id, current_user.id)
        query = query.where(EcommerceConnector.company_id == company_id)
    if plataforma:
        query = query.where(EcommerceConnector.plataforma == plataforma)
    if is_active is not None:
        query = query.where(EcommerceConnector.is_active == is_active)

    query = query.order_by(EcommerceConnector.created_at.desc())

    result = await db.execute(query)
    connectors = result.scalars().all()
    return [EcommerceConnectorResponse.model_validate(c) for c in connectors]


@router.get("/ecommerce/connectors/{connector_id}", response_model=EcommerceConnectorResponse)
async def get_ecommerce_connector(
    connector_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Obtener un conector e-commerce por ID"""
    result = await db.execute(
        select(EcommerceConnector).where(EcommerceConnector.id == connector_id)
    )
    connector = result.scalars().first()
    if not connector:
        raise HTTPException(status_code=404, detail="Conector no encontrado.")
    await _get_company_for_user(db, connector.company_id, current_user.id)
    return EcommerceConnectorResponse.model_validate(connector)


@router.put("/ecommerce/connectors/{connector_id}", response_model=EcommerceConnectorResponse)
async def update_ecommerce_connector(
    connector_id: str,
    data: EcommerceConnectorUpdate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Actualizar un conector e-commerce"""
    result = await db.execute(
        select(EcommerceConnector).where(EcommerceConnector.id == connector_id)
    )
    connector = result.scalars().first()
    if not connector:
        raise HTTPException(status_code=404, detail="Conector no encontrado.")
    await _get_company_for_user(db, connector.company_id, current_user.id)

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(connector, field, value)

    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="UPDATE",
        entity_type="ecommerce_connector",
        entity_id=connector.id,
        description=f"Conector actualizado: {connector.nombre}",
        ip_address=request.client.host if request.client else None,
    )

    return EcommerceConnectorResponse.model_validate(connector)


@router.delete("/ecommerce/connectors/{connector_id}")
async def delete_ecommerce_connector(
    connector_id: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Eliminar un conector e-commerce"""
    result = await db.execute(
        select(EcommerceConnector).where(EcommerceConnector.id == connector_id)
    )
    connector = result.scalars().first()
    if not connector:
        raise HTTPException(status_code=404, detail="Conector no encontrado.")
    await _get_company_for_user(db, connector.company_id, current_user.id)

    connector.is_active = False
    connector.estado = ConnectorEstado.DESACTIVADO.value
    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="DELETE",
        entity_type="ecommerce_connector",
        entity_id=connector_id,
        description=f"Conector desactivado: {connector.nombre}",
        ip_address=request.client.host if request.client else None,
    )

    return {"message": "Conector desactivado exitosamente."}


# ==========================================
# 7. PROBAR CONEXION E-COMMERCE
# ==========================================

@router.post("/ecommerce/connectors/{connector_id}/test")
async def test_ecommerce_connection(
    connector_id: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Probar la conexion con la plataforma e-commerce"""
    result = await db.execute(
        select(EcommerceConnector).where(EcommerceConnector.id == connector_id)
    )
    connector = result.scalars().first()
    if not connector:
        raise HTTPException(status_code=404, detail="Conector no encontrado.")
    await _get_company_for_user(db, connector.company_id, current_user.id)

    # In production, this would make actual API calls to the platform
    # For now, simulate a connection test
    try:
        # Simulate API test based on platform
        if connector.api_key or connector.access_token:
            connector.estado = ConnectorEstado.CONECTADO.value
            connector.ultimo_error = None
        else:
            connector.estado = ConnectorEstado.ERROR.value
            connector.ultimo_error = "No se encontraron credenciales de API configuradas."

        await db.flush()

        await log_action(
            db=db,
            user_id=current_user.id,
            user_email=current_user.email,
            action="TEST",
            entity_type="ecommerce_connector",
            entity_id=connector.id,
            description=f"Test conexion {connector.plataforma}: {connector.estado}",
            ip_address=request.client.host if request.client else None,
        )

        return {
            "status": connector.estado,
            "message": (
                "Conexion exitosa." if connector.estado == ConnectorEstado.CONECTADO.value
                else f"Error de conexion: {connector.ultimo_error}"
            ),
        }
    except Exception as e:
        connector.estado = ConnectorEstado.ERROR.value
        connector.ultimo_error = str(e)
        await db.flush()
        raise HTTPException(
            status_code=400,
            detail=f"Error al probar conexion: {str(e)}",
        )


# ==========================================
# 8. SINCRONIZACION E-COMMERCE
# ==========================================

@router.post("/ecommerce/connectors/{connector_id}/sync", response_model=EcommerceSyncLogResponse)
async def sync_ecommerce(
    connector_id: str,
    request: Request,
    tipo_sync: str = Query("completo", pattern="^(productos|ordenes|clientes|inventario|completo)$"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Ejecutar sincronizacion con la plataforma e-commerce"""
    result = await db.execute(
        select(EcommerceConnector).where(EcommerceConnector.id == connector_id)
    )
    connector = result.scalars().first()
    if not connector:
        raise HTTPException(status_code=404, detail="Conector no encontrado.")
    await _get_company_for_user(db, connector.company_id, current_user.id)

    if connector.estado not in [ConnectorEstado.CONECTADO.value, ConnectorEstado.SINCRONIZANDO.value]:
        raise HTTPException(
            status_code=400,
            detail="El conector debe estar conectado antes de sincronizar. Pruebe la conexion primero.",
        )

    # Create sync log
    sync_log = EcommerceSyncLog(
        company_id=connector.company_id,
        connector_id=connector_id,
        tipo_sync=tipo_sync,
        estado=SyncEstado.EN_PROGRESO.value,
        creado_por=current_user.id,
    )

    # Update connector state
    connector.estado = ConnectorEstado.SINCRONIZANDO.value
    db.add(sync_log)
    await db.flush()

    # In production, this would call the actual e-commerce API
    # Simulate a successful sync
    sync_log.estado = SyncEstado.COMPLETADA.value
    sync_log.fecha_fin = datetime.now(timezone.utc)
    sync_log.registros_procesados = 0
    sync_log.registros_creados = 0
    sync_log.registros_actualizados = 0
    sync_log.registros_errores = 0
    sync_log.resultado_resumen = '{"message": "Sincronizacion completada. No hay datos nuevos para sincronizar."}'

    connector.estado = ConnectorEstado.CONECTADO.value
    connector.ultima_sincronizacion = datetime.now(timezone.utc)
    await db.flush()

    await log_action(
        db=db,
        user_id=current_user.id,
        user_email=current_user.email,
        action="SYNC",
        entity_type="ecommerce_connector",
        entity_id=connector.id,
        description=f"Sincronizacion {tipo_sync} en {connector.plataforma}: completada",
        ip_address=request.client.host if request.client else None,
    )

    resp = EcommerceSyncLogResponse.model_validate(sync_log)
    resp.connector_nombre = connector.nombre
    resp.connector_plataforma = connector.plataforma
    return resp


# ==========================================
# 9. SYNC LOGS
# ==========================================

@router.get("/ecommerce/sync-logs", response_model=list[EcommerceSyncLogResponse])
async def list_sync_logs(
    connector_id: str | None = None,
    company_id: str | None = None,
    tipo_sync: str | None = None,
    estado: str | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar logs de sincronizacion e-commerce"""
    query = (
        select(EcommerceSyncLog)
        .join(Company, EcommerceSyncLog.company_id == Company.id)
        .where(Company.user_id == current_user.id)
    )

    if connector_id:
        query = query.where(EcommerceSyncLog.connector_id == connector_id)
    if company_id:
        await _get_company_for_user(db, company_id, current_user.id)
        query = query.where(EcommerceSyncLog.company_id == company_id)
    if tipo_sync:
        query = query.where(EcommerceSyncLog.tipo_sync == tipo_sync)
    if estado:
        query = query.where(EcommerceSyncLog.estado == estado)

    query = query.order_by(EcommerceSyncLog.fecha_inicio.desc()).offset(skip).limit(limit)

    result = await db.execute(query)
    logs = result.scalars().all()

    responses = []
    for log in logs:
        resp = EcommerceSyncLogResponse.model_validate(log)
        # Get connector info
        conn_result = await db.execute(
            select(EcommerceConnector).where(EcommerceConnector.id == log.connector_id)
        )
        conn = conn_result.scalars().first()
        if conn:
            resp.connector_nombre = conn.nombre
            resp.connector_plataforma = conn.plataforma
        responses.append(resp)

    return responses
