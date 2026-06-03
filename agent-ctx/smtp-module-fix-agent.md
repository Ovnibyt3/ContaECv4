# Task: Fix ContaEC Phase 7 SMTP Module - Multi-Profile Support & Sandbox Enforcement

## Summary
Successfully implemented the ContaEC Phase 7 SMTP module with multi-profile support and sandbox mode enforcement across 6 files.

## Files Created
1. **`/home/z/my-project/backend/app/models/smtp_profile.py`** - SMTPProfile SQLAlchemy model with:
   - UUID PK (PG_UUID pattern), user_id FK to users.id (CASCADE)
   - Fields: nombre, provider_type (enum), host, port, username, password (encrypted), use_ssl, use_tls, protocol (enum)
   - IMAP/POP3 optional fields, is_default, is_active, daily_limit, sent_today, last_sent_at
   - Enums: SmtpProviderType (GMAIL, ZOHO, OFFICE365, OUTLOOK, YAHOO, CUSTOM), SmtpConnectionProtocol (SMTP, SMTP_SSL, STARTTLS)

2. **`/home/z/my-project/backend/app/schemas/smtp_profile.py`** - Pydantic schemas:
   - SMTPProfileCreate, SMTPProfileUpdate, SMTPProfileResponse
   - SMTPTestRequest, SMTPTestResponse
   - Validators for provider_type and protocol

3. **`/home/z/my-project/backend/app/api/v1/endpoints/smtp_profiles.py`** - REST endpoints:
   - POST /smtp-profiles - Create profile
   - GET /smtp-profiles - List profiles (with filters)
   - PUT /smtp-profiles/{id} - Update profile
   - DELETE /smtp-profiles/{id} - Delete profile (auto-reassigns default)
   - POST /smtp-profiles/{id}/test - Test SMTP connection
   - PUT /smtp-profiles/{id}/set-default - Set as default
   - PUT /smtp-profiles/{id}/reset-counter - Reset daily counter

## Files Modified
4. **`/home/z/my-project/backend/app/core/email_service.py`** - Added:
   - `get_smtp_profile_connection(profile_id, db)` - loads SMTPProfile and creates connection params
   - `send_comprobante_email` now accepts optional `smtp_profile_id`, `db`, `environment_mode`
   - Sandbox mode: checks environment_mode, logs but doesn't send if "sandbox"
   - Counter update on successful send via profile

5. **`/home/z/my-project/backend/app/api/v1/router.py`** - Added smtp_profiles router import and include

6. **`/home/z/my-project/backend/app/models/__init__.py`** - Added SMTPProfile, SmtpProviderType, SmtpConnectionProtocol exports

## Verification
- All Python syntax checks passed
- All imports verified working
- Router correctly includes 7 SMTP profile endpoints
- Existing functionality preserved (backward-compatible with UserConfig SMTP)
