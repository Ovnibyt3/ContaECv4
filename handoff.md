# Handoff Document - ContaECv4

**Fecha:** 2026-06-23  
**Autor:** Claude Code  
**Sesión:** Fix errores build frontend - TypeScript type errors + ESLint config

---

## Objetivo Principal

Resolver errores críticos que impiden el build del frontend:
1. **TypeScript:** Propiedades faltantes en interfaces (`AdminUser`)
2. **TypeScript:** Variables no encontradas (`setLicenseData`)
3. **TypeScript:** Type mismatch en feature mapping (`FeatureKey` vs string literals)
4. **ESLint:** Configuración incompatible con Next.js 15
5. **next-intl:** Warning por configuración deprecated

---

## Estado Actual

### ✅ Completado (Archivos Modificados Localmente)

| Archivo | Cambios | Estado |
|---------|---------|--------|
| `src/lib/api.ts` | Agregadas propiedades `is_trial` y `trial_end_date` a interfaz `AdminUser` | ✅ Local |
| `src/components/contaec-dashboard.tsx` | Corregido `setLicenseData` → `setLicense`, featureMap con claves correctas | ✅ Local |
| `src/i18n/request.ts` | Creado archivo (migración de config deprecated) | ✅ Local |
| `next.config.ts` | Actualizado plugin next-intl con ruta explícita | ✅ Local |
| `eslint.config.mjs` | Reescrito para usar flat config compatible con Next.js 15 | ✅ Local |

### ⏳ Pendiente (Deploy a Producción)

| Tarea | Comando/Acción | Prioridad |
|-------|----------------|-----------|
| Copiar archivos frontend modificados | `scp src/lib/api.ts src/components/contaec-dashboard.tsx src/i18n/request.ts next.config.ts eslint.config.mjs` | 🔥 Alta |
| Build frontend | `bun run build` | 🔥 Alta |
| Reiniciar frontend | `systemctl restart contaec-frontend` | 🔥 Alta |
| Verificar health | `curl http://localhost:3000` | 🔥 Alta |

---

## Archivos en los que Trabajé

### Modificados en Esta Sesión

| Archivo | Cambios Detallados | Líneas |
|---------|-------------------|--------|
| `src/lib/api.ts` | Agregadas `is_trial: boolean` y `trial_end_date: string \| null` a `AdminUser` | 453-469 |
| `src/components/contaec-dashboard.tsx` | `setLicenseData` → `setLicense` (línea 204), `featureMap` corregido a `keyof typeof FEATURE_LABELS` con valores minúscula (`pos`, `payroll`, `multi_warehouse`, etc.) | 142, 204, 383-393, 455-470, 634-663 |
| `src/i18n/request.ts` | Archivo nuevo - configuración next-intl según mejor práctica v3.22+ | Todo |
| `next.config.ts` | `createNextIntlPlugin('./src/i18n/request.ts')` en lugar de `createNextIntlPlugin()` | 4 |
| `eslint.config.mjs` | Flat config usando `eslint-config-next` directamente + reglas personalizadas | Todo |

---

## Qué He Intentado

### Exitoso

1. **Diagnosticar error `trial_end_date`** - Interface `AdminUser` no tenía la propiedad que el código usaba
2. **Identificar `setLicenseData`** - Error de naming, el estado se llama `setLicense`
3. **Feature mapping type-safe** - `FEATURE_LABELS` usa claves minúscula (`pos`, `payroll`) no `FeatureKey` (mayúsculas)
4. **ESLint flat config** - Next.js 15 requiere configuración diferente, usar `import nextConfig from "eslint-config-next"` y spread
5. **next-intl migration** - Mover configuración a `src/i18n/request.ts` y referenciar en `next.config.ts`

### Eras / Errores Corregidos

1. **`AdminUser` interface incompleta:**
   ```
   Property 'trial_end_date' does not exist on type 'AdminUser'
   ```
   **Fix:** Agregadas `is_trial` y `trial_end_date`

2. **`setLicenseData` no definido:**
   ```
   Cannot find name 'setLicenseData'. Did you mean 'licenseData'?
   ```
   **Fix:** Cambiado a `setLicense` (nombre real del setter)

3. **Type mismatch en featureMap:**
   ```
   Type '"pos"' is not assignable to type '"POS"'
   ```
   **Fix:** `FEATURE_LABELS` tiene claves en minúscula, `FeatureKey` (de `LICENSE_FEATURES`) tiene valores en mayúscula. Usar `keyof typeof FEATURE_LABELS` directamente.

4. **ESLint config incompatible:**
   ```
   Config (unnamed): Key "extends": This appears to be in eslintrc format
   Failed to patch ESLint because the calling module was not recognized
   ```
   **Fix:** Usar flat config explícito con `import nextConfig from "eslint-config-next"`

5. **next-intl deprecated:**
   ```
   Reading request configuration from ./src/i18n.ts is deprecated
   ```
   **Fix:** Crear `src/i18n/request.ts` y referenciar en `next.config.ts`

---

## Fallos / Errores

1. **Confusión inicial con `FeatureKey` vs `keyof FEATURE_LABELS`:**
   - `FeatureKey = keyof typeof LICENSE_FEATURES` → valores como `'POS'`, `'PAYROLL'` (mayúsculas)
   - `keyof typeof FEATURE_LABELS` → claves como `'pos'`, `'payroll'` (minúsculas)
   - **Solución:** Usar `keyof typeof FEATURE_LABELS` directamente en `featureMap` y `renderLockedView`

2. **ESLint multiple attempts:**
   - Primero intenté `Array.isArray()` check - no funcionó
   - Luego flat config manual sin plugin - error "Could not find plugin"
   - **Solución:** Importar `eslint-config-next` directamente y hacer spread

---

## Próximos Pasos (Plan)

### Inmediato (Producción)

```bash
# ============================================
# 1. COPIAR ARCHIVOS FRONTEND CORREGIDOS
# ============================================
scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\src\lib\api.ts" \
  root@10.0.1.20:/opt/contaec/src/lib/api.ts

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\src\components\contaec-dashboard.tsx" \
  root@10.0.1.20:/opt/contaec/src/components/contaec-dashboard.tsx

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\src\i18n\request.ts" \
  root@10.0.1.20:/opt/contaec/src/i18n/request.ts

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\next.config.ts" \
  root@10.0.1.20:/opt/contaec/next.config.ts

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\eslint.config.mjs" \
  root@10.0.1.20:/opt/contaec/eslint.config.mjs

# ============================================
# 2. BUILD FRONTEND
# ============================================
cd /opt/contaec
bun run build

# Esperar:
# - Compiled successfully
# - Linting and checking validity of types ... done
# - Creating an optimized production build ... done

# ============================================
# 3. REINICIAR FRONTEND
# ============================================
sudo systemctl restart contaec-frontend

# ============================================
# 4. VERIFICAR SALUD
# ============================================
sleep 5
sudo systemctl status contaec-frontend
curl http://localhost:3000
curl https://conta.tymtechnology.shop
```

---

## Notas Técnicas

### TypeScript: Type Safety con Enum-Like Objects

```typescript
//有时候LICENSE_FEATURES 和 FEATURE_LABELS 是不同的映射
export const LICENSE_FEATURES = {
  POS: 'pos',        // key: POS (mayúscula), value: 'pos' (minúscula)
  PAYROLL: 'payroll',
} as const;

export const FEATURE_LABELS = {
  pos: 'Punto de Venta',    // key: pos (minúscula)
  payroll: 'Nómina',
} as const;

// FeatureKey = 'POS' | 'PAYROLL' (las KEYS de LICENSE_FEATURES)
// keyof FEATURE_LABELS = 'pos' | 'payroll' (las KEYS de FEATURE_LABELS)

// Cuando usar cual:
// - checkFeature(feature: FeatureKey) → usa mayúsculas
// - FEATURE_LABELS[feature] → usa minúsculas
// - featureMap para UI → usa minúsculas (keyof FEATURE_LABELS)
```

### ESLint Flat Config (Next.js 15+)

```javascript
// ANTES (eslintrc format - NO FUNCIONA)
module.exports = {
  extends: ['next/core-web-vitals'],
  rules: { ... }
}

// AHORA (flat config - FUNCIONA)
import nextConfig from "eslint-config-next"

export default [
  ...nextConfig,  // Spread de configs predefinidos
  { rules: { ... } },
  { ignores: [...] }
]
```

### next-intl v3.22+ Configuration

```typescript
// next.config.ts
import createNextIntlPlugin from 'next-intl/plugin';
const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts');

// src/i18n/request.ts (nuevo archivo requerido)
import { getRequestConfig } from 'next-intl/server';
export default getRequestConfig(async ({ locale }) => ({
  messages: (await import(`../../messages/${locale}.json`)).default,
  timeZone: 'America/Guayaquil',
  formats: { ... }
}));
```

---

## Riesgos / Advertencias

1. **Build puede fallar si hay más type errors** - Revisar output completo de `bun run build`
2. **ESLint rules pueden causar nuevos warnings** - Configuración actual es permisiva (`warn` en lugar de `error`)
3. **next-intl requiere messages/[locale].json** - Verificar que existen `messages/es.json` y `messages/en.json`

---

## Contacto / Historial

- **Usuario:** Steve2109 (git user)
- **Empresa:** TyM - Sistema Contable ContaECv4
- **Producción:** https://conta.tymtechnology.shop
- **Servidor:** 10.0.1.20:80 (LXC Proxmox)

---

*Última actualización: 2026-06-23*  
*Frontend: ✅ Todos los errores TypeScript/ESLint corregidos localmente, ⏳ Pendiente build en producción*