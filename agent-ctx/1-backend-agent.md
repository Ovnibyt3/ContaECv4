# Task 1 - Backend Agent: Fix backup restore endpoint, add download endpoint, fix midnight_backup_task

## Summary
All 3 issues in `/home/z/my-project/backend/app/api/v1/endpoints/backup.py` were fixed:

### 1. Fixed POST /restore (was a no-op)
- Now actually restores companies and clients to the database
- Companies matched by `user_id + RUC` — created if new, updated if fields differ, skipped if identical
- Clients matched by `company_id + identificacion` — same create/update/skip logic
- Added `company_ruc` field to client entries in backup data (version bumped to 1.1.0) so clients can be associated with the correct company during restore
- Returns accurate counts: `{companies: {created, updated, skipped}, clients: {created, updated, skipped}}`

### 2. Added GET /backup/download/{filename}
- Requires authentication via `get_current_user`
- Only serves files from the authenticated user's own backup directory
- Path traversal protection: validates filename is simple, checks resolved path stays within user's backup dir
- Returns `FileResponse` with `application/octet-stream` media type

### 3. Fixed midnight_backup_task date arithmetic
- Bug: `target.replace(day=now.day + 1)` raises `ValueError` on last day of month (day=32, etc.)
- Fix: `target + timedelta(days=1)` — proper date arithmetic that handles month/year boundaries

### Additional improvements
- Extracted `_derive_fernet_from_user_key()` helper to DRY up Fernet key derivation (was duplicated 3x)
- Moved all imports to top level (no more inline imports)
- Import test passed: `from app.api.v1.endpoints.backup import router; print('OK')`
- All 4 routes verified: POST /create, POST /restore, GET /download/{filename}, GET /list

### No other files modified
