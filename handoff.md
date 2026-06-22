# Handoff Document - ContaECv4

**Fecha:** 2026-06-20  
**Autor:** Claude Code  
**Sesión:** Fix errores build backend + frontend

---

## Objetivo Principal

Resolver errores críticos que impiden el build y despliegue en producción:
1. **Backend:** `NameError: ContribuyenteTipo is not defined`
2. **Frontend:** JSX en archivos `.ts` (deben ser `.tsx`)

---

## Estado Actual

### ✅ Completado

1. **Backend (`backend/app/schemas/sri.py`):**
   - Movidas las clases `ContribuyenteTipo` y `RegimenTipo` a líneas 27-91 (antes de las funciones que las usan)
   - Eliminadas definiciones duplicadas que estaban en líneas 554-591
   - **Estado local:** ✅ Corregido
   - **Estado servidor:** ⏳ Pendiente copiar y reiniciar servicio

2. **Frontend (identificado):**
   - `src/hooks/useLicense.ts` tiene JSX en línea 280 → debe renombrarse a `.tsx`
   - Resto de archivos `.ts` en `src/hooks/` también deben convertirse a `.tsx`

### 📋 Pendiente (Para producción)

| Tarea | Comando/Acción | Prioridad |
|-------|----------------|-----------|
| Copiar `sri.py` al servidor | `scp backend/app/schemas/sri.py root@10.0.1.20:/opt/contaec/backend/app/schemas/sri.py` | 🔥 Alta |
| Renombrar hooks a `.tsx` | `cd /opt/contaec/src/hooks && for f in *.ts; do mv "$f" "${f%.ts}.tsx"; done` | 🔥 Alta |
| Build frontend | `bun run build` | 🔥 Alta |
| Reiniciar backend | `systemctl restart contaec-backend` | 🔥 Alta |
| Verificar health | `curl http://localhost:8000/api/health` | 🔥 Alta |

---

## Archivos en los que Trabajé

### Modificados

| Archivo | Cambios | Estado |
|---------|---------|--------|
| `backend/app/schemas/sri.py` | Clases `ContribuyenteTipo`/`RegimenTipo` movidas arriba (líneas 27-91), duplicados eliminados | ✅ Local |
| `src/hooks/useLicense.ts` | Identificado: tiene JSX en línea 280, requiere renombrar a `.tsx` | ⏳ Pendiente |
| `src/hooks/*.ts` (todos) | Pendiente rename a `.tsx` | ⏳ Pendiente |

### Eliminados (sesiones anteriores)

| Archivo | Razón |
|---------|-------|
| `MIGRACION_NEXT_INTL.md` | Contenido movido a README.md |
| `INSTALL_NEXT_INTL.md` | Contenido movido a README.md |

---

## Qué He Intentado

### Exitoso

1. **Diagnosticar error backend** - `journalctl -u contaec-backend` mostró `NameError: ContribuyenteTipo`
2. **Identificar causa raíz** - Clases definidas después de funciones que las usan como type hints
3. **Reestructurar `sri.py`** - Clases movidas antes que funciones, duplicados eliminados
4. **Identificar error frontend** - JSX en archivo `.ts` no es válido para webpack/Next.js

### Patrón de Fix Documentado

**Backend (Python):**
```python
# ANTES (ERROR)
def get_contribuyente_by_codigo(codigo: str) -> ContribuyenteTipo | None:  # ContribuyenteTipo no definido aún
    ...

class ContribuyenteTipo(BaseModel):  # Definido después
    ...

# AHORA (CORRECTO)
class ContribuyenteTipo(BaseModel):  # Definido primero
    ...

def get_contribuyente_by_codigo(codigo: str) -> ContribuyenteTipo | None:  # Ahora funciona
    ...
```

**Frontend (TypeScript):**
```bash
# ANTES (ERROR)
src/hooks/useLicense.ts  # Contiene JSX como <div className=...>

# AHORA (CORRECTO)
src/hooks/useLicense.tsx  # Extensión correcta para JSX
```

---

## Fallos / Errores

1. **Backend no levanta** - `sri.py` tenía error de orden de definiciones (Python no permite forward references en type hints sin comillas)
2. **Frontend build falla** - webpack rechaza JSX en archivos `.ts`:
   ```
   Expected '>', got 'className'
   ./src/hooks/useLicense.ts:280:1
   <div className="flex items-center justify-center p-8">
   ```
3. **No se pudo ejecutar comandos en servidor** - Sesión actual no tiene conexión SSH directa al servidor

---

## Próximos Pasos (Plan)

### Inmediato (Producción)

```bash
# ============================================
# 1. COPIAR ARCHIVO SRI.PY CORREGIDO
# ============================================
scp "C:\Users\steve\Documentos\Empresas\TyM\Sistema Contable\ContaECv4\ContaECv4\backend\app\schemas\sri.py" \
  root@10.0.1.20:/opt/contaec/backend/app/schemas/sri.py

# ============================================
# 2. RENOMBRAR HOOKS DE .TS A .TSX
# ============================================
cd /opt/contaec/src/hooks
for f in *.ts; do mv "$f" "${f%.ts}.tsx"; done

# Verificar qué archivos fueron renombrados
ls -la

# Si hay más errores de JSX en otros archivos .ts:
grep -rn "className\|<div\|<span\|<button" src/ --include="*.ts"

# ============================================
# 3. BUILD FRONTEND
# ============================================
cd /opt/contaec
bun run build

# ============================================
# 4. REINICIAR BACKEND
# ============================================
sudo systemctl restart contaec-backend

# ============================================
# 5. VERIFICAR SALUD
# ============================================
sleep 10
sudo systemctl status contaec-backend
curl http://localhost:8000/api/health
curl http://localhost:3000
```

---

## Notas Técnicas

### Error Backend: Forward Reference en Type Hints

Python no permite usar una clase en un type hint antes de que esté definida (a menos que uses comillas):

```python
# ❌ ESTO FALLA
def foo() -> MiClase: ...  # MiClase no existe aún
class MiClase: ...

# ✅ ESTO FUNCIONA
class MiClase: ...
def foo() -> MiClase: ...

# ✅ O CON COMILLAS (forward reference)
def foo() -> "MiClase": ...  # string, no evalúa aún
class MiClase: ...
```

### Error Frontend: .ts vs .tsx

| Extensión | Uso |
|-----------|-----|
| `.ts` | TypeScript puro, sin JSX |
| `.tsx` | TypeScript + JSX (componentes React) |

Next.js/webpack requiere `.tsx` para cualquier archivo con JSX (`<div>`, `<Component />`, etc.)

---

## Riesgos / Advertencias

1. **No reiniciar backend sin copiar `sri.py`** - Seguirá fallando con `NameError`
2. **Build puede fallar si hay más `.ts` con JSX** - Revisar output de webpack para identificar archivos pendientes
3. **Hooks renombrados pueden requerir actualizar imports** - TypeScript usualmente lo resuelve solo, pero verificar

---

## Contacto / Historial

- **Usuario:** Steve2109 (git user)
- **Empresa:** TyM - Sistema Contable ContaECv4
- **Producción:** https://conta.tymtechnology.shop
- **Servidor:** 10.0.1.20:80 (LXC Proxmox)

---

*Última actualización: 2026-06-20*  
*Backend sri.py: ✅ Corregido local, ⏳ Pendiente deploy*  
*Frontend hooks: ⏳ Pendiente renombrar .ts → .tsx*