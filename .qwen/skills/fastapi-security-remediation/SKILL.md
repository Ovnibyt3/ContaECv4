---
name: fastapi-security-remediation
description: Systematic approach to fixing security vulnerabilities identified in a FastAPI backend audit
license: MIT
metadata:
  version: "1.0.0"
  domain: backend-security
  triggers: security vulnerabilities, FastAPI security, security audit, XSS, SQLi, XXE, exposed credentials, rate limiting, CORS, security fix, security remediation
  role: specialist
  scope: remediation
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
- Replace `with open(path, "r") as f: json.load(f)` with:
  ```python
  async with aiofiles.open(path, "r", encoding="utf-8") as f:
      content = await f.read()
      data = json.loads(content)
  ```
- For file delete operations in async functions, use `asyncio.to_thread`:
  ```python
  async def _delete_async(path: Path) -> None:
      if path.exists():
          await asyncio.to_thread(path.unlink)
  ```
- Apply to all file reads/writes/deletes in `async def` functions

#### Background Task Cleanup Pattern
- Long-running background tasks with `asyncio.sleep()` cannot be cancelled quickly. Use incremental sleep:
  ```python
  async def background_task() -> None:
      running = True
      try:
          while running:
              await do_work()
              # Sleep in 1s increments for quick exit when stopped
              for _ in range(SLEEP_INTERVAL_SECONDS):
                  if not running:
                      break
                  await asyncio.sleep(1)
      finally:
          running = False
          logger.info("Task stopped cleanly")
  ```
- In lifespan shutdown, set the flag to False and await briefly before cancelling.

#### Pydantic-Settings Absolute .env Path
- `env_file=".env"` resolves relative to CWD, which breaks with systemd services or when running from different directories.
- Always resolve `.env` path relative to the config file:
  ```python
  from pathlib import Path
  _CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
  _ENV_FILE_PATH = _CONFIG_DIR / ".env"

  model_config = SettingsConfigDict(
      env_file=str(_ENV_FILE_PATH),
      env_file_encoding="utf-8",
      ...
  )
  ```

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

#### Middleware Ordering
FastAPI's `add_middleware()` **prepends** each new middleware. The LAST one added executes FIRST in the request phase. To achieve a specific execution order, add them in reverse:

```python
# Desired order: CORS -> SecurityHeaders -> InputSanitization -> RateLimit
# Add in REVERSE order:

app.add_middleware(RateLimitMiddleware, ...)       # executes FIRST
app.add_middleware(InputSanitizationMiddleware)     # executes 2nd
app.add_middleware(SecurityHeadersMiddleware)       # executes 3rd
app.add_middleware(CORSMiddleware, ...)             # executes LAST (outermost)
```

**Why**: CORS must be outermost to handle preflight OPTIONS requests before any other middleware runs. Rate limiting should run first to reject bad requests early.

#### StaticFiles Mount Security
Never mount `StaticFiles` at module import time. Mount during `lifespan` startup:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # ... other startup ...
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")
    yield
```

**Why**: Mounting at import time means `makedirs()` runs before any validation, potentially creating directories in wrong locations. Also, StaticFiles serves files without authentication — consider adding an auth-protected endpoint if uploads contain sensitive data.

#### Health Check Endpoint Best Practices
Health check endpoints should not expose internal information:

```python
@app.get("/api/health")
async def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
    }
    # DO NOT include: developer contact info, email, phone, internal URLs
```

For production, add actual health probes (DB connectivity, disk space):
```python
    # await db.execute(text("SELECT 1"))  # verify DB connection
    # shutil.disk_usage(settings.UPLOAD_DIR)  # verify disk space
```

#### Race Condition Prevention with SELECT ... FOR UPDATE
When multiple concurrent requests increment a counter (e.g., invoice sequences), use row-level locking:

```python
async def get_next_counter_async(self, db: AsyncSession) -> int:
    from sqlalchemy import select, with_for_update

    # Lock the row to prevent concurrent updates
    result = await db.execute(
        select(MyModel).where(MyModel.id == self.id).with_for_update()
    )
    locked = result.scalars().first()
    if not locked:
        raise ValueError("Record not found")

    current = locked.counter
    locked.counter = current + 1
    await db.flush()
    return current
```

**Why**: Without `with_for_update()`, two concurrent requests can read the same value, increment it, and write back the same result — producing duplicate sequence numbers. `SELECT ... FOR UPDATE` locks the row until the transaction commits.

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
