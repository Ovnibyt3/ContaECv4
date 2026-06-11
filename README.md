# ContaEC - Sistema Contable y Facturación Electrónica del Ecuador

**Versión:** 4.0.0  
**Desarrollado por:** T&M Technology Ec  
**Teléfono:** 0960068866  
**Soporte:** info@tymtechnology.shop  
**DNS:** conta.tymtechnology.shop  

---

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Requisitos del Servidor](#requisitos-del-servidor)
4. [Instalación Paso a Paso](#instalación-paso-a-paso)
   - [4.1 Preparación del Servidor](#41-preparación-del-servidor)
   - [4.2 Instalación de PostgreSQL](#42-instalación-de-postgresql)
   - [4.3 Configuración de la Base de Datos](#43-configuración-de-la-base-de-datos)
   - [4.4 Instalación de Python y Dependencias](#44-instalación-de-python-y-dependencias)
   - [4.5 Instalación de Node.js y Bun](#45-instalación-de-nodejs-y-bun)
   - [4.6 Despliegue del Backend (FastAPI)](#46-despliegue-del-backend-fastapi)
   - [4.7 Despliegue del Frontend (Next.js)](#47-despliegue-del-frontend-nextjs)
   - [4.8 Configuración del Archivo .env](#48-configuración-del-archivo-env)
   - [4.9 Configuración de Caddy (Proxy Reverso)](#49-configuración-de-caddy-proxy-reverso)
   - [4.10 Instalación de ClamAV](#410-instalación-de-clamav)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Módulos y Funcionalidades](#módulos-y-funcionalidades)
7. [Variables de Entorno (.env)](#variables-de-entorno-env)
8. [Administración](#administración)
9. [Respaldo y Restauración](#respaldo-y-restauración)
10. [Seguridad](#seguridad)
11. [Solución de Problemas](#solución-de-problemas)

---

## Descripción General

ContaEC es un sistema contable integral con facturación electrónica para el Ecuador, cumpliendo con las normativas del SRI (Servicio de Rentas Internas). Incluye:

- **Facturación Electrónica SRI** (XML, XAdES-BES, SOAP, RIDE)
- **Contabilidad de doble partida** (Plan de Cuentas, Asientos, Balance)
- **Nómina RRHH** (IESS, Décimos, Vacaciones, Fondo de Reserva, Liquidaciones)
- **Inventario y Kardex** (FIFO/LIFO/PP, códigos de barras)
- **Multi-empresa** con roles por empresa
- **Licenciamiento** (mensual, trimestral, semestral, anual)
- **CRM, POS, BI, Presupuestos, Proyectos, Integraciones bancarias, ML/IA**
- **Seguridad** (ClamAV, VirusTotal, JWT con revocación, rate limiting, sanitización)

---

## Arquitectura del Sistema

```
Internet (DNS: conta.tymtechnology.shop)
    │
    ▼
┌─────────────────────────────────┐
│   Caddy (Proxy Reverso :80)     │
│   Certificado Let's Encrypt     │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   Next.js 16 (React 19) :3000   │
│   - Interfaz de usuario         │
│   - API Proxy → FastAPI :8000   │
│   - SSR/SSG + Client Components │
└────────────┬────────────────────┘
             │ /api/*
             ▼
┌─────────────────────────────────┐
│   FastAPI (Python 3.12) :8000   │
│   - REST API (~331 endpoints)   │
│   - SRI SOAP (zeep)             │
│   - XML/XAdES-BES (signxml)     │
│   - RIDE PDF (reportlab)        │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   PostgreSQL :5432              │
│   - 73+ modelos SQLAlchemy      │
│   - UUID primary keys           │
│   - Full-text search            │
└─────────────────────────────────┘
```

---

## Requisitos del Servidor

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| CPU | 2 núcleos | 3+ núcleos |
| RAM | 4 GB | 8 GB |
| Almacenamiento | 50 GB | 200 GB |
| SO | Debian 12/Ubuntu 22.04+ | Debian 12 |
| Python | 3.11+ | 3.12 |
| Node.js | 20+ | 22+ |
| PostgreSQL | 15+ | 16+ |

**Servidor actual (LXC Proxmox):**
- IP: 10.0.1.20:80
- CPU: 8 x Intel Xeon E5-1620 v2 (3 núcleos usados)
- RAM: 10 GB (6 GB libres)
- Disco: 205 GB HDD
- Red: vmbr0 (internet) + vmbr1 (10.0.1.20/24)

---

## Instalación Paso a Paso

### 4.1 Preparación del Servidor

```bash
# Actualizar el sistema
apt update && apt upgrade -y

# Instalar herramientas esenciales
apt install -y curl wget git unzip htop nano sudo gnupg2 lsb-release

# Instalar certificados CA
apt install -y ca-certificates
```

### 4.2 Instalación de PostgreSQL

```bash
# Create Key Directory
sudo install -d /usr/share/postgresql-common/pgdg

# Agregar repositorio oficial de PostgreSQL
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

# Update the Repository List with the Key Path
# Overwrite your existing list file to include the signed-by directive:
sudo sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'   

# Instalar PostgreSQL 16
apt update
apt install -y postgresql-17 postgresql-contrib-17

# Habilitar y arrancar el servicio
systemctl enable postgresql
systemctl start postgresql
```

### 4.3 Configuración de la Base de Datos

```bash
# Cambiar al usuario postgres
sudo -u postgres psql

# Ejecutar los siguientes comandos SQL:
CREATE USER contaec_user WITH PASSWORD 'd';
CREATE DATABASE contaec_db OWNER contaec_user;
GRANT ALL PRIVILEGES ON DATABASE contaec_db TO contaec_user;

# Habilitar extensión UUID (requerida por los modelos)
\c contaec_db
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
\q
```

**Configuración de PostgreSQL** (`/etc/postgresql/17/main/postgresql.conf`):

```ini
# Memoria (ajustar según RAM disponible, 6GB libres → asignar ~2GB)
shared_buffers = 512MB
effective_cache_size = 1536MB
work_mem = 16MB
maintenance_work_mem = 128MB

# Conexiones
max_connections = 100
superuser_reserved_connections = 3

# WAL
wal_buffers = 16MB
min_wal_size = 80MB
max_wal_size = 1GB
checkpoint_completion_target = 0.9

# Logging
log_min_duration_statement = 500
log_checkpoints = on
log_connections = on
log_disconnections = on

# Locale
lc_messages = 'es_EC.UTF-8'
lc_monetary = 'es_EC.UTF-8'
lc_numeric = 'es_EC.UTF-8'
lc_time = 'es_EC.UTF-8'
```

**Configuración de acceso** (`/etc/postgresql/17/main/pg_hba.conf`):

```
# Añadir línea para el usuario de la app (colocar antes de las configuraciones del sistema)
local   contaec_db      contaec_user                    md5
host    contaec_db      contaec_user    127.0.0.1/32    md5
host    contaec_db      contaec_user    ::1/128         md5
```

```bash
# Reiniciar PostgreSQL para aplicar cambios
systemctl restart postgresql

# Verificar conexión
psql -U contaec_user -d contaec_db -h localhost -c "SELECT version();"
```

### 4.4 Instalación de Python y Dependencias

```bash
# Instalar Python 3.12 y herramientas de compilación
apt install -y python3 python3-venv python3-dev python3-pip build-essential libpq-dev
# Crear entorno virtual
cd /opt
mkdir -p contaec
cd contaec

# Clonar el repositorio (o copiar archivos del proyecto)
# git clone <repositorio> .
# O copiar vía scp/rsync
# Para mover el repositorio clonado al directorio padre
# sudo mv /opt/contaec/ContaECv4/* /opt/contaec/ 
# sudo mv /opt/contaec/ContaECv4/.* /opt/contaec/ 2>/dev/null && sudo rmdir /opt/contaec/ContaECv4

# Crear y activar entorno virtual
python3 -m venv /opt/contaec/.venv
source /opt/contaec/.venv/bin/activate

# Instalar dependencias del backend
cd /opt/contaec/backend
pip install -r requirements.txt
```

### 4.5 Instalación de Node.js y Bun

```bash
# Instalar Node.js 22
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs

# Instalar Bun (runtime alternativo, más rápido)
curl -fsSL https://bun.sh/install | bash
source ~/.bashrc

# Verificar instalaciones
node --version   # v22.x
bun --version    # 1.x
```

### 4.6 Despliegue del Backend (FastAPI)

```bash
# Crear directorios necesarios
mkdir -p /opt/contaec/backend/backups
mkdir -p /opt/contaec/backend/uploads
mkdir -p /opt/contaec/backend/temp
mkdir -p /opt/contaec/backend/signatures

# Configurar el archivo .env (ver sección 7)
cp /opt/contaec/.env.example /opt/contaec/backend/.env
nano /opt/contaec/backend/.env  # Editar con valores de producción

# Crear servicio systemd para el backend
cat > /etc/systemd/system/contaec-backend.service << 'EOF'
[Unit]
Description=ContaEC FastAPI Backend
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/opt/contaec/backend
ExecStart=/opt/contaec/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 2
Restart=always
RestartSec=5
Environment=APP_ENV=production

[Install]
WantedBy=multi-user.target
EOF

# Habilitar y arrancar el backend
systemctl daemon-reload
systemctl enable contaec-backend
systemctl start contaec-backend

# Verificar que el backend responde
curl http://localhost:8000/api/health
```

### 4.7 Despliegue del Frontend (Next.js)

```bash
cd /opt/contaec

# Instalar dependencias del frontend
bun install

# Construir el frontend para producción
bun run build

# Crear servicio systemd para el frontend
cat > /etc/systemd/system/contaec-frontend.service << 'EOF'
[Unit]
Description=ContaEC Next.js Frontend
After=network.target contaec-backend.service
Requires=contaec-backend.service

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/opt/contaec
ExecStart=/root/.bun/bin/bun .next/standalone/server.js
Restart=always
RestartSec=5
Environment=PORT=3000
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
EOF

# Habilitar y arrancar el frontend
systemctl daemon-reload
systemctl enable contaec-frontend
systemctl start contaec-frontend

# Verificar que el frontend responde
curl http://localhost:3000
```

### 4.8 Configuración del Archivo .env

Crear el archivo `/opt/contaec/backend/.env` con el siguiente contenido:

```bash
# ============================================
# ContaEC - Variables de Entorno de Producción
# ============================================

# --- Aplicación ---
APP_NAME=ContaEC
APP_VERSION=1.0.0
APP_ENV=production
DEBUG=false

# SECURITY: Generar claves únicas y seguras con:
SECRET_KEY=VGVqoqj0Z252UJR6xmrBCllbZIfmkwrYmlZatrD4cewVqSQc38ZZPyMar70hO6_OVKMfdmX6Eaap9V3dNTHZBA
ENCRYPTION_KEY=Oa4w_01KGCLqV0G3PDusJOoPhMMfMcYTl20d2UjCyHXvHL7YiSsdh9Or3-zivGpd52xx7VM69khuZ1tZR0dmZA
JWT_SECRET_KEY=kkcR9iveo-RfXWvtpBkbdkjc3P9ND2SUerA5uG_96wGjk7RDOIVUhSbxVSMnCWGwcbeLMYWwldv4WALdT2m9Lg

# --- Base de Datos (PostgreSQL) ---
DATABASE_URL=postgresql+asyncpg://contaec_user:EvJcqP2z4zoryZ5@localhost:5432/contaec_db
POSTGRES_USER=contaec_user
POSTGRES_PASSWORD=EvJcqP2z4zoryZ5
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=contaec_db

# --- Autenticación JWT ---
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7

# --- Credenciales Admin ---
ADMIN_EMAIL=steve.mejia@tymtechnology.shop
ADMIN_PASSWORD=Vitaestcum21..

# --- Servicios Web del SRI ---
# (Las URLs ya están configuradas por defecto en config.py)
# SRI_WS_RECEPCION_PRUEBAS=https://celcer.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl
# SRI_WS_AUTORIZACION_PRUEBAS=https://celcer.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl
# SRI_WS_RECEPCION_PRODUCCION=https://cel.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl
# SRI_WS_AUTORIZACION_PRODUCCION=https://cel.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl

# --- Respaldos ---
BACKUP_DIR=./backups
BACKUP_ENCRYPTION_KEY=rXOHnntm1N6yDBvc2-Z2GogT20rpb0KtqiNuxN3VZGU=

# --- ClamAV (Antivirus) ---
CLAMAV_ENABLED=true
CLAMAV_SOCKET=/var/run/clamav/clamd.ctl
CLAMAV_HOST=127.0.0.1
CLAMAV_PORT=3310

# --- VirusTotal ---
VIRUSTOTAL_ENABLED=false
VIRUSTOTAL_API_KEY=778b612188000a11cc6fd51f4aafb3e79ed72674524e82ff6320a9f0dbce9ec9

# --- CORS ---
CORS_ORIGINS=https://conta.tymtechnology.shop,http://10.0.1.20

# --- Rate Limiting ---
RATE_LIMIT_PER_MINUTE=60

# --- Servidor ---
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# --- Almacenamiento Volátil ---
TEMP_DIR=./temp
UPLOAD_DIR=./uploads
```

**GENERACIÓN DE CLAVES SEGURAS:**

```bash
# Ejecutar estas líneas y copiar los resultados al .env
source /opt/contaec/.venv/bin/activate

# SECRET_KEY
python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(64))"

# ENCRYPTION_KEY
python3 -c "import secrets; print('ENCRYPTION_KEY=' + secrets.token_urlsafe(64))"

# JWT_SECRET_KEY
python3 -c "import secrets; print('JWT_SECRET_KEY=' + secrets.token_urlsafe(64))"

# BACKUP_ENCRYPTION_KEY (Fernet)
python3 -c "from cryptography.fernet import Fernet; print('BACKUP_ENCRYPTION_KEY=' + Fernet.generate_key().decode())"
```

### 4.9 Configuración de Caddy (Proxy Reverso)

```bash
# Instalar Caddy
apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
apt update
apt install -y caddy
```

Editar el Caddyfile (`/etc/caddy/Caddyfile`):

```
conta.tymtechnology.shop {
    # Proxy principal → Next.js (frontend + API proxy)
    reverse_proxy localhost:3000

    # Seguridad
    header {
        X-Content-Type-Options nosniff
        X-Frame-Options DENY
        X-XSS-Protection "1; mode=block"
        Referrer-Policy strict-origin-when-cross-origin
        Strict-Transport-Security "max-age=31536000; includeSubDomains"
    }

    # Compresión
    encode gzip zstd

    # Logs
    log {
        output file /var/log/caddy/contaec.log
        format console
    }
}
```

```bash
# Crear directorio de logs
mkdir -p /var/log/caddy
chown caddy:caddy /var/log/caddy

# Reiniciar Caddy
systemctl restart caddy

# Verificar que Caddy obtuvo certificado SSL
systemctl status caddy
journalctl -u caddy --no-pager | tail -20
```

### 4.10 Instalación de ClamAV

```bash
# Instalar ClamAV y el daemon
apt install -y clamav clamav-daemon

# Actualizar base de datos de virus
freshclam

# Configurar clamd para socket TCP (más compatible con Python)
# Editar /etc/clamav/clamd.conf
# Asegurar estas líneas:
# TCPSocket 3310
# TCPAddr 127.0.0.1
# o usar socket Unix:
# LocalSocket /var/run/clamav/clamd.ctl

# Habilitar y arrancar el daemon
systemctl enable clamav-daemon
systemctl start clamav-daemon

# Verificar que está corriendo
systemctl status clamav-daemon

# Configurar actualización automática de la base de datos
systemctl enable clamav-freshclam
systemctl start clamav-freshclam
```

---

## Estructura del Proyecto

```
/opt/contaec/
├── backend/                        # FastAPI Backend
│   ├── app/
│   │   ├── api/v1/
│   │   │   ├── endpoints/          # 27+ archivos de endpoints
│   │   │   │   ├── auth.py         # Autenticación JWT
│   │   │   │   ├── admin.py        # Panel de administración
│   │   │   │   ├── companies.py    # Empresas + consulta RUC SRI
│   │   │   │   ├── comprobantes.py # Facturación electrónica SRI
│   │   │   │   ├── crm.py          # CRM (pipeline, leads, oportunidades)
│   │   │   │   ├── payroll.py      # Nómina (roles, décimos, liquidaciones)
│   │   │   │   ├── bi.py           # Business Intelligence
│   │   │   │   └── ...             # 20+ archivos más
│   │   │   └── router.py           # Router principal (~331 rutas)
│   │   ├── core/
│   │   │   ├── config.py           # Configuración (.env + pydantic)
│   │   │   ├── database.py         # SQLAlchemy async engine
│   │   │   ├── security.py         # JWT + bcrypt + blacklist
│   │   │   ├── xml_generator.py    # Generación XML SRI
│   │   │   ├── xml_signer.py       # Firma XAdES-BES
│   │   │   ├── sri_service.py      # Cliente SOAP SRI
│   │   │   ├── ride_generator.py   # PDF RIDE (factura impresa)
│   │   │   ├── email_service.py    # Envío de correo SMTP
│   │   │   ├── scanner.py          # ClamAV + VirusTotal
│   │   │   ├── encryption.py       # Cifrado Fernet (datos sensibles)
│   │   │   └── ...                 # 10+ módulos más
│   │   ├── middleware/
│   │   │   └── security.py         # Rate limit + sanitización + headers
│   │   ├── models/                 # 20+ archivos de modelos SQLAlchemy
│   │   ├── schemas/                # 24+ archivos de schemas Pydantic
│   │   ├── services/               # ML service
│   │   └── main.py                 # Entry point FastAPI
│   ├── requirements.txt            # 27 dependencias Python
│   ├── deploy/
│   │   └── postgresql_blueprint.md # Guía de migración PostgreSQL
│   └── .env                        # Variables de entorno (NO commitear)
│
├── src/                            # Next.js 16 Frontend
│   ├── app/
│   │   ├── page.tsx                # Entry point (login/dashboard/admin)
│   │   └── api/[...path]/route.ts  # API proxy → FastAPI
│   ├── components/
│   │   ├── contaec-dashboard.tsx   # Dashboard principal
│   │   ├── contaec-admin.tsx       # Panel admin
│   │   ├── contaec-invoices.tsx    # Facturación SRI
│   │   ├── contaec-crm.tsx         # CRM
│   │   ├── contaec-hr.tsx          # Recursos Humanos
│   │   ├── contaec-bi.tsx          # Business Intelligence
│   │   ├── contaec-pos.tsx         # Punto de Venta
│   │   └── ...                     # 15+ componentes más
│   │   └── ui/                     # 45 componentes shadcn/ui
│   └── lib/
│       ├── api.ts                  # ~320 funciones API + ~170 tipos
│       ├── i18n.ts                 # 3 idiomas (es_EC, en_US, pt_BR)
│       └── utils.ts                # Utilidades Tailwind
│
├── prisma/                         # Schema Prisma (legacy, no usado en prod)
├── Caddyfile                       # Configuración proxy reverso
├── package.json                    # Dependencias Node.js
├── next.config.ts                  # Configuración Next.js
└── README.md                       # Este archivo
```

---

## Módulos y Funcionalidades

### Fase 1: Infraestructura ✅
- FastAPI (Python 3.12) + Next.js 16 (React 19)
- PostgreSQL (bloqueado en producción, SQLite solo desarrollo)
- Caddy proxy reverso con SSL Let's Encrypt

### Fase 2: Auth, Multiempresa, Admin, Licencias, ClamAV ✅
- JWT con revocación (blacklist) y rotación de refresh tokens
- Multi-empresa con roles granulares por empresa (UserCompanyRole)
- Panel admin con dashboard, salud del sistema, gestión de usuarios
- Licenciamiento: mensual, trimestral, semestral, anual
- Alerta de licencia por expirar (15 días antes)
- Renovación por WhatsApp (wa.me/593960068866)
- ClamAV + VirusTotal para escaneo de archivos subidos
- Rate limiting (60 req/min por IP)
- Sanitización de entradas (SQL injection + XSS)
- Headers de seguridad (CSP, X-Frame-Options, etc.)

### Fase 3: Facturación Electrónica SRI ✅
- 10 tarifas IVA: 0%, 5%, 8%, 12%, 13%, 14%, 15% (default), No objeto, Exento, Diferenciado
- 34 tarifas ICE con ad valorem + específica
- Retenciones IVA (10%, 20%, 30%, 50%, 70%, 100%, 0%) y Renta (28 códigos)
- 8 estados de comprobante: BORRADOR, FIRMADO, ENVIADO, AUTORIZADO, RECHAZADO, DEVUELTA, CADUCADA, CONTINGENCIA
- 8 tipos de contribuyente y 7 tipos de régimen (incluyendo RIMPE)
- Consumidor Final (cliente por defecto)
- Proformas con conversión a factura
- Facturas, Notas de Crédito/Débito, Retenciones, Guías de Remisión, Liquidación de Compras
- Generación XML per Ficha Técnica SRI v2.32 (clave acceso módulo 11)
- Firma XAdES-BES (RSA-SHA256) con signxml
- Comunicación SOAP con SRI (enviar + consultar con reintentos)
- RIDE PDF con código de barras, QR y todas las secciones SRI
- Pre-validación (8 reglas) y corrección de rechazados
- Envío por email de comprobantes autorizados
- Procesar (1-click: firmar + enviar + consultar)

### Fase 4: Inventario y Kardex ✅
- Control de productos con stock, stock mínimo, código de barras
- Kardex con saldos corridos (saldo_cantidad, saldo_valor)
- Métodos de valoración: FIFO, LIFO, Promedio Ponderado
- Ajustes de inventario
- Importación desde Excel y CSV
- Exportación a Excel, CSV, PDF, ZIP
- Almacenamiento volátil con auto-limpieza

### Fase 5: Nómina RRHH ✅
- Registro de empleados (datos personales, contrato, cargo, salario)
- Cargas familiares
- Evaluaciones de desempeño
- Asistencia con soporte biométrico
- Roles de pago (quincenal/mensual) con IESS 9.45%/11.15%
- Décimo tercero (mensualizado/anual) y décimo cuarto (sierra/costa)
- Vacaciones y fondo de reserva
- Utilidades (15% participación trabajadores)
- Liquidaciones laborales (finiquito/despido/renuncia)
- Impuesto a la Renta progresivo (tabla SRI 2024)
- Rubros personalizables (bonos, comisiones, anticipos, préstamos)
- Reportes: IESS, RDEP, roles de pago
- Exportación Excel y CSV para pago bancario

### Fase 6: Frontend ✅
- React 19 + Next.js 16 + Tailwind CSS + shadcn/ui
- Modo claro/oscuro (colores suaves que no cansan la vista)
- 3 idiomas: Español Ecuador (default), English, Português Brasil
- Dashboard interactivo con KPIs
- 20+ componentes de dominio
- Responsive (mobile-first)

### Fase 7: SMTP + Sandbox ✅
- Múltiples perfiles SMTP por usuario (Gmail, Zoho, Office365, Outlook, Yahoo, Custom)
- IMAP y POP3 para recepción de correo
- Plantillas de email con variables {{variable}}
- Modo sandbox (sin envío real al SRI ni correos)
- Audit logs de operaciones de email

### Fase 8: Compras y Proveedores ✅
- Catálogo de proveedores
- Órdenes de compra (auto-numeración OC-000001)
- Recepción de mercadería (vinculada a OC)
- Cuentas por pagar (pendiente/parcial/pagada/vencida)
- Retenciones de compra (IVA + Renta, auto-cálculo RET-000001)

### Fase 9: Multi-Almacén y Logística ✅
- Múltiples bodegas con ubicaciones (zona/rack/estante/nivel)
- Transferencias entre almacenes (pendiente→en tránsito→recibida→anulada)
- Kardex detallado por almacén
- Stock por ubicación física

### Fase 10: Punto de Venta (POS) ✅
- Terminal táctil con búsqueda por código de barras
- Sesiones de caja (apertura/cierre)
- Arqueo de caja con desglose de denominaciones
- Tickets con múltiples formas de pago
- Anulación de tickets

### Fase 11: Business Intelligence ✅
- 16 KPIs en tiempo real
- Gráficos: ventas mensuales, por tipo, top productos/clientes, flujo efectivo
- 8 tipos de alertas inteligentes
- Cuadro de mando con indicadores de cumplimiento
- Exportación Power BI (star schema JSON)

### Fase 12: Presupuestos ✅
- Presupuesto anual por cuenta (ingresos/egresos)
- Ejecución mensual con porcentaje de avance
- Alertas de sobregiro (50%, 75%, 90%, 100%)
- Comparativo presupuestado vs real

### Fase 13: CRM ✅
- Pipeline visual con etapas personalizables
- Gestión de leads (nuevo→contactado→cualificado→propuesta→ganado/perdido)
- Conversión de lead a oportunidad
- Oportunidades con monto estimado, probabilidad, fecha de cierre
- Actividades (llamada/email/reunión/tarea/nota)
- Segmentación de clientes (manual/regla/RFM)
- Automatizaciones (triggers + actions)

### Fase 14: Proyectos y Servicios ✅
- Gestión de proyectos con estados (planificación→en progreso→completado)
- Asignación de recursos (humano/material/equipo)
- Timesheets con tarifa/hora y facturable/no facturable
- Rentabilidad por proyecto (ingreso - costo = margen)
- Recálculo automático de márgenes

### Fase 15: Integraciones ✅
- Cuentas bancarias con extractos y movimientos
- Conciliación bancaria manual y automática
- Conectores e-commerce: Shopify, WooCommerce, OpenCart, PrestaShop, Magento, Mercado Libre
- Logs de sincronización con métricas

### Fase 16: Machine Learning / IA ✅
- Predicción de ventas (Moving Average, Exponential Smoothing, Linear Regression)
- Detección de fraude (Z-score, duplicados, secuencia anómala, validación RUC)
- Chatbot híbrido (reglas + LLM via z-ai CLI)
- Recomendaciones (producto, cliente, precio, inventario, financiera)
- Auto-categorización (keywords + regex)

---

## Variables de Entorno (.env)

El archivo `.env` va en `/opt/contaec/backend/.env`. Todas las variables se cargan con `pydantic-settings`.

| Variable | Requerida | Default | Descripción |
|----------|-----------|---------|-------------|
| `APP_ENV` | Sí | `development` | `development` o `production` |
| `SECRET_KEY` | Sí (prod) | dev-default | Clave secreta de la aplicación |
| `ENCRYPTION_KEY` | Sí (prod) | dev-default | Clave de cifrado Fernet para datos sensibles |
| `JWT_SECRET_KEY` | Sí (prod) | dev-default | Clave para firmar tokens JWT |
| `DATABASE_URL` | Sí (prod) | SQLite local | URL de conexión a PostgreSQL |
| `POSTGRES_USER` | Sí (prod) | `contaec_user` | Usuario PostgreSQL |
| `POSTGRES_PASSWORD` | Sí (prod) | vacío | Password PostgreSQL |
| `POSTGRES_HOST` | No | `localhost` | Host PostgreSQL |
| `POSTGRES_PORT` | No | `5432` | Puerto PostgreSQL |
| `POSTGRES_DB` | No | `contaec_db` | Nombre de la BD |
| `ADMIN_EMAIL` | No | `steve.mejia@tymtechnology.shop` | Email del administrador |
| `ADMIN_PASSWORD` | Sí | `Vitaestcum21..` | Password del administrador |
| `BACKUP_ENCRYPTION_KEY` | Recomendado | vacío | Clave Fernet para cifrar respaldos |
| `CLAMAV_ENABLED` | No | `false` | Activar escaneo ClamAV |
| `CLAMAV_SOCKET` | No | `/var/run/clamav/clamd.ctl` | Socket Unix de ClamAV |
| `VIRUSTOTAL_ENABLED` | No | `false` | Activar escaneo VirusTotal |
| `VIRUSTOTAL_API_KEY` | Si VT | vacío | API key de VirusTotal |
| `CORS_ORIGINS` | No | `http://localhost:3000` | Orígenes CORS (separados por coma) |
| `RATE_LIMIT_PER_MINUTE` | No | `60` | Requests por minuto por IP |

**⚠️ IMPORTANTE:** En producción, `APP_ENV=production` bloquea SQLite y valida que las claves secretas no tengan valores por defecto.

---

## Administración

### Acceso al Panel Admin

- **URL:** `https://conta.tymtechnology.shop` → Iniciar sesión con credenciales admin
- **Email:** `steve.mejia@tymtechnology.shop`
- **Password:** `Vitaestcum21..`

### Funciones del Panel Admin

1. **Dashboard General** - Resumen de usuarios, licencias, estado del sistema
2. **Salud del Sistema** - CPU, RAM, disco, conexiones BD, uptime
3. **Gestión de Usuarios** - Listar, activar/desactivar, modificar licencias
4. **Problemas de Seguridad** - Alertas de seguridad por usuario

### Sistema de Licencias

| Plan | Duración | Código |
|------|----------|--------|
| Mensual | 30 días | `MENSUAL` |
| Trimestral | 90 días | `TRIMESTRAL` |
| Semestral | 180 días | `SEMESTRAL` |
| Anual | 365 días | `ANUAL` |

Cada tier tiene límites de funcionalidades: empresas, usuarios, comprobantes, empleados, productos.

---

## Respaldo y Restauración

### Respaldo Automático

El sistema realiza un respaldo automático a medianoche (hora Ecuador) de todos los usuarios activos que tienen clave de backup configurada. Los respaldos:

- Se cifran con Fernet usando la clave del usuario
- Se almacenan en `/opt/contaec/backend/backups/`
- Se eliminan automáticamente después de 30 días
- Formato: `backup_{email}_{fecha}.contaec`

### Respaldo Manual

Desde la interfaz: **Configuración → Respaldo → Crear Respaldo**

### Restauración

1. Subir el archivo `.contaec`
2. Ingresar la clave de cifrado
3. El sistema restaura: empresas (por RUC), clientes (por identificación), productos (por código)

---

## Seguridad

### Medidas Implementadas

| Medida | Implementación |
|--------|---------------|
| Autenticación | JWT + bcrypt + refresh token rotation |
| Revocación de tokens | Blacklist in-memory con JTI + cleanup automático |
| Detección de replay | Rotación de refresh tokens con revocación en cadena |
| Cifrado de datos sensibles | Fernet (AES-128) para firmas, passwords SMTP, configs |
| Sanitización | SQL injection + XSS + path traversal en middleware |
| Rate limiting | 60 req/min por IP (configurable) |
| Headers seguridad | CSP, X-Frame-Options, X-XSS-Protection, HSTS |
| Antivirus | ClamAV (default) + VirusTotal (opcional) |
| Configuración por usuario | Cada usuario tiene su propia config cifrada (no .env compartido) |
| Claves no expuestas | Todos los secrets en .env, validación en producción |
| SQLite bloqueado en prod | RuntimeError si se intenta usar SQLite en producción |

### Permisos de Archivos

```bash
# Proteger el archivo .env
chmod 600 /opt/contaec/backend/.env
chown www-data:www-data /opt/contaec/backend/.env

# Proteger directorio de backups
chmod 700 /opt/contaec/backend/backups
chown www-data:www-data /opt/contaec/backend/backups

# Proteger directorio de uploads
chmod 755 /opt/contaec/backend/uploads
chown www-data:www-data /opt/contaec/backend/uploads

# Proteger firmas digitales
chmod 700 /opt/contaec/backend/signatures
chown www-data:www-data /opt/contaec/backend/signatures
```

---

## Solución de Problemas

### El backend no arranca

```bash
# Verificar logs del servicio
journalctl -u contaec-backend --no-pager | tail -50

# Verificar que PostgreSQL está corriendo
systemctl status postgresql

# Verificar conexión a la BD
psql -U contaec_user -d contaec_db -h localhost -c "SELECT 1;"

# Verificar que el .env tiene las variables correctas
cat /opt/contaec/backend/.env | grep DATABASE_URL
```

### Error de certificado SSL SRI

El SRI usa certificados que pueden no estar en el bundle CA del sistema. Si hay errores SSL:

```bash
# Descargar certificado del SRI
echo | openssl s_client -connect celcer.sri.gob.ec:443 2>/dev/null | openssl x509 > /usr/local/share/ca-certificates/sri.crt
update-ca-certificates
```

### Error de firma electrónica

1. Verificar que el archivo .p12/.pfx es válido
2. Verificar que la contraseña es correcta
3. Verificar que la firma no ha expirado
4. El sistema detecta automáticamente CAs ecuatorianas (BCE, Security Data, ANF)

### El frontend no conecta al backend

1. Verificar que el backend está en puerto 8000: `curl http://localhost:8000/api/health`
2. Verificar que Caddy está proxyando correctamente: `curl https://conta.tymtechnology.shop/api/health`
3. Verificar CORS en el .env: `CORS_ORIGINS=https://conta.tymtechnology.shop`

### Resetear password de admin

```bash
cd /opt/contaec/backend
source /opt/contaec/.venv/bin/activate
python3 -c "
import bcrypt
new_pass = 'NUEVA_PASSWORD'
hashed = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt()).decode()
print(f'Hash: {hashed}')
print('Ejecutar en PostgreSQL:')
print(f\"UPDATE users SET hashed_password = '{hashed}' WHERE email = 'steve.mejia@tymtechnology.shop';\")
"
```

---

## Comandos Útiles

```bash
# Reiniciar todos los servicios
systemctl restart postgresql contaec-backend contaec-frontend caddy

# Ver estado de todos los servicios
systemctl status postgresql contaec-backend contaec-frontend caddy

# Ver logs en tiempo real
journalctl -u contaec-backend -f

# Respaldar la base de datos manualmente
sudo -u postgres pg_dump contaec_db > /opt/contaec/backups/manual_$(date +%Y%m%d_%H%M%S).sql

# Restaurar base de datos desde SQL
sudo -u postgres psql contaec_db < /opt/contaec/backups/manual_YYYYMMDD_HHMMSS.sql

# Actualizar la aplicación
cd /opt/contaec
git pull  # o copiar nuevos archivos
cd backend && source /opt/contaec/.venv/bin/activate && pip install -r requirements.txt
cd .. && bun install && bun run build
systemctl restart contaec-backend contaec-frontend
```

---

## Estadísticas del Proyecto

| Métrica | Cantidad |
|---------|----------|
| Modelos SQLAlchemy | 80+ |
| Endpoints API | ~331 |
| Schemas Pydantic | ~7,000 líneas |
| Componentes React | 20+ dominio + 45 UI |
| Funciones API (frontend) | ~320 |
| Tipos TypeScript | ~170 |
| Traducciones i18n | ~130 keys × 3 idiomas |
| Librerías Python | 27 |
| Módulos Core | 15 |

---

**ContaEC** - Sistema Contable y Facturación Electrónica del Ecuador  
© 2024 T&M Technology Ec | info@tymtechnology.shop | 0960068866
