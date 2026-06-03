"""
ContaEC - Catálogos del SRI (Servicio de Rentas Internas del Ecuador)
Esquemas Pydantic y datos completos de los catálogos según FICHA TECNICA

Incluye:
- Tarifas de IVA (Tabla 16)
- Tarifas de ICE (Tabla 18)
- Retenciones de IVA (Tabla 19)
- Retenciones de Renta (Tabla 20)
- Tipos de Comprobante (Tabla 1)
- Tipos de Identificación (Tabla 7)
- Formas de Pago (Tabla 23)
- Estados de Comprobante
- Tipos de Contribuyente
- Tipos de Régimen
"""
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# ==========================================
# Esquemas base de catálogos
# ==========================================

class IVATarifa(BaseModel):
    """
    Tarifa de IVA según Tabla 16 del SRI.
    
    El SRI requiere DOS códigos en el XML de comprobantes electrónicos:
    - 'codigo' → va en el tag <codigo> (identifica el tipo de impuesto: 2=IVA)
    - 'codigo_porcentaje' → va en el tag <codigoPorcentaje> (identifica la tarifa específica)
    
    IMPORTANTE: codigo_porcentaje NO es lo mismo que el porcentaje numérico.
    Ejemplo: codigo_porcentaje="4" corresponde al 15%, codigo_porcentaje="2" al 12%.
    
    La tarifa general vigente es 15% (codigo_porcentaje="4") desde 2024.
    """
    codigo: str = Field(
        ...,
        description="Código del impuesto según Tabla 16. Siempre '2' para IVA. Se usa en el tag <codigo> del XML."
    )
    codigo_porcentaje: str = Field(
        ...,
        description=(
            "Código de la tarifa de IVA según Tabla 16. Se usa en el tag <codigoPorcentaje> del XML. "
            'Valores: "0"=0%, "2"=12%, "3"=14%, "4"=15%, "5"=5%, "6"=No objeto, "7"=Exento, "8"=8%, "10"=13%'
        )
    )
    porcentaje: Decimal = Field(
        ...,
        description="Porcentaje numérico de la tarifa de IVA. Ej: 15.0 para la tarifa general vigente."
    )
    descripcion: str = Field(
        ...,
        description="Descripción legible de la tarifa incluyendo porcentaje y vigencia."
    )


class ICETarifa(BaseModel):
    """
    Tarifa de ICE según Tabla 18 del SRI.
    Impuesto a los Consumos Especiales aplicable a productos específicos.
    """
    codigo: str = Field(..., description="Código de la tarifa de ICE")
    descripcion: str = Field(..., description="Descripción del producto sujeto a ICE")
    tarifa_ad_valorem: Optional[Decimal] = Field(
        None,
        description="Tarifa ad valorem (porcentaje sobre el valor)",
    )
    tarifa_especifica: Optional[Decimal] = Field(
        None,
        description="Tarifa específica (valor fijo por unidad)",
    )


class RetencionIVA(BaseModel):
    """
    Porcentaje de retención de IVA según Tabla 19 del SRI.
    Aplicable según el tipo de bien o servicio.
    """
    codigo: str = Field(..., description="Código de retención de IVA")
    porcentaje: Decimal = Field(..., description="Porcentaje de retención")
    descripcion: str = Field(..., description="Descripción de la retención")


class RetencionRenta(BaseModel):
    """
    Porcentaje de retención de Renta según Tabla 20 del SRI.
    Aplicable según el concepto de retención.
    """
    codigo: str = Field(..., description="Código de retención de Renta")
    porcentaje: Decimal = Field(..., description="Porcentaje de retención")
    descripcion: str = Field(..., description="Descripción de la retención")


class TipoComprobante(BaseModel):
    """
    Tipo de comprobante electrónico según Tabla 1 del SRI.
    """
    codigo: str = Field(..., description="Código del tipo de comprobante")
    nombre: str = Field(..., description="Nombre del tipo de comprobante")
    descripcion: str = Field(..., description="Descripción del tipo de comprobante (igual que nombre, para compatibilidad con frontend)")
    tag_xml: str = Field(..., description="Tag XML correspondiente")


class TipoIdentificacion(BaseModel):
    """
    Tipo de identificación según Tabla 7 del SRI.
    Utilizado para identificar al comprador/sujeto en comprobantes.
    """
    codigo: str = Field(..., description="Código del tipo de identificación")
    nombre: str = Field(..., description="Nombre del tipo de identificación")


class FormaPago(BaseModel):
    """
    Forma de pago según Tabla 23 del SRI.
    """
    codigo: str = Field(..., description="Código de la forma de pago")
    nombre: str = Field(..., description="Nombre de la forma de pago")


class EstadoComprobante(BaseModel):
    """
    Estado del comprobante electrónico en el SRI.
    """
    siglas: str = Field(..., description="Siglas del estado")
    nombre: str = Field(..., description="Nombre descriptivo del estado")


# ==========================================
# Datos completos de catálogos del SRI
# ==========================================

# Tarifas de IVA - Tabla 16
# El campo 'codigo' corresponde al tag <codigo> del impuesto en el XML.
# El campo 'codigo_porcentaje' corresponde al tag <codigoPorcentaje> del XML.
# DEFAULT: codigo_porcentaje=4 (15%) es la tarifa general vigente.
IVA_TARIFAS: list[IVATarifa] = [
    IVATarifa(
        codigo="0",
        codigo_porcentaje="0",
        porcentaje=Decimal("0"),
        descripcion="0% - Bienes exentos de IVA",
    ),
    IVATarifa(
        codigo="5",
        codigo_porcentaje="5",
        porcentaje=Decimal("5"),
        descripcion="5% - Tarifa reducida",
    ),
    IVATarifa(
        codigo="8",
        codigo_porcentaje="8",
        porcentaje=Decimal("8"),
        descripcion="8% - Tarifa reducida intermedia",
    ),
    IVATarifa(
        codigo="2",
        codigo_porcentaje="2",
        porcentaje=Decimal("12"),
        descripcion="12% - Tarifa general hasta 31/12/2023",
    ),
    IVATarifa(
        codigo="10",
        codigo_porcentaje="10",
        porcentaje=Decimal("13"),
        descripcion="13% - Tarifa general desde 01/01/2024",
    ),
    IVATarifa(
        codigo="3",
        codigo_porcentaje="3",
        porcentaje=Decimal("14"),
        descripcion="14% - Período transitorio",
    ),
    IVATarifa(
        codigo="4",
        codigo_porcentaje="4",
        porcentaje=Decimal("15"),
        descripcion="15% - Período transitorio (DEFAULT)",
    ),
    IVATarifa(
        codigo="6",
        codigo_porcentaje="6",
        porcentaje=Decimal("0"),
        descripcion="No objeto de IVA",
    ),
    IVATarifa(
        codigo="7",
        codigo_porcentaje="7",
        porcentaje=Decimal("0"),
        descripcion="Exento de IVA",
    ),
    IVATarifa(
        codigo="9",
        codigo_porcentaje="9",
        porcentaje=Decimal("0"),
        descripcion="IVA diferenciado - Tarifa especial según régimen o producto",
    ),
]

# Tarifas de ICE - Tabla 18 (Catálogo completo de productos sujetos a ICE)
ICE_TARIFAS: list[ICETarifa] = [
    # Bebidas alcohólicas
    ICETarifa(codigo="301", descripcion="Cerveza", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.041698")),
    ICETarifa(codigo="302", descripcion="Bebidas gaseosas", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.018744")),
    ICETarifa(codigo="303", descripcion="Ron y aguardiente", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.052925")),
    ICETarifa(codigo="304", descripcion="Vino y otras bebidas alcohólicas", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.037636")),
    ICETarifa(codigo="305", descripcion="Whisky", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.072769")),
    ICETarifa(codigo="306", descripcion="Vodka y gin", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.054577")),
    ICETarifa(codigo="307", descripcion="Licores y crema de licores", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.054577")),
    ICETarifa(codigo="308", descripcion="Piscos y brandy", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.054577")),
    ICETarifa(codigo="309", descripcion="Tequila y mezcal", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.054577")),
    # Tabaco
    ICETarifa(codigo="310", descripcion="Cigarrillos rubios", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.110855")),
    ICETarifa(codigo="311", descripcion="Cigarrillos negros", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.110855")),
    ICETarifa(codigo="312", descripcion="Tabaco elaborado", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.110855")),
    # Vehículos
    ICETarifa(codigo="313", descripcion="Vehículos motorizados de transporte terrestre hasta 3.5 ton", tarifa_ad_valorem=Decimal("5"), tarifa_especifica=None),
    ICETarifa(codigo="314", descripcion="Vehículos motorizados de transporte terrestre de 3.5 a 8 ton", tarifa_ad_valorem=Decimal("5"), tarifa_especifica=None),
    ICETarifa(codigo="315", descripcion="Vehículos motorizados de transporte terrestre de más de 8 ton", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=None),
    ICETarifa(codigo="316", descripcion="Vehículos motorizados para transporte de 10 o más personas", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=None),
    ICETarifa(codigo="317", descripcion="Vehículos motorizados de transporte terrestre - camionetas y furgonetas", tarifa_ad_valorem=Decimal("5"), tarifa_especifica=None),
    ICETarifa(codigo="318", descripcion="Motos y motocicletas", tarifa_ad_valorem=Decimal("5"), tarifa_especifica=None),
    ICETarifa(codigo="319", descripcion="Cuadrones y vehículos similares", tarifa_ad_valorem=Decimal("5"), tarifa_especifica=None),
    ICETarifa(codigo="320", descripcion="Aviones, helicópteros y demás aeronaves", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=None),
    ICETarifa(codigo="321", descripcion="Barcos, yates y demás embarcaciones", tarifa_ad_valorem=Decimal("10"), tarifa_especifica=None),
    # Otros productos
    ICETarifa(codigo="322", descripcion="Armas de fuego", tarifa_ad_valorem=Decimal("100"), tarifa_especifica=None),
    ICETarifa(codigo="323", descripcion="Municiones y explosivos", tarifa_ad_valorem=Decimal("100"), tarifa_especifica=None),
    ICETarifa(codigo="324", descripcion="Fuegos artificiales", tarifa_ad_valorem=Decimal("50"), tarifa_especifica=None),
    ICETarifa(codigo="325", descripcion="Juegos de azar y apuestas", tarifa_ad_valorem=Decimal("15"), tarifa_especifica=None),
    ICETarifa(codigo="326", descripcion="Focos incandescentes", tarifa_ad_valorem=Decimal("100"), tarifa_especifica=None),
    ICETarifa(codigo="327", descripcion="Bebidas energéticas", tarifa_ad_valorem=Decimal("10"), tarifa_especifica=None),
    ICETarifa(codigo="328", descripcion="Concentrados para bebidas energéticas", tarifa_ad_valorem=Decimal("10"), tarifa_especifica=None),
    ICETarifa(codigo="329", descripcion="Bebidas con azúcar en cantidad superior a 25g/500ml", tarifa_ad_valorem=Decimal("18"), tarifa_especifica=None),
    ICETarifa(codigo="330", descripcion="Servicios de televisión pagada", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.016529")),
    ICETarifa(codigo="331", descripcion="Servicios de telecomunicaciones móvil avanzada", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=Decimal("0.014160")),
    ICETarifa(codigo="332", descripcion="Servicios de casinos, salas de juego y bingos", tarifa_ad_valorem=Decimal("35"), tarifa_especifica=None),
    ICETarifa(codigo="333", descripcion="Perfumes y aguas de tocador", tarifa_ad_valorem=Decimal("20"), tarifa_especifica=None),
    ICETarifa(codigo="334", descripcion="Vehículos híbridos y eléctricos", tarifa_ad_valorem=Decimal("0"), tarifa_especifica=None),
]

# Retenciones de IVA - Tabla 19
RETENCION_IVA: list[RetencionIVA] = [
    RetencionIVA(
        codigo="9",
        porcentaje=Decimal("10"),
        descripcion="10% - Bienes de primera necesidad y servicios básicos",
    ),
    RetencionIVA(
        codigo="10",
        porcentaje=Decimal("20"),
        descripcion="20% - Bienes y servicios en general",
    ),
    RetencionIVA(
        codigo="1",
        porcentaje=Decimal("30"),
        descripcion="30% - Servicios profesionales y técnicos",
    ),
    RetencionIVA(
        codigo="11",
        porcentaje=Decimal("50"),
        descripcion="50% - Servicios de consultoría y asesoría",
    ),
    RetencionIVA(
        codigo="2",
        porcentaje=Decimal("70"),
        descripcion="70% - Servicios entre sociedades (vinculadas)",
    ),
    RetencionIVA(
        codigo="3",
        porcentaje=Decimal("100"),
        descripcion="100% - Retención total (transporte privado, seguros, etc.)",
    ),
    RetencionIVA(
        codigo="7",
        porcentaje=Decimal("0"),
        descripcion="0% - No procede retención de IVA (exportaciones)",
    ),
    RetencionIVA(
        codigo="8",
        porcentaje=Decimal("0"),
        descripcion="No procede retención - Operaciones no sujetas a retención",
    ),
]

# Retenciones de Renta - Tabla 20 (Catálogo completo)
RETENCION_RENTA: list[RetencionRenta] = [
    # Bienes
    RetencionRenta(codigo="1", porcentaje=Decimal("2"), descripcion="Bienes raíces - Enriquecimiento por arrendamiento"),
    RetencionRenta(codigo="2", porcentaje=Decimal("2"), descripcion="Bienes muebles - Enajenación de bienes muebles"),
    RetencionRenta(codigo="3", porcentaje=Decimal("1"), descripcion="Bienes de naturaleza distinta - Enajenación de bienes de naturaleza distinta a los anteriores"),
    # Servicios
    RetencionRenta(codigo="301", porcentaje=Decimal("10"), descripcion="Servicios profesionales - Honorarios profesionales y otros pagos por servicios"),
    RetencionRenta(codigo="302", porcentaje=Decimal("8"), descripcion="Servicios técnicos - Servicios de consultoría, asesoría y asistencia técnica"),
    RetencionRenta(codigo="303", porcentaje=Decimal("8"), descripcion="Servicios de intermediación - Comisiones y demás pagos por intermediación"),
    RetencionRenta(codigo="304", porcentaje=Decimal("2"), descripcion="Servicios de transporte privado de carga"),
    RetencionRenta(codigo="305", porcentaje=Decimal("1"), descripcion="Servicios de transporte público de carga"),
    RetencionRenta(codigo="306", porcentaje=Decimal("1"), descripcion="Servicios de transporte público de pasajeros"),
    RetencionRenta(codigo="307", porcentaje=Decimal("10"), descripcion="Servicios de comunicación"),
    RetencionRenta(codigo="308", porcentaje=Decimal("2"), descripcion="Servicios de construcción"),
    RetencionRenta(codigo="309", porcentaje=Decimal("1"), descripcion="Servicios de vigilancia y seguridad"),
    RetencionRenta(codigo="310", porcentaje=Decimal("5"), descripcion="Servicios de limpieza"),
    RetencionRenta(codigo="311", porcentaje=Decimal("8"), descripcion="Servicios de publicidad y comunicación"),
    RetencionRenta(codigo="312", porcentaje=Decimal("8"), descripcion="Servicios de investigación y desarrollo"),
    RetencionRenta(codigo="313", porcentaje=Decimal("2"), descripcion="Servicios de mantenimiento y reparación"),
    # Otros
    RetencionRenta(codigo="314", porcentaje=Decimal("2"), descripcion="Arrendamiento mercantil - Leasing"),
    RetencionRenta(codigo="315", porcentaje=Decimal("5"), descripcion="Seguros y reaseguros"),
    RetencionRenta(codigo="316", porcentaje=Decimal("8"), descripcion="Regalías y derechos de autor"),
    RetencionRenta(codigo="317", porcentaje=Decimal("8"), descripcion="Marcas, patentes y know-how"),
    RetencionRenta(codigo="318", porcentaje=Decimal("10"), descripcion="Honorarios y comisiones al exterior"),
    RetencionRenta(codigo="319", porcentaje=Decimal("2"), descripcion="Otras rentas - Pagos no especificados"),
    RetencionRenta(codigo="320", porcentaje=Decimal("5"), descripcion="Rendimientos financieros - Intereses y rendimientos"),
    RetencionRenta(codigo="321", porcentaje=Decimal("2"), descripcion="Dividendos y utilidades"),
    RetencionRenta(codigo="322", porcentaje=Decimal("25"), descripcion="Pagos al exterior - No sujetos a convenio de doble tributación"),
    RetencionRenta(codigo="323", porcentaje=Decimal("10"), descripcion="Pagos al exterior - Sujetos a convenio de doble tributación"),
    # Especiales RIMPE
    RetencionRenta(codigo="324", porcentaje=Decimal("2"), descripcion="Régimen RIMPE Emprendedor - Compras de bienes"),
    RetencionRenta(codigo="325", porcentaje=Decimal("1"), descripcion="Régimen RIMPE Negocio Popular - Compras de bienes"),
    RetencionRenta(codigo="326", porcentaje=Decimal("3"), descripcion="Régimen RIMPE Emprendedor - Servicios"),
    RetencionRenta(codigo="327", porcentaje=Decimal("2"), descripcion="Régimen RIMPE Negocio Popular - Servicios"),
]

# Tipos de Comprobante Electrónico - Tabla 1
TIPOS_COMPROBANTE: list[TipoComprobante] = [
    TipoComprobante(
        codigo="01",
        nombre="Factura",
        descripcion="Factura",
        tag_xml="factura",
    ),
    TipoComprobante(
        codigo="02",
        nombre="Nota de Venta",
        descripcion="Nota de Venta - Emitida por sujetos no obligados a llevar contabilidad y emitir comprobantes de venta (RIMPE Negocio Popular, RISE)",
        tag_xml="notaVenta",
    ),
    TipoComprobante(
        codigo="03",
        nombre="Liquidación de Compra de Bienes y Prestación de Servicios",
        descripcion="Liquidación de Compra de Bienes y Prestación de Servicios",
        tag_xml="liquidacionCompra",
    ),
    TipoComprobante(
        codigo="04",
        nombre="Nota de Crédito",
        descripcion="Nota de Crédito",
        tag_xml="notaCredito",
    ),
    TipoComprobante(
        codigo="05",
        nombre="Nota de Débito",
        descripcion="Nota de Débito",
        tag_xml="notaDebito",
    ),
    TipoComprobante(
        codigo="06",
        nombre="Guía de Remisión",
        descripcion="Guía de Remisión",
        tag_xml="guiaRemision",
    ),
    TipoComprobante(
        codigo="07",
        nombre="Comprobante de Retención",
        descripcion="Comprobante de Retención",
        tag_xml="comprobanteRetencion",
    ),
    TipoComprobante(
        codigo="08",
        nombre="Proforma",
        descripcion="Proforma / Cotización - Documento interno sin valor fiscal, no se envía al SRI",
        tag_xml="proforma",
    ),
]

# Tipos de Identificación - Tabla 7
TIPOS_IDENTIFICACION: list[TipoIdentificacion] = [
    TipoIdentificacion(codigo="04", nombre="RUC - Registro Único de Contribuyente"),
    TipoIdentificacion(codigo="05", nombre="Cédula de identidad"),
    TipoIdentificacion(codigo="06", nombre="Pasaporte"),
    TipoIdentificacion(codigo="07", nombre="Consumidor final"),
    TipoIdentificacion(codigo="08", nombre="Identificación del exterior"),
]

# Formas de Pago - Tabla 23
FORMAS_PAGO: list[FormaPago] = [
    FormaPago(codigo="01", nombre="Sin utilización del sistema financiero"),
    FormaPago(codigo="15", nombre="Compensación de deudas"),
    FormaPago(codigo="16", nombre="Tarjeta de débito"),
    FormaPago(codigo="17", nombre="Dinero electrónico"),
    FormaPago(codigo="18", nombre="Tarjeta prepago"),
    FormaPago(codigo="19", nombre="Tarjeta de crédito"),
    FormaPago(codigo="20", nombre="Otros con utilización del sistema financiero"),
    FormaPago(codigo="21", nombre="Endoso de títulos"),
]

# Estados de Comprobante Electrónico
ESTADOS_COMPROBANTE: list[EstadoComprobante] = [
    EstadoComprobante(siglas="PPR", nombre="En procesamiento - Comprobante enviado al SRI, pendiente de autorización"),
    EstadoComprobante(siglas="AUT", nombre="Autorizado - Comprobante autorizado por el SRI"),
    EstadoComprobante(siglas="NAT", nombre="No autorizado - Comprobante rechazado por el SRI"),
    EstadoComprobante(siglas="DEV", nombre="Devuelto - Comprobante devuelto por el SRI para corrección"),
    EstadoComprobante(siglas="CAD", nombre="Caducado - Comprobante que excedió el tiempo para autorización"),
]

# Tipos de Contribuyente
CONTRIBUYENTE_TIPOS: list[dict] = [
    {"codigo": "OB", "nombre": "Obligado a llevar contabilidad", "descripcion": "Persona natural o jurídica obligada a llevar contabilidad según el SRI"},
    {"codigo": "NOB", "nombre": "No obligado a llevar contabilidad", "descripcion": "Persona natural no obligada a llevar contabilidad"},
    {"codigo": "RIMPE_EMP", "nombre": "RIMPE Emprendedor", "descripcion": "Régimen Simplificado para Emprendedores y Negocios Populares - Emprendedor. Ingresos hasta $300,000 anual. Presenta anexo RIMPE."},
    {"codigo": "RIMPE_NPC", "nombre": "RIMPE Negocio Popular", "descripcion": "Régimen Simplificado para Negocios Populares. Ingresos hasta $20,000 anual. No presenta anexo RIMPE."},
    {"codigo": "RIMPE_GEN", "nombre": "Régimen General", "descripcion": "Contribuyente del Régimen General. Sociedades y personas naturales con ingresos superiores a $300,000"},
    {"codigo": "CON_ESP", "nombre": "Contribuyente Especial", "descripcion": "Contribuyente designado como especial por el SRI mediante resolución"},
    {"codigo": "AG_RET", "nombre": "Agente de Retención", "descripcion": "Contribuyente designado como agente de retención por el SRI"},
    {"codigo": "SE_PUBLIC", "nombre": "Sector Público", "descripcion": "Entidades del sector público"},
]

# Tipos de Régimen
REGIMEN_TIPOS: list[dict] = [
    {"codigo": "RIMPE_EMPRENDEDOR", "nombre": "RIMPE Emprendedor", "descripcion": "Ingresos brutos entre $20,001 y $300,000 anuales. Presenta anexo RIMPE mensual."},
    {"codigo": "RIMPE_NEGOCIO_POPULAR", "nombre": "RIMPE Negocio Popular", "descripcion": "Ingresos brutos hasta $20,000 anuales. Régimen simplificado, no presenta declaración."},
    {"codigo": "GENERAL", "nombre": "Régimen General", "descripcion": "Sociedades y personas naturales con ingresos superiores a $300,000. Declaración de IVA y Renta."},
    {"codigo": "RISE", "nombre": "Régimen Simplificado RISE", "descripcion": "Régimen Impositivo Simplificado Ecuatoriano. Cuota fija mensual según actividad."},
    {"codigo": "CONTRIBUYENTE_ESPECIAL", "nombre": "Contribuyente Especial", "descripcion": "Designado por el SRI. Resolución específica con obligaciones particulares."},
    {"codigo": "AGENTE_RETENCION", "nombre": "Agente de Retención", "descripcion": "Designado por el SRI como agente de retención de IVA y/o Renta."},
    {"codigo": "SECTOR_PUBLICO", "nombre": "Sector Público", "descripcion": "Entidades del sector público, organismos del Estado."},
]
