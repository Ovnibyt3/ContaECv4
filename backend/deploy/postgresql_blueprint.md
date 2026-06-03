# ContaEC - Blueprint de Despliegue para PostgreSQL en Producción

## Arquitectura de Despliegue

```
Internet → Caddy (Reverse Proxy :80/:443)
              ↓
         FastAPI Backend (:8000)
              ↓
         PostgreSQL (:5432)
```

## 1. Requisitos de PostgreSQL

### Versión mínima: PostgreSQL 15+
### Extensiones requeridas: `uuid-ossp` (para generación de UUIDs)

## 2. Configuración de la Base de Datos

### Crear usuario y base de datos:

```sql
-- Conectar como postgres
sudo -u postgres psql

-- Crear usuario
CREATE USER contaec_user WITH PASSWORD '<SECURE_PASSWORD>';

-- Crear base de datos
CREATE DATABASE contaec_db OWNER contaec_user ENCODING 'UTF8';

-- Otorgar permisos
GRANT ALL PRIVILEGES ON DATABASE contaec_db TO contaec_user;

-- Conectar a la base de datos
\c contaec_db

-- Habilitar extensión UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Otorgar permisos en esquema público
GRANT ALL ON SCHEMA public TO contaec_user;
```

### Configuración de PostgreSQL (`/etc/postgresql/15/main/postgresql.conf`):

```ini
# Conexiones
listen_addresses = 'localhost'
max_connections = 100

# Memoria (ajustar según RAM del servidor)
shared_buffers = 256MB
effective_cache_size = 768MB
work_mem = 4MB
maintenance_work_mem = 64MB

# WAL
wal_level = replica
max_wal_size = 1GB
min_wal_size = 80MB

# Logging
log_destination = 'stderr'
logging_collector = on
log_directory = 'log'
log_filename = 'postgresql-%Y-%m-%d.log'
log_statement = 'mod'
log_min_duration_statement = 1000

# Locale
lc_messages = 'es_EC.UTF-8'
lc_monetary = 'es_EC.UTF-8'
lc_numeric = 'es_EC.UTF-8'
lc_time = 'es_EC.UTF-8'
```

## 3. Variables de Entorno (.env)

```bash
APP_ENV=production
DEBUG=false
SECRET_KEY=<generar-con-openssl-rand-hex-32>
ENCRYPTION_KEY=<generar-con-openssl-rand-hex-32>
JWT_SECRET_KEY=<generar-con-openssl-rand-hex-32>
DATABASE_URL=postgresql+asyncpg://contaec_user:<PASSWORD>@localhost:5432/contaec_db
POSTGRES_USER=contaec_user
POSTGRES_PASSWORD=<SECURE_PASSWORD>
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=contaec_db
ADMIN_EMAIL=steve.mejia@tymtechnology.shop
ADMIN_PASSWORD=<SECURE_ADMIN_PASSWORD>
BACKUP_ENCRYPTION_KEY=<generar-con-openssl-rand-hex-32>
```

## 4. Migración de SQLite a PostgreSQL

### Opción A: Usando Alembic (recomendado para producción)

```bash
cd /opt/ContaEC/backend

# Generar migración inicial
alembic revision --autogenerate -m "initial_schema"

# Aplicar migraciones
alembic upgrade head
```

### Opción B: Usando pgloader (para migrar datos existentes)

```bash
apt install pgloader
pgloader sqlite:///opt/ContaEC/backend/contaec.db postgresql://contaec_user:PASS@localhost/contaec_db
```

## 5. Respaldo Automático

```bash
# Crontab - Respaldar diario a las 2:00 AM
0 2 * * * pg_dump -U contaec_user -Fc contaec_db > /opt/ContaEC/backups/contaec_db_$(date +\%Y\%m\%d).dump
0 3 * * * find /opt/ContaEC/backups/ -name "*.dump" -mtime +30 -delete
```

## 6. Checklist de Despliegue

- [ ] PostgreSQL 15+ instalado y configurado
- [ ] Usuario contaec_user creado con permisos limitados
- [ ] Extensión uuid-ossp habilitada
- [ ] Base de datos contaec_db creada con encoding UTF8
- [ ] Variables de entorno configuradas en .env
- [ ] APP_ENV=production establecido
- [ ] SECRET_KEY, JWT_SECRET_KEY, ENCRYPTION_KEY generados
- [ ] ADMIN_PASSWORD configurada (NO usar default)
- [ ] Migraciones aplicadas (alembic upgrade head)
- [ ] Respaldo automático configurado
- [ ] Caddy configurado como reverse proxy
- [ ] SSL/TLS configurado
- [ ] Firewall: solo puertos 80, 443
- [ ] PostgreSQL solo accesible desde localhost
