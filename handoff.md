# Handoff Document - ContaECv4

**Fecha:** 2026-06-20  
**Autor:** Claude Code  
**Sesión:** Continuación - Migración a next-intl

---

## Objetivo Principal

Completar la migración del sistema i18n customizado a **next-intl v3**, configurando todos los archivos necesarios para instalación en producción SIN instalar dependencias localmente.

El usuario especificó explícitamente:
> "acaba la migracion a next-intl en lugar de i18n, pero no instales nada en este computador solo configura los archivos para que se pueda instalar en produccion"

---

## Estado Actual

### ✅ Completado

1. **Archivos de traducción creados:**
   - `messages/es.json` - 350+ keys en español
   - `messages/en.json` - Traducciones en inglés
   - `messages/pt.json` - Traducciones en portugués

2. **Configuración next-intl implementada:**
   - `next-intl.config.ts` - Plugin configuration
   - `src/i18n.ts` - getRequestConfig setup
   - `src/i18n-config.ts` - Locales, helpers, conversión legacy
   - `src/middleware.ts` - Detección de idioma (URL, cookie, header)
   - `src/app/layout.tsx` - NextIntlClientProvider con getLocale/getMessages
   - `src/lib/i18n-provider.tsx` - Proveedor opcional
   - `next.config.ts` - Integrado con withNextIntl
   - `package.json` - next-intl@^3.26.0 agregado

3. **Documentación:**
   - `README.md` - Sección completa "Migración a next-intl" agregada
   - Archivos `.md` temporales eliminados (MIGRACION_NEXT_INTL.md, INSTALL_NEXT_INTL.md)

### 📋 Pendiente (Para producción)

| Tarea | Comando/Acción | Prioridad |
|-------|----------------|-----------|
| Instalar dependencias | `cd /opt/contaec && bun install` | 🔥 Alta |
| Build producción | `bun run build` | 🔥 Alta |
| Reiniciar frontend | `systemctl restart contaec-frontend` | 🔥 Alta |
| Migrar componentes | Actualizar `useI18n()` → `useTranslations()` | Media |
| Eliminar archivos obsoletos | `rm src/lib/i18n.ts`, `rm src/lib/i18n-context.tsx` | Baja |

---

## Archivos en los que Trabajé

### Modificados

| Archivo | Cambios | Líneas ~ |
|---------|---------|----------|
| `src/app/layout.tsx` | NextIntlClientProvider + getLocale/getMessages | +15 líneas |
| `next.config.ts` | withNextIntl integration | +4 líneas |
| `package.json` | next-intl@^3.26.0 dependency | +1 línea |
| `README.md` | Sección next-intl completa | +200 líneas |

### Creados

| Archivo | Propósito | Líneas ~ |
|---------|-----------|----------|
| `messages/es.json` | Traducciones español (350+ keys) | 364 |
| `messages/en.json` | Traducciones inglés | 364 |
| `messages/pt.json` | Traducciones portugués | 364 |
| `next-intl.config.ts` | Plugin configuration | 8 |
| `src/i18n.ts` | getRequestConfig + timeZone + formats | 35 |
| `src/i18n-config.ts` | Locales, helpers legacy↔next-intl | 45 |
| `src/middleware.ts` | Locale detection middleware | 35 |
| `src/lib/i18n-provider.tsx` | I18nProvider opcional | 50 |
| `handoff.md` | Este documento | - |

### Eliminados

| Archivo | Razón |
|---------|-------|
| `MIGRACION_NEXT_INTL.md` | Contenido movido a README.md |
| `INSTALL_NEXT_INTL.md` | Contenido movido a README.md |

---

## Qué He Intentado

### Exitoso

1. **Migración completa de configuración** - Todos los archivos next-intl configurados
2. **Traducciones migradas** - 350+ keys de i18n.ts convertidas a formato namespaced JSON
3. **Layout actualizado** - async Server Component con NextIntlClientProvider
4. **Middleware configurado** - Detección automática de locale (URL, cookie, Accept-Language)
5. **Documentación consolidada** - Todo en README.md como solicitó el usuario

### Patrón de Migración Documentado

```typescript
// ANTES (OBSOLETO)
import { useI18n } from '@/lib/i18n-context';
const { t } = useI18n();
t('nav.dashboard')

// AHORA (next-intl)
import { useTranslations } from 'next-intl';
const t = useTranslations('Navigation');
t('dashboard')
```

---

## Fallos / Rechazos

1. **Instalación local rechazada** - El usuario indicó explícitamente NO instalar nada en su computador local
2. **Archivos .md eliminados** - El usuario indicó que no creara archivos .md adicionales, solo configurara los archivos y agregara al README.md

---

## Próximos Pasos (Plan)

### Inmediato (Producción)

1. **Copiar archivos al servidor:**
   ```bash
   # Archivos nuevos a copiar:
   messages/es.json
   messages/en.json
   messages/pt.json
   next-intl.config.ts
   src/i18n.ts
   src/i18n-config.ts
   src/middleware.ts
   src/lib/i18n-provider.tsx
   ```

2. **Instalar en producción:**
   ```bash
   cd /opt/contaec
   bun install              # Instala next-intl
   bun run build            # Build Next.js
   systemctl restart contaec-frontend
   ```

3. **Verificar funcionamiento:**
   ```bash
   curl https://conta.tymtechnology.shop
   bun list next-intl       # Confirmar instalación
   ```

### Migración Gradual de Componentes

1. **Identificar componentes a migrar:**
   ```bash
   grep -r "useI18n" src/components/ --include="*.tsx"
   ```

2. **Actualizar componente por componente:**
   - `contaec-dashboard.tsx`
   - `contaec-login.tsx`
   - `contaec-settings.tsx`
   - (todos los que usen useI18n)

3. **Eliminar archivos obsoletos (después de migrar todo):**
   ```bash
   rm src/lib/i18n.ts
   rm src/lib/i18n-context.tsx
   ```

---

## Notas Técnicas

### next-intl vs i18n Customizado

| Característica | i18n Custom | next-intl |
|----------------|-------------|-----------|
| Carga de traducciones | Client-side | SSR + Client |
| Bundle size | Todas las keys | Solo locale actual |
| SEO | Limitado | Óptimo (html lang dinámico) |
| Routing | Manual | Automático con middleware |
| Formateo fechas/números | Manual | Integrado |
| TypeScript | Manual | Tipado completo |

### Estructura de Claves

```json
// messages/es.json (namespaced/nested)
{
  "Navigation": {
    "dashboard": "Panel Principal"
  },
  "Common": {
    "save": "Guardar"
  }
}

// Uso en componentes
t('Navigation.dashboard')  // o useTranslations('Navigation') + t('dashboard')
```

### Compatibilidad Legacy

El sistema soporta conversión entre códigos:
- Legacy: `es_EC`, `en_US`, `pt_BR`
- next-intl: `es`, `en`, `pt`

Usar helpers en `src/i18n-config.ts`:
```typescript
legacyToNextIntl('es_EC')     // → 'es'
nextIntlToLegacy('es')        // → 'es_EC'
```

---

## Decisiones de Diseño

### Por qué next-intl

1. **Oficial para Next.js App Router** - Mantenido por el equipo de Next.js
2. **SSR nativo** - Traducciones cargan en servidor (mejor SEO, performance)
3. **Tree-shaking automático** - Solo carga el locale actual
4. **Middleware integrado** - Routing automático por locale
5. **Formateo integrado** - Fechas, números, monedas, tiempo relativo

### Por qué archivos namespaced

1. **Mejor organización** - Keys agrupadas por dominio (Navigation, Common, Dashboard)
2. **Easier mantenimiento** - 350+ keys en un solo archivo plano eran difíciles de navegar
3. **Soporte para splitting** - next-intl permite cargar namespaces por ruta/componente

### Por qué Documentation en README.md

1. **Single source of truth** - El usuario pidió no crear archivos .md adicionales
2. **Fácil acceso** - README.md es el primer archivo que se consulta
3. **Versionado con el código** - Cambios en migración quedan en el mismo commit

---

## Riesgos / Advertencias

1. **No eliminar i18n.ts hasta migrar todos los componentes** - El sistema fallará si hay componentes usando useI18n()

2. **Build required después de cambiar JSON** - En producción, editar messages/*.json requiere `bun run build` para aplicar cambios

3. **Middleware intercepta rutas** - Las rutas sin locale (`/dashboard`) redirigen a `/es/dashboard`

4. **Cookie NEXT_LOCALE** - El locale se guarda en cookie, no en localStorage (cambio de comportamiento)

---

## Contacto / Historial

- **Usuario:** Steve2109 (git user)
- **Empresa:** TyM - Sistema Contable ContaECv4
- **Producción:** https://conta.tymtechnology.shop
- **Sesión anterior:** erro.md (715 líneas), ESTADO_ERRORES.md, handoff.md (CRM fixes)

---

*Última actualización: 2026-06-20*
*Configuración next-intl: ✅ Completa, lista para instalar en producción*