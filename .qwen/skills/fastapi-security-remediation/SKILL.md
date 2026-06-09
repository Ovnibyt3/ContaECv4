---
name: fastapi-security-remediation
description: Systematic approach to fixing security vulnerabilities identified in a FastAPI backend audit
source: auto-skill
extracted_at: '2026-06-09T16:50:35.365Z'
---

# FastAPI Security Remediation Workflow

## When to Use
When you receive a security audit report identifying vulnerabilities (XSS, XXE, SQLi, exposed credentials, rate limiting gaps, etc.) in a FastAPI/Python backend and need to systematically fix them.

## Procedure

### 1. Parse the Audit Report
- Read the audit document (e.g., `ia.md`, security report) and extract each finding
- For each finding, note: file path, line numbers, vulnerability type, and recommended fix
- Create a todo list prioritizing by severity (credentials > injection > rate limiting > architecture)

### 2. Locate and Read Affected Files
- Use `glob` or `grep` to find files mentioned in the audit
- Read the specific lines mentioned AND surrounding context (minimum 20-50 lines around the issue)
- Understand WHY the code exists before changing it (e.g., `verify=False` may have been intentional for development)

### 3. Apply Fixes by Category

#### Exposed Credentials
- Replace hardcoded values with empty strings (`""`)
- Update validation functions to check for empty strings, not just dev defaults
- Remove development fallback passwords entirely
- **Pattern**: `config.py` defaults → empty → env var required → validation warns on empty

#### XSS in HTML Generation
- Add `import html` at the top
- Wrap ALL user-controlled variables in `html.escape()` when building HTML strings
- Apply to email bodies, template rendering, and any f-string HTML construction
- **Pattern**: `f"...{user_value}..."` → `f"...{html.escape(user_value)}..."`

#### XXE in XML Parsing
- Add security flags to `lxml.etree.XMLParser`:
  ```python
  parser = etree.XMLParser(
      remove_blank_text=True,
      encoding="UTF-8",
      resolve_entities=False,
      no_network=True,
      dtd_validation=False,
      load_dtd=False,
  )
  ```

#### SSL Verification Disabled
- **Production**: `verify=True`
- **Development**: Use `ssl.create_default_context()` with `verify_mode=ssl.CERT_NONE` but log a warning
- Never leave `verify=False` without environment gating

#### Blocking I/O in Async Functions
- Add `import aiofiles`
- Replace `with open(path, "wb") as f: f.write(data)` with:
  ```python
  async with aiofiles.open(path, "wb") as f:
      await f.write(data)
  ```
- Apply to all file reads/writes in `async def` functions

#### Rate Limiting with slowapi
1. Create a `rate_limiter.py` module:
   ```python
   from slowapi import Limiter
   from slowapi.util import get_remote_address
   limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])
   AUTH_LOGIN_LIMIT = "10/minute"  # Define route-specific limits as constants
   ```
2. In endpoint files, add decorator: `@limiter.limit(AUTH_LOGIN_LIMIT)`
3. Add `request: Request` as first parameter to decorated endpoints
4. In `main.py`:
   ```python
   from slowapi import _rate_limit_exceeded_handler
   from slowapi.errors import RateLimitExceeded
   app.state.limiter = limiter
   app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
   ```

#### CORS with Whitespace
- Use a sanitized property: `[origin.strip() for origin in CORS_ORIGINS.split(",")]`
- Never use `.split(",")` directly without stripping

#### Timezone Handling
- Replace `datetime.now()` with `datetime.now(timezone.utc)`
- For specific timezones, use `zoneinfo.ZoneInfo("America/Guayaquil")` and convert:
  ```python
  now_utc = datetime.now(timezone.utc)
  now_local = now_utc.astimezone(ZoneInfo("America/Guayaquil"))
  ```

#### Implicit Database Commits
- If removing implicit commits would break many endpoints, document the risk instead:
  ```python
  # TODO: Remove implicit commit - endpoints should call commit() explicitly
  await session.commit()
  ```
- Add architectural warning in docstring

### 4. Document What You Fixed
- Save a summary to memory with: issue, files changed, what was done, and notes for future work
- Note any mitigations that don't require code changes (e.g., "SQLi prevented by SQLAlchemy ORM usage")

## Key Principles
- **Understand before changing**: `verify=False` exists for a reason—gate it by environment, don't just flip it
- **Don't break working code**: If removing implicit commits would silently break all write endpoints, document the risk instead
- **Defense in depth**: Rate limiting is in addition to (not a replacement for) input sanitization
- **Log security changes**: Add comments like `# Security: escape all user-controlled variables to prevent XSS`
