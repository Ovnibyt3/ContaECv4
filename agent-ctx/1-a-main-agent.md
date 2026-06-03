# Task 1-a: Fix Backup API, Add RIDE Endpoint, Add Products to Backup

## Work Summary

### Task 1: Fix Backup API Layer (api.ts)

**Problem:** Frontend backup functions didn't match actual backend endpoints.

**Changes in `/home/z/my-project/src/lib/api.ts`:**

- Updated `BackupInfo` interface: removed `id` and `type` fields, changed `size` to `size_bytes`
- Added `BackupListResponse` interface (wraps `{backups: BackupInfo[]}`)
- Added `CreateBackupResponse` interface (`{message, filename, size_bytes, timestamp}`)
- Added `RestoreBackupResponse` interface with companies/clients/products counters
- `getBackups()`: Changed from `apiGet<BackupInfo[]>('/backups')` to `apiGet<BackupListResponse>('/v1/backup/list')` then unwraps `.backups`
- `createBackup()`: Changed from `apiPost<BackupInfo>('/backups', { type })` to `apiPost<CreateBackupResponse>('/v1/backup/create')` (no type parameter)
- `downloadBackup(filename)`: Changed from `downloadBackup(id)` using `/backups/${id}/download` to `/v1/backup/download/${filename}`
- `restoreBackup(file)`: Changed from `restoreBackup(id)` POST with ID to multipart file upload to `/v1/backup/restore`
- Exported all new types

### Task 2: Add RIDE PDF Download Endpoint

**Changes in `/home/z/my-project/backend/app/api/v1/endpoints/comprobantes.py`:**

- Added imports: `FileResponse`, `generate_ride_pdf`, `Path`
- New endpoint `GET /{comprobante_id}/ride`:
  - Gets comprobante, company, detalles, and client from DB
  - Builds `comprobante_data` dict with all comprobante fields (tipo, secuencial, clave_acceso, totales, cliente info, retenciones, etc.)
  - Builds `company_data` dict with company info (ruc, razon_social, dir, cod_establecimiento, etc.)
  - Builds `detalles_data` list of dicts from ComprobanteDetalle records
  - Calls `generate_ride_pdf()` with output to `settings.TEMP_DIR / ride_{comprobante_id}.pdf`
  - Returns `FileResponse` with `media_type="application/pdf"`

**Changes in `/home/z/my-project/src/lib/api.ts`:**

- Added `downloadRIDE(id: string): Promise<Blob>` function
- Uses fetch with auth header to `/v1/comprobantes/${id}/ride`
- Exported in both function and type export sections

### Task 3: Add Products to Backup/Restore

**Changes in `/home/z/my-project/backend/app/api/v1/endpoints/backup.py`:**

- Added `from app.models.product import Product` import
- Added `from decimal import Decimal` import
- In `create_backup_data()`:
  - Query products for each company (same pattern as clients)
  - Added `"products"` list to backup dict with fields: company_ruc, codigo_principal, codigo_auxiliar, descripcion, tipo, precio_unitario, iva_codigo, iva_porcentaje, ice_codigo, ice_porcentaje, unidad_medida, descuento
  - Decimal fields serialized as strings for JSON compatibility
  - Bumped version to "1.2.0"
- In `restore_backup()`:
  - Added product counters: products_created, products_updated, products_skipped
  - Added section 3: Restore products (match by company_id + codigo_principal)
  - New products created with all fields, Decimal values parsed from strings
  - Existing products: string fields compared with normalization, numeric fields compared as strings then set as Decimal
  - Updated logger.info to include product counts
  - Updated return response to include `"products"` stats object

## Verification

- `bun run lint` passes with zero errors
- `python3 -c "from app.api.v1.endpoints.backup import router; print('OK')"` → OK
- `python3 -c "from app.api.v1.endpoints.comprobantes import router; print('OK')"` → OK
- All comprobantes routes registered including `/{comprobante_id}/ride`
- All backup routes registered: `/create`, `/restore`, `/download/{filename}`, `/list`
