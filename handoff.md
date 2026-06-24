# Handoff Document - ContaECv4

**Fecha:** 2026-06-24
**Autor:** Claude Code
**Sesión 1:** 2026-06-23 — Fix errores build frontend - TypeScript type errors + ESLint config
**Sesión 2:** 2026-06-24 — Fix import faltante `previewEmailTemplateCustom` + FlatCompat ESLint

---

## Objetivo Principal

Resolver todos los errores críticos que impiden el build de producción del frontend:

### Sesión 1 (completado)
1. **TypeScript:** Propiedades faltantes en `LicenseStatus` (`trial_active`, `license_active`, `license_days_remaining`)
2. **TypeScript:** Type mismatch en feature mapping (`FeatureKey` vs valores minúsculas)
3. **TypeScript:** Tipos incorrectos en `FEATURE_LABELS` declaration
4. **ESLint:** Configuración incompatible con Next.js 15 / ESLint v9
5. **next-intl:** Warning por configuración deprecated

### Sesión 2 (completado en local)
6. **TypeScript:** `'previewEmailTemplateCustom'` no exportado desde `@/lib/api`
7. **ESLint:** Error persistente `@rushstack/eslint-patch: calling module not recognized` — fix con `FlatCompat`

---

## Estado Actual

### ✅ Completado y Modificado Localmente

| Archivo | Cambio | Sesión |
|---------|--------|--------|
| `src/lib/api.ts` | Agregadas props `trial_active`, `license_active`, `license_days_remaining` a `LicenseStatus` | 1 |
| `src/lib/api.ts` | Agregado `previewEmailTemplateCustom` a la lista de exports | 2 |
| `src/hooks/useLicense.tsx` | Corregido tipo `FEATURE_LABELS` con `as const satisfies Record<FeatureValue, string>` + nuevo type `FeatureValue` | 1 |
| `src/components/contaec-dashboard.tsx` | `featureMap` con `as const` en ambas declaraciones (líneas 384 y 457) | 1 |
| `src/i18n/request.ts` | Archivo nuevo — migración de config next-intl deprecated | 1 |
| `next.config.ts` | `createNextIntlPlugin('./src/i18n/request.ts')` con ruta explícita | 1 |
| `eslint.config.mjs` | Reescrito usando `FlatCompat` de `@eslint/eslintrc` (fix oficial Next.js 15 + ESLint v9) | 2 |

### ⏳ Pendiente (Deploy a Producción)

| Tarea | Comando/Acción | Prioridad |
|-------|----------------|-----------|
| Instalar `@eslint/eslintrc` si no está | `cd /opt/contaec && bun install @eslint/eslintrc --no-save` (suele venir transit con eslint v9) | 🔥 Alta |
| Copiar archivos al servidor | `scp` de los 7 archivos modificados | 🔥 Alta |
| Build frontend (en producción, NO local) | `bun run build` | 🔥 Alta |
| Reiniciar servicio | `systemctl restart contaec-frontend` | 🔥 Alta |
| Verificar health | `curl http://localhost:3000` y `curl https://conta.tymtechnology.shop` | 🔥 Alta |

---

## Archivos en los que Trabajé

### Sesión 1 (2026-06-23)
- `src/lib/api.ts` (líneas 525-541, 4805)
- `src/hooks/useLicense.tsx` (líneas 72-92)
- `src/components/contaec-dashboard.tsx` (líneas 384, 457)
- `src/i18n/request.ts` (archivo completo nuevo)
- `next.config.ts` (línea 4)
- `eslint.config.mjs` (archivo completo)

### Sesión 2 (2026-06-24)
- `src/lib/api.ts` (línea 4806)
- `eslint.config.mjs` (archivo completo reescrito)

---

## Qué He Cambiado

### `src/lib/api.ts`

**Sesión 1:** Agregadas 3 propiedades a `LicenseStatus`:
```typescript
trial_active: boolean;
license_active: boolean;
license_days_remaining: number | null;
```

**Sesión 2:** Agregado una línea al bloque de exports (después de `previewEmailTemplate,`):
```typescript
previewEmailTemplateCustom,
```
La función ya existía definida internamente (línea 1899) pero faltaba en la lista de exports — bug de export faltante.

### `src/hooks/useLicense.tsx` (Sesión 1)

```typescript
// ANTES
type FeatureKey = keyof typeof LICENSE_FEATURES;
export const FEATURE_LABELS = {
  pos: 'Punto de Venta',
  payroll: 'Nómina',
} as Record<FeatureKey, string>;  // ❌ type mismatch: keys son minúsculas pero FeatureKey es mayúsculas

// AHORA
type FeatureKey = keyof typeof LICENSE_FEATURES;                    // 'POS' | 'PAYROLL'
type FeatureValue = typeof LICENSE_FEATURES[keyof typeof LICENSE_FEATURES]; // 'pos' | 'payroll'
export const FEATURE_LABELS = {
  pos: 'Punto de Venta',
  payroll: 'Nómina',
} as const satisfies Record<FeatureValue, string>;  // ✅ correcta
```

### `src/components/contaec-dashboard.tsx` (Sesión 1)

Dos `featureMap` declarations con `as const` agregado (líneas 384 y 457) para que TypeScript infiera tipos literales.

### `src/i18n/request.ts` (Sesión 1 — archivo nuevo)

```typescript
import { getRequestConfig } from 'next-intl/server';
export default getRequestConfig(async ({ locale }) => ({
  messages: (await import(`../../messages/${locale}.json`)).default,
  timeZone: 'America/Guayaquil',
  formats: { /* ... */ },
}));
```

### `next.config.ts` (Sesión 1)

```typescript
// ANTES
const withNextIntl = createNextIntlPlugin();

// AHORA
const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts');
```

### `eslint.config.mjs` (Sesión 2 — reescrito completo)

```javascript
// ANTES — Sesión 1 intentaba esto pero fallaba en producción:
import nextConfig from "eslint-config-next";
const eslintConfig = [
  ...nextConfig,
  { rules: { /* ... */ } },
];

// AHORA — Sesión 2, fix oficial Next.js 15 + ESLint 9:
import { FlatCompat } from "@eslint/eslintrc";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({ baseDirectory: __dirname });
const eslintConfig = [
  ...compat.extends("next/core-web-vitals"),
  { rules: { /* mismas reglas */ } },
  { ignores: [...] },
];
```

**Por qué `FlatCompat`:** El error `Failed to patch ESLint because the calling module was not recognized` viene de `@rushstack/eslint-patch` (usado internamente por `@next/eslint-plugin-next`). Cuando el config se carga via ESM estático (`.mjs`), el patcher no puede reconocer el módulo que lo invoca. `FlatCompat` envuelve la carga legacy en un contexto CJS donde el patch sí funciona.

---

## Qué He Intentado

### Exitoso

| # | Intento | Resultado |
|---|---------|-----------|
| 1 | Diagnosticar `trial_active` faltante en `LicenseStatus` | ✅ Agregadas las props |
| 2 | Identificar mismatch `FeatureKey` vs valores reales | ✅ Creado `FeatureValue` |
| 3 | Patrón `as const satisfies Record<FeatureValue, string>` | ✅ Type-safe con inferencia |
| 4 | Migrar next-intl a `src/i18n/request.ts` | ✅ Elimina warning deprecated |
| 5 | Rename `setLicenseData` → `setLicense` | ✅ error `Cannot find name` resuelto |
| 6 | (S2) Diagnosticar `previewEmailTemplateCustom` no exportado | ✅ Agregado al export |
| 7 | (S2) Aplicar `FlatCompat` de `@eslint/eslintrc` para ESLint | ✅ Fix oficial Next.js 15 |

### Fallos / Lecciones Aprendidas

| # | Intento Fallido | Por qué falló | Solución |
|---|-----------------|---------------|----------|
| 1 | `Record<FeatureKey, string>` en `FEATURE_LABELS` | `FeatureKey` son las keys en mayúscula (`'POS'`) pero el map usa los values en minúscula (`'pos'`) | Crear `FeatureValue` type |
| 2 | `import nextConfig from "eslint-config-next"` + spread directo (Sesión 1) | `@rushstack/eslint-patch` no reconoce el calling module cuando se carga vía ESM estático | Usar `FlatCompat` (Sesión 2) |
| 3 | ESLint flat config manual sin plugin (intento previo) | Error "Could not find plugin" — faltaban los plugins de Next | Volver a extender `next/core-web-vitals` via `FlatCompat` |
| 4 | Intentar agregar `as const` solo en `featureMap` | El problema real estaba en `FEATURE_LABELS`, no en el map | Corregir el tipo base |

---

## Errores Corregidos (Consolidado)

1. `Property 'trial_active' does not exist on type 'LicenseStatus'` — ✅ Fix: agregar props
2. `Type '"pos"' is not assignable to type '"POS"'` — ✅ Fix: `as const satisfies Record<FeatureValue, string>`
3. `Cannot find name 'setLicenseData'` — ✅ Fix: renombrar a `setLicense`
4. `Key "extends": This appears to be in eslintrc format` — ✅ Fix: flat config con FlatCompat
5. `Failed to patch ESLint because the calling module was not recognized` — ✅ Fix: FlatCompat de `@eslint/eslintrc`
6. `Reading request configuration from ./src/i18n.ts is deprecated` — ✅ Fix: migración a `src/i18n/request.ts`
7. `'"@/lib/api"' has no exported member named 'previewEmailTemplateCustom'` (Sesión 2) — ✅ Fix: agregar a export list

---

## Próximos Pasos (Plan de Deploy)

### Inmediato (Producción 10.0.1.20)

```bash
# ============================================
# 0. ASEGURAR QUE @eslint/eslintrc ESTÁ INSTALADO
# ============================================
ssh root@10.0.1.20
cd /opt/contaec
test -d node_modules/@eslint/eslintrc || bun install @eslint/eslintrc --no-save

# ============================================
# 1. COPIAR ARCHIVOS FRONTEND CORREGIDOS
# ============================================
scp "src/lib/api.ts" root@10.0.1.20:/opt/contaec/src/lib/api.ts
scp "src/hooks/useLicense.tsx" root@10.0.1.20:/opt/contaec/src/hooks/useLicense.tsx
scp "src/components/contaec-dashboard.tsx" root@10.0.1.20:/opt/contaec/src/components/contaec-dashboard.tsx
scp "src/i18n/request.ts" root@10.0.1.20:/opt/contaec/src/i18n/request.ts
scp "next.config.ts" root@10.0.1.20:/opt/contaec/next.config.ts
scp "eslint.config.mjs" root@10.0.1.20:/opt/contaec/eslint.config.mjs

# ============================================
# 2. BUILD FRONTEND
# ============================================
ssh root@10.0.1.20 "cd /opt/contaec && bun run build"
# Esperar:
#   ✓ Compiled successfully
#   ✓ Linting and checking validity of types ... done

# ============================================
# 3. REINICIAR FRONTEND
# ============================================
ssh root@10.0.1.20 "systemctl restart contaec-frontend"

# ============================================
# 4. VERIFICAR SALUD
# ============================================
ssh root@10.0.1.20 "sleep 5 && curl http://localhost:3000 && curl https://conta.tymtechnology.shop"
```

### Riesgo / Backout

Si `bun run build` falla por otro error no anticipado:
- Revisar el output completo (puede haber type errors adicionales en otros archivos)
- Si ESLint pasa pero Next reporta errores de tipo, ejecutar `bun run build` con `NEXT_TELEMETRY_DISABLED=1` para output limpio
- Si `@eslint/eslintrc` no está instalado y `bun install --no-save` falla, agregar a `package.json` y commitear

---

## Notas Importantes del Entorno

**⚠️ ESTE EQUIPO ES SOLO CÓDIGO FUENTE**

- **No ejecutar comandos de build localmente** — este equipo solo almacena el código
- **Producción:** 10.0.1.20 (LXC Proxmox)
- **Build real:** se ejecuta en el servidor con `bun run build`
- **Deploy:** vía SCP desde esta máquina al servidor
- **Validación:** los errores de tipo/ESLint vienen del build en producción

Flujo de trabajo:
```
1. Modificar archivos aquí (Windows local)
2. Copiar a producción con SCP
3. Ejecutar build en servidor Linux
4. Recibir errores del build en producción
5. Corregir aquí, repetir
```

---

## Contexto Técnico Útil

### `LICENSE_FEATURES` y `FEATURE_LABELS` — patrón clave-valor

```typescript
export const LICENSE_FEATURES = {
  POS: 'pos',        // key mayúscula, value minúscula
  PAYROLL: 'payroll',
} as const;

export type FeatureKey = keyof typeof LICENSE_FEATURES;                              // 'POS' | 'PAYROLL'
export type FeatureValue = typeof LICENSE_FEATURES[keyof typeof LICENSE_FEATURES];  // 'pos' | 'payroll'

export const FEATURE_LABELS = {
  pos: 'Punto de Venta',     // usa values como keys
  payroll: 'Nómina',
} as const satisfies Record<FeatureValue, string>;
```

### ESLint Flat Config — Next.js 15 + ESLint 9

```javascript
// ❌ NO funciona: @rushstack/eslint-patch no reconoce el calling module
import nextConfig from "eslint-config-next";
export default [...nextConfig, ...];

// ✅ Funciona: FlatCompat envuelve la carga legacy en contexto CJS
import { FlatCompat } from "@eslint/eslintrc";
const compat = new FlatCompat({ baseDirectory: __dirname });
export default [...compat.extends("next/core-web-vitals"), ...];
```

---

## Contacto / Historial

- **Usuario:** Steve2109 (git user)
- **Empresa:** TyM — Sistema Contable ContaECv4
- **Producción:** https://conta.tymtechnology.shop
- **Servidor:** 10.0.1.20:80 (LXC Proxmox)
- **Equipo local:** Solo código fuente, NO ejecutar builds

---

*Última actualización: 2026-06-24*
*Estado: ✅ Fixes Sesión 2 aplicados en local, ⏳ Pendiente deploy + build en producción (10.0.1.20)*
