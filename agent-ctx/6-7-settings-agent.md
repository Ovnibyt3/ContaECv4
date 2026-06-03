# Task 6-7: Settings Page Implementation

## Work Completed

### 1. Updated `/home/z/my-project/src/lib/api.ts`
Added the following new types and API functions:

**Types:**
- `UserConfig` - Full user configuration response with environment mode, signature status, SMTP config, user profile, and security features
- `SignatureValidation` - Digital signature validation result with subject, issuer, expiry, warnings

**API Functions:**
- `getUserConfig()` - GET `/v1/config/user-config`
- `uploadDigitalSignature(file, password)` - POST `/v1/config/digital-signature` (FormData)
- `getSignatureStatus()` - GET `/v1/config/signature-status`
- `toggleVirusTotal(enabled)` - PUT `/v1/config/virustotal?enabled=`
- `configureSMTP(data)` - POST `/v1/config/smtp`
- `testSMTP()` - POST `/v1/config/test-smtp`
- `switchEnvironmentMode(mode)` - PUT `/v1/config/environment-mode?mode=`
- `updateProfile(data)` - PUT `/v1/config/profile`
- `setBackupKey(key)` - POST `/v1/config/backup-key`
- `uploadCompanyLogo(file)` - POST `/v1/config/company-logo` (FormData)
- `validateSignature(file, password)` - POST `/v1/uploads/validate-signature` (FormData)

All functions follow existing patterns using `apiGet`, `apiPost`, `apiPut` helpers. File upload functions use `FormData` with `fetch` directly (not JSON helpers).

### 2. Created `/home/z/my-project/src/components/contaec-settings.tsx`
Comprehensive settings page with 5 tabs:

**Tab 1: Perfil (Profile)**
- Full name, phone, email (read-only), language selector (es_EC/en_US), theme toggle (light/dark/system)
- Logo upload with preview
- Save button calls `updateProfile()`

**Tab 2: Firma Electrónica (Digital Signature)**
- Status indicator with color-coded badges (none/valid/expired/expiring_soon/uploaded)
- Upload .p12/.pfx file with password field (show/hide toggle)
- "Validar Firma" button validates without saving
- Displays validation results: validity checks grid, subject/issuer info, dates, serial number, warnings
- Alert if signature is expired or expiring soon

**Tab 3: Ambiente (Environment)**
- Sandbox/Production selection cards with visual indicators
- Sandbox: "Los comprobantes se envían al SRI de pruebas. No tienen validez fiscal."
- Production: "Los comprobantes se envían al SRI de producción. Tienen validez fiscal. Requiere firma electrónica válida."
- Warning confirmation when switching to production without valid signature
- Active mode badge display

**Tab 4: Correo (SMTP)**
- Quick-select provider buttons: Gmail, Zoho, Outlook, Office 365
- Manual entry: host, port, user, password (with show/hide), SSL toggle, protocol selector (TLS/SSL/STARTTLS/NONE)
- "Guardar Configuración" and "Probar Configuración" buttons
- Current SMTP status display

**Tab 5: Seguridad (Security)**
- ClamAV status indicator (available/unavailable)
- VirusTotal toggle (if available on server) with Switch component
- Backup encryption key setup with confirmation field
- Password change section (placeholder for future implementation)

### 3. Updated `/home/z/my-project/src/components/contaec-dashboard.tsx`
- Added `Wrench` icon import from lucide-react
- Added `ContaECSettings` import
- Extended `NavItem` type: `'dashboard' | 'companies' | 'sri' | 'license' | 'invoices' | 'settings'`
- Added "Configuración" nav item with Wrench icon to sidebar
- Added render condition for `activeNav === 'settings'` to display `<ContaECSettings />`

### 4. Quality Checks
- Lint passes with zero errors
- Dev server compiles successfully
- All labels in Spanish (Ecuador)
- Green/teal primary color scheme (no indigo/blue)
- Responsive design (mobile-first)
- Dark/light mode support via next-themes
- Proper loading states and error handling throughout
