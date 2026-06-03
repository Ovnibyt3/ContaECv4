"""
ContaEC - Constantes de Recursos Humanos / Nómina Ecuador
Tasas IESS, décimos, vacaciones, horas extras y salario básico
conforme a la legislación laboral ecuatoriana vigente 2024
"""
from decimal import Decimal

# ==========================================
# Tasas IESS 2024
# ==========================================
IESS_PERSONAL_RATE = Decimal("9.45")    # Aporte personal del empleado al IESS
IESS_PATRONAL_RATE = Decimal("11.15")   # Aporte patronal del empleador al IESS
IESS_RIESGOS_RATE = Decimal("0.5")      # Seguro de Riesgos del Trabajo (empleador)
SECAP_RATE = Decimal("0.2")             # Servicio Ecuatoriano de Capacitación Profesional
CENACES_RATE = Decimal("0.1")           # Consejo Nacional de Evaluación y Acreditación

# Total aporte empleador = IESS_PATRONAL + IESS_RIESGOS + SECAP + CENACES = 11.95%
TOTAL_APORTE_PATRONAL_RATE = IESS_PATRONAL_RATE + IESS_RIESGOS_RATE + SECAP_RATE + CENACES_RATE

# Base de cálculo IESS: el aporte se calcula sobre el total de ingresos gravados
# (sueldo + horas extras + comisiones + bonos + otros_ingresos)

# ==========================================
# Décimos
# ==========================================
DECIMO_TERCERO_MONTHS = 12  # Se divide el sueldo mensual entre 12 meses
DECIMO_CUARTO_SALARIO_BASICO = Decimal("450.00")  # Salario básico unificado para décimo cuarto 2024
DECIMO_CUARTO_REGION_SIERRA = "sierra"  # Pago en agosto (Sierra/Amazonía)
DECIMO_CUARTO_REGION_COSTA = "costa"    # Pago en marzo (Costa/Galápagos)

# ==========================================
# Vacaciones
# ==========================================
VACACIONES_DIAS_ANIO = 15                # 15 días de vacaciones por cada año completo
VACACIONES_DIAS_ACUMULADOS_MAX = 30      # Máximo de días acumulables
VACACIONES_PROVISION_RATE = Decimal("15") / Decimal("360")  # 15/360 del sueldo diario por día trabajado

# ==========================================
# Horas extras - Recargos según Código del Trabajo
# ==========================================
HORA_EXTRA_DIURNA_MULT = Decimal("1.25")    # 25% recargo sobre valor hora normal
HORA_EXTRA_NOCTURNA_MULT = Decimal("1.50")  # 50% recargo sobre valor hora normal
HORA_EXTRA_DOMINICAL_MULT = Decimal("2.00") # 100% recargo sobre valor hora normal

# Horas de trabajo
DIAS_MES = 30                             # Días del mes para cálculos
HORAS_SEMANAL_DEFAULT = Decimal("40.00")  # Horas semanales por defecto
HORAS_MENSUAL_DEFAULT = Decimal("240.00") # 40 horas/semana * 4 semanas

# ==========================================
# Fondo de reserva
# ==========================================
FONDO_RESERVA_ANIOS_MIN = 1               # Mínimo 1 año para tener derecho
FONDO_RESERVA_RATE = Decimal("8.33")      # Un sueldo mensual por cada año (1/12 mensual)

# ==========================================
# Salario básico unificado 2024
# ==========================================
SALARIO_BASICO_UNIFICADO_2024 = Decimal("460.00")

# ==========================================
# Tipos de contrato válidos
# ==========================================
TIPOS_CONTRATO = ["indefinido", "fijo", "por_obra", "temporal", "pasantia"]

# ==========================================
# Tipos de pago válidos
# ==========================================
TIPOS_PAGO = ["mensual", "quincenal", "semanal"]

# ==========================================
# Estados del empleado válidos
# ==========================================
ESTADOS_EMPLEADO = ["activo", "vacaciones", "licencia", "suspendido", "cese"]

# ==========================================
# Estados del rol de pago válidos
# ==========================================
ESTADOS_ROL = ["borrador", "aprobado", "pagado", "anulado"]

# ==========================================
# Géneros válidos
# ==========================================
GENEROS = ["M", "F"]

# ==========================================
# Tipos de cuenta bancaria
# ==========================================
TIPOS_CUENTA = ["ahorro", "corriente"]
