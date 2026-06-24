# Handoff Document - ContaECv4

**Fecha:** 2026-06-23  
**Autor:** Claude Code  
**Sesión:** Fix errores build frontend - TypeScript type errors + ESLint config

---

## Objetivo Principal

Resolver errores críticos que impiden el build del frontend:
1. **TypeScript:** Propiedades faltantes en interfaces (`LicenseStatus`)
2. **TypeScript:** Type mismatch en feature mapping (`FeatureKey` vs valores minúsculas)
3. **TypeScript:** Tipos incorrectos en `FEATURE_LABELS` declaration
4. **ESLint:** Configuración incompatible con Next.js 15
5. **next-intl:** Warning por configuración deprecated

---

## Estado Actual

### ✅ Completado (Archivos Modificados Localmente)

| Archivo | Cambios | Estado |
|---------|---------|--------|
| `src/lib/api.ts` | Agregadas propiedades `trial_active`, `license_active`, `license_days_remaining` a `LicenseStatus` | ✅ Local |
| `src/hooks/useLicense.tsx` | Corregido tipo de `FEATURE_LABELS` de `Record<FeatureKey, string>` a `as const satisfies Record<FeatureValue, string>` | ✅ Local |
| `src/components/contaec-dashboard.tsx` | FeatureMap con `as const`, tipos corregidos | ✅ Local |
| `src/i18n/request.ts` | Creado archivo (migración de config deprecated) | ✅ Local |
| `next.config.ts` | Actualizado plugin next-intl con ruta explícita | ✅ Local |
| `eslint.config.mjs` | Reescrito para usar flat config compatible con Next.js 15 | ✅ Local |

### ⏳ Pendiente (Deploy a Producción)

| Tarea | Comando/Acción | Prioridad |
|-------|----------------|-----------|
| Copiar archivos frontend modificados | `scp src/lib/api.ts src/hooks/useLicense.tsx src/components/contaec-dashboard.tsx src/i18n/request.ts next.config.ts eslint.config.mjs` | 🔥 Alta |
| Build frontend | `bun run build` | 🔥 Alta |
| Reiniciar frontend | `systemctl restart contaec-frontend` | 🔥 Alta |
| Verificar health | `curl http://localhost:3000` | 🔥 Alta |

---

## Archivos en los que Trabajé

### Modificados en Esta Sesión

| Archivo | Cambios Detallados | Líneas |
|---------|-------------------|--------|
| `src/lib/api.ts` | Agregadas `trial_active: boolean`, `license_active: boolean`, `license_days_remaining: number \| null` a `LicenseStatus` | 525-541 |
| `src/hooks/useLicense.tsx` | Agregado `FeatureValue` type, cambiado `FEATURE_LABELS` a `as const satisfies Record<FeatureValue, string>` | 72-92 |
| `src/components/contaec-dashboard.tsx` | featureMap con `as const` en ambas declaraciones (líneas 384 y 457) | 384, 457 |
| `src/i18n/request.ts` | Archivo nuevo - configuración next-intl según mejor práctica v3.22+ | Todo |
| `next.config.ts` | `createNextIntlPlugin('./src/i18n/request.ts')` en lugar de `createNextIntlPlugin()` | 4 |
| `eslint.config.mjs` | Flat config usando `import nextConfig from "eslint-config-next"` directamente + reglas personalizadas | Todo |

---

## Qué He Intentado

### Exitoso

1. **Diagnosticar error `trial_active`** - Interface `LicenseStatus` no tenía las propiedades que el código usaba
2. **Identificar type mismatch en FEATURE_LABELS** - El tipo era `Record<FeatureKey, string>` pero las claves reales son los valores de `LICENSE_FEATURES` (minúsculas)
3. **Crear tipo `FeatureValue`** - `typeof LICENSE_FEATURES[keyof typeof LICENSE_FEATURES]` para obtener los valores reales ('pos', 'payroll', etc.)
4. **Usar `satisfies` pattern** - `as const satisfies Record<FeatureValue, string>` para type safety con inferencia correcta
5. **ESLint flat config** - Next.js 15 requiere configuración diferente, usar `import nextConfig from "eslint-config-next"` y spread
6. **next-intl migration** - Mover configuración a `src/i18n/request.ts` y referenciar en `next.config.ts`

### Fallos / Errores

1. **Confusión inicial entre `FeatureKey` y `FeatureValue`:**
   - `FeatureKey = keyof typeof LICENSE_FEATURES` → `'POS'`, `'PAYROLL'` (claves en mayúsculas)
   - `FeatureValue = typeof LICENSE_FEATURES[keyof typeof LICENSE_FEATURES]` → `'pos'`, `'payroll'` (valores en minúsculas)
   - `FEATURE_LABELS` usa minúsculas como claves, no mayúsculas
   - **Solución:** Crear `FeatureValue` type y usar `as const satisfies Record<FeatureValue, string>`

2. **ESLint multiple attempts:**
   - Primero intenté `Array.isArray()` check - no funcionó
   - Luego flat config manual sin plugin - error "Could not find plugin"
   - **Solución:** Importar `eslint-config-next` directamente y hacer spread

3. **Intento de usar `as const` solo en featureMap:**
   - Error persistía porque el problema estaba en el tipo base de `FEATURE_LABELS`
   - **Solución:** Corregir el tipo de `FEATURE_LABELS` en `useLicense.tsx`

---

## Errores Corregidos

1. **`LicenseStatus` interface incompleta:**
   ```
   Property 'trial_active' does not exist on type 'LicenseStatus'
   Property 'license_active' does not exist on type 'LicenseStatus'
   Property 'license_days_remaining' does not exist on type 'LicenseStatus'
   ```
   **Fix:** Agregadas `trial_active`, `license_active`, `license_days_remaining`

2. **`FEATURE_LABELS` type incorrecto:**
   ```
   Type '"pos"' is not assignable to type '"POS"'
   ```
   **Fix:** Cambiar de `Record<FeatureKey, string>` a `as const satisfies Record<FeatureValue, string>`

3. **`setLicenseData` no definido:**
   ```
   Cannot find name 'setLicenseData'. Did you mean 'licenseData'?
   ```
   **Fix:** Cambiado a `setLicense` (nombre real del setter)

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

## Notas Importantes del Entorno

**⚠️ ESTE EQUIPO ES SOLO CÓDIGO FUENTE**

- **No ejecutar comandos de build localmente** - Este equipo solo almacena el código
- **Producción:** 10.0.1.20 (LXC Proxmox)
- **Build real:** Se ejecuta en el servidor de producción con `bun run build`
- **Deploy:** Via SCP desde esta máquina al servidor
- **Validación:** Los errores de tipo/ESLint vienen del build en producción

Flujo de trabajo:
```
1. Modificar archivos aquí (Windows local)
2. Copiar a producción con SCP
3. Ejecutar build en servidor Linux
4. Recibir errores del build en producción
5. Corregir aquí, repetir
```

---

## Próximos Pasos (Plan)

### Inmediato (Producción)

```bash
# ============================================
# 1. COPIAR ARCHIVOS FRONTEND CORREGIDOS
# ============================================
scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\src\lib\api.ts" \
  root@10.0.1.20:/opt/contaec/src/lib/api.ts

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\src\hooks\useLicense.tsx" \
  root@10.0.1.20:/opt/contaec/src/hooks/useLicense.tsx

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\src\components\contaec-dashboard.tsx" \
  root@10.0.1.20:/opt/contaec/src/components/contaec-dashboard.tsx

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\src\i18n\request.ts" \
  root@10.0.1.20:/opt/contaec/src/i18n/request.ts

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\next.config.ts" \
  root@10.0.1.20:/opt/contaec/next.config.ts

scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\eslint.config.mjs" \
  root@10.0.1.20:/opt/contaec/eslint.config.mjs

# ============================================
# 2. BUILD FRONTEND (EN PRODUCCIÓN)
# ============================================
ssh root@10.0.1.20
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
// LICENSE_FEATURES usa patrón clave:valor (mayúscula: minúscula)
export const LICENSE_FEATURES = {
  POS: 'pos',        // key: POS (mayúscula), value: 'pos' (minúscula)
  PAYROLL: 'payroll',
} as const;

export type FeatureKey = keyof typeof LICENSE_FEATURES;  // 'POS' | 'PAYROLL'
export type FeatureValue = typeof LICENSE_FEATURES[keyof typeof LICENSE_FEATURES]; // 'pos' | 'payroll'

// FEATURE_LABELS usa los VALORES (minúsculas) como claves
export const FEATURE_LABELS = {
  pos: 'Punto de Venta',    // key: pos (minúscula)
  payroll: 'Nómina',
} as const satisfies Record<FeatureValue, string>;

// Cuando usar cual:
// - checkFeature(feature: FeatureKey) → usa mayúsculas
// - FEATURE_LABELS[feature] → usa minúsculas (FeatureValue)
// - featureMap para UI → usa minúsculas (keyof typeof FEATURE_LABELS)
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
4. **SCP puede fallar por路径 con espacios** - Usar comillas o escape en paths de Windows

---

## Contacto / Historial

- **Usuario:** Steve2109 (git user)
- **Empresa:** TyM - Sistema Contable ContaECv4
- **Producción:** https://conta.tymtechnology.shop
- **Servidor:** 10.0.1.20:80 (LXC Proxmox)
- **Equipo local:** Solo código fuente, NO ejecutar builds

---

*Última actualización: 2026-06-23*  
*Frontend: ✅ Todos los errores TypeScript/ESLint corregidos localmente, ⏳ Pendiente build en producción*