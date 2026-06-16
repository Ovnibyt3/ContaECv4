Guía para contribuyentes
Ficha técnica:
Manual de usuario, catálogo y
especificaciones técnicas.
“Emisión de comprobantes electrónicos”
Método de automatización off-line.
ACTUALIZADO OCTUBRE 2025.
Versión 2.32
1

Índice
1. Introducción ...................................................................................................................................... 6
2. Consideraciones generales ................................................................................................................ 6
3. Base legal ........................................................................................................................................... 6
4. Proceso de solicitud de certificación de emisión de documentos electrónicos ............................... 8
5. Proceso de generación, firma electrónica y solicitud de autorización en línea de comprobantes
electrónicos ......................................................................................................................................... 10
6. Proceso de firmas electrónicas y lineamientos de parametrización en los aplicativos .................. 14
7. Servicios expuestos en internet para la autorización de comprobantes electrónicos ................... 15
8. Servicios expuestos en internet para consultas de comprobantes electrónicos ............................ 20
9. Facturador gratuito de generación de comprobantes electrónicos ............................................... 25
10. Caso específico de retenciones en la comercializadores / Distribuidores de derivados del
petróleo y retención presuntiva de IVA a los editores, distribuidores y voceadores que participan en
la comercialización de periódicos y/o revistas. ................................................................................... 34
11. Códigos de errores y advertencias de validación .......................................................................... 35
12. Códigos de error para aplicación de la devolución automática del IVA ....................................... 38
13. Servicios web para la devolución automática del IVA a personas adultas mayores - DIG............ 40
14. Anexos ........................................................................................................................................... 47
ANEXO 1 - FORMATOS XML VERSIÓN 1.0.0 ........................................................................................ 47
ANEXO 2 - FORMATO DE REPRESENTACIONES IMPRESAS DE DOCUMENTOS ELECTRÓNICOS (RIDE)
............................................................................................................................................................. 60
ANEXO 3 - FORMATOS XML VERSIÓN 1.1.0 ........................................................................................ 66
ANEXO 4 - FORMATOS XML FACTURA EXPORTACIÓN APLICADOS A LAS VERSIONES 1.0.0 y 1.1.0 ... 75
ANEXO 5 - FORMATOS XML FACTURA REEMBOLSO APLICADO EN LAS VERSIONES 1.0.0 y 1.1.0 ...... 83
ANEXO 6 - FORMATOS XML FACTURA CON SUBSIDIOS APLICADO EN LAS VERSIONES 1.0.0 y 1.1.0 89
ANEXO 7 – FORMATOS DE REPRESENTACIÓN IMPRESA DE DOCUMENTO ELECTRÓNICO CON
SUBSIDIO (RIDE) .................................................................................................................................. 94
ANEXO 8 - FORMATOS XML FACTURA CON RUBROS DE TERCEROS APLICADO EN LAS VERSIONES
2.0.0 y 2.1.0 ......................................................................................................................................... 95
2

ANEXO 9 - FORMATOS XML FACTURA SUSTITUTIVA DE GUÍA DE REMISIÓN APLICADO EN LAS
VERSIONES 2.0.0 y 2.1.0 .................................................................................................................... 100
ANEXO 10 - FORMATO XML DE COMPROBANTE DE RETENCIÓN ATS VERSIÓN 2.0.0 ...................... 106
ANEXO 11 – REQUISITOS OBLIGATORIOS PARA EL XML DE FACTURA COMERCIAL NEGOCIABLE .... 111
ANEXO 12 – REQUISITO OBLIGATORIO PARA EL XML DE FACTURA EN VENTA DE COMBUSTIBLES
LÍQUIDOS DERIVADOS DE HIDROCARBUROS Y BIOCOMBUSTIBLES. ................................................ 112
ANEXO 13 – REQUISITO OBLIGATORIO PARA XML DE COMPROBANTES EMITIDOS DESDE UNA
MÁQUINA FISCAL .............................................................................................................................. 113
ANEXO 14 – EJEMPLO FIRMA ELECTRÓNICA BAJO ESTÁNDAR XADES_BES ..................................... 113
ANEXO 15 – COMPATIBILIDAD DISPOSITIVOS PROVISTOS ............................................................... 115
ANEXO 16 – REQUISITO OBLIGATORIO DE LLENADO PARA EL XML DE FACTURA EN LA VENTA DE
COMBUSTIBLES LÍQUIDOS DERIVADOS DE HIDROCARBUROS Y BIOCOMBUSTIBLES. ...................... 116
ANEXO 17 – FORMATOS XML LIQUIDACIÓN DE COMPRA DE BIENES Y PRESTACIÓN DE SERVICIOS EN
LAS VERSIONES 1.0.0 Y 1.1.0 ............................................................................................................. 117
ANEXO 18 – REQUISITOS OBLIGATORIOS DE LLENADO EN LA FACTURA ELECTRÓNICA POR LA
ENTREGA DE FUNDAS PLÁSTICAS ...................................................................................................... 125
ANEXO 19 – APLICACIÓN DE LAS AUTORETENCIONES ...................................................................... 126
ANEXO 20 – REQUISITO PARA LA APLICACIÓN DE LA DEVOLUCIÓN AUTOMÁTICA DEL IVA EN EL XML
DE FACTURAS, NOTAS DE CRÉDITO Y NOTAS DE DÉBITO. ................................................................ 129
ANEXO 21 – REQUISITO OBLIGATORIO PARA COMPROBANTES ELECTRÓNICOS EMITIDOS POR
CONTRIBUYENTES DESIGNADOS COMO AGENTES DE RETENCIÓN. ................................................. 130
ANEXO 22 – REQUISITO OBLIGATORIO PARA COMPROBANTES ELECTRÓNICOS EMITIDOS POR
CONTRIBUYENTES RIMPE. ................................................................................................................. 131
ANEXO 23 – REQUISITO OBLIGATORIO EL LLENADO PARA EL XML DE COMPROBANTES DE VENTA EN
LA TRANSFERENCIA LOCAL DE MATERIALES DE CONSTRUCCIÓN. .................................................... 134
ANEXO 24 – REQUISITO OBLIGATORIO PARA COMPROBANTES ELECTRÓNICOS EMITIDOS POR
GRANDES CONTRIBUYENTES. ............................................................................................................ 135
ANEXO 25 – REQUISITO OBLIGATORIO DE LLENADO PARA EL XML DE FACTURAS EMITIDAS POR
OPERADORAS TRANSPORTE COMERCIAL (NO APLICA PARA TAXIS Y SOCIOS O ACCIONISTAS DE
TAXIS). ............................................................................................................................................... 136
15. Glosario de términos ................................................................................................................... 137
16. Preguntas técnicas frecuentes .................................................................................................... 140
3

Fecha de
Versión Descripción de los cambios
modificación
Nuevos WS para ambiente de pruebas.
2.0 05/08/2015
Se elimina las claves de uso complementario (contingencia).
2.01 10/11/2015 Nuevos WS para ambiente de producción.
2.02 29/01/2016 Nuevos campos para factura con subsidios.
Nuevos campos para factura con rubros de terceros y factura sustitutiva de guía de
2.03 21/03/2016
remisión.
Tabla 18: nuevos códigos de ICE.
2.04 01/05/2016
Tabla 24: nuevas formas de pago.
Tabla 17: nueva tarifa de IVA vigente a partir del 01 de junio de 2016.
2.05 01/06/2016 Se incluye en el numeral 11.8 (ANEXO 7) los requisitos obligatorios para el XML de
Factura Comercial Negociable.
Tabla 27: nuevo código descuento solidario 2% IVA.
Tabla 28: nuevos códigos para las devoluciones de IVA por uso de medios electrónicos
2.06 22/06/2016 exclusivamente para notas de crédito.
Se incluye ANEXO 8 nuevos campos para la inclusión del descuento solidario 2% de IVA,
devoluciones de IVA por uso de medios electrónicos y formas de pago.
Actualización tabla 24: formas de Pago.
2.07 28/06/2016
Actualización tabla 20: retenciones de IVA.
Actualización tabla 24: formas de pago.
2.08 15/09/2016 Actualización tabla 28: código para las devoluciones de IVA por descuento solidario 2%
IVA exclusivamente para notas de crédito.
Eliminación de la tabla 27: nuevo código descuento solidario 2% IVA
Eliminación de la tabla 28: nuevos códigos para las devoluciones de IVA por uso de medios
2.09 18/09/2017 electrónicos exclusivamente para notas de crédito.
Eliminación del anexo 8: nuevos campos para la inclusión del descuento solidario 2% de
IVA.
2.10 01/12/2017 Anexo 10: comprobante de retención ATS versión 2.0.0.
Inclusión de campo placa para los XML de factura en la venta de combustibles líquidos
2.11 07/08/2018 derivados de hidrocarburos (CLDH) y biocombustibles para las versiones 1.0.0, 1.1.0,
2.0.0, 2.1.0.
Inclusión de los campos marca, tipo y serie en todas sus versiones para los XML de
2.12 07/01/2019 Factura, Nota de Crédito, Nota de Débito, Guía de Remisión y Comprobantes de Retención
emitidos desde una máquina fiscal.
Tabla 29: formatos de llenado del campo placa establecido por la Agencia de Regulación y
Control de Energía y Recursos Naturales no Renovables.
2.13 15/05/2019 Tabla 30: códigos y descripción de llenado en la factura electrónica por la venta de
combustibles, según formatos establecido por la Agencia de Regulación y Control de
Energía y Recursos Naturales no Renovables.
Anexo 17 – Formatos XML liquidación de compra de bienes y prestación de servicios en
2.14 19/07/2019
las versiones 1.0.0 y 1.1.0.
Actualización tabla 29: formatos de llenado del campo placa establecido por la Agencia de
2.15 03/01/2020 Regulación y Control de Energía y Recursos Naturales no Renovables.
Actualización tabla 18: tarifa del ICE.
Actualización tabla 29: formatos de llenado del campo placa establecido por la Agencia de
Regulación y Control de Energía y Recursos Naturales no Renovables.
2.16 03/02/2020 Actualización tabla 30: códigos y descripción de llenado en la factura electrónica por la
venta de combustibles, según formatos establecido por la Agencia de Regulación y Control
de Energía y Recursos Naturales no Renovables.
Anexo 18 – Requisitos obligatorios de llenado en la factura electrónica por la entrega de
2.17 21/08/2020
fundas plásticas.
2.18 29/09/2020 Anexo 19 – Aplicación de las autoretenciones.
Servicios web para la devolución automática del IVA a personas adultas mayores - DIG
2.19 19/11/2020 Anexo 20 – Inclusión de campo para la devolución automática del IVA a personas adultas
mayores en facturas, notas de crédito y notas de débito.
Anexo 21 – Requisito obligatorio para comprobantes electrónicos emitidos por
2.20 11/12/2020
contribuyentes designados Microempresas y/o Agentes de Retención.
4

Fecha de
Versión Descripción de los cambios
modificación
Anexo 22 – Requisito obligatorio para comprobantes electrónicos emitidos por
contribuyentes RIMPE.
2.21 06/01/2022
Actualización de porcentajes de retención de ISD.
Actualización de porcentajes de retención de IVA.
Actualización de tarifas de IVA.
Actualización del Anexo 10 - Formato XML de comprobante de retención ATS versión
2.0.0.
2.22 01/09/2022
Actualización del Anexo 22 – Requisito obligatorio para comprobantes electrónicos
emitidos por contribuyentes RIMPE Emprendedor y RIMPE Negocio Popular.
Actualización del monto máximo para emitir una factura a consumidor final.
2.23 01/02/2023
Actualización de porcentajes de retención de ISD.
2.24 07/02/2023 Actualización tabla 18: tarifa del ICE.
Actualización de porcentajes de retención de ISD.
2.25 30/01/2024
Actualización Anexo 19 – Aplicación de las autoretenciones.
Actualización Tabla 17: Tarifas de IVA
2.26 05/03/2024
Actualización de porcentajes de retención del impuesto a la renta
Actualización de porcentajes de retención de ISD.
Anexo 2: Formato de representaciones impresas de documentos electrónicos (RIDE)
2.27 28/03/2024
Anexo 23 – Requisito obligatorio de llenado para los XML de comprobantes de venta y
documentos complementarios en la venta de materiales de construcción
Anexo 24 - Requisito obligatorio para comprobantes electrónicos emitidos por Grandes
2.28 25/06/2024
Contribuyentes.
Actualización de servicios web para la devolución automática del IVA a personas adultas
2.29 25/10/2024
mayores - DIG
2.30 06/03/2025 Actualización de porcentajes de retención de ISD.
8. Nuevos servicios expuestos en internet para consultas de comprobantes electrónicos:
2.31 27/03/2025 WS - Consulta de validez de comprobantes electrónicos
WS - Consulta de factura comercial negociable
Anexo 25 – Requisito obligatorio de llenado para el XML de facturas emitidas por
2.32 08/10/2025
operadoras de transporte comercial (no aplica para taxis y socios o accionistas de taxis).
5

FICHA TÉCNICA: MANUAL DE USUARIO,
CATÁLOGO Y ESPECIFICACIONES TÉCNICAS
SOBRE EL PROCESO DE AUTORIZACIÓN Y
EMISIÓN DE DOCUMENTOS ELECTRÓNICOS
(Aplica para la ciudadanía que emite facturas, comprobantes de retención,
guías de remisión, notas de crédito, notas de débito y liquidaciones de
compra de bienes y prestación de servicios firmadas electrónicamente)
1. Introducción
El presente documento tiene la finalidad de brindar la información, el servicio y la
asistencia a la ciudadanía, a los contribuyentes que opten por certificarse en el
Sistema de Comprobantes Electrónicos brindado por el Servicio de Rentas Internas
a través del portal web institucional www.sri.gob.ec.
Las directrices y actualizaciones de una implementación efectiva para los
contribuyentes se las realizará sobre este documento, el mismo que será
socializado a través de los medios de comunicación que dispone la Administración
Tributaria y principales medios de información a escala nacional.
2. Consideraciones generales
Las especificaciones operativas y técnicas se enmarcan en las siguientes
descripciones:
➢ Solicitud de certificación de emisión de comprobantes electrónicos para los
ambientes de pruebas y producción;
➢ Lineamientos en la parametrización de aplicativos del contribuyente (estándar en
firmas electrónicas);
➢ Servicios expuestos a través de WEB Service, conexiones con internet para la
autorización de comprobantes electrónicos;
➢ Uso del facturador electrónico gratuito para generar, firmar y solicitar autorización
de los comprobantes electrónicos;
➢ Esquemas XSD, formatos XML (generación individual y generación agrupados por
lotes de comprobantes electrónicos para solicitar la autorización).
Los emisores de comprobantes firmados electrónicamente operarán con
certificados digitales de firma electrónica adquiridos en cualquiera de las entidades
de certificación autorizadas en el país.
3. Base legal
• Ley de Régimen Tributario Interno.
6

• Ley de Comercio Electrónico, Firmas y Mensajes de Datos publicado en el
Suplemento del Registro Oficial No. 557 de 17 de abril de 2002.
• Ley Orgánica de Solidaridad y de Corresponsabilidad Ciudadana para la
Reconstrucción y Reactivación de las zonas Afectadas por el Terremoto de 16
de abril de 2016.
• Ley Orgánica de Simplificación y Progresividad Tributaria, Suplemento Registro
Oficial Nro. 111 de 31 de diciembre de 2019.
• Decreto No. 181 publicado en el Registro Oficial No. 553 de 11 de octubre del
2011, en el cual norma la numeración de identificadores de campo y campos
mínimos de los tipos de certificados.
• Reglamento para la Aplicación de la Ley de Régimen Tributario Interno.
• Reglamento de Comprobantes de Venta, Retención y Documentos
Complementarios.
• Reglamento a la Ley de Comercio Electrónico, Firmas y Mensajes de Datos,
publicado en el Registro Oficial No. 735 de 31 de diciembre de 2002.
• Reglamento para la Aplicación de la Ley Orgánica de Simplificación y
Progresividad Tributaria, Segundo Suplemento al Registro Oficial Nro. 260 de 04
de agosto de 2020.
• Resolución No. NAC-DGERCGC12-00105 de 09 de marzo de 2012, publicada
en Registro Oficial No. 666 de 21 de marzo de 2012.
• Resolución NAC-DGERCGC14-00788, publicada en el Registro Oficial 351 del 9
de octubre de 2014.
• Resolución NAC-DGERCGC15-00000284, publicada en el Registro Oficial 473
de 6 de abril de 2015.
• Resolución NAC-DGERCGC15-00003184, publicada en el Registro Oficial 661
de 4 de enero de 2016.
• Resolución NAC-DGERCGC16-00000247, publicada en el Registro Oficial 781
de 22 de junio de 2016.
• Resolución NAC-DGERCGC16-00000385, publicada en el Registro Oficial 838
de 12 de septiembre de 2016.
• Resolución NAC-DGERCGC17-00000309, publicada en el Segundo Suplemento
del Registro Oficial 8 de 6 de junio de 2017.
• Resolución NAC-DGERCGC17-00000460, publicada en el Registro Oficial 72 de
5 de septiembre de 2017.
• Resolución NAC-DGERCGC18-00000214, publicada en el Registro Oficial 255
de 5 de junio de 2018.
• Resolución NAC-DGERCGC18-00000233, publicada en el Registro Oficial 255
de 5 de junio de 2018.
• Resolución NAC-DGERCGC19-00000023 publicada en el Suplemento del
Registro Oficial No. 501 de 04 de junio de 2019.
• Resolución NAC-DGERCGC20-00000059 publicada en la Edición Especial del
Registro Oficial No. 1100 de 30 de septiembre de 2020.
Los contribuyentes que ingresen una solicitud de certificación y emisión de
documentos electrónicos deberán emitir los comprobantes de venta, retención y
documentos complementarios firmados electrónicamente bajo las condiciones
señaladas en esta ficha técnica.
7

4. Proceso de solicitud de certificación de
emisión de documentos electrónicos
4.1 El contribuyente, previo a la solicitud de certificación debe tener conocimiento
general del proceso de emisión de documentos electrónicos propuesto por la
Administración Tributaria (puede solicitar asistencia llamando al Centro de
Atención Telefónica 1700 774 774 o solicitar información y asistencia a los
funcionarios del SRI a escala nacional a través de nuestro canal de atención
presencial).
4.2 El contribuyente que se incorpore a la modalidad de emisión electrónica de
documentos deberá obtener un certificado digital de firma electrónica que
puede ser adquirido en cualquier entidad de certificación autorizada por el
organismo competente. En el enlace https://www.sri.gob.ec/nl/facturacion-
electronica encontrará las direcciones electrónicas de las entidades en donde
obtendrá detalles específicos de los certificados digitales de firma electrónica.
Hay que considerar que con la publicación del Decreto 181 de 11 de octubre de
2011, las entidades de certificación deberán actualizar los certificados digitales
de firma electrónica conforme a lo detallado en dicho decreto.
4.3 La solicitud de certificación para los ambientes de pruebas y producción deberá
realizarla directamente a través del portal web del SRI (Servicios en línea),
recuerde que debe encontrarse en estado activo, al día en sus obligaciones
tributarias y haber registrado un convenio de débito para pago de
declaraciones1 para obtener exitosamente la autorización, esta solicitud se
realizará una sola vez para cada ambiente.
La solicitud de certificación en el ambiente de pruebas es obligatoria para todos
los solicitantes, puesto que en este ambiente los emisores podrán realizar
todas sus acciones en desarrollo, ejecutando y verificando que los
comprobantes electrónicos cumplan con los esquemas XSD, así como con el
tipo de firma electrónica incorporada en los comprobantes; adicionalmente se
verificará la conexión con los enlaces a través de WEB Service que se
utilizarán para solicitar la autorización de los comprobantes electrónicos
generados y recibir la respuesta por parte de la Administración Tributaria
conforme al acuerdo de nivel de servicio; cabe mencionar que los
comprobantes emitidos en ambiente de pruebas no tendrán ninguna validez
tributaria, ni legal.
Cabe recalcar que el ambiente de pruebas fue diseñado únicamente para
verificar que el comprobante electrónico generado cumpla con las validaciones
indicadas en el presente documento, por tal motivo no se deben hacer pruebas
1 Mediante Resolución No. NAC-DGERCGC18-00000108 publicada en Primer Suplemento del Registro Oficial No. 202 de 16 de marzo de
2018, se dispuso que los contribuyentes que se encuentran obligados a emitir comprobantes de venta, retención y documentos
complementarios a través de mensajes de datos y firmados electrónicamente, así como los que soliciten autorización para la emisión de dichos
comprobantes bajo esta modalidad de facturación están obligados al pago de impuestos mediante débito automático.
8

de stress o de masividad en este ambiente. Adicionalmente se recomienda
que, en este ambiente los contribuyentes consideren los diferentes escenarios
que podrían darse de acuerdo con su giro de negocio.
Los solicitantes, una vez que hayan verificado en el ambiente de desarrollo que
el proceso de generación de comprobantes electrónicos, así como su envío y
autorización, están estructurados correctamente y que sus pruebas realizadas
sean de calidad, podrán ingresar la solicitud de emisión en el ambiente de
producción; todas las acciones que se realicen en este ambiente, así como los
comprobantes electrónicos autorizados tendrán validez tributaria. Es
responsabilidad del emisor garantizar que el sistema utilizado para la
generación del comprobante electrónico cumpla con las validaciones y
requisitos establecidos en el Reglamento de Comprobantes de Venta,
Retención y Documentos Complementarios y Resoluciones relacionadas, a fin
de garantizar que los comprobantes generados en este ambiente sean
autorizados.
4.4 En la misma solicitud de certificación realizada para el ambiente de pruebas o
producción, el contribuyente deberá escoger el tipo de comprobante que va a
emitir de manera electrónica.
4.5 Todas las transacciones realizadas por los contribuyentes son sustentadas en
los comprobantes firmados electrónicamente, los mismos que deberán ser
enviados al SRI a través del canal WEB Service para la recepción y validación,
el sistema de comprobantes electrónicos realizará las validaciones
correspondientes, generando una contestación conforme al acuerdo de nivel de
servicio.
4.6 Todos los comprobantes que no son autorizados tendrán su descripción del
motivo por el cual no fueron autorizados.
4.7 Una vez generados los comprobantes electrónicos, el emisor tiene la obligación
de enviar dichos comprobantes al receptor mediante correo electrónico;
adicionalmente podrá utilizar otros medios de notificación (publicación en portal
web, mensaje de texto, entre otros).
4.8 En el caso de comprobantes no autorizados, el emisor deberá corregir el error
detectado y enviar nuevamente al SRI para su respectiva validación. Una vez
que el comprobante se encuentre validado y en estado autorizado, deberá
entregar y notificar al receptor.
4.9 Los contribuyentes podrán solicitar adicionalmente la inclusión de nuevos
comprobantes, según su giro de negocio.
9

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

5. Proceso de generación, firma electrónica y
| solicitud  | de  autorización  |     | en  línea  | de  |
| ---------- | ----------------- | --- | ---------- | --- |
comprobantes electrónicos

5.1 Los contribuyentes generarán sus comprobantes electrónicos en formato .xml
conforme a los esquemas .xsd que están disponibles en el portal web del SRI,
a  través  de  sus  propios  aplicativos  informáticos  o  mediante  el  facturador
electrónico que el SRI dispone gratuitamente para los contribuyentes.

5.2 Cada comprobante generado contendrá una clave de acceso única que estará
compuesta por 49 dígitos numéricos, el aplicativo a utilizar por el contribuyente
deberá  generar  de  manera  automática  esta  clave,  la  cual  constituye  un
requisito obligatorio que le dará el CARACTER de único a cada comprobante y
a la vez se constituirá en el número de autorización del mismo; en base a esta
clave el SRI generará la respuesta de autorizado o no; a continuación, se
describe su conformación:

TABLA 1

 No.  Descripción de campo  Tipo de  Formato  Longitud  Requisito  Etiqueta o tag
campo  en archivo XML
| 1  Fecha de emisión        |           | ddmmaaaa        | 8               |                |
| -------------------------- | --------- | --------------- | --------------- | -------------- |
| 2  Tipo de comprobante     |           | Tabla 3         | 2               |                |
| 3  Número de RUC           |           |  1234567890001  | 13              |                |
| 4  Tipo de ambiente        |           | Tabla 4         | 1               |                |
| 5  Serie                   | Numérico  | 001001          | 6  Obligatorio  | <claveAcceso>  |
| 6  Número del comprobante  |           | 000000001       | 9               |                |
(secuencial)
| 7  Código numérico                 |     | Numérico  | 8   |     |
| ---------------------------------- | --- | --------- | --- | --- |
| 8  Tipo de emisión                 |     | Tabla 2   | 1   |     |
| 9  Dígito verificador (módulo 11)  |     | Numérico  | 1   |     |

Nota: todos los campos deben completarse conforme a la longitud indicada, es
decir si en el número secuencial no completa los 9 dígitos, la clave de acceso
estará mal conformada y será motivo de rechazo para su autorización.

El dígito verificador será aplicado sobre toda la clave de acceso (48 dígitos) y
deberá  ser  incorporado  por  el  contribuyente  a  través  del  método  denominado
“Módulo  11”,  con  un  factor  de  chequeo  ponderado  (2),  este  mecanismo  de
detección de errores será verificado al momento de la recepción del comprobante.
Cuando el resultado del dígito verificador obtenido sea igual a once (11), el digito
verificador será el cero (0) y cuando el resultado del dígito verificador obtenido sea
igual a diez 10, el dígito verificador será el uno (1).

10

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
El código numérico constituye un mecanismo para brindar seguridad al emisor en
cada comprobante emitido, el algoritmo numérico para conformar este código es
potestad absoluta del contribuyente emisor.

Ejemplo de verificación utilizando algoritmo de módulo 11:

                Cadena de verificación: 41261533

|               |     |   +---+---+---+---+---+---+---+---+   +---+          |     |     |     |     |     |
| ------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|               |     |    | 4  | 1  | 2 |  6 |  1 |  5 |  3 |  3 | - | ? |  |     |     |     |     |     |
| Pasos 1 y 2   |     | +---+---+---+---+---+---+---+---+   +---+            |     |     |     |     |     |
  |    |      |      |    |     |     |    |
  x3  x2   x7   x6  x5  x4  x3  x2
  |    |      |      |    |      |     |    |
=12 =2 =14 =36 =5 =20 =9 =6

| Paso 3     |     |    12 +2 +14 +36 +5 +20 +9 +6 = 104  |     |     |     |     |     |
| ---------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |

| Paso 4     |     |   104 mod 11 = 5 (ya que 104 = 11 x 9 + 5)  |     |     |     |     |     |
| ---------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |

| Paso 5     |     |   11 - 5 = 6  |     |     |     | Resultado = 6  |     |
| ---------- | --- | ------------- | --- | --- | --- | -------------- | --- |

5.3 El  código  que  conformará  el  tipo  de  emisión  según  la  clave  de  acceso
generada se detalla a continuación:

TABLA 2

|     |     | No.  | Tipo de emisión  |     |     | Código  | Requisito    |
| --- | --- | ---- | ---------------- | --- | --- | ------- | ------------ |
|     |     | 1    | Emisión normal2  |     |     | 1       | Obligatorio  |

5.4 Los tipos de comprobantes que pueden generar los contribuyentes de manera
electrónica se detalla conforme al siguiente cuadro:

TABLA 3

Etiqueta o tag en
|     |  No.  | Nombre comprobante  |     |     | Código  | Requisito  |     |
| --- | ----- | ------------------- | --- | --- | ------- | ---------- | --- |
archivo XML
|     | 1   | FACTURA  |     |     | 01  |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- |
LIQUIDACIÓN DE COMPRA DE
|     | 2   |     |     |     | 03  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
BIENES Y PRESTACIÓN DE
SERVICIOS
|     | 3   | NOTA DE CRÉDITO           |     |     | 04  | Obligatorio  | <codDoc>  |
| --- | --- | ------------------------- | --- | --- | --- | ------------ | --------- |
|     | 4   | NOTA DE DÉBITO            |     |     | 05  |              |           |
|     | 5   | GUÍA DE REMISIÓN          |     |     | 06  |              |           |
|     | 6   | COMPROBANTE DE RETENCIÓN  |     |     | 07  |              |           |

2  Para el método de autorización offline, solo existe el tipo de emisión normal.

11

5.5  El código que conformará el tipo de ambiente según la clave de acceso se
cita a continuación:

TABLA 4

|  No.  | Tipo de ambiente  |     | Código  |     | Requisito  |
| ----- | ----------------- | --- | ------- | --- | ---------- |
| 1     | Pruebas           |     | 1       |     |            |
Obligatorio
| 2   | Producción  |     | 2   |     |     |
| --- | ----------- | --- | --- | --- | --- |

5.6 Los  contribuyentes  que  generen  sus  comprobantes  de  venta,  retención  y
documentos  complementarios  firmados  electrónicamente  en  el  ambiente  de
pruebas,  pueden  utilizar  en  el  campo  de  la  razón  social  del  receptor,
destinatario  y  agente  retenido  la  denominación  PRUEBAS  SERVICIO  DE
RENTAS INTERNAS.

TABLA 5

Identificación
|  No.  |     | Número  |     | Razón Social  |     |
| ----- | --- | ------- | --- | ------------- | --- |
Receptor
| 1  RUC                  |     | xxxxxxxxxx001  |                      |     |     |
| ----------------------- | --- | -------------- | -------------------- | --- | --- |
| 2  Cédula de identidad  |     | xxxxxxxxxx     | PRUEBAS SERVICIO DE  |     |     |
RENTAS INTERNAS
| 3  Pasaporte  |     | xxxxxxxxxxxxx  |     |     |     |
| ------------- | --- | -------------- | --- | --- | --- |

5.7 Conforme al tipo de transacción efectuada deberá señalar el tipo de cliente,
sujeto retenido o destinatario, según el detalle:

TABLA 6

| No.                             | Tipo de identificación  |     | Código  |     | Requisito    |
| ------------------------------- | ----------------------- | --- | ------- | --- | ------------ |
| 1  RUC                          |                         |     |         | 04  | Obligatorio  |
| 2  CÉDULA                       |                         |     |         | 05  | Obligatorio  |
| 3  PASAPORTE                    |                         |     |         | 06  | Obligatorio  |
| 4  VENTA A CONSUMIDOR FINAL*    |                         |     |         | 07  | Obligatorio  |
| 5  IDENTIFICACIÓN DELEXTERIOR*  |                         |     |         | 08  | Obligatorio  |

*Venta a consumidor final: se consignará 13 dígitos de nueve en la identificación del cliente
(9999999999999).
*Identificación  del  exterior:  corresponderá  al  número  de  Identificación  otorgado  por  la
Administración Tributaria (AT) del país que es residente fiscal.
* En el caso de emisión de liquidaciones de compra de bienes y prestación de servicios no se
encuentra habilitado el uso del tipo de identificación venta a consumidor final
* En el caso de emisión de notas de crédito, notas de débito y comprobantes de retención, se
debe obligatoriamente identificar al receptor o sujeto retenido con el tipo de identificación
correspondiente (RUC, cédula, pasaporte o identificación del exterior).

5.8  Si  los  comprobantes  electrónicos  cumplen  con  los  esquemas  y  firmas
electrónicas, el Servicio de Rentas Internas autorizará los comprobantes de
manera  automática,  en  caso  de  no  autorizarlos  se  indicará  el  motivo  del
rechazo.

12

5.9 En el método de autorización offline la clave de acceso generada por el
emisor se constituye en el número de autorización del mismo.
Como parte de la respuesta que el SRI genera por cada comprobante emitido
correctamente, se insertará un listado de advertencias; como por ejemplo para el
caso en que los comprobantes hayan sido emitidos en el ambiente de pruebas y
por alguna indicación que se quiera comunicar.
Aparecerá texto informativo, por ejemplo, si es
Listado de advertencias una autorización para un ambiente de pruebas
o algún comunicado por parte del SRI.
5.10 En caso de que un comprobante haya sido rechazado debido a problemas de
inconsistencia en su información (ver tabla de códigos de errores y
advertencias de validación), el emisor deberá utilizar la misma clave de
acceso y secuencial para que una vez corregida la inconsistencia, pueda ser
enviado nuevamente al SRI para su autorización.
5.11 En el caso de que un comprobante se encuentre autorizado, el WEB Service
de autorización devuelve el XML autorizado, pero si el comprobante fue no
autorizado varias veces, el WEB Service retornará únicamente el último
estado.
5.12 Constituye obligación del contribuyente el envío del comprobante electrónico
al SRI de manera individual o en lote; y la verificación de que el comprobante
conste en estado autorizado. A continuación, se describen los estados del
comprobante electrónico:
TABLA 6
Estado del comprobante
No. SIGLAS
electrónico
1 En procesamiento PPR
2 Autorizado AUT
3 No autorizado NAT
Cuando el comprobante electrónico se encuentre en estado No Autorizado (NAT),
el emisor estará en la obligación de corregir y enviar nuevamente el comprobante
electrónico a través del WEB Service y posteriormente notificar y entregar al
receptor: destinatario o sujeto retenido el nuevo comprobante electrónico, mediante
correo electrónico. Cabe aclarar que el tiempo máximo que le tomará al SRI en
procesar un comprobante electrónico será de 24 horas.
Es obligación de los ciudadanos que reciben comprobantes electrónicos validar sus
comprobantes mediante el portal web del Servicio de Rentas Internas.
13

6. Proceso de firmas electrónicas y
lineamientos de parametrización en los
aplicativos
6.1 Para la generación y emisión de los documentos electrónicos deberán
obligatoriamente firmar cada archivo xml bajo el estándar de firma digital de
documentos XML: XadES_BES, esto quiere decir que cada archivo .xml
tendrá dentro de su estructura la firma electrónica y constituirá un documento
electrónico válido una vez que el SRI proceda con la autorización.
6.2 A continuación, se detallan las especificaciones técnicas relacionadas al
estándar:
Descripción Especificación Documentación técnica relacionada
Estándar de firma XadES_BES http://uri.etsi.org/01903/v1.3.2/ts_101903v010302p.pdf
Versión del esquema 1.3.2 http://uri.etsi.org/01903/v1.3.2#
Codificación UTF-8
Tipo de firma ENVELOPED http://www.w3.org/2000/09/xmldsig#enveloped-signature
6.3 La estructura del formato básico de firma electrónica avanzada acorde con la
presente política se adecua a las especificaciones definidas en XADES_BES
que incluyen los campos que se describen en el esquema 1.3.2 del cuadro
anterior.
6.4 La firma electrónica se considera un nodo más a añadir en el documento .xml.
El nivel de seguridad en la firma electrónica está ejecutado sobre tres partes
de la trama de datos:
• Todos los elementos o nodos que conforman el comprobante electrónico.
• Los elementos de firma ubicados en el contenedor “SignedProperties”.
• El certificado digital con el que se ha firmado incluido en el elemento
“KeyInfo”.
6.5 Es necesario utilizar el elemento ds: KeyInfo, conteniendo al menos el
certificado firmante codificado en base64. Además, dicha información precisa
ser firmada con objeto de evitar la posibilidad de sustitución del certificado.
6.6 En el anexo 4 se muestra un ejemplo de una factura firmada bajo el estándar
XadES_BES.
Cada comprobante deberá incorporar la firma electrónica en formato XADES-
Bes, misma que se puede realizar con librerías destinadas para el efecto. El
SRI utilizó el siguiente set de librerías para incorporar y validar la firma de
cada comprobante:
MITyCLibXADES
MITyCLibTSA
14

MITyCLibAPI
MITyCLibOCSP
MITyCLibTrust
Para más información del estándar se puede explorar el siguiente enlace:
http://webapp.etsi.org/workprogram/Report_WorkItem.asp?WKI_ID=21353
6.7 Sobre aspectos técnicos del estándar de encriptación, se puede revisar la
siguiente dirección: http://www.ietf.org/rfc/rfc2313.txt (RSA Encryption).
6.8 A continuación, se detallan las especificaciones técnicas relacionadas al
algoritmo de encriptación:
• Algoritmo de firmado: RSA-SHA1
• Longitud de clave: 2048 bits. Recomendación técnica basada en documento:
http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf
• Archivo de Intercambio de Información: PKCS12 (extensión. p12). Este
archivo deberá ser proporcionado ya sea de manera directa (a través de API´s
de acceso al token USB), o de manera indirecta a través de la extracción del
mismo y posterior instalación en una carpeta específica de la cual el software
proporcionado por el SRI lo utilizará para firmar los comprobantes.
7. Servicios expuestos en internet para la
autorización de comprobantes electrónicos
Los servicios expuestos en el internet por la Administración Tributaria están
estandarizados a través de canales seguros con protocolos de seguridad y
certificados SSL.
7.1 Procesos que ejecutan los servicios expuestos en internet:
7.1.1 Los procesos tienen la función de aceptar o rechazar comprobantes de
manera individual o por lotes.
7.1.2 Para el intercambio de información entre el contribuyente y la Administración
Tributaria, es requisito indispensable que el contribuyente cuente con acceso
a la red de internet banda ancha (por definición y recomendación del
MINTEL la conexión debe ser mayor a 256Kbps).
7.1.3 Para poder acceder al servicio de autorización de comprobantes
electrónicos, el contribuyente deberá crear el software cliente para poder
invocar a los WEB Service que el SRI pone a disposición.
7.1.4 Para garantizar que la conexión es segura se empleará Certificados Digitales
SSL, es decir, el SRI emitirá un certificado válido cuando se realice la
petición de los WEB Service.
15

Sin embargo, considerando que los certificados pueden ser cambiados
durante el periodo de su vigencia por causas técnicas o institucionales, se
recomienda a los contribuyentes que, en la programación de sus sistemas,
se considere los mecanismos necesarios para que no se queme en su
código la información, ni los certificados digitales de comprobantes
electrónicos del SRI, puesto que estos podrían cambiar sin previo aviso por
la urgencia según sea el caso.
7.2 Existen dos ambientes disponibles para la invocación de los WS publicados
por la Administración Tributaria:
7.2.1 Uno es para el ambiente de pruebas, donde cada contribuyente certificará
que su aplicación funcione correctamente con cada tipo de comprobante
electrónico, las direcciones de los WS son las siguientes:
https://celcer.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl
https://celcer.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl
7.2.2 El segundo es para el ambiente de producción, al cual cada contribuyente
deberá acceder una vez que ha realizado las pruebas y esté seguro de que
su aplicación funciona correctamente, las direcciones de los WS son las
siguientes:
https://cel.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl
https://cel.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl
7.2.3 Los WS expuestos por la Administración Tributaria son los siguientes:
Recepción de comprobantes electrónicos
@WebMethod
@WebResult(name="RespuestaRecepcionComprobante")
public RespuestaSolicitud validarComprobante(@WebParam(name = "xml")
byte[] xml);
Parámetros:
I/O Nombre Tipo Descripción
IN Xml byte[] Equivale al archivo xml del comprobante, el cual debe estar firmado por el contribuyente.
Retorna un objeto XML el cual indica la aceptación o rechazo del comprobante.
En caso de rechazo se envía el arreglo con los motivos.
La estructura que cumplirá la respuesta a la invocación del servicio es la siguiente:
Recepción exitosa
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
RespuestaC <soap:Body>
OUT omprobante Objeto <ns2:validarComprobanteResponse xmlns:ns2="http://ec.gob.sri.ws.recepcion">
Autorizacion <RespuestaRecepcionComprobante>
<estado>RECIBIDA</estado>
<comprobantes/>
</RespuestaRecepcionComprobante>
</ns2:validarComprobanteResponse>
</soap:Body>
</soap:Envelope>
16

Recepción fallida
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:validarComprobanteResponse xmlns:ns2="http://ec.gob.sri.ws.recepcion">
<RespuestaRecepcionComprobante>
<estado>DEVUELTA</estado>
<comprobantes>
<comprobante>
<claveAcceso>1702201205176001321000110010030001000011234567816</claveAcceso>
<mensajes>
<mensaje>
<identificador>35</identificador>
<mensaje>DOCUMENTO INVÁLIDO</mensaje>
<informacionAdicional>Se encontró el siguiente error en la estructura del comprobante: cvc-
complex-type.2.4.a: Invalid content was found starting with element 'totalSinImpuestos'. One
of '{fechaEmisionDocSustento}' is expected.</informacionAdicional>
<tipo>ERROR</tipo>
</mensaje>
</mensajes>
</comprobante>
</comprobantes>
</RespuestaRecepcionComprobante>
</ns2:validarComprobanteResponse>
</soap:Body>
</soap:Envelope>
Consulta de respuesta de autorización:
@WebMethod
@WebResult(name = "RespuestaAutorizacionComprobante")
public RespuestaComprobante autorizacionComprobante(
@WebParam(name = "claveAccesoComprobante") String
claveAccesoComprobante) ;
Consulta de respuesta de lote
@WebMethod
@WebResult(name = "RespuestaAutorizacionLote")
public RespuestaLote autorizacionComprobanteLote(@WebParam(name =
"claveAccesoLote") String claveAccesoLote) ;
Parámetros:
I/O Nombre Tipo Descripción
IN ClaveAcces String Equivale a la clave de acceso del comprobante a ser consultado.
o
OUT RespuestaL Objeto Retorna un objeto XML el cual indica la aceptación o rechazo de cada uno de los
oteCompAu comprobantes ingresado en el lote.
torizacion En caso de rechazo se envía el arreglo con los motivos por cada comprobante del lote.
Comprobante Autorizado
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:autorizacionComprobanteResponse
xmlns:ns2="http://ec.gob.sri.ws.autorizacion">
<RespuestaAutorizacionComprobante>
<claveAccesoConsultada>
0503201201176001321000110010030009900641234567814
</claveAccesoConsultada>
<numeroComprobantes>1</numeroComprobantes>
<autorizaciones>
<autorizacion>
<estado>AUTORIZADO</estado>
<numeroAutorizacion>
17

I/O Nombre Tipo Descripción
0503201201176001321000110010030009900641234567814
</numeroAutorizacion>
<fechaAutorizacion>2012-03-05T16:57:34.997-05:00</fechaAutorizacion>
<ambiente>PRUEBAS</ambiente>
<comprobante><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<factura id="comprobante" version="1.0.0">
<!-- FACTURA FIRMADA DIGITALMENTE, VER ANEXO 3 -->
</factura>]]>
</comprobante>
<mensajes>
<mensaje>
<identificador>60</identificador>
<mensaje>ESTE PROCESO FUE REALIZADO EN EL AMBIENTE DE
PRUEBAS
</mensaje>
<tipo>ADVERTENCIA</tipo>
</mensaje>
</mensajes>
</autorizacion>
</autorizaciones>
</RespuestaAutorizacionComprobante>
</ns2:autorizacionComprobanteResponse>
</soap:Body>
</soap:Envelope>
Comprobante No Autorizado
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:autorizacionComprobanteResponse
xmlns:ns2="http://ec.gob.sri.ws.autorizacion">
<RespuestaAutorizacionComprobante>
<claveAccesoConsultada>
1302201201176001321000120010030000050431234567814
</claveAccesoConsultada>
<numeroComprobantes>1</numeroComprobantes>
<autorizaciones>
<autorizacion>
<estado>RECHAZADO</estado>
<fechaAutorizacion>2012-02-13T16:34:48.997-05:00</fechaAutorizacion>
<ambiente>PRUEBAS</ambiente>
<comprobante><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<factura id="comprobante" version="1.0.0">
<!-- FACTURA FIRMADA DIGITALMENTE, VER ANEXO 4 -->
</factura>]]>
</comprobante>
<mensajes>
<mensaje>
<identificador>46</identificador>
<mensaje> RUC no existe </mensaje>
<tipo>ERROR</tipo>
</mensaje>
</mensajes>
</autorizacion>
</autorizaciones>
</RespuestaAutorizacionComprobante>
</ns2:autorizacionComprobanteResponse>
</soap:Body>
</soap:Envelope>
7.3 El Sistema de Autorización de Documentos Electrónicos soporta un proceso a
través de un ambiente computacional seguro, que brinda alta disponibilidad y
rendimiento, opta por utilizar la infraestructura necesaria para brindar el servicio
a la ciudadanía que realizan transferencias de bienes o prestación de servicios.
7.4 La manera correcta de consumir las direcciones URL de los WS, es de manera
asíncrona; es decir una vez que el contribuyente envíe el comprobante al WS
18

de  recepción  y  obtenga  la  respuesta  “RECIBIDA”,  se  debe  esperar  un
determinado tiempo (se recomienda que este tiempo sea parametrizable) antes
de proceder a consumir la segunda dirección URL de autorización mediante la
clave de acceso del comprobante, para obtener el resultado: procesamiento
(PPR), autorizado (AUT), no autorizado (NAT).

7.5 Procesos que ejecuta el Sistema de Autorización de Documentos Electrónicos:

•  Exposición de componentes tecnológicos para el servicio de autorización de
comprobantes electrónicos.

•  Receptar  los  documentos  firmados  electrónicamente  (primera  validación
general).

•  Validación de los documentos firmados electrónicamente (segunda validación
a detalle con certificados de firma electrónica).

•  Autorizar  de  manera  automática  cada  comprobante  electrónico.  El  tiempo
estimado  de  entrega  de  la  autorización  o  motivos  de  errores  de  un
comprobante, será de un tiempo máximo de 24 horas a partir de la respuesta
de RECIBIDA, generada por el WS de recepción.

•  El límite máximo en tamaño y número de comprobantes electrónicos a ser
validados  y  autorizados  por  lote  es  de  500  kb  o  50  comprobantes
aproximadamente  (considerando  cada  comprobante  con  un  solo  ítem);
mientras que, para el envío individual, el tamaño máximo por comprobante
será de 320 Kb.

TABLA 8: FORMATO XML PARA ENVÍO POR LOTE

LONGITUD /
|     | ETIQUETAS O TAGS  | CARACTER  | TIPO DE CAMPO  |     |
| --- | ----------------- | --------- | -------------- | --- |
FORMATO
| <?xml version="1.0" encoding="UTF-8"?>  |     | Obligatorio  | -   | -   |
| --------------------------------------- | --- | ------------ | --- | --- |
| -  <lote version="1.0.0">               |     | Obligatorio  | -   | -   |

<claveAcceso>2808201400179210439400110010010000000091234567812< Obligatorio  Numérico  49
/claveAcceso>
| -<ruc>1792104394001</ruc>           |     | Obligatorio  | Numérico  | 13  |
| ----------------------------------- | --- | ------------ | --------- | --- |
| -<comprobantes>                     |     | Obligatorio  | -         | -   |
|  -<comprobante>                     |     | Obligatorio  | -         | -   |
|            <![CDATA[COMPROBANTE]]>  |     | Obligatorio  | -         | -   |
|  -</comprobante>                    |     | Obligatorio  | -         | -   |
|  -<comprobante>                     |     | Obligatorio  | -         | -   |
|            <![CDATA[COMPROBANTE]]>  |     | Obligatorio  | -         | -   |
|  -</comprobante>                    |     | Obligatorio  | -         | -   |
| -</comprobantes>                    |     | Obligatorio  | -         | -   |
| </lote>                             |     | Obligatorio  | -         | -   |

TABLA 9:

Las claves de acceso para el envío de lote de máximo 50 comprobantes (512 kb)
estarán  compuestas de  49  caracteres  numéricos,  la herramienta  o  aplicativo a
utilizar  por  el  contribuyente  deberá  generar  de  manera  automática  la  clave  de
acceso, que constituirá un requisito que dará el CARACTER de único a cada lote, y
la misma servirá para que el SRI indique si fue recibido; se describe a continuación
su conformación:

19

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|                                    |                  | Tipo de   |                |           |              | Etiqueta o tag  |
| ---------------------------------- | ---------------- | --------- | -------------- | --------- | ------------ | --------------- |
| No.  Descripción de campo          |                  |           | Formato        | Longitud  | Requisito    |                 |
|                                    |                  | campo     |                |           |              | en archivo XML  |
| 1  Fecha de emisión                |                  |           | ddmmaaaa       | 8         |              |                 |
| 2  Tipo de comprobante             |                  |           | Tabla 3        | 2         |              |                 |
| 3  Número de RUC                   |                  |           | 1234567890001  | 13        |              |                 |
| 4  Tipo de ambiente                |                  |           | Tabla 4        | 1         |              |                 |
| 5                                  | Serie*           | Numérico  | 001001         | 6         | Obligatorio  | <claveAcceso>   |
| 6  Número secuencial*              |                  |           | 000000001      | 9         |              |                 |
| 7  Código numérico                 |                  |           | Numérico       | 8         |              |                 |
| 8                                  | Tipo de emisión  |           | Tabla 2        | 1         |              |                 |
| 9  Dígito verificador (módulo 11)  |                  |           | Numérico       | 1         |              |                 |
*El emisor deberá asignar la serie y secuencial que corresponderá únicamente al envío en lote.

| 8.  Servicios  |     | expuestos  |     | en  | internet  | para  |
| -------------- | --- | ---------- | --- | --- | --------- | ----- |
consultas de comprobantes electrónicos

Los  servicios  expuestos  en  el  internet  por  la  Administración  Tributaria  están
estandarizados  a  través  de  canales  seguros  con  protocolos  de  seguridad  y
certificados SSL.

8.1 Procesos que ejecutan los servicios expuestos en internet:

8.1.1 Los  procesos  tienen  la  función  de  consulta  comprobantes  de  manera
individual.

8.1.2 Para el intercambio de información entre el contribuyente y la Administración
Tributaria, es requisito indispensable que el contribuyente cuente con acceso
a la red de internet banda ancha (por definición y recomendación del MINTEL
la conexión debe ser mayor a 256Kbps).

8.1.3 Para poder acceder al servicio de consulta de comprobantes electrónicos, el
contribuyente deberá crear el software cliente para poder invocar a los WEB
Service que el SRI pone a disposición.

8.1.4 Para garantizar que la conexión es segura se empleará Certificados Digitales
SSL,  es  decir,  el  SRI  emitirá  un  certificado  válido  cuando  se  realice  la
petición de los WEB Service.

Sin  embargo,  considerando  que  los  certificados  pueden  ser  cambiados
durante el periodo de su vigencia por causas técnicas o institucionales, se
recomienda a los contribuyentes que, en la programación de sus sistemas,
se  considere  los  mecanismos  necesarios  para  que  no  se  queme  en  su
código  la  información,  ni  los  certificados  digitales  de  comprobantes
electrónicos del SRI, puesto que estos podrían cambiar sin previo aviso por
la urgencia según sea el caso.

20

8.2 Existen dos ambientes disponibles para la invocación de los WS publicados por
la Administración Tributaria:
8.2.1 Uno es para el ambiente de pruebas, donde cada contribuyente certificará
que su aplicación funcione correctamente con cada tipo de comprobante
electrónico, las direcciones de los WS son las siguientes:
https://celcer.sri.gob.ec/comprobantes-electronicos-ws/ConsultaComprobante?wsdl
https://celcer.sri.gob.ec/comprobantes-electronicos-ws/ConsultaFactura?wsdl
8.2.2 El segundo es para el ambiente de producción, al cual cada contribuyente
deberá acceder una vez que ha realizado las pruebas y esté seguro de que
su aplicación funciona correctamente, las direcciones de los WS son las
siguientes:
https://cel.sri.gob.ec/comprobantes-electronicos-ws/ConsultaComprobante?wsdl
https://cel.sri.gob.ec/comprobantes-electronicos-ws/ConsultaFactura?wsdl
8.2.3 Los WS expuestos por la Administración Tributaria son los siguientes:
Consulta de validez de comprobantes electrónicos
@WebMethod
@WebResult(name = " EstadoAutorizacionComprobante")
public RespuestaConsultaComprobante consultarEstadoAutorizacionComprobante
(@WebParam(name = "claveAcceso") String claveAcceso)
Parámetros:
I/O Nombre Tipo Descripción
IN claveAcceso String Clave de acceso del comprobante electrónico
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ec="http://ec.gob.sri.ws.consultas">
<soapenv:Header/>
<soapenv:Body>
<ec:consultarEstadoAutorizacionComprobante>
<claveAcceso>0211202401050306179800120010020000000677300995216</claveAcceso>
</ec:consultarEstadoAutorizacionComprobante>
</soapenv:Body>
OUT EstadoAutori Objeto </soapenv:Envelope>
zacionCompr
obante
Retorna un objeto XML con la información del estado del comprobante electrónico.
Dependiendo del estado de autorización del comprobante electrónicos, el servicio web,
devolverá en la etiqueta estadoAutorizacion el valor:
“AUTORIZADO”
“NO AUTORIZADO”
“PENDIENTE DE ANULAR” y
“ANULADO”
21

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:consultarEstadoAutorizacionComprobanteResponse
xmlns:ns2="http://ec.gob.sri.ws.consultas">
<EstadoAutorizacionComprobante>
<claveAcceso>2111202405176001321000110010010000001241234567810</claveAcceso>
<mensajes/>
<estadoAutorizacion>AUTORIZADO</estadoAutorizacion>
<tipoComprobante>Nota de Débito</tipoComprobante>
<rucEmisor>1760013210001</rucEmisor>
<fechaAutorizacion>2024-12-12T10:49:37-05:00</fechaAutorizacion>
</EstadoAutorizacionComprobante>
</ns2:consultarEstadoAutorizacionComprobanteResponse>
</soap:Body>
</soap:Envelope>
Si el comprobante consultado se encuentra fuera del rango de fechas permitido por el
SRI, devolverá en la etiqueta estadoAutorizacion el valor “RECHAZADA”, con el
identificador 99 correspondiente a “ERROR AL CONSULTAR DATOS DEL SERVICIO WEB” y
con el mensaje de informacionAdicional “No es posible validar la clave de acceso ya que
la fecha de emision esta fuera del rango permitido.”
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:consultarEstadoAutorizacionComprobanteResponse
xmlns:ns2="http://ec.gob.sri.ws.consultas">
<EstadoAutorizacionComprobante>
<estadoConsulta>RECHAZADA</estadoConsulta>
<claveAcceso>1510202407099313057500110010010000103591234567816</claveAcceso>
<mensajes>
<mensaje>
<identificador>99</identificador>
<mensaje>ERROR AL CONSULTAR DATOS DEL SERVICIO WEB</mensaje>
<informacionAdicional>No es posible validar la clave de acceso ya que la fecha de
emision esta fuera del rango permitido.</informacionAdicional>
<tipo>ERROR</tipo>
</mensaje>
</mensajes>
</EstadoAutorizacionComprobante>
</ns2:consultarEstadoAutorizacionComprobanteResponse>
</soap:Body>
</soap:Envelope>
Si el comprobante no se encuentra en las bases de datos del SRI, devolverá en la etiqueta
estadoAutorizacion el valor “RECHAZADA”, con el identificador 99 correspondiente a
“ERROR AL CONSULTAR DATOS DEL SERVICIO WEB”
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:consultarEstadoAutorizacionComprobanteResponse
xmlns:ns2="http://ec.gob.sri.ws.consultas">
<EstadoAutorizacionComprobante>
<estadoConsulta>RECHAZADA</estadoConsulta>
<claveAcceso>2111202401176001321000110010010000011171234567810</claveAcceso>
<mensajes>
<mensaje>
<identificador>99</identificador>
<mensaje>ERROR AL CONSULTAR DATOS DEL SERVICIO WEB</mensaje>
22

<informacionAdicional>No existen datos para los parámetros
ingresados</informacionAdicional>
<tipo>ERROR</tipo>
</mensaje>
</mensajes>
</EstadoAutorizacionComprobante>
</ns2:consultarEstadoAutorizacionComprobanteResponse>
</soap:Body>
</soap:Envelope>
Consulta de factura comercial negociable:
@WebMethod
@WebResult(name = "EstadoConfirmacionFacturaComercialNegociable")
public RespuestaConsultaFacturaComercialNegociable
consultarEstadoConfirmacionFacturaComercialNegociable
(@WebParam(name = "claveAcceso") String claveAcceso)
Parámetros:
I/O Nombre Tipo Descripción
IN ClaveAcceso String Clave de acceso del comprobante electrónico
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ec="http://ec.gob.sri.ws.consultas">
<soapenv:Header/>
<soapenv:Body>
<ec:consultarEstadoConfirmacionFacturaComercialNegociable>
<claveAcceso>1211202401092554321700110021000000000790925543211</claveAcceso>
</ec:consultarEstadoConfirmacionFacturaComercialNegociable>
</soapenv:Body>
</soapenv:Envelope>
OUT EstadoConfir Objeto Retorna un objeto XML con la información de la factura electrónica indicando si ha sido
macionFactu aceptada como factura comercial negociable
raComercial Dependiendo si la factura electrónica tiene estado de confirmación, aceptado como
Negociable factura comercial negociable, el servicio web devolverá en la etiqueta
estadoConfirmacion el valor: “SI”
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:consultarEstadoConfirmacionFacturaComercialNegociableResponse
xmlns:ns2="http://ec.gob.sri.ws.consultas">
<EstadoConfirmacionFacturaComercialNegociable>
<claveAcceso>1111202401099338176200110020010000003961234567815</claveAcceso>
<mensajes/>
<estadoConfirmacion>SI</estadoConfirmacion>
</EstadoConfirmacionFacturaComercialNegociable>
</ns2:consultarEstadoConfirmacionFacturaComercialNegociableResponse>
</soap:Body>
</soap:Envelope>
23

I/O Nombre Tipo Descripción
Si la factura consultada se encuentra fuera del rango de fechas permitido por el SRI,
devolverá en la etiqueta estadoConsulta el valor “RECHAZADA”, con el identificador 99
correspondiente a “ERROR AL CONSULTAR DATOS DEL SERVICIO WEB” y con el mensaje
de informacionAdicional “No es posible validar la clave de acceso ya que la fecha de
emision esta fuera del rango permitido.”
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:consultarEstadoConfirmacionFacturaComercialNegociableResponse
xmlns:ns2="http://ec.gob.sri.ws.consultas">
<EstadoConfirmacionFacturaComercialNegociable>
<estadoConsulta>RECHAZADA</estadoConsulta>
<claveAcceso>1111202401099338176200110020010000003961234567815</claveAcceso>
<mensajes>
<mensaje>
<identificador>99</identificador>
<mensaje>ERROR AL CONSULTAR DATOS DEL SERVICIO WEB</mensaje>
<informacionAdicional>No es posible validar la clave de acceso ya que la fecha de
emision esta fuera del rango permitido.</informacionAdicional>
<tipo>ERROR</tipo>
</mensaje>
</mensajes>
</EstadoConfirmacionFacturaComercialNegociable>
</ns2:consultarEstadoConfirmacionFacturaComercialNegociableResponse>
</soap:Body>
</soap:Envelope>
Si la factura consultada no se encuentra en las bases de datos del SRI o no fue aceptada
como factura comercial negociable, devolverá en la etiqueta estadoConsulta el valor
“RECHAZADA”, con el identificador 99 correspondiente a “ERROR AL CONSULTAR DATOS
DEL SERVICIO WEB”
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<ns2:consultarEstadoConfirmacionFacturaComercialNegociableResponse
xmlns:ns2="http://ec.gob.sri.ws.consultas">
<EstadoConfirmacionFacturaComercialNegociable>
<estadoConsulta>RECHAZADA</estadoConsulta>
<claveAcceso>1211202401092554321700110021000000000790925543211</claveAcceso>
<mensajes>
<mensaje>
<identificador>99</identificador>
<mensaje>ERROR AL CONSULTAR DATOS DEL SERVICIO WEB</mensaje>
<informacionAdicional>No existen datos para los parametros
ingresados</informacionAdicional>
<tipo>ERROR</tipo>
</mensaje>
</mensajes>
</EstadoConfirmacionFacturaComercialNegociable>
</ns2:consultarEstadoConfirmacionFacturaComercialNegociableResponse>
</soap:Body>
</soap:Envelope>
8.3 El Sistema de Autorización de Documentos Electrónicos soporta un proceso a
través de un ambiente computacional seguro, que brinda alta disponibilidad y
24

rendimiento, opta por utilizar la infraestructura necesaria para brindar el servicio
a la ciudadanía que realizan transferencias de bienes o prestación de servicios.
8.4 Una vez que el contribuyente realice la consulta con la clave de acceso del
comprobante electrónico en el WS de consulta de validez obtendrá en
respuesta los estados del comprobante “AUTORIZADO”, “NO AUTORIZADO”,
“PENDIENTE DE ANULAR” o “ANULADO”.
8.5 En el caso de la consulta de si es una factura comercial negociable, cuando el
contribuyente realice la consulta con la clave de acceso del comprobante
electrónico en el WS obtendrá en respuesta “SI”, caso contrario obtendrá el
valor “RECHAZADA”.
8.6 Es fundamental señalar que solo la factura comercial negociable generará la
respuesta “SI” una vez que haya sido notificada y aceptada a través del portal
web, en la opción de Comprobantes Electrónicos / Ambientes de Pruebas o
Producción / Factura Comercial Negociable
9. Facturador gratuito de generación de
comprobantes electrónicos
9.1 El Servicio de Rentas Internas pone a disposición de la ciudadanía de manera
gratuita, un facturador electrónico, el cual permitirá generar comprobantes,
firmarlos electrónicamente y visualizarlos de manera amigable.
9.2 El facturador electrónico tiene la particularidad de asignar y modificar directorios
para los archivos de los comprobantes electrónicos, validar el esquema y firma
electrónica de comprobantes, también se puede visualizar los documentos
electrónicos.
9.3 Para instalar el facturador, los contribuyentes deberán descargar el instalador
desde el portal web del Servicio de Rentas Internas, ingresando a Inicio / Guía
Básica Tributaria / Facturación / Facturación Electrónica / Facturador electrónico
gratuito.
Para una correcta instalación, se recomienda descargar el Manual de Usuario
que le servirá como guía y pasos a seguir.
9.4 Una vez instalado el facturador electrónico, se deberá parametrizar los
directorios disponibles:
TABLA 10
No. Ruta o Directorios Observación
1 Comprobantes generados Directorio donde se encuentren los documentos para ser firmados.
Comprobantes firmados Directorio donde se guardarán los documentos firmados
2
electrónicamente electrónicamente de manera satisfactoria.
25

|                          |             |        |              |                    |           |
| ------------------------ | ----------- | ------ | ------------ | ------------------ | --------- |
| No.  Ruta o Directorios  |             |        | Observación  |                    |           |
|                          | Directorio  | donde  | almacenarán  | los  comprobantes  | firmados  |
Comprobantes transmitidos y
2.1  electrónicamente remitidos a la Administración Tributaria y no se ha
sin respuesta de autorización*
recibido una respuesta.
Directorio donde se almacenarán los comprobantes autorizados por el
3  Comprobantes autorizados  SRI y automáticamente deberán eliminarse de los directorios 1 y/o 2
únicamente si son autorizados.
Directorio donde se almacenarán los archivos con los motivos de por
4  Comprobantes no autorizados
qué no se autorizó los comprobantes.
|     | Directorio  | donde  | se  almacenarán  | los  comprobantes  | en  estado  en  |
| --- | ----------- | ------ | ---------------- | ------------------ | --------------- |
5  Comprobantes enviados
procesamiento.
5.1  Comprobantes rechazados*  Directorio donde no cumple esquemas o sin autorización de emisión.
* Estos directorios se configuran automáticamente dentro de la carpeta de documentos firmados.

9.5 De manera obligatoria deberá parametrizarse la información del emisor, con la
finalidad  de  que  cuando  se  genera  un  comprobante  electrónico,  esta
información  aparezca  por  defecto  sin  la  necesidad  de  digitar  en  cada
transacción  la  misma  información,  generando  posibles  errores  de  forma  y
digitación.

TABLA 11

 No.  Descripción (emisor o agente de retención)  Tipo de campo  Longitud  Requisito
| 1  Número de RUC  |     |     | Numérico  | 13  | Obligatorio  |
| ----------------- | --- | --- | --------- | --- | ------------ |
2  Razón social / nombres o apellidos  Alfanumérico  Max. 300  Obligatorio
| 3  Nombre comercial  |     |     | Alfanumérico  | Max. 300  | Opcional  |
| -------------------- | --- | --- | ------------- | --------- | --------- |
4  Dirección del establecimiento matriz  Alfanumérico  Max. 300  Obligatorio
5  Dirección del establecimiento emisor  Alfanumérico  Max. 300  Opcional
6  Código del establecimiento emisor  Numérico  3  Obligatorio
| 7  Código del punto de emisión  |     |     | Numérico  | 3   | Obligatorio  |
| ------------------------------- | --- | --- | --------- | --- | ------------ |
8  Contribuyente especial (Número de resolución)  Numérico  Min. 3 y Max. 5  Opcional
Obligado a llevar contabilidad (Opciones SI o
| 9   |     |     | De selección  | 2   | Opcional  |
| --- | --- | --- | ------------- | --- | --------- |
NO)
| 10  Logo del emisor   |     |     | Imagen    | -   | Opcional     |
| --------------------- | --- | --- | --------- | --- | ------------ |
| 11  Tipo de ambiente  |     |     | Numérico  | 1   | Obligatorio  |
| 12  Tipo de emisión   |     |     | Numérico  | 1   | Obligatorio  |

9.6 Para una óptima utilización del facturador, también se deberá parametrizar los
productos o servicios que ofrece el vendedor, ingresando el detalle y un código
de producto y/o servicio, en conjunto con su tarifa de impuesto de IVA, ICE,
IRBPNR o ISD de ser el caso. Se podrá importar o exportar los productos o
servicios a parametrizar en formato txt.

TABLA 12

|  No.                                    | Descripción  |     |     |     | Requisito    |
| --------------------------------------- | ------------ | --- | --- | --- | ------------ |
| 1  Impuestos y tarifas parametrizables  |              |     |     |     | Obligatorio  |
2  Código identificador del producto o servicio asignado por el contribuyente.  Obligatorio
2  Código identificador auxiliar del producto o servicio  Opcional
| 3  Nombre del producto o servicio  |     |     |     |     | Obligatorio  |
| ---------------------------------- | --- | --- | --- | --- | ------------ |

26

|                         |     |     |     |              |
| ----------------------- | --- | --- | --- | ------------ |
| 4  Valor unitario       |     |     |     | Obligatorio  |
| 5  Descuento            |     |     |     | Obligatorio  |
| 6  Impuesto             |     |     |     | Obligatorio  |
| 7  Tarifa del impuesto  |     |     |     | Obligatorio  |
8  Campos adicionales (máximo tres campos de hasta 300 caracteres)  Opcional

9.7 De  igual  manera  se  podrá  parametrizar  a  los  clientes  ya  identificados,  a
quienes van a transferir los bienes o realizar la prestación de servicios, así
también la información de los transportistas para el caso de guías de remisión y
los agentes retenidos para los comprobantes de retención. Se podrá importar
los clientes a parametrizar en formato txt.

TABLA 13

|  No.  | Descripción  |     |     | Requisito  |
| ----- | ------------ | --- | --- | ---------- |
1  Identificación (Número de RUC, cédula o pasaporte)  Obligatorio
| 2  Nombres y apellidos o razón social         |     |     |     | Obligatorio  |
| --------------------------------------------- | --- | --- | --- | ------------ |
| 3  Dirección de correo electrónico            |     |     |     | Obligatorio  |
| 4  Placa (para el caso de guías de remisión)  |     |     |     | Obligatorio  |
| 5  Teléfono                                   |     |     |     | Opcional     |
| 6  Dirección / ubicación                      |     |     |     | Opcional     |

9.8 Por defecto aparecerá la denominación de la moneda de curso actual en el
país “DÓLAR”.

9.9 Se detalla en el cuadro adjunto los campos a ser llenados que corresponden a
facturas, comprobantes de retención, notas de crédito y notas de débito:

TABLA  14:  FACTURAS,  COMPROBANTES  DE  RETENCIÓN,  NOTAS  DE
CRÉDITO Y NOTAS DE DÉBITO:

Descripción de llenado  Tipo de
|  No.                           |        | Longitud  | Requisito  | Comprobante  |
| ------------------------------ | ------ | --------- | ---------- | ------------ |
| (comprador o agente retenido)  | campo  |           |            |              |
Número secuencial del
| 1   | Numérico  | 9   | Obligatorio  | TODOS  |
| --- | --------- | --- | ------------ | ------ |
comprobante
Razón social / Nombres o
| 2   | Alfanumérico  | Max. 300  | Obligatorio  | TODOS  |
| --- | ------------- | --------- | ------------ | ------ |
apellidos
Identificación (RUC, Cédula,
3  pasaporte, identificación del  Alfanumérico  Max 20  Obligatorio  TODOS
exterior o placa)
| 4  Fecha de emisión  | Numérico  | 8   | Obligatorio  | TODOS  |
| -------------------- | --------- | --- | ------------ | ------ |
5  Número de la guía de remisión  Numérico  15  Opcional  CAMPO SOLO PARA FACTURA
| Denominación del comprobante  |           |     | CAMPO SOLO PARA NOTAS DE   |     |
| ----------------------------- | --------- | --- | -------------------------- | --- |
| 6                             | Numérico  | 2   | Obligatorio                |     |
| de venta que se modifica      |           |     | CRÉDITO Y NOTAS DE DÉBITO  |     |
| Número del comprobante de     |           |     | CAMPO SOLO PARA NOTAS DE   |     |
| 7                             | Numérico  | 15  | Obligatorio                |     |
| venta que se modifica         |           |     | CRÉDITO Y NOTAS DE DÉBITO  |     |
CAMPO SOLO PARA
Denominación del comprobante
| 8   | Numérico  | 2   | Obligatorio  | COMPROBANTES DE  |
| --- | --------- | --- | ------------ | ---------------- |
de venta que motiva la retención
RETENCIÓN
CAMPO SOLO PARA
| 9  Número del comprobante de  | Numérico  | 15  | Obligatorio  |     |
| ----------------------------- | --------- | --- | ------------ | --- |
COMPROBANTE DE
venta que motiva la retención
RETENCIÓN

27

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
CAMPO SOLO PARA
10  Ejercicio fiscal (mmaaaa)  Numérico  6  Obligatorio  COMPROBANTE DE
RETENCIÓN
| 11  Código numérico  | Numérico  | 8 / 23  Obligatorio  |     | TODOS  |
| -------------------- | --------- | -------------------- | --- | ------ |
12  Dígito verificador (Módulo 11)  Numérico  1  Obligatorio  TODOS

TABLA 15: GUÍAS DE REMISIÓN:

 No.  Descripción de Llenado  Tipo de campo  Longitud  Requisito
1  Número secuencial del comprobante  Numérico  9  Obligatorio
2  Razón social / nombres o apellidos (Destinatario)  Alfanumérico  Max. 300  Obligatorio
Identificación destinatario (RUC, cédula, pasaporte,
| 3   |     | Alfanumérico  | 10 a 20  | Obligatorio  |
| --- | --- | ------------- | -------- | ------------ |
identificación del exterior)
4  Dirección del punto de partida  Alfanumérico  Max. 300  Obligatorio
5  Dirección del destinatario o destinos  Alfanumérico  Max. 300  Obligatorio
6  Razón social / Nombres o apellidos (transportista o  Alfanumérico  Max. 300  Obligatorio
remitente)
Identificación transportista o remitente (ruc, cédula,
| 7   |     | Alfanumérico  | 10 a 13  | Obligatorio  |
| --- | --- | ------------- | -------- | ------------ |
pasaporte)
| 8  Número de placa  |     | Alfanumérico  | Max. 20  | Obligatorio  |
| ------------------- | --- | ------------- | -------- | ------------ |
9  Descripción de la mercadería transportada  Alfanumérico  Max. 300  Obligatorio
10  Cantidad de la mercadería transportada  Alfanumérico  Libre  Obligatorio
11  Motivo del traslado  Alfanumérico  Max. 300  Obligatorio
12  Denominación del comprobante de venta  Numérico  2  Opcional
13  Número de autorización del comprobante de venta  Numérico  10 ó 37  Opcional
14  Fecha de emisión del comprobante de venta  Numérico  8  Opcional
15  Numeración del comprobante de venta  Numérico  15  Opcional
16  Número de la declaración aduanera  Numérico  20  Opcional
| 17  Fecha de Inicio de transporte  |     | Numérico  | 8   | Obligatorio  |
| ---------------------------------- | --- | --------- | --- | ------------ |
18  Fecha de terminación del transporte  Numérico  8  Obligatorio
| 19  Ruta  |     | Alfanumérico  | Max. 300  | Opcional  |
| --------- | --- | ------------- | --------- | --------- |
20  Código del establecimiento del destinatario del  Numérico  3  Opcional
producto
| 21  Código numérico     |     | Numérico  | 8 / 23  | Obligatorio  |
| ----------------------- | --- | --------- | ------- | ------------ |
| 22  Dígito verificador  |     | Numérico  | 1       | Obligatorio  |

9.10  Entre la lista de clientes se encuentra el “Consumidor final”, para que por
defecto se identifique en ventas a consumidores finales. Si el valor de la factura
es  mayor  a  50  USD  se  deberá  especificar  obligatoriamente  los  datos  del
adquirente.
9.11   Se  podrá  ingresar  información  adicional  por  cada  comprobante,  como
máximo quince campos de hasta 300 caracteres alfanuméricos.

9.12  Se detalla a continuación los códigos de los impuestos.

TABLA 16

|     | Impuesto  | Código  |     |     |
| --- | --------- | ------- | --- | --- |
|     | IVA       | 2       |     |     |
|     | ICE       | 3       |     |     |
|     | IRBPNR    | 5       |     |     |

28

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
9.13  Se enlista a continuación los códigos de las tarifas de los impuestos:

17: TARIFA DEL IVA

|     |     | Porcentaje de IVA      |     | Código  |     |     |
| --- | --- | ---------------------- | --- | ------- | --- | --- |
|     |     | 0%                     |     | 0       |     |     |
|     |     | 12%                    |     | 2       |     |     |
|     |     | 14%                    |     | 3       |     |     |
|     |     | 15%                    |     | 4       |     |     |
|     |     | 5%                     |     | 5       |     |     |
|     |     | No Objeto de Impuesto  |     | 6       |     |     |
|     |     | Exento de IVA          |     | 7       |     |     |
|     |     | IVA diferenciado3      |     | 8       |     |     |
|     |     | 13%                    |     | 10      |     |     |

TABLA 18: TARIFA DEL ICE:

A  continuación,  se detalla  el listado  de  códigos del Impuesto a  los  Consumos
Especiales, las tarifas deberán calcularse en base a la normativa vigente.

|     |     |     |            |         | Tarifa Ad  | Tarifa         |
| --- | --- | --- | ---------- | ------- | ---------- | -------------- |
|     |     |     | Tarifa Ad  | Tarifa  | Valorem    | específica de  |
Código  Descripción  Valorem  específica de  febrero a  febrero a
|     |     |     | enero 2023  | enero 2023  |            |            |
| --- | --- | --- | ----------- | ----------- | ---------- | ---------- |
|     |     |     |             |             | diciembre  | diciembre  |
2023
2023
| 3011  ICE Cigarrillos Rubios   |                           |                        | -     | 0,17   | -     | 0,16  |
| ------------------------------ | ------------------------- | ---------------------- | ----- | ------ | ----- | ----- |
| 3021  ICE Cigarrillos Negros   |                           |                        | -     | 0,17   | -     | 0,16  |
| I C E   P ro                   | d u c to s   d e l  T a b | a c o   y  Sucedáneos  |       |        |       |       |
| 3023                           |                           |                        | 150%  | -      | 150%  | -     |
| d e l T a b a                  | c o  e x c e p to  C i g  | a rr il lo s           |       |        |       |       |
| 3031  ICE Bebidas Alcohólicas  |                           |                        | 75%   | 10,36  | 75%   |       |
10,00
| 3041  ICE Cerveza Industrial Gran Escala  |     |     | 75%  | -   | 75%  |     |
| ----------------------------------------- | --- | --- | ---- | --- | ---- | --- |
-
| 3041  ICE Cerveza Industrial Mediana Escala  |     |     | 75%  | -   | 75%  |     |
| -------------------------------------------- | --- | --- | ---- | --- | ---- | --- |
-
| 3041  ICE Cerveza Industrial Pequeña Escala  |     |     | 75%  | -   | 75%  | -   |
| -------------------------------------------- | --- | --- | ---- | --- | ---- | --- |
3073  I C E   V e h í c u lo s   M o t or izados cuyo PVP sea  5%  -  5%
|               |                     |     |     |     |     | -   |
| ------------- | ------------------- | --- | --- | --- | --- | --- |
| h a st a  d e |   2 0 0 0 0   U S D |     |     |     |     |     |
3075  I C E   V e h íc u lo s   Motorizados  PVP  entre  15%  -  15%
|                 |                          |                          |      |     |      | -   |
| --------------- | ------------------------ | ------------------------ | ---- | --- | ---- | --- |
| 3 0 00 0  y  4  | 0 0 0 0                  |                          |      |     |      |     |
| I C E   V e     | hí cu l o s   M o t o ri | z a d o s   c u yo  PVP  |      |     |      |     |
| 3077            |                          |                          | 20%  | -   | 20%  | -   |
| s u pe ri or  U | S D   4 0 .0 00   h a    | s t a  5 0 . 00 0        |      |     |      |     |
| I C E   V e     | hí cu l o s   M o t o ri | z a d o s   c u yo  PVP  |      |     |      |     |
| 3078            |                          |                          | 25%  | -   | 25%  | -   |
| s u pe ri or  U | S D   5 0 .0 00   h a    | s t a  6 0 . 00 0        |      |     |      |     |
| I C E   V e     | hí cu l o s   M o t o ri | z a d o s   c u yo  PVP  |      |     |      |     |
| 3079            |                          |                          | 30%  | -   | 30%  | -   |
| s u pe ri or  U | S D   6 0 .0 00   h a    | s t a  7 0 . 00 0        |      |     |      |     |
3080  I C E   V e hí cu l o s   M o torizados  cuyo  PVP  35%  -  35%
|                 |                 |     |     |     |     | -   |
| --------------- | --------------- | --- | --- | --- | --- | --- |
| s u pe ri or  U | S D   7 0 .0 00 |     |     |     |     |     |
3081  I C E   A v iones,  Tricares,  yates,  Barcos  de  15%  -  10%
| R e c re o                                   |     |     |     |     |     | -   |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 3092  ICE Servicios de Televisión Prepagada  |     |     | 0%  | -   | 0%  |     |
-
| 3610  ICE Perfumes y Aguas de Tocador  |     |     | 20%  | -   | 20%  |     |
| -------------------------------------- | --- | --- | ---- | --- | ---- | --- |
-
| 3620  ICE Videojuegos  |     |     | 0%  | -   | 0%  |     |
| ---------------------- | --- | --- | --- | --- | --- | --- |
-
| I C E   A r m  | a s   de Fuego, Armas deportivas y  |     |       |     |      |     |
| -------------- | ----------------------------------- | --- | ----- | --- | ---- | --- |
| 3630           |                                     |     | 300%  | -   | 30%  | -   |
| M u n i ci o n | e s                                 |     |       |     |      |     |

3 Mediante decreto ejecutivo el presidente de la República podrá aplicar una tafia de IVA diferenciada del 8% para el sector turístico hasta 12
días al año según se establezca en el respectivo decreto.

29

|     |     |     |     |     |     |            |         |            |                |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ---------- | -------------- |
|     |     |     |     |     |     |            |         | Tarifa Ad  | Tarifa         |
|     |     |     |     |     |     | Tarifa Ad  | Tarifa  | Valorem    | específica de  |
Código  Descripción  Valorem  específica de  febrero a  febrero a
|     |     |     |     |     |     | enero 2023  | enero 2023  |            |            |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | ---------- | ---------- |
|     |     |     |     |     |     |             |             | diciembre  | diciembre  |
2023
2023
| 3640  | ICE Focos Incandescentes            |           |             |     |               | 100%  | -   | 100%  | -   |
| ----- | ----------------------------------- | --------- | ----------- | --- | ------------- | ----- | --- | ----- | --- |
|       | I C E                               | C u otas  | Membresías  |     | Afiliaciones  |       |     |       |     |
| 3660  |                                     |           |             |     |               | 35%   | -   | 35%   | -   |
|       | A c c ione                          | s         |             |     |               |       |     |       |     |
| 3093  | ICE Servicios Telefonía Sociedades  |           |             |     |               | 15%   | -   | 15%   |     |
-
| 3101  | ICE Bebidas Energizantes  |     |     |     |     | 10%  | -   | 10%  |     |
| ----- | ------------------------- | --- | --- | --- | --- | ---- | --- | ---- | --- |
-
|       |         |                                          |     |     |     |     | 0,19 por 100      |     | 0,18 por 100      |
| ----- | ------- | ---------------------------------------- | --- | --- | --- | --- | ----------------- | --- | ----------------- |
|       | I C E   | B e b id as Gaseosas con Alto Contenido  |     |     |     |     |                   |     |                   |
| 3053  |         | r                                        |     |     |     | -   | gr a m o s   d e  | -   | gr a m o s   d e  |
|       | d e  A  | z ú c a                                  |     |     |     |     |                   |     |                   |
|       |         |                                          |     |     |     |     | a z ú c a r       |     | a z ú c a r       |
3054  I C E  B e b id as Gaseosas con Bajo Contenido  10%  -  10%
|     |        | r      |     |     |     |     |               |     | -             |
| --- | ------ | ------ | --- | --- | --- | --- | ------------- | --- | ------------- |
|     | d e  A | zú c a |     |     |     |     |               |     |               |
|     |        |        |     |     |     |     | 0,19 por 100  |     | 0,18 por 100  |
3111  ICE Bebidas No Alcohólicas  -  gramos de  -  gramos de
|       |                        |     |     |     |     |     | azúcar  |     | azúcar  |
| ----- | ---------------------- | --- | --- | --- | --- | --- | ------- | --- | ------- |
| 3043  | ICE Cerveza Artesanal  |     |     |     |     | -   | 1,55    | -   |         |
1,50
| 3033  | ICE Alcohol  |     |     |     |     | 75%  | 10,36  | 75%  |     |
| ----- | ------------ | --- | --- | --- | --- | ---- | ------ | ---- | --- |
10,00
3671  I C E   c a le f o n e s   y  s i stemas de calentamiento  100%  100%
|     |        |               |            |     |     |     | -   |     | -   |
| --- | ------ | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
|     | d e  a | g u a   a   g | a s  S R I |     |     |     |     |     |     |
ICE vehículos motorizados camionetas y de
| 3684  |                                       |     |     |     |     | 5%  |     | 5%  |     |
| ----- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|       | rescate cuyo PVP sea hasta DE 30.000  |     |     |     |     |     | -   |     | -   |
USD
|     | ICE  | vehículos  | motorizados  |     | excepto  |     |     |     |     |
| --- | ---- | ---------- | ------------ | --- | -------- | --- | --- | --- | --- |
3686  camionetas  y  de  rescate  cuyo  PVP  sea  10%  -  10%  -
superior USD 20.000 hasta DE 30.000
|       | I C E   | v e h íc u l   | o s  h íb r idos cuyo PVP sea de  |                            |     |     |     |     |     |
| ----- | ------- | -------------- | --------------------------------- | -------------------------- | --- | --- | --- | --- | --- |
| 3688  |         |                |                                   |                            |     | 0%  |     | 0%  |     |
|       | h a st  | a   U S D .    | 3 5 .0 0 0                        |                            |     |     |     |     |     |
| 3691  | I C E   | v e h íc u l   | o s   h í b r i d                 | o s   c u yo PVP superior  |     | 8%  |     |     |     |
|       |         |                |                                   |                            |     |     |     | 8%  |     |
|       | U S D   | .   3 5. 0 0 0 |   h a s t a   4 0                 | . 0 0 0                    |     |     |     |     |     |
3692  I C E   v e h íc u l o s   h í b r i d o s   c u yo PVP superior  14%     14%
|       | U S D   | .   4 0. 0 0 0 |   h a s t a   5 0 | . 0 0 0                    |     |      |     |      |     |
| ----- | ------- | -------------- | ----------------- | -------------------------- | --- | ---- | --- | ---- | --- |
|       | I C E   | v e h íc u l   | o s   h í b r i d | o s   c u yo PVP superior  |     |      |     |      |     |
| 3695  |         |                |                   |                            |     | 20%  |     | 20%  |     |
|       | U S D   | .   5 0. 0 0 0 |   h a s t a   6 0 | . 0 0 0                    |     |      |     |      |     |
|       | I C E   | v e h íc u l   | o s   h í b r i d | o s   c u yo PVP superior  |     |      |     |      |     |
| 3696  |         |                |                   |                            |     | 26%  |     | 26%  |     |
|       | U S D   | .   6 0. 0 0 0 |   h a s t a   7 0 | . 0 0 0                    |     |      |     |      |     |
3698  I C E  v e h í c u lo s híbridos cuyo PVP superior a  32%  -  32%
|     |       |              |     |     |     |     |     |     | -   |
| --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|     | U S D |  7 0 . 0 0 0 |     |     |     |     |     |     |     |
3682  I C E   c o n s u m i b le s   ta b a co  calentado  y  150%  -  150%
|       |                       |                                           |                   |     |     |     |       |     | -   |
| ----- | --------------------- | ----------------------------------------- | ----------------- | --- | --- | --- | ----- | --- | --- |
|       | lí q ui               | do s  c o n                               |   ni c o ti n a S | R I |     |     |       |     |     |
|       | I C E                 | s e rv icios de telefonía móvil personas  |                   |     |     |     |       |     |     |
| 3681  |                       |                                           |                   |     |     | 0%  | -     | 0%  | -   |
|       | n a tu                | r a le s                                  |                   |     |     |     |       |     |     |
| 3680  | ICE fundas plásticas  |                                           |                   |     |     | -   | 0,10  | -   |     |
0,08
| 3533  | ICE Import. Bebidas Alcohólicas  |     |     |     |     | 75%  | -   | 75%  |     |
| ----- | -------------------------------- | --- | --- | --- | --- | ---- | --- | ---- | --- |
-
| 3541  | ICE Cerveza Gran Escala CAE  |     |     |     |     | 75%  | -   | 75%  |     |
| ----- | ---------------------------- | --- | --- | --- | --- | ---- | --- | ---- | --- |
-
|       | I C E   | Cerveza Industrial de Mediana Escala  |     |     |     |      |     |      |     |
| ----- | ------- | ------------------------------------- | --- | --- | --- | ---- | --- | ---- | --- |
| 3541  |         |                                       |     |     |     | 75%  | -   | 75%  | -   |
|       | C A E   |                                       |     |     |     |      |     |      |     |
3541  I C E   Cerveza Industrial de Pequeña Escala  75%  -  75%
|       |                             |              |                  |                   |                |       |     |       | -   |
| ----- | --------------------------- | ------------ | ---------------- | ----------------- | -------------- | ----- | --- | ----- | --- |
|       | C A E                       |              |                  |                   |                |       |     |       |     |
| 3542  | ICE Cigarrillos Rubios CAE  |              |                  |                   |                | -     | -   | -     | -   |
| 3543  | ICE Cigarrillos Negros CAE  |              |                  |                   |                | -     | -   | -     | -   |
|       | I C E                       | P ro d u c   | to s   d e l  Ta | b a c o   y       | S u ce dáneos  |       |     |       |     |
| 3544  |                             |              |                  |                   |                | 150%  | -   | 150%  | -   |
|       | d e l T                     | a b a c o  E | x c e p to  C    | ig a r ri llo s   | C A E          |       |     |       |     |
| 3581  | ICE Aeronaves CAE           |              |                  |                   |                | 15%   | -   | 10%   |     |
-
|       | I C E                              | A v i o n e s  | ,   A v i o n e t   | a s  y   H e l i c | ó p te ros Exct.  |      |     |      |     |
| ----- | ---------------------------------- | -------------- | ------------------- | ------------------ | ----------------- | ---- | --- | ---- | --- |
| 3582  |                                    |                |                     |                    |                   | 15%  | -   | 10%  | -   |
|       | A q u                              | e ll o s   d e | s t i n a d o s   A | l  T r a n s .   C | A E               |      |     |      |     |
| 3710  | ICE Perfumes Aguas de Tocador Cae  |                |                     |                    |                   | 20%  | -   | 20%  | -   |
| 3720  | ICE Video Juegos CAE               |                |                     |                    |                   | 35%  | -   | 35%  | -   |
3730  I C E  I m p o rt a c io n e s   A rm a s  d e  Fuego, Armas  300%  -  30%
|       |                               |                |                |           |     |       |     |       | -   |
| ----- | ----------------------------- | -------------- | -------------- | --------- | --- | ----- | --- | ----- | --- |
|       | d e po                        | r tiv a s   y  | M u n i c io n | es  C A E |     |       |     |       |     |
| 3740  | ICE Focos Incandescentes CAE  |                |                |           |     | 100%  | -   | 100%  | -   |
3871  I C E - v e h í c u lo s   m o to ri z a d o s  c uyo PVP SEA  5%  -  5%  -
|     | h a st | a   d e   2 0 | 0 0 0  U S D   | S E N A E   |     |     |     |     |     |
| --- | ------ | ------------- | -------------- | ----------- | --- | --- | --- | --- | --- |

30

|     |     |     |            |         |            |                |
| --- | --- | --- | ---------- | ------- | ---------- | -------------- |
|     |     |     |            |         | Tarifa Ad  | Tarifa         |
|     |     |     | Tarifa Ad  | Tarifa  | Valorem    | específica de  |
Código  Descripción  Valorem  específica de  febrero a  febrero a
|     |     |     | enero 2023  | enero 2023  |            |            |
| --- | --- | --- | ----------- | ----------- | ---------- | ---------- |
|     |     |     |             |             | diciembre  | diciembre  |
2023
2023
3873  I C E -v e hí c u l o s  m o t or iz ados  PVP  entre  15%  -  15%  -
| 3 0 00 0  Y    | 4 0 0 0 0 S E N A E   |                                |      |     |      |     |
| -------------- | --------------------- | ------------------------------ | ---- | --- | ---- | --- |
| I C E -v e h í | cu lo s   m o to ri   | z a d o s   c u y o   P V P    |      |     |      |     |
| 3874           |                       |                                | 20%  | -   | 20%  | -   |
| s u pe ri o r  | U S D   40. 00 0  h a | s t a  5 0 .0 0 0  S E N A E   |      |     |      |     |
| I C E -v e h í | cu lo s   m o to ri   | z a d o s   c u y o   P V P    |      |     |      |     |
| 3875           |                       |                                | 25%  | -   | 25%  | -   |
| s u pe ri o r  | U S D   50. 00 0  h a | s t a  6 0 .0 0 0  S E N A E   |      |     |      |     |
3876  I C E -v e h í cu lo s   m o to ri z a d o s   c u y o   P V P   30%  -  30%
|                |                       |                              |     |     |     | -   |
| -------------- | --------------------- | ---------------------------- | --- | --- | --- | --- |
| s u pe ri o r  | U S D   60. 00 0  h a | s t a  7 0 .0 0 0  S E N A E |     |     |     |     |
3877  I C E -v e h í cu lo s   m o to ri za d o s  cuyo  PVP  35%  -  35%
| s u pe ri o r                         | U S D   70. 00 0  S | E N A E             |      |     |      | -   |
| ------------------------------------- | ------------------- | ------------------- | ---- | --- | ---- | --- |
| I C E - A v io                        | n e s ,  Tricares,  | Yates,  Barcos  de  |      |     |      |     |
| 3878                                  |                     |                     | 15%  | -   | 10%  | -   |
| R e c   S E N                         | A E                 |                     |      |     |      |     |
| 3601  ICE Bebidas Energizantes SENAE  |                     |                     | 10%  | -   | 10%  |     |
-
|                |                                           |     |     | 0,19 por 100      |     | 0,18 por 100      |
| -------------- | ----------------------------------------- | --- | --- | ----------------- | --- | ----------------- |
| I C E   b e b  | i d a s   g as e osas con alto contenido  |     |     |                   |     |                   |
| 3552           |                                           |     | -   | gr a m o s   d e  | -   | gr a m o s   d e  |
| d e  a z ú c a | r   S E N A E                             |     |     |                   |     |                   |
|                |                                           |     |     | a z ú c a r       |     | a z ú c a r       |
3553  I C E   b e b id a s   ga s e osas con bajo contenido  10%  -  10%
|                |              |     |     |               |     | -             |
| -------------- | ------------ | --- | --- | ------------- | --- | ------------- |
| d e  a z ú c a | r  S E N A E |     |     |               |     |               |
|                |              |     |     | 0,19 por 100  |     | 0,18 por 100  |
3602  ICE bebidas no alcohólicas SENAE  -  gramos de  -  gramos de
|                                    |     |     |      | azúcar  |      | azúcar  |
| ---------------------------------- | --- | --- | ---- | ------- | ---- | ------- |
| 3545  ICE cerveza artesanal SENAE  |     |     | 75%  | 1,55    | 75%  |         |
1,5
| 3532  ICE Import. alcohol SENAE  |     |     | 75%  | 10,36  | 75%  |     |
| -------------------------------- | --- | --- | ---- | ------ | ---- | --- |
10
| I C E   c a le | f o n e s   y  s i stemas de calentamiento  |     |       |     |       |     |
| -------------- | ------------------------------------------- | --- | ----- | --- | ----- | --- |
| 3671           |                                             |     | 100%  | -   | 100%  | -   |
| d e  a g u a   | a   g a s  S R I                            |     |       |     |       |     |
3771  I C E   c a le f o n e s   y  s is te m as de calentamiento  100%  -  100%
|                |                      |     |     |     |     | -   |
| -------------- | -------------------- | --- | --- | --- | --- | --- |
| d e  a g u a   | a   g a s  S E N A E |     |     |     |     |     |
ICE vehículos motorizados camionetas y de
| 3685  rescate PVP sea hasta DE 30.000 USD  |     |     | 5%  | -   | 5%  | -   |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- |
SENAE
| ICE  vehículos  | motorizados     | excepto            |      |     |      |     |
| --------------- | --------------- | ------------------ | ---- | --- | ---- | --- |
| camionetas      | y  de  rescate  | cuyo  PVP  sea     |      |     |      |     |
| 3687            |                 |                    | 10%  | -   | 10%  | -   |
| superior        | USD  20.000     | hasta  de  30.000  |      |     |      |     |
SENAE
3689  I C E   v e h íc u l o s  h íb r id o s  c u yo PVP sea de  0%  -  0%
| h a st a   U S   | D .  3 5 .0 0 0  S E N      | A E                          |      |     |      | -   |
| ---------------- | --------------------------- | ---------------------------- | ---- | --- | ---- | --- |
| I C E   v e h íc | u l o s   h í b r i d o s   |   c u y o   P V P  superior  |      |     |      |     |
| 3690             |                             |                              | 8%   | -   | 8%   | -   |
| U S D .   3 5.   | 0 0 0   h a s t a   4 0 . 0 | 0 0   S E N A E              |      |     |      |     |
| I C E   v e h íc | u l o s   h í b r i d o s   |   c u y o   P V P  superior  |      |     |      |     |
| 3693             |                             |                              | 14%  | -   | 14%  | -   |
| U S D .   4 0.   | 0 0 0   h a s t a   5 0 . 0 | 0 0   S E N A E              |      |     |      |     |
| I C E   v e h íc | u l o s   h í b r i d o s   |   c u y o   P V P  superior  |      |     |      |     |
| 3694             |                             |                              | 20%  | -   | 20%  | -   |
| U S D .   5 0.   | 0 0 0   h a s t a   6 0 . 0 | 0 0   S E N A E              |      |     |      |     |
3697  I C E   v e h íc u l o s   h í b r i d o s   c u y o   P V P  superior  26%  -  26%
|                |                             |                 |     |     |     | -   |
| -------------- | --------------------------- | --------------- | --- | --- | --- | --- |
| U S D .   6 0. | 0 0 0   h a s t a   7 0 . 0 | 0 0   S E N A E |     |     |     |     |
3699  I C E  v e h í c u lo s   h íb ri do s cuyo PVP superior a  32%  -  32%  -
| U S D  7 0 . 0  | 0 0   S E N A E         |                     |       |     |      |     |
| --------------- | ----------------------- | ------------------- | ----- | --- | ---- | --- |
| I C E   c o     | n s u m i b le s   ta   | b a co   calentado  | y     |     |      |     |
| 3683            |                         |                     | 150%  |     | 50%  |     |
| lí q ui do s  c | o n   ni c o ti n a S E | N A E               |       |     |      |     |

9.14  Lista de códigos por impuestos asignados para la retención.

TABLA 19
|     |     | Impuesto a retener  |     | Código  |     |     |
| --- | --- | ------------------- | --- | ------- | --- | --- |
|     |     | RENTA               |     | 1       |     |     |
|     |     | IVA                 |     | 2       |     |     |
|     |     | ISD                 |     | 6       |     |     |

9.15  Se  describe  los  códigos  por  impuesto  de  acuerdo  con  el  porcentaje  de
retención.

31

TABLA 20: TABLAS DE RETENCIONES

RETENCIÓN DEL IVA

|     |     | Porcentaje IVA  | Código  |     |
| --- | --- | --------------- | ------- | --- |
|     |     | 10%             | 9       |     |
|     |     | 20%             | 10      |     |
|     |     | 30%             | 1       |     |
|     |     | 50%             | 11      |     |
|     |     | 70%             | 2       |     |
|     |     | 100%            | 3       |     |

•  Retención en cero:

|     |     | Porcentaje IVA  | Código  |     |
| --- | --- | --------------- | ------- | --- |
|     |     | 0.00%           | 7       |     |
*Aplica de conformidad con la Disposición Transitoria Única de la Resolución NAC-DGERCGC15-00000284.

•  No procede retención:

|     |     | Porcentaje IVA  | Código  |     |
| --- | --- | --------------- | ------- | --- |
|     |     | 0.00%           | 8       |     |

RETENCIÓN DEL ISD

| Porcentaje  |     | Vigencia  |     |     |
| ----------- | --- | --------- | --- | --- |
Código
ISD
|        |       | Desde                 |                                   | Hasta  |
| ------ | ----- | --------------------- | --------------------------------- | ------ |
| 5%     | 4580  | -                     | Hasta el 31 de diciembre de 2021  |        |
| 4.75%  | 4580  | 1 de enero de 2022    | 31 de marzo de 20224              |        |
| 4.50%  | 4580  | 1 de abril de 2022    | 30 de junio de 2022               |        |
| 4.25%  | 4580  | 1 de julio de 2022    | 30 de septiembre de 2022          |        |
| 4.00%  | 4580  | 1 de octubre de 2022  | 31 de diciembre de 2022           |        |
| 3.75%  | 4580  | 1 de febrero de 2023  | 30 de junio de 20235              |        |
1 de julio de 20236
| 3.50%  | 4580  |                       | 31 de marzo de 2024  |     |
| ------ | ----- | --------------------- | -------------------- | --- |
| 5%     | 4580  | 1 de abril del 20247  |                      |     |

4 Los porcentajes para el año 2022 se establecieron en el Decreto Ejecutivo No. 298 publicado en el Segundo Suplemento del Registro Oficial
No. 604 del 23 de diciembre de 2021.
5 Los porcentajes para el año 2023 se establecieron en el Decreto Ejecutivo No. 643 publicado en el Segundo Suplemento del Registro Oficial
No. 235 del 23 de enero de 2023.
6 El porcentaje para el año 2024 se establecieron en el Decreto Ejecutivo No. 98 publicado en el Segundo Suplemento del Registro Oficial No.
467 del 29 de diciembre de 2023
7 Ley Orgánica para Enfrentar el Conflicto Armado Interno, la Crisis Social y Económica publicada en el Registro Oficial No. 516 del 12 de
marzo de 2024 que reforma el artículo 162 de la Ley. Reformatoria para la Equidad Tributaria en el Ecuador.

32

|     |             |     |     |     |           |     |     |
| --- | ----------- | --- | --- | --- | --------- | --- | --- |
|     | Porcentaje  |     |     |     | Vigencia  |     |     |
Código
ISD
|     |       |       | Desde               |     |     |     | Hasta  |
| --- | ----- | ----- | ------------------- | --- | --- | --- | ------ |
|     | 2.5%  | 4586  | 1 de mayo de 20258  |     |     |     |        |

RETENCIÓN DE RENTA:

Los porcentajes de retención del Impuesto a la Renta se aplicarán conforme lo
establecido en la normativa legal vigente, para lo cual se deberán considerar los
porcentajes  establecidos  en  las  tablas  del  Catálogo  de  Anexo  Transaccional
Simplificado,  publicado  en  la  página  web  www.sri.gob.ec:  Información  sobre
impuestos/Cómo declaro mis impuestos?/Anexos y guías o directamente a través
del siguiente link: http://www.sri.gob.ec/web/guest/formularios-e-instructivos1.

9.16  A continuación, se detallan los valores subtotales y totales con impuestos
que deben constar en los comprobantes de venta, según el caso.

TABLA 21

| No.  | Campos de valores  |            | Tipo de campo  |               |                 |          | Requisito    |
| ---- | ------------------ | ---------- | -------------- | ------------- | --------------- | -------- | ------------ |
|      |                    | Sumarán    | todos          | los  precios  | totales         | de  los  |              |
| 1    | Sub total IVA _%:  |            |                |               |                 |          | Obligatorio  |
|      |                    | productos  | gravados       | con           | la  tarifa  de  | IVA      |              |
vigente.
|     |                | Sumarán  | todos  | los  precios  | totales  | de  los  |              |
| --- | -------------- | -------- | ------ | ------------- | -------- | -------- | ------------ |
| 2   | Sub total 0%:  |          |        |               |          |          | Obligatorio  |
productos gravados con tarifa de IVA 0%.
|     | Sub total no objeto  | Sumarán                      | todos  | los  precios  | totales  | de  los  |              |
| --- | -------------------- | ---------------------------- | ------ | ------------- | -------- | -------- | ------------ |
| 3   |                      |                              |        |               |          |          | Obligatorio  |
|     | IVA:                 | productos No Objeto de IVA.  |        |               |          |          |              |
3  Sub total exento de  Sumarán  todos  los  precios  totales  de  los  Obligatorio
|     | IVA:  | productos Exento de IVA.  |     |     |     |     |     |
| --- | ----- | ------------------------- | --- | --- | --- | --- | --- |
Sumará las tres bases (Tarifa de IVA vigente,
| 4   | Sub total:  |     |     |     |     |     | Obligatorio  |
| --- | ----------- | --- | --- | --- | --- | --- | ------------ |
0%, no objeto de IVA o Exento de IVA).
5  Total descuento:  Sumará los valores de los descuentos.  Obligatorio
|     |     | Calculará  | del  campo  | Sub  | total  según  | el  |     |
| --- | --- | ---------- | ----------- | ---- | ------------- | --- | --- |
Obligatorio cuando corresponda /
| 6   | Valor ICE:  | porcentaje ingresado, este campo será editable  |     |     |     |     |     |
| --- | ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
editable
por la naturaleza del cálculo del impuesto.
Este campo será editable por la naturaleza del  Obligatorio cuando corresponda /
| 7   | Valor IRBPNR:  |                        |     |     |     |     |           |
| --- | -------------- | ---------------------- | --- | --- | --- | --- | --------- |
|     |                | cálculo del impuesto.  |     |     |     |     | editable  |
Sumará el campo Sub total IVA _% y el valor
8  Valor IVA _%:  del campo Valor ICE, el resultado aplicará la  Obligatorio
tarifa de IVA vigente.
|     |     | Este  campo  | aparecerá  | vacío,  | si  ingresa  | un  |     |
| --- | --- | ------------ | ---------- | ------- | ------------ | --- | --- |
9  Propina:  valor el sistema validará que el valor ingresado  Obligatorio
no supere el 10% del campo Sub total
Sumará los campos Sub total, ICE, IRBPNR,
| 10  | VALOR TOTAL  |     |     |     |     |     | Obligatorio  |
| --- | ------------ | --- | --- | --- | --- | --- | ------------ |
Valor IVA _% y Propina.

9.17 El  formato  para  todo  campo  correspondiente  a  valores  será  123456.98
utilizando el punto como separador de decimales; se utilizará como máximo

8
 El porcentaje para mayo de 2025 se estableció en el Decreto ejecutivo No. 589 publicado en el Registro Oficial – Cuarto Suplemento 9 del 31

de marzo de 2025.

33

dos decimales, a excepción de los campos de precio unitario y cantidad que
se podrá utilizar hasta 6 decimales, aplica para versión de comprobantes
1.1.0 (Anexo 3)
9.18 Los contribuyentes deberán implementar los controles necesarios en sus
sistemas informáticos que utilizan para la generación de comprobantes
electrónicos, con el fin de que los comprobantes sean emitidos en orden
cronológico y secuencial, controlando que no exista duplicidad tanto en la
secuencia como en las claves de acceso; así como también evitar el reenvío
innecesario de comprobantes para su autorización
9.19 Las representaciones impresas de los comprobantes electrónicos (RIDE),
tendrán validez tributaria y jurídica (Resolución 233 de junio 2018); como
anexos se adjuntan modelos en los cuales se detallan las posiciones de los
requisitos. Se podrán imprimir datos adicionales en el RIDE conforme lo
requiera el contribuyente.
9.20 En las representaciones impresas el emisor podrá incorporar un código de
barras que contenga la clave de acceso u otro código opcional de información
que el contribuyente crea importante para sus procesos.
9.21 Se recomienda revisar aspectos técnicos acerca de la ubicación de la
impresión de código de barras (GS1 – 128), para que puedan ser leídos por
máquinas lectoras de códigos de barras. Para más información pueden
ingresar a la siguiente dirección: http://www.gs1mexico.org/site/wp-
content/uploads/2012/06/Guia-codigo-GS1-128.pdf
10. Caso específico de retenciones en la
comercializadores / Distribuidores de
derivados del petróleo y retención presuntiva
de IVA a los editores, distribuidores y
voceadores que participan en la
comercialización de periódicos y/o revistas.
Los comercializadores y distribuidores de derivados de petróleo, deberán aplicar
los siguientes códigos de impuestos y tarifas de retenciones para la emisión de sus
facturas:
TABLA 22
IMPUESTO A RETENER CÓDIGO
IVA PRESUNTIVO Y RENTA 4
34

|     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLA 23

•  Retención IVA

TARIFA EN EL
|     | PORCENTAJE IVA RETENIDO Y/O PRESUNTIVO  |     |     |     |     |     | CÓDIGO  |     |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
XML
|     | ** 100%9  |             |          |             |                |     | 3   |     | 1     |     |     |
| --- | --------- | ----------- | -------- | ----------- | -------------- | --- | --- | --- | ----- | --- | --- |
|     | 12%       | (Retención  | de  IVA  | presuntivo  | por  Editores  | a   |     |     |       |     |     |
|     |           |             |          |             |                |     | 4   |     | 0.12  |     |     |
Margen de Comercialización Voceadores)
* 100% (Retención IVA venta periódicos y/o Revistas a
|     |     |     |     |     |     |     | 5   |     | 100  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
Distribuidores)
|     | *  100%  | (Retención  | IVA  | Venta  | de  Periódicos  | y/o  |     |     |      |     |     |
| --- | -------- | ----------- | ---- | ------ | --------------- | ---- | --- | --- | ---- | --- | --- |
|     |          |             |      |        |                 |      | 6   |     | 100  |     |     |
revistas a voceadores)
*Aplica para comprobantes de retención.
** Aplica para las retenciones de IVA de conformidad con Resolución No. NAC-DGERCGC21-00000063.

•  Ejemplo

LLENADO DEL XML
| DESCRIPCIÓN     |     | %    |           |                     |     |     |           |                      |            |     |     |
| --------------- | --- | ---- | --------- | ------------------- | --- | --- | --------- | -------------------- | ---------- | --- | --- |
|                 |     |      | <codigo>  | <codigoPorcentaje>  |     |     | <tarifa>  |                      | <valor>10  |     |     |
| Gasolina súper  |     | 13%  | 4         |                     | 3   |     | 1         | IVA EN VENTAS * 13%  |            |     |     |
Gasolina extra o
|     |     | 5.85%  | 4   |     | 3   |     | 1   | IVA EN VENTAS * 5.85%  |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- |
Ecopaís
| Diesel           |     | 4%    | 4   |     | 3   |     | 1   | IVA EN VENTAS * 4%       |     |     |     |
| ---------------- | --- | ----- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
| Otros derivados  |     |       |     |     |     |     |     | IVA DEL MARGEN DE        |     |     |     |
|                  |     | 100%  | 4   |     | 3   |     | 1   |                          |     |     |     |
| de petróleo      |     |       |     |     |     |     |     | COMERCIALIZACIÓN * 100%  |     |     |     |

•  Retención RENTA

|     |     | PORCENTAJE RENTA   |     |     | CÓDIGO  |     | TARIFA EN EL XML  |       |     |     |     |
| --- | --- | ------------------ | --- | --- | ------- | --- | ----------------- | ----- | --- | --- | --- |
|     |     | 0.002 (2 por mil)  |     |     | 327     |     |                   | 0.20  |     |     |     |
|     |     | 0.003 (3 por mil)  |     |     | 328     |     |                   | 0.30  |     |     |     |

| 11.  | Códigos  |     | de  | errores  |     | y   | advertencias  |     |     |     | de  |
| ---- | -------- | --- | --- | -------- | --- | --- | ------------- | --- | --- | --- | --- |
validación

VALIDACIÓN:
CÓDIGO
RECEPCIÓN
| DE  | DESCRIPCIÓN  |     |     |     | MOTIVO DE ERROR  |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
/AUTORIZACIÓN/
ERROR
EMISOR
RUC del emisor se
Verificar que el número de RUC se encuentre en estado
| 2   | encuentra NO  |     |     |     |     |     |     |     |     | AUTORIZACIÓN  |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
ACTIVO
ACTIVO.
|     | Establecimiento del  |     | No se autorizará comprobantes si el establecimiento  |     |     |     |     |     |     |     |     |
| --- | -------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
10  emisor se encuentra  emisor ha sido clausurado, automáticamente se habilitará  AUTORIZACIÓN
|     | Clausurado.  |     |     | el servicio una vez concluido la clausura.  |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Tamaño máximo
| 26  |     |     |     | Tamaño del archivo supera lo establecido  |     |     |     |     |     | RECEPCIÓN  |     |
| --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
superado

9 Para el llenado de la sección de IVA presuntivo en el XML de la factura electrónica se utilizará este código y la tarifa; sin embargo, los valores de los
porcentajes de retención corresponderán a los establecidos en la Resolución Nro. NAC-DGERCGC21-00000063.

10 Para el llenado de esta etiqueta se debe considerar el tipo de campo, formato y longitud establecida en el anexo 3.

35

VALIDACIÓN:
CÓDIGO
RECEPCIÓN
DE DESCRIPCIÓN MOTIVO DE ERROR
/AUTORIZACIÓN/
ERROR
EMISOR
La clase del contribuyente no puede emitir comprobantes
27 Clase no permitido AUTORIZACIÓN
electrónicos.
Siempre el contribuyente debe haber aceptado el acuerdo
Acuerdo de medios
de medio electrónicos en el cual se establece que se
28 electrónicos no RECEPCIÓN
acepta que lleguen las notificaciones al buzón del
aceptado
contribuyente.
35 Documento inválido Cuando el XML no pasa validación de esquema. RECEPCIÓN
Versión esquema
36 Cuando la versión del esquema no es la correcta. RECEPCIÓN
descontinuada
RUC sin autorización Cuando el RUC del emisor no cuenta con una solicitud de
37 AUTORIZACIÓN
de emisión emisión de comprobantes electrónicos.
39 Firma inválida Firma electrónica del emisor no es válida. AUTORIZACIÓN
No se encontró el certificado o no se puede convertir en
40 Error en el certificado AUTORIZACIÓN
certificad X509.
Clave acceso Cuando la clave de acceso ya se encuentra registrada en
43 RECEPCIÓN
registrada la base de datos.
Secuencial del comprobante ya se encuentra registrado en
45 Secuencial registrado RECEPCIÓN
la base de datos
Cuando el RUC emisor no existe en el Registro Único de
46 RUC no existe AUTORIZACIÓN
Contribuyentes.
Tipo de comprobante Cuando envían en el tipo de comprobante uno que no
47 RECEPCIÓN
no existe exista en el catálogo de nuestros tipos de comprobantes.
Esquema XSD no Cuando el esquema para el tipo de comprobante enviado
48 RECEPCIÓN
existe no existe.
Argumentos que
49 Cuando se consume el WS con argumentos nulos. RECEPCIÓN
envían al WS nulos
50 Error interno general Cuando ocurre un error inesperado en el servidor. RECEPCIÓN
52 Error en diferencias Cuando existe error en los cálculos del comprobante. AUTORIZACIÓN
Establecimiento Cuando el establecimiento desde el cual se genera el
56 AUTORIZACIÓN
cerrado comprobante se encuentra cerrado.
Cuando la autorización para emisión de comprobantes
electrónicos para el emisor se encuentra suspendida por
Autorización procesos de control de la Administración Tributaria o el
57 AUTORIZACIÓN
suspendida contribuyente no tenía la autorización para emitir
comprobantes electrónicos a la fecha de emisión del
comprobante
Error en la estructura Cuando la clave de acceso tiene componentes diferentes
58 AUTORIZACIÓN
de clave acceso a los del comprobante.
Cuando el RUC del emisor se encuentra clausurado por
63 RUC clausurado AUTORIZACIÓN
procesos de control de la Administración Tributaria.
Cuando el comprobante emitido no fue enviado de
Fecha de emisión EMISOR/
65 acuerdo con el tiempo del tipo de emisión en el cual fue
extemporánea RECEPCIÓN
realizado.
67 Fecha inválida Cuando existe errores en el formato de la fecha. RECEPCIÓN
Cuando se desea enviar un comprobante que ha sido
Clave de acceso en
70 enviado anteriormente y el mismo no ha terminado su RECEPCIÓN
procesamiento
procesamiento.
36

VALIDACIÓN:
CÓDIGO
RECEPCIÓN
DE DESCRIPCIÓN MOTIVO DE ERROR
/AUTORIZACIÓN/
ERROR
EMISOR
Cuando se ejecuta la consulta de autorización por clave de
Error en la estructura acceso y el valor de este parámetro supera los 49 dígitos,
80 AUTORIZACIÓN
de clave acceso tiene caracteres alfanuméricos o cuando el tag
(claveAccesoComprobante) está vacío
Error en la fecha de Cuando la fecha de inicio de transporte es menor a la
82 RECEPCIÓN
inicio de transporte fecha de emisión de la guía de remisión.
Error al validar monto Cuando el valor registrado en el campo de devolución del
92 de devolución del IVA, en facturas y notas de débito, no corresponde al que RECEPCIÓN
IVA. fue autorizado por el servicio web DIG.
Notas:
1. Todos aquellos comprobantes que hayan sido rechazados por cualquiera de
los errores señalados en la tabla anterior pueden ser reenviados para su
autorización una vez corregido el error motivo del rechazo sin generar nuevos
números de clave de acceso o secuenciales para los comprobantes. A
excepción de aquellos casos específicos en los que aun cuando el archivo
esté correcto, el sistema no pueda autorizar el comprobante debido a algún
impedimento como, por ejemplo: en el caso de RUC o establecimiento
clausurado, RUC inactivo, establecimiento cerrado, entre otros. Los
comprobantes devueltos no se guardarán en la base de datos del SRI, se
almacenarán únicamente los comprobantes que no hayan sido autorizados.
2. En el caso del error con código 70 – Clave de acceso en procesamiento, no
se deberá reenviar el comprobante o generar el comprobante con otra clave
de acceso y secuencial hasta recibir una respuesta de autorización o rechazo
del mismo, en un tiempo máximo de 24 horas.
CÓDIGO DE
DESCRIPCIÓN POSIBLE SOLUCIÓN
ADVERTENCIA
59 Identificación no existe Cuando el número de la identificación del adquirente no existe.
Siempre que el comprobante sea emitido en ambiente de
60 Ambiente ejecución. certificación o pruebas se enviará como parte de la autorización
esta advertencia.
Cuando el número de la identificación del adquirente del
62 Identificación incorrecta comprobante está incorrecto. Por ejemplo, cédulas no pasan el
dígito verificador.
68 Documento sustento Cuando el comprobante relacionado no existe como electrónico.
Al momento de receptar el archivo se realizarán las siguientes validaciones,
según el orden especificado, cabe mencionar que estas no serán revisadas
en su totalidad; es decir, si el sistema detecta como inconsistente el tamaño
del archivo ese será el error remitido:
ORDEN VALIDACIÓN DESCRIPCIÓN
Tamaño archivo
1 Validación XML Esquema activo
XML bien formado y válido
RUC activo
2 Validación contribuyente emisor
Establecimiento activo
37

|        |             |     |     |              |     |     |
| ------ | ----------- | --- | --- | ------------ | --- | --- |
| ORDEN  | VALIDACIÓN  |     |     | DESCRIPCIÓN  |     |     |
Autorización para emitir comprobantes electrónicos
activa
Autorización para emisión del tipo de comprobante
Clave acceso única
| 3   | Validación unicidad  |     |     | Secuencial único  |     |     |
| --- | -------------------- | --- | --- | ----------------- | --- | --- |
Clave acceso bien formada
Validez firma y cadena de confianza
Validación Firma
4
OCSP
Fecha emisión
5  Verificaciones adicionales  identificación del receptor del comprobante
documentos de sustento
| 6   | Validación diferencias  |     |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- |

3.  Las validaciones que se muestran a continuación deberán ser implementadas
en  el  sistema  del  contribuyente,  a  fin  de  garantizar  que  la  información
transmitida a la base de datos del SRI cumpla con los requisitos establecidos
en la normativa tributaria y comercio electrónico.

VALIDACIÓN:
CÓDIGO
RECEPCIÓN
DESCRIPCIÓN  POSIBLE SOLUCIÓN
DE
| ERROR  |     |     |     |     |     | /AUTORIZACIÓN/  |
| ------ | --- | --- | --- | --- | --- | --------------- |
EMISOR
Comprobante no  Cuando el comprobante no ha sido autorizado como parte
| 34          |     |                                                |     |     |     | EMISOR  |
| ----------- | --- | ---------------------------------------------- | --- | --- | --- | ------- |
| autorizado  |     | de la solicitud de emisión del contribuyente.  |     |     |     |         |
Certificado que ha superado su fecha de caducidad, y no
| 42  Certificado revocado  |     |     |     |     |     | EMISOR  |
| ------------------------- | --- | --- | --- | --- | --- | ------- |
ha sido renovado.
52  Error en diferencias  Cuando existe error en los cálculos del comprobante.  EMISOR
Cuando el código del documento sustento no existe en el
Código documento
| 64  |     | catálogo de documentos que se tiene en la  |     |     |     | EMISOR  |
| --- | --- | ------------------------------------------ | --- | --- | --- | ------- |
sustento
Administración.
Cuando el comprobante emitido no fue enviado de
| 65  Fecha de emisión  |     |     |     |     |     | EMISOR/  |
| --------------------- | --- | --- | --- | --- | --- | -------- |
extemporánea  acuerdo con el tiempo del tipo de emisión en el cual fue  RECEPCIÓN
realizado.
Cuando la identificación asociada al adquirente no existe.
Identificación del
69  En general cuando el RUC del adquirente no existe en el  EMISOR
receptor
Registro Único de Contribuyentes.

Para  acceder  al  catastro  de  RUC  podrán  descargarlo  desde  el  siguiente  link:
http://www.sri.gob.ec/web/guest/catastros

| 12.  Códigos  | de  | error  | para  | aplicación  |     | de  la  |
| ------------- | --- | ------ | ----- | ----------- | --- | ------- |
devolución automática del IVA

| CÓDIGO DE VALIDACIÓN   |     |     |                      | DESCRIPCIÓN  |     |     |
| ---------------------- | --- | --- | -------------------- | ------------ | --- | --- |
| 2000 EXITO             |     |     | Éxito.               |              |     |     |
| 2001 EXITO_VALIDACION  |     |     | Validación exitosa.  |              |     |     |

38

CÓDIGO DE VALIDACIÓN DESCRIPCIÓN
Estimado contribuyente, los campos registrados no cu
3000 ERROR_FORMATO
mplen con el formato establecido.
3001 ERROR_TRANSACCION No se logró hacer la transacción.
3003 ERROR_CLAVE_YA_PROCESADA Comprobante ya procesado.
3004 ERROR_CODIGO_OPERACION_INVALIDO Código operación inválido.
3005 ERROR_INTERNO_SERVIDOR Se ha producido un error.
3006 ERROR_TIME_OUT No se ha podido responder a tiempo.
Estimado contribuyente, el código de verificación
3007 ERROR_CODIGO_BENEFICIO
ingresado no se encuentra vigente.
3008 ERROR_WS_NO_DISPONIBLE WEB Service no disponible.
3009 ERROR_WS_NO_AUTORIZADO No está autorizado.
3011 ERROR_NO_MONTO_MINIMO El valor no cumple en monto mínimo a devolver.
La tarifa del impuesto calculado no coincide con el
3013 ERROR_TARIFA_IMPUESTO
enviado.
3014 ERROR_TOKEN_BENEFICIARIO El token no pertenece al emisor.
3015
El beneficiario no tiene el canal automático habilitado o
ERROR_CANAL_AUTOMATICO_NO_HABILITADO_
no existe un monto a devolver.
SALDO
3016: El beneficiario registra más de una
ERROR_MULTIPLE_TRANSACCIONES_LOTE transacción en el lote enviado
4000 LOTE_RECIBIDO Lote recibido.
4001 LOTE_RECHAZADO Lote rechazado.
4002 LOTE_EN_PROCESO Lote en proceso.
4003 LOTE_PROCESADO Lote procesado.
Los parámetros: rucs, fecha inicio o fecha fin para el
5001 ERROR_CONFIGURACION_PILOTO
piloto no están configurados.
6000 ANULACION_ERROR Error al realizar la anulación.
6001
No se realizó la transacción: comprobante electrónico
ANULACION_COMPROBANTE_NO_ENCONTRAD
no encontrado.
O
No se realizó la transacción: el monto del IVA a
6002 ANULACION_IVA_DEVOLVER_DIFERENTES
devolver no es igual al que se registró en el débito.
El código del beneficio no corresponde al registrado en
6004 ANULACION_BENEFICIO_INCORRECTO
el SRI.
6005 ANULACION_FECHA_DIFERENTE_HOY La fecha de emisión no corresponde a la de hoy.
6006
El comprobante tiene que ser una factura o una nota de
ANULACION_TIPO_COMPROBANTE_INCORRECT
débito.
O
39

|                               |                       |     |     |                               |              |     |
| ----------------------------- | --------------------- | --- | --- | ----------------------------- | ------------ | --- |
|                               | CÓDIGO DE VALIDACIÓN  |     |     |                               | DESCRIPCIÓN  |     |
| 6007 ANULACION_ENVIADA_EXITO  |                       |     |     | Anulación enviada con éxito.  |              |     |
6008  No se realizó la transacción: falta el monto del IVA a
| ANULACION_IVA_DEVOLVER_NO_ENCONTRADO  |     |     |     | devolver.                                           |     |     |
| ------------------------------------- | --- | --- | --- | --------------------------------------------------- | --- | --- |
| 6009                                  |     |     |     | No se realizó la transacción: la identificación no  |     |     |
ANULACION_IDENTIFICACIONES_DIFERENTES  corresponde a la clave de acceso.
| 6010  |     |     |     | No se realizó la transacción: el cálculo del IVA a  |     |     |
| ----- | --- | --- | --- | --------------------------------------------------- | --- | --- |
ANULACION_IVA_CALCULADO_DIFERENTES  devolver no es igual al que se registró en el débito.
| 6011  |     |     |     | No se realizó la transacción: la base imponible no es  |     |     |
| ----- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
ANULACION_BASE_IMPONIBLE_DIFERENTES  igual a la que se registró en el débito.
6012 ANULACION_NO_SALDO_DISPONIBLE  No se realizó la transacción: no tiene saldo disponible.
7000
No existen registros en el canal automático.
BENEFICIARIOS_ARCHIVO_NO_ENCONTRADO

| 13.         | Servicios  |      | web  | para  | la        | devolución  |
| ----------- | ---------- | ---- | ---- | ----- | --------- | ----------- |
| automática  |            | del  | IVA  | a     | personas  | adultas     |
mayores - DIG

13.1 Los enlaces WEB Service habilitados para los emisores electrónicos son los
siguientes:

1.  Servicio para obtención de lista de beneficiarios
2.  Servicio para la recepción de información por lotes
3.  Servicio para la consulta de información por lote (respuesta)
4.  Servicio para la recepción de información individual
5.  Servicio para anulación de descuento de devolución del IVA

Existen dos ambientes disponibles para la invocación de los enlaces WEB
Service publicados por la Administración Tributaria:

| Protocolo  |     | URL BASE  |     |     | Versión  | Ambiente  |
| ---------- | --- | --------- | --- | --- | -------- | --------- |
HTTPS  https://celcer.sri.gob.ec/devolucion-iva/rest  V1  Certificación producción
HTTPS  https://srienlinea.sri.gob.ec/devolucion-iva/rest  V1  Producción producción

Uno es para el ambiente de pruebas, donde cada contribuyente certificará que
su  aplicación  funcione  correctamente  con  cada  tipo  de  comprobante
electrónico.

El segundo es para el ambiente de producción, al cual cada contribuyente
deberá acceder una vez que ha realizado las pruebas y esté seguro de que su
aplicación funciona correctamente.

40

Se deberá configurar el dominio para el consumo de los enlaces WEB Service
dependiendo del ambiente a utilizar.
13.2 La seguridad para los servicios será provista mediante tokens del protocolo
OAuth2:
Protocolo URL Autenticación Versión
https://celcer.sri.gob.ec/sri-seguridad-sso-api-servicio-internet/rest/seguridad-sso-
HTTPS rest/access- V1
token/RUC_CONTRIBUYENTE[AD]CEDULA_ADICIONAL/CLAVE_ENCRIPTAD
A_ADICIONAL_SHA-512
https://srienlinea.sri.gob.ec/sri-seguridad-sso-api-servicio-internet/rest/seguridad-
HTTPS sso-rest/access- V1
token/RUC_CONTRIBUYENTE[AD]CEDULA_ADICIONAL/CLAVE_ENCRIPTAD
A_ADICIONAL_SHA-512
Los parámetros de “RUC_CONTRIBUYENTE”, “CEDULA_ADICIONAL” y
“CLAVE_ENCRIPTADA_ADICIONAL_SHA-512” deberán ser reemplazados
con los datos propios del contribuyente emisor electrónico.
El Token tendrá una vigencia de 35 minutos.
En las llamadas a los servicios se deberá incluir el token generado como un
parámetro de cabecera con la etiqueta Authorization.
Tipo de
Tipo de operación Parámetros Tipo de dato Tamaño
parámetros
USUARIO_ADICIONAL
String Query
GET 13
CLAVE_ENCRIPTADA_
string Query
ADICIONAL_ SHA-512
Para los valores monetarios que son variables de entrada o salida de los
servicios deberán ser enviados o receptados con una precisión de dos
decimales.
13.3 Servicio web para obtención de lista de beneficiarios
La información que se requiere para el consumo de este servicio es:
• RUC del emisor electrónico
El dato que devolverá el servicio es:
• Un archivo zip “cedulas_canal” que contiene las identificaciones de las
personas que se encuentran habilitadas para acceder al beneficio por
el mecanismo automático.
Esta información se actualizará diariamente entre las 0:30 am y 2:00 am, y
estará disponible durante el día.
Para utilizar el servicio se deberá considerar lo siguiente:
41

|     | Método  |                             |     | URL  |     |     |
| --- | ------- | --------------------------- | --- | ---- | --- | --- |
|     | POST    | /devolucionesBeneficiarios  |     |      |     |     |

|     | URL BASE CON EL SERVICIO  |     |     |     |     | Ambiente  |
| --- | ------------------------- | --- | --- | --- | --- | --------- |
Certificación
https://celcer.sri.gob.ec/devolucion-iva/rest/devolucionesBeneficiarios
Producción
| https://srienlinea.sri.gob.ec/devolucion- |                                     |     |     |     |     | Producción  |
| ----------------------------------------- | ----------------------------------- | --- | --- | --- | --- | ----------- |
|                                           | iva/rest/devolucionesBeneficiarios  |     |     |     |     | Producción  |

| Tipo de operación  |       | Parámetros  | Tipo de dato  |         | Tipo de parámetros  |         |
| ------------------ | ----- | ----------- | ------------- | ------- | ------------------- | ------- |
|                    | HEAD  | Token       |               | String  |                     | Header  |
|                    |       |             |               |         |                     |         |
|                    | POST  | ruc         |               | string  |                     | body    |

13.4  Servicio web para la recepción de información por lotes

El servicio para la recepción de información por lotes devolverá un código de
operación por el lote (lista datos enviados).

La longitud máxima de la lista de datos será de diez mil elementos, si los
emisores requieren enviar listas más largas deberán dividir los datos y hacer
uso varias veces del servicio.

La  información  que  se  requiere  en  este  servicio  por  parte  del  emisor
electrónico en cada uno de los ítems de la lista de datos deberá contener:

•  RUC del emisor electrónico
•  Clave de acceso del comprobante
•  Identificación del beneficiario (cédula)
•  Base imponible gravada diferente a cero (subtotal del comprobante con
IVA gravada diferente a cero)
•  Tarifa (porcentaje) del IVA diferente de cero
•  Monto del IVA diferente de cero

El dato que devolverá el servicio es:

•  Código de operación (código lote)

Para utilizar el servicio se deberá considerar lo siguiente:

|     | Método  |                                |     | URL  |     |     |
| --- | ------- | ------------------------------ | --- | ---- | --- | --- |
|     | POST    | /devolucionesLotesRecepciones  |     |      |     |     |

URL BASE CON EL SERVICIO  Ambiente
Certificación
https://celcer.sri.gob.ec/devolucion-iva/rest/devolucionesLotesRecepciones
Producción

42

Producción
https://srienlinea.sri.gob.ec/devolucion-iva/rest/devolucionesLotesRecepciones
Producción

Tipo de operación  Parámetros  Tipo de dato  Tipo de parámetro
| HEAD  | Token           | String  | header  |
| ----- | --------------- | ------- | ------- |
|       |                 |         |         |
| POST  | datosBeneficio  | json    | body    |

| Trama que recibe         |             | Trama de respuesta  |     |
| ------------------------ | ----------- | ------------------- | --- |
| DatosBeneficio:          | Respuesta:  |                     |     |
| type: array              |             | type: object        |     |
| properties:              |             | properties:         |     |
| rucEmisor:               |             | codigoLote          |     |
| required: true           |             | required: true      |     |
| type: string             |             | type: string        |     |
| claveAccesoComprobante:  |             | MensajeRespueta     |     |
| required: true           |             | required: true      |     |
| type: string             |             | type: string        |     |
idBeneficiario:

| required: true  | MensajeRespuesta:  |     |     |
| --------------- | ------------------ | --- | --- |
| type: string    | type: string       |     |     |
| baseImponible:  |                    |     |     |
required: true
type: number
porcentajeIva:
required: true
type: number
montoIva:
requiered: true
type: number

13.5 Servicio web para la respuesta de información por lotes (respuesta)

Con el código de operación que se obtuvo del servicio para la recepción de
información por lote, se podrán consultar los resultados de los descuentos de
cada ítem de la lista de datos enviados anteriormente.

La  información  que  se  requiere  en  este  servicio  por  parte  del  emisor
electrónico es:

• Código de operación (Código lote)

Los datos que devolverá el servicio es una lista de objetos cuyos atributos
son:

• Clave de acceso del comprobante
• Valor del descuento IVA.
• Mensaje asociado al valor.

Para utilizar el servicio se deberá considerar lo siguiente:

43

Método URL
POST /devolucionesLotesRespuestas
URL BASE CON EL SERVICIO Ambiente
Certificación
https://celcer.sri.gob.ec/devolucion-iva/rest/devolucionesLotesRespuestas
Producción
Producción
https://srienlinea.sri.gob.ec/devolucion-iva/rest/devolucionesLotesRespuestas
Producción
Tipo de operación Parámetros Tipo de dato Tipo de parámetro
HEAD Token String Header
POST codigoOperacion string body
Trama que recibe Trama de respuesta
codigoLote body:
application/json:
type: Respuesta
required: true
example:
{listaDescuento:
[
{ "claveAcceso": 12345678901234567890123454545454,
"valor": 1,”descripcion”:”aprobado”},
{ "claveAcceso": 12345678901234567890123454545455,
"valor": 2,”descripcion”:”aprobado”}
] , “codigo”: “4003”,”mensaje”:”lote_procesado”}
13.6 Servicio web para la recepción de información individual
Este servicio estará disponible para aquellos emisores electrónicos cuya
facturación se genere a demanda del cliente.
La información que se requiere en este servicio por parte del emisor
electrónico es:
• RUC del emisor electrónico
• Clave de acceso del comprobante
• Identificación del beneficiario (cédula)
• Código de acceso otorgado al beneficiario
• Base imponible gravada diferente a cero (Subtotal del comprobante con
IVA gravada diferente a cero)
• Tarifa(porcentaje) del IVA diferente de cero
• Monto del IVA diferente de cero
Los datos que devolverá el servicio son:
• Mensaje asociado al valor
• Valor del descuento IVA
44

Nota: el código de confirmación en el ambiente de “Certificación Producción”
es 1234 para los beneficiarios que se encuentren en el servicio web para
obtención de lista de beneficiarios.

Para utilizar el servicio se deberá considerar lo siguiente:

| Método  |                                       | URL  |     |
| ------- | ------------------------------------- | ---- | --- |
| POST    | /devolucionesIndividualesRecepciones  |      |     |

| URL BASE CON EL SERVICIO  |     |     | Ambiente  |
| ------------------------- | --- | --- | --------- |
Certificación
https://celcer.sri.gob.ec/devolucion-iva/rest/devolucionesIndividualesRecepciones
Producción
Producción
https://srienlinea.sri.gob.ec/devolucion-iva/rest/devolucionesIndividualesRecepciones
Producción

Tipo de operación  Parámetros  Tipo de dato  Tipo de parámetro
| HEAD  | Token           | String       | header  |
| ----- | --------------- | ------------ | ------- |
|       |                 |              |         |
| POST  | DatosBeneficio  | Object-json  | query   |

| Trama que recibe         |     | Trama de respuesta  |     |
| ------------------------ | --- | ------------------- | --- |
| DatosBeneficio:          |     | Descuento:          |     |
| type: object             |     | type: object        |     |
| properties:              |     | properties:         |     |
| rucEmisor:               |     | montoIvaDevolver:   |     |
| required: true           |     | required: true      |     |
| type: string             |     | type: number        |     |
| claveAccesoComprobante:  |     | codigo:             |     |
| required: true           |     | required: true      |     |
| type: string             |     | type: String        |     |
| idBeneficiario:          |     | mensaje:            |     |
| required: true           |     | required: true      |     |
| type: string             |     | type: string        |     |
codigoBeneficio:
required: true
type: string
baseImponible:
required: true
type: number
porcentajeIva:
required: true
type: number
montoIva:
required: true
type: number

13.7  Servicio web para anulación de descuento de devolución del IVA

El  servicio  se  expone  para  los  casos  en  que  no  se  pueda  concretar  la
transacción entre el cliente y el local comercial del emisor electrónico.

La  información  que  se  requiere  en  este  servicio  por  parte  del  emisor
electrónico es:

45

• RUC del emisor electrónico
• Clave de acceso del comprobante
• Identificación del beneficiario (cédula)
• Código de acceso otorgado al beneficiario
• Base imponible gravada diferente a cero (Subtotal del comprobante con IVA
gravada diferente a cero)
• Tarifa (porcentaje) del IVA diferente de cero
• Monto del IVA diferente de cero
• Monto IVA a devolver
El dato que devolverá el servicio es:
• Mensaje de respuesta
Nota: el código de confirmación en el ambiente de “Certificación Producción”
es 1234 para los beneficiarios que se encuentren en el servicio web para
obtención de lista de beneficiarios.
Para utilizar el servicio se deberá considerar lo siguiente:
Método URL
POST /devolucionesIndividualesAnulaciones
URL BASE CON EL SERVICIO Ambiente
Certificación
https://celcer.sri.gob.ec/devolucion-iva/rest/devolucionesIndividualesAnulaciones
Producción
Producción
https://srienlinea.sri.gob.ec/devolucion-iva/rest/devolucionesIndividualesAnulaciones
Producción
Tipo de operación Parámetros Tipo de dato Tipo de parámetro
HEAD Token String header
POST DatosAnulacion object body
46

Trama que recibe Trama de respuesta
DatosAnulacion: mensaje:
type: object required: true
properties: type: string
rucEmisor:
required: true
type: string
claveAccesoComprobante:
required: true
type: string
idBeneficiario:
required: true
type: string
codigoBeneficio:
required: true
type: string
baseImponible:
required: true
type: number
porcentajeIva:
required: true
type: number
montoIva:
required: true
type: number
montoIvaDevolver:
required: true
type: number
14. Anexos
Se describe a continuación la estructura de los comprobantes electrónicos (no
incluye firma electrónica ni autorización por parte del SRI).
ANEXO 1 - FORMATOS XML VERSIÓN 1.0.0
Para el desarrollo de los XML de cualquier comprobante, se recuerda que los
campos de tipo alfanumérico no deberán contener espacios generados entre sus
caracteres, ya que esto será motivo de error de esquema que puede ocasionar
rechazo del comprobante o falta de respuesta en el envío; por ejemplo:
Error:
<campoAdicional nombre="Dirección">Av. 27 de febrero 1-47 y Av 10 de
Agosto</campoAdicional>
Corrección:
<campoAdicional nombre="Dirección">Av. 27 de febrero 1-47 y Av 10 de
Agosto</campoAdicional>
47

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
FORMATO XML FACTURA

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                          |     |     |              |           |               |
| ---------------------------------------- | --- | --- | ------------ | --------- | ------------- |
|                                          |     |     |              | C A M P O | F O R M A T O |
| <?xml version="1.0" encoding="UTF-8" ?>  |     |     | Obligatorio  | -         | -             |
<factura id="comprobante" version="1.0.0">  Obligatorio  -  -
| <infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ----------------- | --- | --- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1 </ambiente>  |     |     |     | Numérico  | 1   |
| ------------------------ | --- | --- | --- | --------- | --- |
conforme
tabla 4
Obligatorio,
| <tipoEmision>1 </ tipoEmision>  |     |     |     | Numérico  | 1   |
| ------------------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 2
<razonSocial>Distribuidora de Suministros Nacional S.A.</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio
<nombreComercial>Empresa Importadora y Exportadora de Piezas</ nombreComercial >  cuando  Alfanumérico  Max 300
corresponda
| <ruc>1792146739001</ruc>  |     |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2110201101179214673900110020010000000011234567813</claveAcceso>  Numérico  49
conforme
tabla 1
Obligatorio,
| <codDoc>01</codDoc>  |     |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 3
| <estab>002</estab>    |     |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | --- | ------------ | --------- | --- |
| <ptoEmi>001</ptoEmi>  |     |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000001</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Enrique Guerrero Portilla OE1-34 AV. Galo Plaza Lasso</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ------------------ | --- | --- | ------------ | --- | --- |
| <infoFactura>      |     |     | Obligatorio  | -   | -   |
<fechaEmision>21/10/2012</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio
<dirEstablecimiento>Sebastián Moreno S/N Francisco García</ dirEstablecimiento >  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
<contribuyenteEspecial>5368</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
Obligatorio
<obligadoContabilidad>SI</ obligadoContabilidad >  Texto  SI / NO
cuando
corresponda
Obligatorio,
<tipoIdentificacionComprador>04</ tipoIdentificacionComprador >  Numérico  2
conforme
tabla 6
Obligatorio
<guiaRemision>001-001-000000001</guiaRemision>  Numérico  15
cuando
corresponda
< ra z o n S oc ia l C o m p ra d o r> P R U E B A S  S ERVICIO DE RENTAS  Obligatorio  Alfanumérico  Max 300
| IN T E R N A S | < / ra z on S o c ia lC o | m p r ad o r>   |     |     |     |
| -------------- | ------------------------- | --------------- | --- | --- | --- |
<identificacionComprador>1713328506001</ identificacionComprador >  Obligatorio  Alfanumérico  Max 20
Obligatorio,
<direccionComprador>salinas y santiago</direccionComprador>  cuando  Alfanumérico  Max 300
corresponda
<totalSinImpuestos>295000.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>5005.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  |     |     | Obligatorio  | -   | -   |
| -------------------- | --- | --- | ------------ | --- | --- |
| <totalImpuesto>      |     |     | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>3</codigo >  |     |     |     | Numérico  | 1   |
| -------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>3072</ codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 18
<baseImponible>295000.00</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>14750.00</valor >  |     |     | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | --- | --- | ------------ | --------- | ------- |
| </totalImpuesto >         |     |     | Obligatorio  | -         | -       |
| <totalImpuesto>           |     |     | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>2</codigo >  |     |     |     | Numérico  | 1   |
| -------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 16
<codigoPorcentaje>2</ codigoPorcentaje>  Obligatorio,  Numérico  Min 1 Max 4
conforme

48

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
tabla 17
Opcional,
<descuentoAdicional>5.00</descuentoAdicional>  aplica para  Numérico  Max 14
código
impuesto 2.
<baseImponible>309750.00</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>37169.40</valor >  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
| </totalImpuesto >         | Obligatorio  | -         | -       |
| <totalImpuesto>           | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>5</codigo >  | conforme  | Numérico  | 1   |
| -------------------- | --------- | --------- | --- |
tabla 16
Obligatorio,
<codigoPorcentaje>5001</ codigoPorcentaje>  conforme  Numérico  Min 1 Max 4
tabla 18
<baseImponible>12000.00</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>240.00</valor >   | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </totalImpuesto >        | Obligatorio  | -         | -       |
| </totalConImpuestos >    | Obligatorio  | -         | -       |
| <propina>0.00</propina>  | Obligatorio  | Numérico  | Max 14  |
<importeTotal>347159.40</ importeTotal>  Obligatorio  Numérico  Max 14
Obligatorio
| <moneda>DOLAR</moneda>  | cuando  | Alfanumérico  | Max 15  |
| ----------------------- | ------- | ------------- | ------- |
corresponda
| <pagos>  | Obligatorio  | -   | -   |
| -------- | ------------ | --- | --- |
| <pago>   | Obligatorio  | -   |     |

Obligatorio,
| <formaPago>01</formaPago>  |     | Numérico  | 2   |
| -------------------------- | --- | --------- | --- |
conforme
tabla 24
| <total>347159.40</total>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>30<plazo>  |     | Numérico  | Max 14  |
| ----------------- | --- | --------- | ------- |
cuando
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |     | Texto  | Max 10  |
| ---------------------------------- | --- | ------ | ------- |
cuando
corresponda
| </pago>   | Obligatorio  | -   | -   |
| --------- | ------------ | --- | --- |
| </pagos>  | Obligatorio  | -   | -   |
<valorRetIva>10620.00</valorRetIva>  Opcional  Numérico  Max 14
<valorRetRenta>2950.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |
| <detalles>      | Obligatorio  | -   | -   |
| <detalle>       | Obligatorio  | -   | -   |
<codigoPrincipal>125BJC-01</codigoPrincipal >  Obligatorio  Alfanumérico  Max 25
Obligatorio
<codigoAuxiliar>1234D56789-A</codigoAuxiliar>  cuando  Alfanumérico  Max 25
corresponda
<descripcion>CAMIONETA 4X4 DIESEL 3.7</descripcion>  Obligatorio  Alfanumérico  Max 300
| <cantidad>10.00</cantidad>  | Obligatorio  | Numérico  | Max 14  |
| --------------------------- | ------------ | --------- | ------- |
<precioUnitario>300000.00</precioUnitario>  Obligatorio  Numérico  Max 14
<descuento>5000.00</descuento>  Obligatorio  Numérico  Max 14
<precioTotalSinImpuesto>295000.00</ precioTotalSinImpuesto>  Obligatorio  Numérico  Max 14
Obligatorio
| <detallesAdicionales>  | cuando  | -   | -   |
| ---------------------- | ------- | --- | --- |
corresponda
Obligatorio
<detAdicional nombre="Marca Chevrolet" valor="Chevrolet"/>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
<detAdicional nombre="Modelo " valor="2012"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<detAdicional nombre="Chasis" valor="8LDETA03V20003289"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
| </detallesAdicionales>  |     | -   | -   |
| ----------------------- | --- | --- | --- |
cuando
corresponda
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |

49

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|             |              |           |               |
| ----------- | ------------ | --------- | ------------- |
|             |              | C A M P O | F O R M A T O |
| <impuesto>  | Obligatorio  | -         | -             |
Obligatorio,
| <codigo>3</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>3072</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 18
| <tarifa>5</ tarifa>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| -------------------- | ------------ | --------- | ------------ |
<baseImponible>295000.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>14750.00</valor>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </impuesto>              | Obligatorio  | -         | -       |
| <impuesto>               | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>2</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 17
Min 1 Max 4 /
| <tarifa>12</ tarifa>  | Obligatorio  | Numérico  |     |
| --------------------- | ------------ | --------- | --- |
2 enteros, 2
decimales
<baseImponible>309750.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>37170.00</valor>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </impuesto>              | Obligatorio  | -         | -       |
| <impuesto>               | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>5</codigo>  | conforme  | Numérico  | 1   |
| ------------------- | --------- | --------- | --- |
tabla 16
Obligatorio,
<codigoPorcentaje>5001</codigoPorcentaje>  conforme  Numérico  Min 1 Max 4
tabla 18
| <tarifa>0.02</ tarifa>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| ----------------------- | ------------ | --------- | ------------ |
<baseImponible>12000.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>240.00</valor>  | Obligatorio  | Numérico  | Max 14  |
| ---------------------- | ------------ | --------- | ------- |
| </impuesto>            | Obligatorio  | -         | -       |
| </impuestos>           | Obligatorio  | -         | -       |
| <detalle>              | Obligatorio  | -         | -       |
| <detalles>             | Obligatorio  | -         | -       |
Obligatorio
| <infoAdicional>  |     | -   | -   |
| ---------------- | --- | --- | --- |
cuando
corresponda
Obligatorio
<campoAdicional nombre="Codigo Impuesto ISD">4580</campoAdicional>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<campoAdicional nombre="Impuesto ISD">15.42x</campoAdicional>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
| </infoAdicional>  |     | -   | -   |
| ----------------- | --- | --- | --- |
cuando
corresponda
| </factura>  | Obligatorio  | -   | -   |
| ----------- | ------------ | --- | --- |

50

FORMATO XML COMPROBANTE RETENCIÓN

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                          |     |              |           |               |
| ---------------------------------------- | --- | ------------ | --------- | ------------- |
|                                          |     |              | C A M P O | F O R M A T O |
| <?xml version="1.0" encoding="UTF-8" ?>  |     | Obligatorio  | -         | -             |
<comprobanteRetencion id="comprobante" version="1.0.0">  Obligatorio  -  -
| <<     <infoTributaria>  |     | Obligatorio  | -   | -   |
| ------------------------ | --- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1</ambiente>  |     |     | Numérico  | 1   |
| ----------------------- | --- | --- | --------- | --- |
conforme
tabla 4
Obligatorio,
| <tipoEmision>1</ tipoEmision>  |     |     | Numérico  | 1   |
| ------------------------------ | --- | --- | --------- | --- |
conforme
tabla 2
<razonSocial>Distribuidora de Suministros Nacional S.A.</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio
< n o m b r e C o m e rc ia l> E m p r e s a  I m p ortadora y Exportadora de Piezas y Partes de Equipos  Alfanumérico  Max 300
  c u a n d o
| d e  O f ic i n a < | / n o m b re C o m e r c ia l  > | da  |     |     |
| ------------------- | -------------------------------- | --- | --- | --- |
cor r e s p o n
| <ruc>1792146739001</ruc>  |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2410201107179214673900110020010000000011234567815</claveAcceso>  Numérico  49
conforme
tabla 1
Obligatorio,
| <codDoc>07</codDoc>  |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --------- | --- |
conforme
tabla 3
| <estab>002</estab>    |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | ------------ | --------- | --- |
| <ptoEmi>001</ptoEmi>  |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000001</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Enrique Guerrero Portilla OE1-34 AV. GALO PLAZA LASSO</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>    |     | Obligatorio  | -   | -   |
| -------------------- | --- | ------------ | --- | --- |
| <infoCompRetencion>  |     | Obligatorio  | -   | -   |
<fechaEmision>15/01/2012</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio
<dirEstablecimiento>Rodrigo Moreno S/N Francisco García</ dirEstablecimiento >  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
<contribuyenteEspecial>5368</contribuyenteEspecial>  cuando  Alfanumérico  Min 3 Max 13
corresponda
Obligatorio
<obligadoContabilidad>SI</ obligadoContabilidad >  cuando  Texto  SI / NO
corresponda
Obligatorio,
<tipoIdentificacionSujetoRetenido>04</tipoIdentificacionSujetoRetenido>  conforme  Numérico  2
tabla 6
<razonSocialSujetoRetenido>Juan Pablo Chávez Núñez</razonSocialSujetoRetenido>  Obligatorio  Alfanumérico  Max 300
<identificacionSujetoRetenido>1713328506001</identificacionSujetoRetenido>  Obligatorio  Alfanumérico  Max 20
<periodoFiscal>03/2012</periodoFiscal>  Obligatorio  Fecha  mm/aaaa
| </infoCompRetencion>  |     | Obligatorio  | -   | -   |
| --------------------- | --- | ------------ | --- | --- |
| <impuestos>           |     | Obligatorio  | -   | -   |
| <impuesto>            |     | Obligatorio  | -   | -   |
Obligatorio,
| <código>2</código>  |     | conforme tabla  | Numérico  | 1   |
| ------------------- | --- | --------------- | --------- | --- |
19
Obligatorio,
<codigoRetencion>1</codigoRetencion>  conforme tabla  Alfanumérico  Min 1 Max 5
20
<baseImponible>101.94</baseImponible>  Obligatorio  Numérico  Max 14
|                                            |     | Obligatorio,    |           | Min 1 Max 5    |
| ------------------------------------------ | --- | --------------- | --------- | -------------- |
| <porcentajeRetener>30</porcentajeRetener>  |     |                 | Numérico  |                |
|                                            |     | conforme tabla  |           | entre enteros  |
|                                            |     | 20              |           | y decimales    |
<valorRetenido>30.58</valorRetenido>  Obligatorio  Numérico  Max 14
<codDocSustento>01</codDocSustento>  Obligatorio  Numérico  2
<numDocSustento>002001000000001</numDocSustento>  Opcional  Numérico  15

51

ETIQUETAS O TAGS CARACTER
T
C
I
A
PO
M P
D
O
E L
F
O
O
N
R
G
M
IT
A
U
T
D
O
/
Obligatorio
<fechaEmisionDocSustento>20/01/2012</fechaEmisionDocSustento> cuando Fecha dd/mm/aaaa
corresponda
</impuesto> Obligatorio - -
<impuesto> Obligatorio - -
Obligatorio,
<código >1</código> conforme tabla Numérico 1
19
Obligatorio,
<codigoRetencion>323B1</codigoRetencion> conforme tabla Alfanumérico Min 1 Max 5
20
<baseImponible>10904.50</baseImponible> Obligatorio Numérico Max 14
Obligatorio,
<porcentajeRetener>2</porcentajeRetener> conforme tabla Numérico Min 1 Max 5
20
<valorRetenido>218.09</valorRetenido> Obligatorio Numérico Max 14
<codDocSustento>01</codDocSustento> Opcional Numérico 2
<numDocSustento>002001000000001</numDocSustento> Opcional Numérico 15
Obligatorio
<fechaEmisionDocSustento>20/01/2012</fechaEmisionDocSustento> cuando Fecha dd/mm/aaaa
corresponda
</impuesto> Obligatorio - -
<impuesto> Obligatorio - -
Obligatorio,
<código>6</código> conforme tabla Numérico 1
19
Obligatorio,
<codigoRetencion>4580</codigoRetencion> conforme tabla Alfanumérico Min 1 Max 5
20
<baseImponible>2000</baseImponible> Obligatorio Numérico Max 14
Obligatorio,
<porcentajeRetener>5</porcentajeRetener> conforme tabla Numérico Min 1 Max 5
20
<valorRetenido>100</valorRetenido> Obligatorio Numérico Max 14
<codDocSustento>12</codDocSustento> Obligatorio Numérico 2
<numDocSustento>002001000000001</numDocSustento> Opcional Numérico 15
Obligatorio
<fechaEmisionDocSustento>20/01/2012</fechaEmisionDocSustento> cuando Fecha dd/mm/aaaa
corresponda
</impuesto> Obligatorio - -
</impuestos> Obligatorio - -
Obligatorio
<infoAdicional> cuando - -
corresponda
Obligatorio
<campoAdicional nombre="ConvenioDobleTributacion">MA123456</campoAdicional> cuando Alfanumérico Max 300
corresponda
Obligatorio
<campoAdicional nombre="documentoIFIS">BP2010-01-0014</campoAdicional> cuando Alfanumérico Max 300
corresponda
Obligatorio
<campoAdicional nombre="valorpagadoIRsociedaddividendos">20000</campoAdicional> cuando Alfanumérico Max 300
corresponda
Obligatorio
</infoAdicional> cuando - -
corresponda
</comprobanteRetencion> Obligatorio - -
52

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
FORMATO XML GUÍA DE REMISIÓN

|                                          |                   |              | T I PO   D E   | L O N G IT U D   /  |
| ---------------------------------------- | ----------------- | ------------ | -------------- | ------------------- |
|                                          | ETIQUETAS O TAGS  | CARACTER     |                |                     |
|                                          |                   |              | C A M P O      | F O R M A T O       |
| <?xml version="1.0" encoding="UTF-8" ?>  |                   | Obligatorio  | -              | -                   |
<guiaRemision id="comprobante" version="1.0.0">  Obligatorio  -  -
| <infoTributaria>  |     | Obligatorio  | -   | -   |
| ----------------- | --- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1</ambiente>  |     |     | Numérico  | 1   |
| ----------------------- | --- | --- | --------- | --- |
conforme
tabla 4
Obligatorio,
| <tipoEmision>1</ tipoEmision>  |     | conforme  | Numérico  | 1   |
| ------------------------------ | --- | --------- | --------- | --- |
tabla 2
<razonSocial>Distribuidora de Suministros Nacional S.A.</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio
< n o m b r e C o m e rc ia l> E m p r e s a  Importadora y Exportadora de Piezas y Partes de Equipos de  Alfanumérico  Max 300
O fi c in a < /  n o m b re C o m er c i a l >   c u a n d o
cor r e s p o n da
| <ruc>1792146739001</ruc>  |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2110201106179214673900100110020010000000011234567815</claveAcceso>  Numérico  49
conforme
tabla 1
Obligatorio,
| <codDoc>06</codDoc>  |     | conforme  | Numérico  | 2   |
| -------------------- | --- | --------- | --------- | --- |
tabla 3
| <estab>002</estab>    |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | ------------ | --------- | --- |
| <ptoEmi>001</ptoEmi>  |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000001</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Enrique Guerrero Portilla OE1-34 AV. Galo Plaza Lasso</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>   |     | Obligatorio  | -   | -   |
| ------------------- | --- | ------------ | --- | --- |
| <infoGuiaRemision>  |     | Obligatorio  | -   | -   |
Obligatorio
<dirEstablecimiento>Sebastián Moreno S/N Francisco García</ dirEstablecimiento >  Alfanumérico  Max 300
cuando
corresponda
<dirPartida>Av. Eloy Alfaro 34 y Av. Libertad Esq.</dirPartida>  Obligatorio  Alfanumérico  Max 300
<razonSocialTransportista>Transportes S.A.</razonSocialTransportista>  Obligatorio  Alfanumérico  Max 300
Obligatorio,
<tipoIdentificacionTransportista>04</tipoIdentificacionTransportista>  conforme  Numérico  2
tabla 6
<rucTransportista>1796875790001</rucTransportista>  Obligatorio  Alfanumérico  Max 13
Obligatorio
<rise>Contribuyente Regimen Simplificado RISE</rise>  Alfanumérico  Max 40
cuando
corresponda
Obligatorio
<obligadoContabilidad>SI</ obligadoContabilidad >  cuando  Texto  SI / NO
corresponda
Obligatorio
<contribuyenteEspecial>5368</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
<fechaIniTransporte>21/10/2011</fechaIniTransporte>  Obligatorio  Fecha  dd/mm/aaaa
<fechaFinTransporte>22/10/2011</fechaFinTransporte>  Obligatorio  Fecha  dd/mm/aaaa
| <placa>MCL0827</placa>  |     | Obligatorio  | Alfanumérico  | Max 20  |
| ----------------------- | --- | ------------ | ------------- | ------- |
| </infoGuiaRemision>     |     | Obligatorio  | -             | -       |
| <destinatarios>         |     | Obligatorio  | -             | -       |
| <destinatario>          |     | Obligatorio  | -             | -       |
<identificacionDestinatario>1716849140001</identificacionDestinatario>  Obligatorio  Alfanumérico  Max 20
<razonSocialDestinatario>Alvarez Mina John Henry</razonSocialDestinatario>  Obligatorio  Alfanumérico  Max 300
<dirDestinatario>Av. Simón Bolívar S/N Intercambiador</dirDestinatario>  Obligatorio  Alfanumérico  Max 300
<motivoTraslado>Venta de Maquinaria de Impresión</motivoTraslado>  Obligatorio  Alfanumérico  Max 300
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico>  Alfanumérico  Max 20
cuando
corresponda
Obligatorio
| <codEstabDestino>001</codEstabDestino>  |     | cuando  | Numérico  | 3   |
| --------------------------------------- | --- | ------- | --------- | --- |
corresponda
Obligatorio
<ruta>Quito – Cayambe - Otavalo</ruta>  Alfanumérico  Max 300
cuando
corresponda

53

ETIQUETAS O TAGS CARACTER
T
C
I
A
PO
M P
D
O
E L
F
O
O
N
R
G
M
IT
A
U
T
D
O
/
Obligatorio
cuando
<codDocSustento>01</codDocSustento> corresponda, Numérico 2
conforme tabla
3
Obligatorio
<numDocSustento>002-001-000000001</numDocSustento> cuando Numérico 15
corresponda
Obligatorio
<numAutDocSustento>2110201116302517921467390011234567891</numAutDocSustento> cuando Numérico 10 o 37 o 49
corresponda
Obligatorio
<fechaEmisionDocSustento>21/10/2011</fechaEmisionDocSustento> cuando Fecha dd/mm/aaaa
corresponda
<detalles> Obligatorio - -
<detalle> Obligatorio - -
<codigoInterno>125BJC-01</ codigoInterno > Opcional11 Alfanumérico Max 25
Obligatorio
<codigoAdicional>1234D56789-A</codigoAdicional> cuando Alfanumérico Max 25
corresponda
<descripcion>CAMIONETA 4X4 DIESEL 3.7</descripcion> Obligatorio Alfanumérico Max 300
<cantidad>10.00</cantidad> Obligatorio Numérico Max 14
Obligatorio
<detallesAdicionales> cuando - -
corresponda
Obligatorio
<detAdicional nombre="Marca" valor="Chevrolet"/> cuando Alfanumérico Max 300
corresponda
Obligatorio
<detAdicional nombre="Modelo" valor="2012"/> cuando Alfanumérico Max 300
corresponda
Obligatorio
<detAdicional nombre="Chasis" valor="8LDETA03V20003289"/> cuando Alfanumérico Max 300
corresponda
Obligatorio
</detallesAdicionales> cuando - -
corresponda
</detalle> Obligatorio - -
</detalles> Obligatorio - -
</destinatario> Obligatorio - -
</destinatarios> Obligatorio - -
Obligatorio
<infoAdicional> cuando - -
corresponda
Obligatorio
<campoAdicional nombre="TELEFONO">098568541</campoAdicional> cuando Alfanumérico Max 300
corresponda
Obligatorio
<campoAdicional nombre="E-MAIL">info@organizacion.com</campoAdicional> cuando Alfanumérico Max 300
corresponda
Obligatorio
<
U
c
n
a
iv
m
e
p
r
o
s
A
o
d
<
i
/
c
c
i
a
o
m
na
p
l
o
n
A
o
d
m
ic
b
io
re
n
=
a
"
l>
S UCURSAL 03">Guayaquil–12 de octubre y
cor
c
r
u
e
a
s
n
p
d
o
o
n da
Alfanumérico Max 300
Obligatorio
</infoAdicional> cuando - -
corresponda
</guiaRemision> Obligatorio - -
11 Reglamento de Comprobantes de Venta, Retención y Documentos Complementarios. - Artículo 19, numeral 2: Descripción o concepto del
bien transferido o del servicio prestado, indicando la cantidad y unidad de medida, cuando proceda. Tratándose de bienes que están
identificados mediante códigos, número de serie o número de motor, deberá consignarse obligatoriamente dicha información.
54

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
FORMATO XML NOTA DE CRÉDITO

Nota: La tarifa de IVA corresponderá a la fecha de emisión del documento de
sustento.

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                          |     |     |              | C A M P O   | F O R M A T O   |
| ---------------------------------------- | --- | --- | ------------ | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8" ?>  |     |     | Obligatorio  | -           | -               |
<notaCredito id="comprobante" version="1.0.0">  Obligatorio  -  -
| <infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ----------------- | --- | --- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1</ambiente>  |     |     |     | Numérico  | 1   |
| ----------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 4
Obligatorio,
| <tipoEmision>1</ tipoEmision>  |     |     |     | Numérico  | 1   |
| ------------------------------ | --- | --- | --- | --------- | --- |
conforme
tabla 2
<razonSocial>Distribuidora de Suministros Nacional S.A.</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio
<nombreComercial>Empresa Importadora y Exportadora de Piezas </ nombreComercial >  cuando  Alfanumérico  Max 300
corresponda
| <ruc>1792146739001001</ruc>  |     |     | Obligatorio  | Numérico  | 13  |
| ---------------------------- | --- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2110201104179214673900110020010000000011234567812</claveAcceso>  Numérico  49
conforme
tabla 1
Obligatorio,
| <codDoc>04</codDoc>  |     |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 3
| <estab>002</estab>    |     |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | --- | ------------ | --------- | --- |
| <ptoEmi>001</ptoEmi>  |     |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000001</secuencial>  Obligatorio  Numérico  9
< d i rM a tr iz > E N R IQ U E GUERRERO PORTILLA OE1-34 AV. GALO PLAZA  Obligatorio  Alfanumérico  Max 300
| L A S S O < /d     | i rM a tr iz>   |     |              |     |     |
| ------------------ | --------------- | --- | ------------ | --- | --- |
| </infoTributaria>  |                 |     | Obligatorio  | -   | -   |
| <infoNotaCredito>  |                 |     | Obligatorio  | -   | -   |
<fechaEmision>21/10/2012</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio
<dirEstablecimiento>Sebastián Moreno S/N Francisco García</ dirEstablecimiento>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio,
<tipoIdentificacionComprador>04</ tipoIdentificacionComprador >  conforme  Numérico  2
tabla 6
< ra z o n S oc ia l C o m p ra d o r> P R U E B A S  S ERVICIO DERENTAS  Obligatorio  Alfanumérico  Max 300
| IN T E R N A S | < / ra z on S o c ia lC o | m p r ad o r>   |     |     |     |
| -------------- | ------------------------- | --------------- | --- | --- | --- |
<identificacionComprador>1713328506001</identificacionComprador>  Obligatorio  Alfanumérico  Max 20
Obligatorio
<contribuyenteEspecial>5368</contribuyenteEspecial>  cuando  Alfanumérico  Min 3 Max 13
corresponda
Obligatorio
<obligadoContabilidad>SI</ obligadoContabilidad>  cuando  Texto  SI / NO
corresponda
Obligatorio
<rise>Contribuyente Régimen Simplificado RISE</rise>  cuando  Alfanumérico  Max 40
corresponda
Obligatorio,
<codDocModificado>01</codDocModificado>  conforme  Numérico  2
tabla 3
<numDocModificado>002-001-000000001</numDocModificado>  Obligatorio  Numérico  15
<fechaEmisionDocSustento>21/10/2011</fechaEmisionDocSustento>  Obligatorio  Fecha  dd/mm/aaaa
<totalSinImpuestos>295000.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<valorModificacion>346920.00</valorModificacion>  Obligatorio  Numérico  Max 14
Obligatorio
| <moneda>DOLAR</moneda>  |     |     | cuando  | Alfanumérico  | Max 15  |
| ----------------------- | --- | --- | ------- | ------------- | ------- |
corresponda

55

|     |     | T I PO   D E   | L O N G IT U D   /  |
| --- | --- | -------------- | ------------------- |
ETIQUETAS O TAGS  CARACTER
|                      |              | C A M P O   | F O R M A T O   |
| -------------------- | ------------ | ----------- | --------------- |
| <totalConImpuestos>  | Obligatorio  | -           | -               |
| <totalImpuesto>      | Obligatorio  | -           | -               |
Obligatorio,
| <codigo>3</codigo >  |     | Numérico  | 1   |
| -------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>3072</ codigoPorcentaje>  conforme  Numérico  Min 1 Max 4
tabla 18
<baseImponible>295000.00</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>14750.00</valor >  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
| </totalImpuesto >         | Obligatorio  | -         | -       |
| <totalImpuesto>           | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>2</codigo >  | conforme  | Numérico  | 1   |
| -------------------- | --------- | --------- | --- |
tabla 16
Obligatorio,
<codigoPorcentaje>2</ codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 17
<baseImponible>339250.25</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>37170.00</valor >  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
| </totalImpuesto >         | Obligatorio  | -         | -       |
| </totalConImpuestos >     | Obligatorio  | -         | -       |
<motivo>DEVOLUCIÓN</motivo>  Obligatorio  Alfanumérico  Max 300
| </infoNotaCredito>  | Obligatorio  | -   | -   |
| ------------------- | ------------ | --- | --- |
| <detalles>          | Obligatorio  | -   | -   |
| <detalle>           | Obligatorio  | -   | -   |
<codigoInterno>125BJC-01</codigoInterno >  Opcional  Alfanumérico  Max 25
Obligatorio
<codigoAdicional>1234D56789-A</codigoAdicional>  Alfanumérico  Max 25
cuando
corresponda
<descripcion>CAMIONETA 4X4 DIESEL 3.7</descripcion>  Obligatorio  Alfanumérico  Max 300
| <cantidad>10.00</cantidad>  | Obligatorio  | Numérico  | Max 14  |
| --------------------------- | ------------ | --------- | ------- |
<precioUnitario>30000.00</precioUnitario>  Obligatorio  Numérico  Max 14
Obligatorio
| <descuento>5000.00</descuento>  |     | Numérico  | Max 14  |
| ------------------------------- | --- | --------- | ------- |
cuando
corresponda
<precioTotalSinImpuesto>295000.00</ precioTotalSinImpuesto>  Obligatorio  Numérico  Max 14
Obligatorio
<detallesAdicionales>
|     | cuando  |     |     |
| --- | ------- | --- | --- |
corresponda
Obligatorio
<detAdicional nombre="Marca" valor="Chevrolet"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<detAdicional nombre="Modelo" valor="2012"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<detAdicional nombre="Chasis" valor="8LDETA03V20003289"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
</detallesAdicionales>
|     | cuando  |     |     |
| --- | ------- | --- | --- |
corresponda
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |
| <impuesto>   | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>3</codigo>  | conforme  | Numérico  | 1   |
| ------------------- | --------- | --------- | --- |
tabla 16

56

|     |     | T I PO   D E |   L O N G IT U D   /  |
| --- | --- | ------------ | --------------------- |
ETIQUETAS O TAGS  CARACTER
|     |     | C A M P O |   F O R M A T O   |
| --- | --- | --------- | ----------------- |
Obligatorio,
<codigoPorcentaje>3072</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 18
Obligatorio
| <tarifa>5</ tarifa>  | cuando  | Numérico  | Min 1 Max 3  |
| -------------------- | ------- | --------- | ------------ |
corresponda
<baseImponible>295000.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>14750.00</valor>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </impuesto>              | Obligatorio  | -         | -       |
| <impuesto>               | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>2</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  conforme  Numérico  Min 1 Max 4
tabla 17
|                       | Obligatorio  |           | Min 1 Max 4     |
| --------------------- | ------------ | --------- | --------------- |
| <tarifa>12</ tarifa>  |              | Numérico  |                 |
|                       | cuando       |           | / 2 enteros, 2  |
|                       | corresponda  |           | decimales       |
<baseImponible>309750.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>37170.00</valor>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </impuesto>              | Obligatorio  | -         | -       |
| </impuestos>             | Obligatorio  | -         | -       |
| <detalle>                | Obligatorio  | -         | -       |
| <detalles>               | Obligatorio  | -         | -       |
Obligatorio
| <infoAdicional>  | cuando  | -   | -   |
| ---------------- | ------- | --- | --- |
corresponda
Obligatorio
<campoAdicional nombre="E-MAIL">info@organizacion.com</campoAdicional>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
| </infoAdicional>  | cuando  | -   | -   |
| ----------------- | ------- | --- | --- |
corresponda
| </notaCredito>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |

57

FORMATO XML NOTA DE DÉBITO

Nota: la tarifa de IVA corresponderá a la fecha de emisión del documento de
sustento.

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>  Obligatorio  -  -
<notaDebito version="1.0.0" id="comprobante">  Obligatorio  -  -
| <infoTributaria>  | Obligatorio  | -   | -   |
| ----------------- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1</ambiente>  | conforme  | Numérico  | 1   |
| ----------------------- | --------- | --------- | --- |
tabla 4
Obligatorio,
| <tipoEmision>1</tipoEmision>  | conforme  | Numérico  | 1   |
| ----------------------------- | --------- | --------- | --- |
tabla 2
<razonSocial>PRUEBA</razonSocial>  Obligatorio  Alfanumérico  Max 300
<nombreComercial>PRUEBA 2</nombreComercial>  O b lig a t o ri o
|     |               | Alfanumérico  | Max 300  |
| --- | ------------- | ------------- | -------- |
|     | c u a n d o   |               |          |
corresponda
| <ruc>1760013210001</ruc>  | Obligatorio  | Numérico  | 13  |
| ------------------------- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2103201605176001321000110010010000000011234567814</claveAcceso>  conforme  Numérico  49
tabla 1
Obligatorio,
| <codDoc>05</codDoc>  | conforme  | Numérico  | 2   |
| -------------------- | --------- | --------- | --- |
tabla 3
| <estab>001</estab>    | Obligatorio  | Numérico  | 3   |
| --------------------- | ------------ | --------- | --- |
| <ptoEmi>001</ptoEmi>  | Obligatorio  | Numérico  | 3   |
<secuencial>000000001</secuencial>  Obligatorio  Numérico  9
<dirMatriz>SALINAS</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  | Obligatorio  | -   | -   |
| ------------------ | ------------ | --- | --- |
| <infoNotaDebito>   | Obligatorio  | -   | -   |
<fechaEmision>21/03/2016</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio
<dirEstablecimiento>PÁEZ</dirEstablecimiento>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<tipoIdentificacionComprador>04</tipoIdentificacionComprador>  Alfanumérico  Max 20
conforme
tabla 6
<razonSocialComprador>PRUEBA SRI</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionComprador>1713328506001</identificacionComprador>  Obligatorio  Alfanumérico  Max 20
Obligatorio
<contribuyenteEspecial>12345</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
Obligatorio
<obligadoContabilidad>SI</obligadoContabilidad>  Texto  SI / NO
cuando
corresponda
Obligatorio,
| <codDocModificado>01</codDocModificado>  |     | Numérico  | 2   |
| ---------------------------------------- | --- | --------- | --- |
conforme
tabla 3
<numDocModificado>001-001-112312315</numDocModificado>  Obligatorio  Numérico  15
<fechaEmisionDocSustento>21/03/2016</fechaEmisionDocSustento>  Obligatorio  Fecha  dd/mm/aaaa
<totalSinImpuestos>50.0</totalSinImpuestos>  Obligatorio  Numérico  Max 14
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |
| <impuesto>   | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 17

58

|     |                   |           |                |                     |
| --- | ----------------- | --------- | -------------- | ------------------- |
|     |                   |           | T I PO   D E   | L O N G IT U D   /  |
|     | ETIQUETAS O TAGS  | CARACTER  |                |                     |
|     |                   |           | C A M P O      | F O R M A T O       |
Min 1 Max 4
| <tarifa>12.00</tarifa>  |     | Obligatorio  | Numérico  |     |
| ----------------------- | --- | ------------ | --------- | --- |
/ 2 enteros, 2
decimales
<baseImponible>50.0</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>  |     | Obligatorio  | Numérico  | Max 14  |
| -------------------- | --- | ------------ | --------- | ------- |
| </impuesto>          |     | Obligatorio  | -         | -       |
| </impuestos>         |     | Obligatorio  | -         | -       |
<valorTotal>56.00</valorTotal>  Obligatorio  Numérico  Max 14
| <pagos>  |     | Obligatorio  | -   | -   |
| -------- | --- | ------------ | --- | --- |
| <pago>   |     | Obligatorio  | -   | -   |
Obligatorio,
| <formaPago>17</formaPago>  |     | conforme  | Numérico  | 2   |
| -------------------------- | --- | --------- | --------- | --- |
tabla 24
| <total>56,00</total>  |     | Obligatorio  | Numérico  | Max 14  |
| --------------------- | --- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>15<plazo>  |     | cuando  | Numérico  | Max 14  |
| ----------------- | --- | ------- | --------- | ------- |
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |     |         | Texto  |         |
| ---------------------------------- | --- | ------- | ------ | ------- |
|                                    |     | cuando  |        | Max 10  |
corresponda
| </pago>            |     | Obligatorio  | -   | -   |
| ------------------ | --- | ------------ | --- | --- |
| </pagos>           |     | Obligatorio  | -   | -   |
| </infoNotaDebito>  |     | Obligatorio  | -   | -   |
| <motivos>          |     | Obligatorio  | -   | -   |
| <motivo>           |     | Obligatorio  | -   | -   |
<razon>Interés por mora</razon>  Obligatorio  Alfanumérico  Max 300
| <valor>50.00</valor>  |     | Obligatorio  | Alfanumérico  | Max 300  |
| --------------------- | --- | ------------ | ------------- | -------- |
| </motivo>             |     | Obligatorio  | -             | -        |
| </motivos>            |     | Obligatorio  | -             | -        |
| <infoAdicional>       |     | Obligatorio  | -             | -        |
Obligatorio
<campoAdicional nombre="Dirección">AMAZONAS S/N ROCA</campoAdicional>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<campoAdicional nombre="Email">prueba@sri.gob.ec</campoAdicional>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
<campoAdicional nombre="Teléfono">0222222222222 ext. 3322</campoAdicional>  cuando  Alfanumérico  Max 300
corresponda
| </infoAdicional>  |     | Obligatorio  | -   | -   |
| ----------------- | --- | ------------ | --- | --- |
| </notaDebito>     |     | Obligatorio  | -   | -   |

59

ANEXO 2 - FORMATO DE
REPRESENTACIONES IMPRESAS DE
DOCUMENTOS ELECTRÓNICOS (RIDE)
FACTURA
Nota:
•
Para los contribuyentes comercializadores de derivados de petróleo, y, Editores, Distribuidores y Voceadores que
participan en la comercialización de periódicos y/o revistas, deberán ajustar el formato RIDE de acuerdo con la
información contenida en el comprobante electrónico con respecto a las retenciones. Se podrán imprimir datos
adicionales en el RIDE conforme lo requiera el contribuyente.
•
Los RIDE que se descarguen del portal web del SRI contendrán hora y fecha de autorización, dicha información no
es obligatoria registrarla en el RIDE generado por los emisores de comprobantes electrónicos.
•
El número de la clave de acceso corresponde al número de autorización.
60

•
Conforme consta en el numeral 9.20, el código de barras es opcional.
•
El campo “Subtotal tarifa especial” corresponde a la tarifa de IVA por actividades de turismo.
•
Los contribuyentes podrán visualizar solo los subtotales que fueron llenos.
NOTA DE CRÉDITO
61

NOTA DE DÉBITO
62

COMPROBANTE DE RETENCIÓN
63

GUÍA DE REMISIÓN
64

|              |             |             |                |     |
| ------------ | ----------- | ----------- | -------------- | --- |
| LIQUIDACIÓN  | DE  COMPRA  | DE  BIENES  | Y  PRESTACIÓN  | DE  |
SERVICIOS

65

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
ANEXO 3 - FORMATOS XML VERSIÓN 1.1.0

Incluyen el aumento de 2 a 6 decimales en los campos de cantidad y precio unitario
para  quienes  lo  requieran.  En  el  caso  del  formato  de  factura  adicionalmente
contiene información de retenciones de IVA presuntivo e Impuesto a la Renta que
aplica para comercializadores de derivados de petróleo y retención presuntiva de
IVA  a  los  editores,  distribuidores  y  voceadores  que  participan  en  la
comercialización de periódicos y/o revistas.

FORMATO XML FACTURA

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                          |     |     |              | C A M P O   | F O R M A T O   |
| ---------------------------------------- | --- | --- | ------------ | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8" ?>  |     |     | Obligatorio  | -           | -               |
<factura id="comprobante" version="1.1.0">  Obligatorio  -  -
| <infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ----------------- | --- | --- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1 </ambiente>  |     |     |     | Numérico  | 1   |
| ------------------------ | --- | --- | --- | --------- | --- |
conforme
tabla 4
Obligatorio,
| <tipoEmision>1 </ tipoEmision>  |     |     |     | Numérico  | 1   |
| ------------------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 2
| < r a z on S o ci | a l> E M P R E S A  P U | B L I C A DE HIDROCARBUROS DEL ECUADOR EP  |              |               |          |
| ----------------- | ----------------------- | ------------------------------------------ | ------------ | ------------- | -------- |
|                   |                         |                                            | Obligatorio  | Alfanumérico  | Max 300  |
| P E T R O E C     | U A D O R < / ra z on S | o ci a l>                                  |              |               |          |
< n o m b re C o m e rc ia l> E M P R E S A  P U B L IC A  DE HIDROCARBUROS DEL ECUADOR EP  Obligatorio
|               |                          |                   | c u a n d o   | Alfanumérico  | Max 300  |
| ------------- | ------------------------ | ----------------- | ------------- | ------------- | -------- |
| P E T R O E C | U A D O R < / n o m b re | C o m e rc ia l > | da            |               |          |
cor r e s p o n
| <ruc>1768153530001</ruc>  |     |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>0403201301176815353000110015010000000081234567816</claveAcceso>  conforme  Numérico  49
tabla 1
Obligatorio,
| <codDoc>01</codDoc>  |     |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 3
| <estab>001</estab>    |     |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | --- | ------------ | --------- | --- |
| <ptoEmi>501</ptoEmi>  |     |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Alpallana</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ------------------ | --- | --- | ------------ | --- | --- |
| <infoFactura>      |     |     | Obligatorio  | -   | -   |
<fechaEmision>04/03/2013</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio
<dirEstablecimiento>Alpallana</ dirEstablecimiento >  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<contribuyenteEspecial>5368</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
Obligatorio
<obligadoContabilidad>SI</ obligadoContabilidad >  cuando  Texto  SI / NO
corresponda
Obligatorio,
<tipoIdentificacionComprador>04</ tipoIdentificacionComprador >  conforme  Numérico  2
tabla 6
Obligatorio
<guiaRemision>001-001-000000001</guiaRemision>  cuando  Numérico  15
corresponda
< ra z o n S oc ia l C o m p ra d o r> P R U E B A S  S ERVICIO DERENTAS  Obligatorio  Alfanumérico  Max 300
| IN T E R N A S | < / ra z on S o c ia lC o | m p r ad o r>   |     |     |     |
| -------------- | ------------------------- | --------------- | --- | --- | --- |
<identificacionComprador>1760013210001</ identificacionComprador >  Obligatorio  Alfanumérico  Max 20
Obligatorio,
<direccionComprador>salinas y santiago</direccionComprador>  cuando  Alfanumérico  Max 300
corresponda
<totalSinImpuestos>64.94</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>5.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  |     |     | Obligatorio  | -   | -   |
| -------------------- | --- | --- | ------------ | --- | --- |

66

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                  |              |           |               |
| ---------------- | ------------ | --------- | ------------- |
|                  |              | C A M P O | F O R M A T O |
| <totalImpuesto>  | Obligatorio  | -         | -             |
Obligatorio,
| <codigo>2</codigo >  |     | Numérico  | 1   |
| -------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>2</ codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 17
Opcional,
<descuentoAdicional>5.00</descuentoAdicional>  aplica para  Numérico  Max 14
código
impuesto 2.
<baseImponible>68.19</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>7.58</valor >  | Obligatorio  | Numérico  | Max 14  |
| --------------------- | ------------ | --------- | ------- |
| </totalImpuesto >     | Obligatorio  | -         | -       |
| <totalImpuesto>       | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>3</codigo >  | conforme  | Numérico  | 1   |
| -------------------- | --------- | --------- | --- |
tabla 16
Obligatorio,
<codigoPorcentaje>3072</ codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 18
<baseImponible>64.94</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>3.25</valor >     | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </totalImpuesto >        | Obligatorio  | -         | -       |
| </totalConImpuestos >    | Obligatorio  | -         | -       |
| <propina>0.00</propina>  | Obligatorio  | Numérico  | Max 14  |
<importeTotal>73.09</ importeTotal>  Obligatorio  Numérico  Max 14
Obligatorio
| <moneda>DOLAR</moneda>  |     | Alfanumérico  | Max 15  |
| ----------------------- | --- | ------------- | ------- |
cuando
corresponda
| <pagos>  | Obligatorio  | -   | -   |
| -------- | ------------ | --- | --- |
| <pago>   | Obligatorio  | -   |     |
Obligatorio,
| <formaPago>21</formaPago>  |           | Numérico  |     |
| -------------------------- | --------- | --------- | --- |
|                            | conforme  |           | 2   |
tabla 24
| <total>73,09</total>  | Obligatorio  | Numérico  |     |
| --------------------- | ------------ | --------- | --- |
Max 14
Obligatorio,
| <plazo>60<plazo>  |         | Numérico  |         |
| ----------------- | ------- | --------- | ------- |
|                   | cuando  |           | Max 14  |
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |         | Texto  |         |
| ---------------------------------- | ------- | ------ | ------- |
|                                    | cuando  |        | Max 10  |
corresponda
| </pago>                          | Obligatorio  | -         | -       |
| -------------------------------- | ------------ | --------- | ------- |
| </pagos>                         | Obligatorio  |           |         |
|                                  |              |           |         |
| <valorRetIva>0.00</valorRetIva>  | Opcional     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |
| <detalles>      | Obligatorio  | -   | -   |
| <detalle>       | Obligatorio  | -   | -   |
<codigoPrincipal>125BJC-01</codigoPrincipal >  Obligatorio  Alfanumérico  Max 25
Obligatorio
<codigoAuxiliar>1234D56789-A</codigoAuxiliar>  Alfanumérico  Max 25
cuando
corresponda
<descripcion>DERIVADOS PETRÓLEO</descripcion>  Obligatorio  Alfanumérico  Max 300
Max 18,
| <cantidad>2.542563</cantidad>  | Obligatorio  | Numérico  |     |
| ------------------------------ | ------------ | --------- | --- |
hasta 6
decimales
Max 18,
<precioUnitario>25.542365</precioUnitario>  Obligatorio  Numérico
hasta 6
decimales
| <descuento>0.00</descuento>  | Obligatorio  | Numérico  | Max 14  |
| ---------------------------- | ------------ | --------- | ------- |
<precioTotalSinImpuesto>64.94</ precioTotalSinImpuesto>  Obligatorio  Numérico  Max 14
Obligatorio
| <detallesAdicionales>  |     | -   | -   |
| ---------------------- | --- | --- | --- |
cuando
corresponda
Obligatorio
<detAdicional nombre="ABCD" valor="EFGH"/>  Alfanumérico  Max 300
cuando
corresponda
<detAdicional nombre="ABCD " valor="EFGH"/>  Obligatorio  Alfanumérico  Max 300
cuando

67

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
corresponda
Obligatorio
<detAdicional nombre="ABCD" valor="EFGH"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
| </detallesAdicionales>  |     | -   | -   |
| ----------------------- | --- | --- | --- |
cuando
corresponda
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |
| <impuesto>   | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 17
Min 1 Max 4
| <tarifa>12</ tarifa>  | Obligatorio  | Numérico  | / 2 enteros, 2  |
| --------------------- | ------------ | --------- | --------------- |
decimales
<baseImponible>68.19</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>8.18</valor>  | Obligatorio  | Numérico  | Max 14  |
| -------------------- | ------------ | --------- | ------- |
| </impuesto>          | Obligatorio  | -         | -       |
| <impuesto>           | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>3</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>3072</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 18
| <tarifa>5</ tarifa>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| -------------------- | ------------ | --------- | ------------ |
<baseImponible>64.94</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>3.25</valor>  | Obligatorio  | Numérico  | Max 14  |
| -------------------- | ------------ | --------- | ------- |
| </impuesto>          | Obligatorio  | -         | -       |
| </impuestos>         | Obligatorio  | -         | -       |
| </detalle>           | Obligatorio  | -         | -       |
| </detalles>          | Obligatorio  | -         | -       |
Obligatorio
| <retenciones>  |     | -   | -   |
| -------------- | --- | --- | --- |
cuando
corresponda
Obligatorio
| <retencion>  |     | -   | -   |
| ------------ | --- | --- | --- |
cuando
corresponda
Obligatorio
cuando
| <codigo>4</codigo>  | corresponda,  | Numérico  | 1   |
| ------------------- | ------------- | --------- | --- |
conforme
tabla 22
Obligatorio
cuando
<codigoPorcentaje>327</codigoPorcentaje>  corresponda,  Numérico  Min 1 Max 3
conforme
tabla 23
Min 1 Max 5 /
Obligatorio
| <tarifa>0.20</tarifa>  |     | Numérico  | 3 enteros,  |
| ---------------------- | --- | --------- | ----------- |
cuando
|     | corresponda  |     | d os   |
| --- | ------------ | --- | ------ |
dec im a les
|                      | Obligatorio  |           | Max 14 /12  |
| -------------------- | ------------ | --------- | ----------- |
| <valor>0.13</valor>  | cuando       | Numérico  | enteros, 2  |
|                      | corresponda  |           | decimales   |
Obligatorio
| </retencion>  | cuando  | -   | -   |
| ------------- | ------- | --- | --- |
corresponda
Obligatorio
| <retencion>  | cuando  | -   | -   |
| ------------ | ------- | --- | --- |
corresponda
Obligatorio
cuando
| <codigo>4</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
corresponda,
conforme
tabla 22
Obligatorio
cuando
<codigoPorcentaje>328</codigoPorcentaje>  Numérico  Min 1 Max 3
corresponda,
conforme
tabla 23

68

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                        |              |           |                |
| ---------------------- | ------------ | --------- | -------------- |
|                        |              | C A M P O | F O R M A T O  |
|                        | Obligatorio  |           | Min 1 Max 5 /  |
| <tarifa>0.30</tarifa>  |              | Numérico  | 3 enteros,     |
cuando
|     | corresponda  |     | d os   |
| --- | ------------ | --- | ------ |
dec im a les
|                      | Obligatorio  |           | Max 14 /12  |
| -------------------- | ------------ | --------- | ----------- |
| <valor>0.19</valor>  |              | Numérico  |             |
|                      | cuando       |           | enteros, 2  |
|                      | corresponda  |           | decimales   |
Obligatorio
| </retencion>  |     | -   | -   |
| ------------- | --- | --- | --- |
cuando
corresponda
Obligatorio
| <retencion>  |     | -   | -   |
| ------------ | --- | --- | --- |
cuando
corresponda
Obligatorio
cuando
| <codigo>4</codigo>  | corresponda,  | Numérico  | 1   |
| ------------------- | ------------- | --------- | --- |
conforme
tabla 22
Obligatorio
cuando
<codigoPorcentaje>3</codigoPorcentaje>  corresponda,  Numérico  Min 1 Max 3
conforme
tabla 23
Min 1 Max 5 /
Obligatorio
| <tarifa>1</tarifa>  |              | Numérico  | 3 enteros,  |
| ------------------- | ------------ | --------- | ----------- |
|                     | cuando       |           | d os        |
|                     | corresponda  |           | les         |
dec im a
|                      | Obligatorio  |           | Max 14 /12  |
| -------------------- | ------------ | --------- | ----------- |
| <valor>2.00</valor>  | cuando       | Numérico  | enteros, 2  |
|                      | corresponda  |           | decimales   |
Obligatorio
| </retencion>  | cuando  | -   | -   |
| ------------- | ------- | --- | --- |
corresponda
Obligatorio
| </retenciones>  | cuando  | -   | -   |
| --------------- | ------- | --- | --- |
corresponda
Obligatorio
| <infoAdicional>  | cuando  | -   | -   |
| ---------------- | ------- | --- | --- |
corresponda
Obligatorio
<campoAdicional nombre="Codigo Impuesto ISD">4580</campoAdicional>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<campoAdicional nombre="Impuesto ISD">15.42x</campoAdicional>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
| </infoAdicional>  |     | -   | -   |
| ----------------- | --- | --- | --- |
cuando
corresponda
| </factura>  | Obligatorio  | -   | -   |
| ----------- | ------------ | --- | --- |

69

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
FORMATO XML GUÍA DE REMISIÓN

|                                          |                   |              | T I PO   D E   | L O N G IT U D   /  |
| ---------------------------------------- | ----------------- | ------------ | -------------- | ------------------- |
|                                          | ETIQUETAS O TAGS  | CARACTER     |                |                     |
|                                          |                   |              | C A M P O      | F O R M A T O       |
| <?xml version="1.0" encoding="UTF-8" ?>  |                   | Obligatorio  | -              | -                   |
<guiaRemision id="comprobante" version="1.1.0">  Obligatorio  -  -
| <infoTributaria>  |     | Obligatorio  | -   | -   |
| ----------------- | --- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1</ambiente>  |     | conforme  | Numérico  | 1   |
| ----------------------- | --- | --------- | --------- | --- |
tabla 4
Obligatorio,
| <tipoEmision>1</ tipoEmision>  |     | conforme  | Numérico  | 1   |
| ------------------------------ | --- | --------- | --------- | --- |
tabla 2
< r a z on S o ci a l>  E M P R E S A  P U B L I C A DE HIDROCARBUROS DEL ECUADOR EP  Obligatorio  Alfanumérico  Max 300

| P E T R O E C U A D O R  < / ra z on S o | ci a l> |     |     |     |
| ---------------------------------------- | ------- | --- | --- | --- |
Obligatorio
< n o m b re C o m e rc ia l>  E M P R E S A  P U B L IC A  DE HIDROCARBUROS DEL ECUADOR EP  Alfanumérico  Max 300
|     |     | c u a n d o   |     |     |
| --- | --- | ------------- | --- | --- |
P E T R O E C U A D O R  < / n o m b re C o m e rc ia l > da
cor r e s p o n
| <ruc>1760013210001</ruc>  |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>0603201306176001321000110015010000000081234567812</claveAcceso>  Numérico  49
conforme
tabla 1
Obligatorio,
| <codDoc>06</codDoc>  |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --------- | --- |
conforme
tabla 3
| <estab>001</estab>    |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | ------------ | --------- | --- |
| <ptoEmi>501</ptoEmi>  |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>ALPALLANA</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>   |     | Obligatorio  | -   | -   |
| ------------------- | --- | ------------ | --- | --- |
| <infoGuiaRemision>  |     | Obligatorio  | -   | -   |
Obligatorio
<dirEstablecimiento>ALPALLANA</ dirEstablecimiento >  cuando  Alfanumérico  Max 300
corresponda
<dirPartida>Av. Eloy Alfaro 34 y Av. Libertad Esq.</dirPartida>  Obligatorio  Alfanumérico  Max 300
<razonSocialTransportista>Transportes S.A.</razonSocialTransportista>  Obligatorio  Alfanumérico  Max 300
Obligatorio,
<tipoIdentificacionTransportista>04</tipoIdentificacionTransportista>  conforme  Numérico  2
tabla 6
<rucTransportista>1796875790001</rucTransportista>  Obligatorio  Alfanumérico  Max 13
Obligatorio
<rise>Contribuyente Regimen Simplificado RISE</rise>  Alfanumérico  Max 40
cuando
corresponda
Obligatorio
<obligadoContabilidad>SI</ obligadoContabilidad >  Texto  SI / NO
cuando
corresponda
Obligatorio
<contribuyenteEspecial>5368</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
<fechaIniTransporte>06/03/2013</fechaIniTransporte>  Obligatorio  Fecha  dd/mm/aaaa
<fechaFinTransporte>06/03/2013</fechaFinTransporte>  Obligatorio  Fecha  dd/mm/aaaa
| <placa>MCL0827</placa>  |     | Obligatorio  | Alfanumérico  | Max 20  |
| ----------------------- | --- | ------------ | ------------- | ------- |
| </infoGuiaRemision>     |     | Obligatorio  | -             | -       |
| <destinatarios>         |     | Obligatorio  | -             | -       |
| <destinatario>          |     | Obligatorio  | -             | -       |
<identificacionDestinatario>1716849140001</identificacionDestinatario>  Obligatorio  Alfanumérico  Max 20
<razonSocialDestinatario>Alvarez Mina John Henry</razonSocialDestinatario>  Obligatorio  Alfanumérico  Max 300
<dirDestinatario>Av. Simón Bolívar S/N Intercambiador</dirDestinatario>  Obligatorio  Alfanumérico  Max 300
<motivoTraslado>Venta de Maquinaria de Impresión</motivoTraslado>  Obligatorio  Alfanumérico  Max 300
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico>  Alfanumérico  Max 20
cuando
corresponda
Obligatorio
| <codEstabDestino>001</codEstabDestino>  |     |     | Numérico  | 3   |
| --------------------------------------- | --- | --- | --------- | --- |
cuando
corresponda

70

ETIQUETAS O TAGS CARACTER
T
C
I
A
PO
M P
D
O
E L
F
O
O
N
R
G
M
IT
A
U
T
D
O
/
Obligatorio
<ruta>Quito – Cayambe - Otavalo</ruta> cuando Alfanumérico Max 300
corresponda
Obligatorio
cuando
<codDocSustento>01</codDocSustento> corresponda, Numérico 2
conforme tabla
3
Obligatorio
<numDocSustento>002-001-000000001</numDocSustento> cuando Numérico 15
corresponda
Obligatorio
<numAutDocSustento>211020111630251792146739011234567891</numAutDocSustento> cuando Numérico 10 o 37 o 49
corresponda
Obligatorio
<fechaEmisionDocSustento>21/10/2011</fechaEmisionDocSustento> cuando Fecha dd/mm/aaaa
corresponda
<detalles> Obligatorio - -
<detalle> Obligatorio - -
<codigoInterno>125BJC-01</ codigoInterno > Opcional1 Alfanumérico Max 25
Obligatorio
<codigoAdicional>1234D56789-A</codigoAdicional> cuando Alfanumérico Max 25
corresponda
<descripcion>DIESEL</descripcion> Obligatorio Alfanumérico Max 300
Max 18,
<cantidad>10.254632</cantidad> Obligatorio Numérico hasta 6
decimales
Obligatorio
<detallesAdicionales> cuando - -
corresponda
Obligatorio
<detAdicional nombre="ABCD" valor="EFGH"/> cuando Alfanumérico Max 300
corresponda
Obligatorio
<detAdicional nombre="ABCD" valor="EFGH"/> cuando Alfanumérico Max 300
corresponda
Obligatorio
<detAdicional nombre="ABCD" valor="EFHG"/> cuando Alfanumérico Max 300
corresponda
Obligatorio
</detallesAdicionales> cuando - -
corresponda
</detalle> Obligatorio - -
</detalles> Obligatorio - -
</destinatario> Obligatorio - -
</destinatarios> Obligatorio - -
Obligatorio
<infoAdicional> cuando - -
corresponda
Obligatorio
<campoAdicional nombre="TELEFONO">098568541</campoAdicional> cuando Alfanumérico Max 300
corresponda
Obligatorio
<campoAdicional nombre="E-MAIL">info@organizacion.com</campoAdicional> cuando Alfanumérico Max 300
corresponda
Obligatorio
<
U
c
n
a
iv
m
e
p
r
o
s
A
o
d
<
i
/
c
c
i
a
o
m
na
p
l
o
n
A
o
d
m
ic
b
io
re
n
=
a
"
l>
S UCURSAL 03">Guayaquil–12 de octubre y
cor
c
r
u
e
a
s
n
p
d
o
o
n da
Alfanumérico Max 300
Obligatorio
</infoAdicional> cuando - -
corresponda
</guiaRemision> Obligatorio - -
71

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
FORMATO XML NOTA DE CRÉDITO

|                                          |     |                   |              | T I PO   D E   | L O N G IT U D   /  |
| ---------------------------------------- | --- | ----------------- | ------------ | -------------- | ------------------- |
|                                          |     | ETIQUETAS O TAGS  | CARACTER     |                |                     |
|                                          |     |                   |              | C A M P O      | F O R M A T O       |
| <?xml version="1.0" encoding="UTF-8" ?>  |     |                   | Obligatorio  | -              | -                   |
<notaCredito id="comprobante" version="1.1.0">  Obligatorio  -  -
| <infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ----------------- | --- | --- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1</ambiente>  |     |     |     | Numérico  | 1   |
| ----------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 4
Obligatorio,
| <tipoEmision>1</ tipoEmision>  |     |     |     | Numérico  | 1   |
| ------------------------------ | --- | --- | --- | --------- | --- |
conforme
tabla 2
| < r a z on S o ci | a l>  E M P R E S A  P | U B L I C A DE HIDROCARBUROS DEL ECUADOR EP  |              |               |          |
| ----------------- | ---------------------- | -------------------------------------------- | ------------ | ------------- | -------- |
|                   |                        |                                              | Obligatorio  | Alfanumérico  | Max 300  |
| P E T R O E C     | U A D O R  < / ra z on | S o ci a l>                                  |              |               |          |
Obligatorio
< n o m b re C o m e rc ia l> E M P R E S A  P U B L IC A  DE HIDROCARBUROS DEL ECUADOR EP  c u a n d o   Alfanumérico  Max 300
| P E T R O E C | U A D O R < / n o m b | re C o m e rc ia l >   |     |     |     |
| ------------- | --------------------- | ---------------------- | --- | --- | --- |
cor r e s p o n da
| <ruc>1760013210001</ruc>  |     |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>0603201304176001321000110015010000000461234567817</claveAcceso>  Numérico  49
conforme
tabla 1
Obligatorio,
| <codDoc>04</codDoc>  |     |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 3
| <estab>001</estab>    |     |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | --- | ------------ | --------- | --- |
| <ptoEmi>501</ptoEmi>  |     |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000046</secuencial>  Obligatorio  Numérico  9
<dirMatriz>ALPALLANA</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ------------------ | --- | --- | ------------ | --- | --- |
| <infoNotaCredito>  |     |     | Obligatorio  | -   | -   |
<fechaEmision>06/03/2013</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio
<dirEstablecimiento>ALPALLANA</ dirEstablecimiento>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<tipoIdentificacionComprador>04</ tipoIdentificacionComprador >  Numérico  2
conforme
tabla 6
| < ra z o n S oc | ia l C o m p ra d o r> P | R U E B A S  S ERVICIO DE RENTAS  |              |               |          |
| --------------- | ------------------------ | --------------------------------- | ------------ | ------------- | -------- |
|                 |                          |                                   | Obligatorio  | Alfanumérico  | Max 300  |
| IN T E R N A S  | < / ra z on S o c ia lC  | o m p r ad o r>                   |              |               |          |
<identificacionComprador>1792107865001</identificacionComprador>  Obligatorio  Alfanumérico  Max 20
Obligatorio
<contribuyenteEspecial>5368</contribuyenteEspecial>  cuando  Alfanumérico  Min 3 Max 13
corresponda
Obligatorio
<obligadoContabilidad>SI</ obligadoContabilidad>  cuando  Texto  SI / NO
corresponda
Obligatorio
<rise>Contribuyente Régimen Simplificado RISE</rise>  cuando  Alfanumérico  Max 40
corresponda
Obligatorio,
<codDocModificado>01</codDocModificado>  conforme  Numérico  2
tabla 3
<numDocModificado>002-001-000000001</numDocModificado>  Opcional  Numérico  15
<fechaEmisionDocSustento>03/03/2013</fechaEmisionDocSustento>  Obligatorio  Fecha  dd/mm/aaaa
<totalSinImpuestos>38327.96</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<valorModificacion>45073.68</valorModificacion>  Obligatorio  Numérico  Max 14
Obligatorio
| <moneda>DOLAR</moneda>  |     |     |     | Alfanumérico  | Max 15  |
| ----------------------- | --- | --- | --- | ------------- | ------- |
cuando
corresponda
| <totalConImpuestos>  |     |     | Obligatorio  | -   | -   |
| -------------------- | --- | --- | ------------ | --- | --- |
| <totalImpuesto>      |     |     | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>3</codigo >  |     |     |     | Numérico  | 1   |
| -------------------- | --- | --- | --- | --------- | --- |
conforme
tabla 16
Obligatorio,
<codigoPorcentaje>3072</ codigoPorcentaje>  Numérico  Min 1 Max 4
conforme
tabla 18
<baseImponible>38327.96</ baseImponible >  Obligatorio  Numérico  Max 14

72

|                          |                   |              |                |                     |
| ------------------------ | ----------------- | ------------ | -------------- | ------------------- |
|                          |                   |              | T I PO   D E   | L O N G IT U D   /  |
|                          | ETIQUETAS O TAGS  | CARACTER     |                |                     |
|                          |                   |              | C A M P O      | F O R M A T O       |
| <valor>1916.40</valor >  |                   | Obligatorio  | Numérico       | Max 14              |
| </totalImpuesto >        |                   | Obligatorio  | -              | -                   |
| <totalImpuesto>          |                   | Obligatorio  | -              | -                   |
Obligatorio,
| <codigo>2</codigo >  |     | conforme  | Numérico  | 1   |
| -------------------- | --- | --------- | --------- | --- |
tabla 16
Obligatorio,
<codigoPorcentaje>2</ codigoPorcentaje>  conforme  Numérico  Min 1 Max 4
tabla 17
<baseImponible>40244.36</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>4829.32</valor >  |     | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | --- | ------------ | --------- | ------- |
| </totalImpuesto >        |     | Obligatorio  | -         | -       |
| </totalConImpuestos >    |     | Obligatorio  | -         | -       |
<motivo>DEVOLUCIÓN</motivo>  Obligatorio  Alfanumérico  Max 300
| </infoNotaCredito>  |     | Obligatorio  | -   | -   |
| ------------------- | --- | ------------ | --- | --- |
| <detalles>          |     | Obligatorio  | -   | -   |
| <detalle>           |     | Obligatorio  | -   | -   |
<codigoInterno>125BJC-01</codigoInterno >  Opcional  Alfanumérico  Max 25
Obligatorio
<codigoAdicional>1234D56789-A</codigoAdicional>  Alfanumérico  Max 25
cuando
corresponda
<descripcion> ABCD</descripcion>  Obligatorio  Alfanumérico  Max 300
M a x  1 8 , h a s ta
| <cantidad>1500.564125</cantidad>  |     | Obligatorio  | Numérico  |     |
| --------------------------------- | --- | ------------ | --------- | --- |
6  d e c im a le s
<precioUnitario>25.542365</precioUnitario>  Obligatorio  Numérico  M a x  1 8 , h a s ta
6  d e c im a le s
Obligatorio
| <descuento>0.00</descuento>  |     |     | Numérico  | Max 14  |
| ---------------------------- | --- | --- | --------- | ------- |
cuando
corresponda
<precioTotalSinImpuesto>38327.96</ precioTotalSinImpuesto>  Obligatorio  Numérico  Max 14
Obligatorio
<detallesAdicionales>
|     |     | cuando  |     |     |
| --- | --- | ------- | --- | --- |
corresponda
Obligatorio
<detAdicional nombre="Marca" valor="Chevrolet"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<detAdicional nombre="Modelo" valor="2012"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<detAdicional nombre="Chasis" valor="8LDETA03V20003289"/>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
| </detallesAdicionales>  |     | cuando  |     |     |
| ----------------------- | --- | ------- | --- | --- |
corresponda
| <impuestos>  |     | Obligatorio  | -   | -   |
| ------------ | --- | ------------ | --- | --- |
| <impuesto>   |     | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>3</codigo>  |     | conforme  | Numérico  | 1   |
| ------------------- | --- | --------- | --------- | --- |
tabla 16
Obligatorio,
<codigoPorcentaje>3072</codigoPorcentaje>  conforme  Numérico  Min 1 Max 4
tabla 18
Obligatorio
| <tarifa>5</ tarifa>  |     | cuando  | Numérico  | Min 1 Max 3  |
| -------------------- | --- | ------- | --------- | ------------ |
corresponda
<baseImponible>38327.96</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>1916.40</valor>  |     | Obligatorio  | Numérico  | Max 14  |
| ----------------------- | --- | ------------ | --------- | ------- |
| </impuesto>             |     | Obligatorio  | -         | -       |
| <impuesto>              |     | Obligatorio  | -         | -       |
Obligatorio,
| <codigo>2</codigo>  |     | conforme  | Numérico  | 1   |
| ------------------- | --- | --------- | --------- | --- |
tabla 16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  conforme  Numérico  Min 1 Max 4
tabla 17
| <tarifa>12</ tarifa>  |     | Obligatorio  | Numérico  |     |
| --------------------- | --- | ------------ | --------- | --- |
Min 1 Max 4
cuando

73

|     |                   |           |                |                     |
| --- | ----------------- | --------- | -------------- | ------------------- |
|     |                   |           | T I PO   D E   | L O N G IT U D   /  |
|     | ETIQUETAS O TAGS  | CARACTER  |                |                     |
|     |                   |           | C A M P O      | F O R M A T O       |
corresponda
/ 2 enteros, 2
decimales
<baseImponible>40244.36</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>4829.32</valor>  |     | Obligatorio  | Numérico  | Max 14  |
| ----------------------- | --- | ------------ | --------- | ------- |
| </impuesto>             |     | Obligatorio  | -         | -       |
| </impuestos>            |     | Obligatorio  | -         | -       |
| <detalle>               |     | Obligatorio  | -         | -       |
| <detalles>              |     | Obligatorio  | -         | -       |
Obligatorio
| <infoAdicional>  |     | cuando  | -   | -   |
| ---------------- | --- | ------- | --- | --- |
corresponda
Obligatorio
<campoAdicional nombre="E-MAIL">info@organizacion.com</campoAdicional>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
| </infoAdicional>  |     | cuando  | -   | -   |
| ----------------- | --- | ------- | --- | --- |
corresponda
| </notaCredito>  |     | Obligatorio  | -   | -   |
| --------------- | --- | ------------ | --- | --- |

74

|              |       |            |      |          |     |      |
| ------------ | ----- | ---------- | ---- | -------- | --- | ---- |
| ANEXO        | 4  -  | FORMATOS   | XML  | FACTURA  |     |      |
| EXPORTACIÓN  |       | APLICADOS  |      | A        |     | LAS  |
VERSIONES 1.0.0 y 1.1.0

Incluyen los campos requeridos para exportación, adicionalmente en el diseño del
Ride  se  podrá  incluir  e  imprimir  datos  adicionales  conforme  lo  requiera  el
contribuyente. Los campos nuevos contenidos en los siguientes formatos deberán
ser utilizados únicamente en exportaciones, caso contrario se deberá utilizar los
formatos de factura establecidos en el Anexo 1 y Anexo 3 según corresponda.

FACTURA VERSIÓN 1.0.0

|                                          |                   |     |              |     | T I PO   D E   | L O N G IT U D   /  |
| ---------------------------------------- | ----------------- | --- | ------------ | --- | -------------- | ------------------- |
|                                          | ETIQUETAS O TAGS  |     | CARACTER     |     |                |                     |
|                                          |                   |     |              |     | C A M P O      | F O R M A T O       |
| <?xml version="1.0" encoding="UTF-8" ?>  |                   |     | Obligatorio  |     | -              | -                   |
<factura id="comprobante" version="1.0.0">  Obligatorio  -  -
| <infoTributaria>         |     |     | Obligatorio  |              | -         | -   |
| ------------------------ | --- | --- | ------------ | ------------ | --------- | --- |
| <ambiente>1 </ambiente>  |     |     | O b li ga    | t o ri o ,   | Numérico  | 1   |
 4
con fo r m e   ta b l a
|                                 |     |     | O b li ga | t o ri o ,   |           |     |
| ------------------------------- | --- | --- | --------- | ------------ | --------- | --- |
| <tipoEmision>1 </ tipoEmision>  |     |     |           |  2           | Numérico  | 1   |
con fo r m e   ta b l a
<razonSocial>CONTRIBUYENTE PRUEBA</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio,
<nombreComercial>PRUEBA UNO</nombreComercial>  cuando  Alfanumérico  Max 300
corresponda
| <ruc>1792261104001</ruc>  |     |     | Obligatorio  |     | Numérico  | 13  |
| ------------------------- | --- | --- | ------------ | --- | --------- | --- |
< c la v eAcceso>0403201301179226110400110015010000000081234567816</claveAcc O b li ga t o ri o ,   Numérico  49
| es o >               |     |     | con fo r m e |   ta b l a  1  |           |     |
| -------------------- | --- | --- | ------------ | -------------- | --------- | --- |
| <codDoc>01</codDoc>  |     |     | O b li ga    | t o ri o ,     | Numérico  | 2   |
 3
con fo r m e   ta b l a
| <estab>001</estab>    |     |     | Obligatorio  |     | Numérico  | 3   |
| --------------------- | --- | --- | ------------ | --- | --------- | --- |
| <ptoEmi>501</ptoEmi>  |     |     | Obligatorio  |     | Numérico  | 3   |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Alpallana</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     | Obligatorio  |     | -   | -   |
| ------------------ | --- | --- | ------------ | --- | --- | --- |
| <infoFactura>      |     |     | Obligatorio  |     | -   | -   |
<fechaEmision>04/03/2013</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio,
<dirEstablecimiento>Alpallana</dirEstablecimiento>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio,
<contribuyenteEspecial>5368</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
Ob l ig a t o ri o,
<obligadoContabilidad>SI</ obligadoContabilidad >  Texto  SI/NO
c u a n d o
|     |     |     | corresponda  |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- |
Texto,
<comercioExterior>EXPORTADOR</comercioExterior>  Obligatorio  Mayúsculas,  10
siempre es
EXPORTADOR
<IncoTermFactura>CIF</IncoTermFactura>  Obligatorio  T e x t o ,   Max 10
|     |     |     |     |     | Ma y ú s c u l as  |     |
| --- | --- | --- | --- | --- | ------------------ | --- |
<lugarIncoTerm>GUAYAQUIL</lugarIncoTerm>  Obligatorio  Alfanumérico  Max 300
<paisOrigen>593</paisOrigen>  O b lig a t o r io ,  Numérico  3
 25
con fo rm e   t a b la
<puertoEmbarque>GUAYAQUIL</puertoEmbarque>  Obligatorio  Alfanumérico  Max 300
<puertoDestino>CHINA</puertoDestino>  Obligatorio  Alfanumérico  Max 300
<paisDestino>593</paisDestino>  O p c io n a l ,   Numérico  3
 25
confo r m e  t a b l a
<paisAdquisicion>593</paisAdquisicion>  O p c io n a l ,   Numérico  3
 25
confo r m e  t a b l a
<tipoIdentificacionComprador>04</tipoIdentificacionComprador>  Numérico  2
Obligatorio,

75

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |     |           |               |
| --- | --- | --- | --- | --------- | ------------- |
|     |     |     |     | C A M P O | F O R M A T O |
conforme tabla 6
Obligatorio,
<guiaRemision>001-001-000000001</guiaRemision>  Numérico  15
cuando
corresponda
< ra z o n S oc ia l C o m p ra d o r> P R U E B A S  S ERVICIO DE RENTAS  Obligatorio  Alfanumérico  Max 300

| IN T E R N A S | < / ra z on S o c ia lC | o m p ra d o r> |     |     |     |
| -------------- | ----------------------- | --------------- | --- | --- | --- |
<identificacionComprador>1760013210001</identificacionComprador>  Obligatorio  Numérico  Max 20
Obligatorio,
<direccionComprador>salinas y santiago</direccionComprador>  Alfanumérico  Max 300
cuando
corresponda
<totalSinImpuestos>295000.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<incoTermTotalSinImpuestos>FOB</incoTermTotalSinImpuestos>  Obligatorio  T e x t o ,   Max 10
Ma y ú s c u l as
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  |     |     | Obligatorio  | -   | -   |
| -------------------- | --- | --- | ------------ | --- | --- |
| <totalImpuesto>      |     |     | Obligatorio  | -   | -   |
O b lig a t o r io ,
| <codigo>2</codigo>  |     |     |  16  | Numérico  | 1   |
| ------------------- | --- | --- | ---- | --------- | --- |
con fo rm e   t a b la
<codigoPorcentaje>0</codigoPorcentaje>  O b lig a t o r io ,  Numérico  Min 1 Max 4
con fo rm e   t a b la  17
Opcional, aplica
<descuentoAdicional>0.00</descuentoAdicional>  Numérico  Max 14
para código
impuesto 2.
<baseImponible>295000.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>0.00<valor>      |     |     | Obligatorio  | Numérico  | Max 14  |
| ----------------------- | --- | --- | ------------ | --------- | ------- |
| </totalImpuesto>        |     |     | Obligatorio  | -         | -       |
| </totalConImpuesto>     |     |     | Obligatorio  | -         | -       |
| <propina>0.00<propina>  |     |     | Obligatorio  | Numérico  | Max 14  |
Obligatorio,
<fleteInternacional>1000.00<fleteInternacional>  cuando  Numérico  Max 14
corresponda
Obligatorio,
<seguroInternacional>200.00<seguroInternacional>  cuando  Numérico  Max 14
corresponda
Obligatorio,
<gastos Aduaneros>800.00<gastos Aduaneros>  cuando  Numérico  Max 14
corresponda
Obligatorio,
<gastosTransporteOtros>350.00<gastosTransporteOtros>  cuando  Numérico  Max 14
corresponda
<importeTotal>297350.00<importeTotal>  Obligatorio  Numérico  Max 14
Obligatorio,
| <moneda>DOLAR<moneda>  |     |     |     | Alfanumérico  | Max 15  |
| ---------------------- | --- | --- | --- | ------------- | ------- |
cuando
corresponda
| <pagos>  |     |     | Obligatorio  | -   | -   |
| -------- | --- | --- | ------------ | --- | --- |
| <pago>   |     |     | Obligatorio  | -   |     |

<formaPago>15</formaPago>  O b l ig a t o r io ,  Numérico  2
 24
con fo r m e   t a b la
| <total>200000</total>  |     |     | Obligatorio  | Numérico  | Max 14  |
| ---------------------- | --- | --- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>30<plazo>  |     |     | cuando  | Numérico  | Max 14  |
| ----------------- | --- | --- | ------- | --------- | ------- |
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |     |     | cuando  | Texto  | Max 10  |
| ---------------------------------- | --- | --- | ------- | ------ | ------- |
corresponda
| </pago>  |     |     | Obligatorio  | -   | -   |
| -------- | --- | --- | ------------ | --- | --- |
| <pago>   |     |     | Obligatorio  | -   | -   |
<formaPago>18</formaPago>  O b lig a t o r io ,  Numérico  2
 24
con fo rm e   t a b la
| <total>97350</total>  |     |     | Obligatorio  | Numérico  | Max 14  |
| --------------------- | --- | --- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>15<plazo>  |     |     |     | Numérico  | Max 14  |
| ----------------- | --- | --- | --- | --------- | ------- |
cuando
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |     |     |     | Texto  | Max 10  |
| ---------------------------------- | --- | --- | --- | ------ | ------- |
cuando
corresponda
| </pago>                          |     |     | Obligatorio  | -         | -       |
| -------------------------------- | --- | --- | ------------ | --------- | ------- |
| </pagos>                         |     |     | Obligatorio  | -         | -       |
| <valorRetIva>0.00</valorRetIva>  |     |     | Opcional     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14

76

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                 |              |     |           |               |
| --------------- | ------------ | --- | --------- | ------------- |
|                 |              |     | C A M P O | F O R M A T O |
| </infoFactura>  | Obligatorio  |     | -         | -             |
| <detalles>      | Obligatorio  |     | -         | -             |
| <detalle>       | Obligatorio  |     | -         | -             |
<codigoPrincipal>003</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
Obligatorio,
<codigoAuxiliar>SER003</codigoAuxiliar>  Alfanumérico  Max 25
cuando
corresponda
<descripcion>FROZEN MOONFISH WR</descripcion>  Obligatorio  Alfanumérico  Max 300
Obligatorio,
| <unidadMedida>Kilos</unidadMedida>  |     |     | Alfanumérico  | Max 50  |
| ----------------------------------- | --- | --- | ------------- | ------- |
cuando
corresponda
| <cantidad>100.00</cantidad>  | Obligatorio  |     | Numérico  | Max 14  |
| ---------------------------- | ------------ | --- | --------- | ------- |
<precioUnitario>2950.00</precioUnitario>  Obligatorio  Numérico  Max 14
| <descuento>0.00</descuento>  | Obligatorio  |     | Numérico  | Max 14  |
| ---------------------------- | ------------ | --- | --------- | ------- |
<precioTotalSinImpuestos>295000.00</precioTotalSinImpuestos>  Obligatorio  Numérico  Max 14
Obligatorio,
| <detallesAdicionales>  |     |     | -   | -   |
| ---------------------- | --- | --- | --- | --- |
cuando
corresponda
Obligatorio,
<detAdicional valor="KILOS"nombre="PESO NETO"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<detAdicional valor="KILOS"nombre="PESO BRUTO"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<detAdicional valor="KILOS"nombre="PARTIDA ARANCELARIA"/>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
| </detallesAdicionales>  |     |     | -   | -   |
| ----------------------- | --- | --- | --- | --- |
cuando
corresponda
| <impuestos>         | Obligatorio  |               | -         | -   |
| ------------------- | ------------ | ------------- | --------- | --- |
| <impuesto>          | Obligatorio  |               | -         | -   |
|                     | O b lig      | a t o r io ,  |           |     |
| <codigo>2</codigo>  |              |  16           | Numérico  | 1   |
|                     | con fo rm e  |   t a b la    |           |     |
<codigoPorcentaje>0</codigoPorcentaje>  O b lig a t o r io ,  Numérico  Min 1 Max 4
|     | con fo rm e |   t a b la  17  |     |     |
| --- | ----------- | --------------- | --- | --- |
Min 1 Max 4
| <tarifa>0</ tarifa>  | Obligatorio  |     | Numérico  |     |
| -------------------- | ------------ | --- | --------- | --- |
/ 2 enteros, 2
decimales
<baseImponible>295000.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>0.00</valor>  | Obligatorio     |                | Numérico  | Max 14  |
| -------------------- | --------------- | -------------- | --------- | ------- |
| </impuesto>          | Obligatorio     |                | -         | -       |
| </impuestos>         | Obligatorio     |                | -         | -       |
| </detalle>           | Obligatorio     |                | -         | -       |
| </detalles>          | Obligatorio     |                | -         | -       |
| <infoAdicional>      | Obl ig a t o ri | o  c u a n do  | -         | -       |
|                      | c o rr e s      | p o n d a      |           |         |
< c a m p o A d i ci o n al  n o m b r e = "DESCRIPCION DE CARGA">CAJAS DE 10  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300

K IL O S < / c a m p o A d ic io n a l > c o rr e s p o n d a
< c a m p o A d i c io n a l  n o m br e = "I N F O R M A CION BANCARIA">NUMERO DE CUENTA DE  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300

B A N C O   1 2 4 3 5 4 6 < / c am p o A d ic io n a l> c o rr e s p o n d a
| </infoAdicional>  | Obl ig a t o ri | o  c u a n do  | -   |     |
| ----------------- | --------------- | -------------- | --- | --- |
|                   | c o rr e s      | p o n d a      |     |     |
| </factura>        | Obligatorio     |                | -   |     |

77

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
FACTURA VERSIÓN 1.1.0

En esta versión se podrá utilizar de 2 a 6 decimales en los campos de cantidad y
precio unitario para contribuyentes que lo requieran.

|                                          |     |                   |              |     | T I PO   D E   | L O N G IT U D   /  |
| ---------------------------------------- | --- | ----------------- | ------------ | --- | -------------- | ------------------- |
|                                          |     | ETIQUETAS O TAGS  | CARACTER     |     |                |                     |
|                                          |     |                   |              |     | C A M P O      | F O R M A T O       |
| <?xml version="1.0" encoding="UTF-8" ?>  |     |                   | Obligatorio  |     | -              | -                   |
-<factura id="comprobante" version="1.1.0">  Obligatorio  -  -
| - <infoTributaria>  |     |     | Obligatorio  |     | -   | -   |
| ------------------- | --- | --- | ------------ | --- | --- | --- |
O b l i ga t o ri o ,
| <ambiente>1 </ambiente>  |     |     |     |  4  | Numérico  | 1   |
| ------------------------ | --- | --- | --- | --- | --------- | --- |
con f o r m e   ta b l a
<tipoEmision>1 </ tipoEmision>  O b l i ga t o ri o ,   Numérico  1
|     |     |     | con f o r m e |   ta b l a  2  |     |     |
| --- | --- | --- | ------------- | -------------- | --- | --- |
< r a z on S o ci a l> E M P R E S A  P U B L I C A DE HIDROCARBUROS DEL ECUADOR EP  Obligatorio  Alfanumérico  Max 300

| P E T R O E C | U A D O R < / ra z on S | o ci a l> |     |     |     |     |
| ------------- | ----------------------- | --------- | --- | --- | --- | --- |
< n o m b re C o m e rc ia l> E M P R E S A  P U B L IC A  DE HIDROCARBUROS DEL ECUADOR EP  Obl ig a t o ri o  c u a n do
|     |     |     |     |     | Alfanumérico  | Max 300  |
| --- | --- | --- | --- | --- | ------------- | -------- |
P E T R O E C U A D O R < / n o m b re C o m e rc ia l > c o rr e s p o n d a
| <ruc>1768153530001</ruc>  |     |     | Obligatorio  |     | Numérico  | 13  |
| ------------------------- | --- | --- | ------------ | --- | --------- | --- |
< c la veAcceso>0403201301176815353000110015010000000081234567816</claveAcce O b l i ga t o ri o ,
|                       |     |     |               |  1             | Numérico  | 49  |
| --------------------- | --- | --- | ------------- | -------------- | --------- | --- |
| so >                  |     |     | con f o r m e |   ta b l a     |           |     |
| <codDoc>01</codDoc>   |     |     | O b l i ga    | t o ri o ,     | Numérico  | 2   |
|                       |     |     | con f o r m e |   ta b l a  3  |           |     |
| <estab>001</estab>    |     |     | Obligatorio   |                | Numérico  | 3   |
| <ptoEmi>501</ptoEmi>  |     |     | Obligatorio   |                | Numérico  | 3   |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Alpallana</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     | Obligatorio  |     | -   | -   |
| ------------------ | --- | --- | ------------ | --- | --- | --- |
| <infoFactura>      |     |     | Obligatorio  |     | -   | -   |
<fechaEmision>04/03/2013</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
<dirEstablecimiento>Alpallana</ dirEstablecimiento >  Obli g a t o ri o   c u an do  Alfanumérico  Max 300

c o rr e s p o n d a
|     |     |     | Obl ig a t o ri o |  c u a n do  |     |     |
| --- | --- | --- | ----------------- | ------------ | --- | --- |
<contribuyenteEspecial>5368</contribuyenteEspecial>    Alfanumérico  Min 3 Max 13
c o rr e s p o n d a
<obligadoContabilidad>SI</ obligadoContabilidad >  Obl ig a t o ri o  c u a n do  Texto  SI / NO
c o rr e s p o n d a
Texto,
<comercioExterior>EXPORTADOR</comercioExterior>  Obligatorio  Mayúsculas,  10
siempre es
EXPORTADOR
<IncoTermFactura>FOB</IncoTermFactura>  Obligatorio  T e x t o ,   Max 10
|     |     |     |     |     | Ma y ú s c u l as  |     |
| --- | --- | --- | --- | --- | ------------------ | --- |
<lugarIncoTerm>GUAYAQUIL</lugarIncoTerm>  Obligatorio  Alfanumérico  Max 300
<paisOrigen>593</paisOrigen>  O b l ig a t o r io ,  Numérico  3
con fo r m e   t a b la  25
<puertoEmbarque>GUAYAQUIL</puertoEmbarque>  Obligatorio  Alfanumérico  Max 300
<puertoDestino>CHINA</puertoDestino>  Obligatorio  Alfanumérico  Max 300
Opcion a l,   c o n forme
| <paisDestino>593</paisDestino>  |     |     |     |     | Numérico  | 3   |
| ------------------------------- | --- | --- | --- | --- | --------- | --- |
ta b l a   25
<paisAdquisicion>593</paisAdquisicion>  Opcion a l,   c o n forme  Numérico  3
ta b l a   25
<tipoIdentificacionComprador>04</ tipoIdentificacionComprador >  O b l i ga t o ri o ,   Numérico  2
 6
con f o r m e   ta b l a
|     |     |     | Obl ig a t o ri o |  c u a n do  |     |     |
| --- | --- | --- | ----------------- | ------------ | --- | --- |
<guiaRemision>001-001-000000001</guiaRemision>    Numérico  15
c o rr e s p o n d a
< ra z o n S oc ia l C o m p ra d o r> P R U E B A S  S ERVICIO DE RENTAS  Obligatorio  Alfanumérico  Max 300
| IN T E R N A S | < / ra z on S o c ia lC o | m p r ad o r>   |     |     |     |     |
| -------------- | ------------------------- | --------------- | --- | --- | --- | --- |
<identificacionComprador>1760013210001</ identificacionComprador >  Obligatorio  Alfanumérico  Max 20
<direccionComprador>salinas y santiago</direccionComprador>  Obligatorio  Alfanumérico  Max 300
<totalSinImpuestos>64.94</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<incoTermTotalSinImpuestos>FOB</incoTermTotalSinImpuestos>  Obligatorio  T e x t o ,   Max 10
as
|     |     |     |     |     | Ma y ú s c u l |     |
| --- | --- | --- | --- | --- | -------------- | --- |
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  |     |     | Obligatorio  |     | -   | -   |
| -------------------- | --- | --- | ------------ | --- | --- | --- |
| <totalImpuesto>      |     |     | Obligatorio  |     | -   | -   |
O b l ig a t o r io ,
| <codigo>2</codigo >  |     |     |     |     | Numérico  | 1   |
| -------------------- | --- | --- | --- | --- | --------- | --- |
con fo r m e   t a b la  16
<codigoPorcentaje>0</ codigoPorcentaje>  O b l ig a t o r io ,  Numérico  Min 1 Max 4
con fo r m e   t a b la  17
Opcional, aplica
<descuentoAdicional>0.00</descuentoAdicional>  Numérico  Max 14
para código
impuesto 2.
<baseImponible>64.94</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>0.00</valor >     |     |     | Obligatorio  |     | Numérico  | Max 14  |
| ------------------------ | --- | --- | ------------ | --- | --------- | ------- |
| </totalImpuesto >        |     |     | Obligatorio  |     | -         | -       |
| </totalConImpuestos >    |     |     | Obligatorio  |     | -         | -       |
| <propina>0.00</propina>  |     |     | Obligatorio  |     | Numérico  | Max 14  |
<fleteInternacional>0.00<fleteInternacional>  Obli g a t o r io ,  c u a n do  Numérico  Max 14
|     |     |     | c o r r e s p | o n d a   |     |     |
| --- | --- | --- | ------------- | --------- | --- | --- |

78

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |           |               |
| --- | --- | --- | --------- | ------------- |
|     |     |     | C A M P O | F O R M A T O |
<seguroInternacional>0.00<seguroInternacional>  Obli g a t o r io ,  c u a n do  Numérico  Max 14
|     | c o r r e s p | o n d a   |     |     |
| --- | ------------- | --------- | --- | --- |
<gastos Aduaneros>0.00<gastos Aduaneros>  Obli g a t o r io ,  c u a n do  Numérico  Max 14
|     | c o r r e s p | o n d a   |     |     |
| --- | ------------- | --------- | --- | --- |
<gastosTransporteOtros>0.00<gastosTransporteOtros>  Obli g a t o r io ,  c u a n do  Numérico  Max 14

|     | c o r r e s p | o n d a |     |     |
| --- | ------------- | ------- | --- | --- |
<importeTotal>65.07</ importeTotal>  Obligatorio  Numérico  Max 14
<moneda>DOLAR</moneda>  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 15

|          | c o rr e s p | o n d a |     |     |
| -------- | ------------ | ------- | --- | --- |
| <pagos>  | Obligatorio  |         | -   |     |

| <pago>  | Obligatorio  |     | -   |     |
| ------- | ------------ | --- | --- | --- |
<formaPago>16</formaPago>  O b l ig a t o r io ,  Numérico  2
 24
|                       | con fo r m e |   t a b la |           |         |
| --------------------- | ------------ | ---------- | --------- | ------- |
| <total>30.00</total>  | Obligatorio  |            | Numérico  | Max 14  |
<plazo>90<plazo>  Obli g a t o r io ,  c u a n do  Numérico  Max 14

|                                    | c o r r e s p     | o n d a        |        |         |
| ---------------------------------- | ----------------- | -------------- | ------ | ------- |
|                                    | Obli g a t o r io | ,  c u a n do  |        |         |
| <unidadTiempo>dias</unidadTiempo>  |                   |                | Texto  | Max 10  |
|                                    | c o r r e s p     | o n d a        |        |         |
| </pago>                            | Obligatorio       |                | -      | -       |
| <pago>                             | Obligatorio       |                | -      | -       |
<formaPago>19</formaPago>  O b l ig a t o r io ,  Numérico  2
 24
|                       | con fo r m e |   t a b la |           |         |
| --------------------- | ------------ | ---------- | --------- | ------- |
| <total>34.94</total>  | Obligatorio  |            | Numérico  | Max 14  |
<plazo>90<plazo>  Obli g a t o r io ,  c u a n do  Numérico  Max 14

|                                    | c o r r e s p     | o n d a        |        |         |
| ---------------------------------- | ----------------- | -------------- | ------ | ------- |
|                                    | Obli g a t o r io | ,  c u a n do  |        |         |
| <unidadTiempo>dias</unidadTiempo>  |                   |                | Texto  | Max 10  |
|                                    | c o r r e s p     | o n d a        |        |         |
| </pago>                            | Obligatorio       |                | -      |         |

| </pagos>                         | Obligatorio  |     | -         | -       |
| -------------------------------- | ------------ | --- | --------- | ------- |
| <valorRetIva>0.00</valorRetIva>  | Opcional     |     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  |     | -   | -   |
| --------------- | ------------ | --- | --- | --- |
| - <detalles>    | Obligatorio  |     | -   | -   |
| - <detalle>     | Obligatorio  |     | -   | -   |
<codigoPrincipal>003</codigoPrincipal >  Alfanumérico  Max 25
Obligatorio
|     | Obl ig a t o ri o |  c u a n do  |     |     |
| --- | ----------------- | ------------ | --- | --- |
<codigoAuxiliar>001</codigoAuxiliar>    Alfanumérico  Max 25
|     | c o rr e s p | o n d a |     |     |
| --- | ------------ | ------- | --- | --- |
<descripcion> FROZEN MOONFISH WR </descripcion>  Obligatorio  Alfanumérico  Max 300
Max 18,
| <cantidad>2.542563</cantidad>  | Obligatorio  |     | Numérico  |     |
| ------------------------------ | ------------ | --- | --------- | --- |
hasta 6
decimales
Max 18,
<precioUnitario>25.542365</precioUnitario>  Obligatorio  Numérico
hasta 6
decimales
| <descuento>0.00</descuento>  | Obligatorio  |     | Numérico  | Max 14  |
| ---------------------------- | ------------ | --- | --------- | ------- |
<precioTotalSinImpuesto>64.94</ precioTotalSinImpuesto>  Obligatorio  Numérico  Max 14
| <detallesAdicionales>  | Obl ig a t o ri o |  c u a n do  | -   |     |
| ---------------------- | ----------------- | ------------ | --- | --- |
|                        | c o rr e s p      | o n d a      |     | -   |
<detAdicional nombre="KILOS" valor="PESO NETO"/>  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300

|     | c o rr e s p      | o n d a      |     |     |
| --- | ----------------- | ------------ | --- | --- |
|     | Obl ig a t o ri o |  c u a n do  |     |     |
<detAdicional nombre="KILOS " valor="PESO BRUTO"/>    Alfanumérico  Max 300
|     | c o rr e s p | o n d a |     |     |
| --- | ------------ | ------- | --- | --- |
<detAdicional nombre="0303.89.00.90" valor="PARTIDA ARANCELARIA"/>  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300
|                         | c o rr e s p      | o n d a         |           |     |
| ----------------------- | ----------------- | --------------- | --------- | --- |
| </detallesAdicionales>  | Obl ig a t o ri o |  c u a n do     | -         |     |
|                         |                   |                 |           | -   |
|                         | c o rr e s p      | o n d a         |           |     |
| <impuestos>             | Obligatorio       |                 | -         | -   |
| <impuesto>              | Obligatorio       |                 | -         | -   |
| <codigo>2</codigo>      | O b l ig a        | t o r io ,      | Numérico  | 1   |
|                         | con fo r m e      |   t a b la  16  |           |     |
<codigoPorcentaje>0</codigoPorcentaje>  O b l ig a t o r io ,  Numérico  Min 1 Max 4
 17
|     | con fo r m e |   t a b la |     |     |
| --- | ------------ | ---------- | --- | --- |
Min 1 Max 4
| <tarifa>0</ tarifa>  | Obligatorio  |     | Numérico  | / 2 enteros, 2  |
| -------------------- | ------------ | --- | --------- | --------------- |
decimales
<baseImponible>64.94</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>0.00</valor>  | Obligatorio  |     | Numérico  | Max 14  |
| -------------------- | ------------ | --- | --------- | ------- |
| </impuesto>          | Obligatorio  |     | -         | -       |
| </impuestos>         | Obligatorio  |     | -         | -       |
| </detalle>           | Obligatorio  |     | -         | -       |
| </detalles>          | Obligatorio  |     | -         | -       |
Obligatorio cuando
corresponda. Aplica
para
| <retenciones>  |     |     | -   | -   |
| -------------- | --- | --- | --- | --- |
comercializadores de
Derivados de
Petróleo y Retención
presuntiva de IVA a

79

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |     |     |     |     |     |       |     |               |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------------- |
|     |     |     |     |     |     |     |     | C A M | P O | F O R M A T O |
los Editores,
Distribuidores y
Voceadores que
participan en la
comercialización de
periódicos y/o
revistas.
| -<retencion>  |     |     |     |     |     | Obl ig a | t o ri o  c u a n do  |     | -   | -   |
| ------------- | --- | --- | --- | --- | --- | -------- | --------------------- | --- | --- | --- |
|               |     |     |     |     |     | c o rr   | e s p o n d a         |     |     |     |
Obligatorio cuando
| <codigo>4</codigo>  |     |     |     |     |     |     |     | Numérico  |     | 1   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
corresponda
conforme tabla 22
Obligatorio cuando
<codigoPorcentaje>327</codigoPorcentaje>  Numérico  Min 1 Max 3
corresponda
conforme tabla 23
Min 1 Max 5 /
<tarifa>0.20</tarifa>  Obl ig a t o ri o  c u a n do  Numérico  3 en t e r os,
|     |     |     |     |     |     | c o rr | e s p o n d a   |     |     | d o s   |
| --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | --- | ------- |
decimales
|                      |     |     |     |     |     | Obl ig a | t o ri o  c u a n do  |           |     | Max 14 /12         |
| -------------------- | --- | --- | --- | --- | --- | -------- | --------------------- | --------- | --- | ------------------ |
| <valor>0.13</valor>  |     |     |     |     |     |          |                       | Numérico  |     | e n te ro s ,  2   |
|                      |     |     |     |     |     | c o rr   | e s p o n d a         |           |     |                    |
|                      |     |     |     |     |     |          |                       |           |     | d e c im a l e s   |
| </retencion>         |     |     |     |     |     | Obl ig a | t o ri o  c u a n do  |           | -   | -                  |
|                      |     |     |     |     |     | c o rr   | e s p o n d a         |           |     |                    |
| </retenciones>       |     |     |     |     |     | Obl ig a | t o ri o  c u a n do  |           | -   | -                  |
|                      |     |     |     |     |     | c o rr   | e s p o n d a         |           |     |                    |
| <infoAdicional>      |     |     |     |     |     | Obl ig a | t o ri o  c u a n do  |           | -   | -                  |

|     |     |     |     |     |     | c o rr | e s p o n d a |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | --- | --- |
< c a m p o A d ic io n a l  no mbre=" DESCRIPCION DE CARGA "> CAJAS DE 10 KILOS  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300
| < /c a m | p o A d ic io n a l>   |     |     |     |     | c o rr | e s p o n d a   |     |     |     |
| -------- | ---------------------- | --- | --- | --- | --- | ------ | --------------- | --- | --- | --- |
< c a m p o A d i c io n a ln o m b r e = " I N F O R M A CION BANCARIA "> NUMERO DE CUENTA DE  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300
B A N C O   1 2 4 3 5 4 6 < /c a m p o A d ic io n a l>   c o rr e s p o n d a
| </infoAdicional>  |     |     |     |     |     | Obl ig a | t o ri o  c u a n do  |     | -   | -   |
| ----------------- | --- | --- | --- | --- | --- | -------- | --------------------- | --- | --- | --- |

|             |     |     |     |     |     | c o rr       | e s p o n d a |     |     |     |
| ----------- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | --- | --- |
| </factura>  |     |     |     |     |     | Obligatorio  |               |     | -   | -   |

TABLA 24: FORMAS DE PAGO

|     |                                         |                         | FORMAS DE PAGO      |     | CÓDIGO  |     | FECHA INICIO  | FECHA FIN  |     |     |
| --- | --------------------------------------- | ----------------------- | ------------------- | --- | ------- | --- | ------------- | ---------- | --- | --- |
|     | SIN UTILIZACION DEL SISTEMA FINANCIERO  |                         |                     |     |         | 01  | 01/01/2013    |            | -   |     |
|     |                                         | COMPENSACIÓN DE DEUDAS  |                     |     |         | 15  | 01/01/2013    |            | -   |     |
|     |                                         |                         | TARJETA DE DÉBITO   |     |         | 16  | 01/06/2016    |            | -   |     |
|     |                                         |                         | DINERO ELECTRÓNICO  |     |         | 17  | 01/06/2016    |            | -   |     |
|     |                                         |                         | TARJETA PREPAGO     |     |         | 18  | 01/06/2016    |            | -   |     |
|     |                                         |                         | TARJETA DE CRÉDITO  |     |         | 19  | 01/06/2016    |            | -   |     |
OTROS CON UTILIZACIÓN DEL SISTEMA FINANCIERO  20  01/06/2016  -
|     |     |     | ENDOSO DE TÍTULOS  |     |     | 21  | 01/06/2016  |     | -   |     |
| --- | --- | --- | ------------------ | --- | --- | --- | ----------- | --- | --- | --- |

Las formas de pago señaladas corresponden al Catálogo del Anexo Transaccional
Simplificado,  publicado  en  la  página  web  www.sri.gob.ec:  Información  sobre
impuestos/Cómo declaro mis impuestos? / Anexos y guías.

TABLA 25: PAÍSES

|     | CÓDIGO  |     | DESCRIPCIÓN     |   CÓDIGO  |     |     | DESCRIPCIÓN  |     |     |     |
| --- | ------- | --- | --------------- | --------- | --- | --- | ------------ | --- | --- | --- |
|     | 016     |     | AMERICAN SAMOA  |   334     |     |     | QATAR        |     |     |     |
|     | 074     |     | BOUVET ISLAND   |   335     |     |     | MALDIVAS     |     |     |     |
|     | 101     |     | ARGENTINA       | 336       |     |     | NEPAL        |     |     |     |

|     | 102  |     | BOLIVIA  |   337  |     |     | OMAN                |     |     |     |
| --- | ---- | --- | -------- | ------ | --- | --- | ------------------- | --- | --- | --- |
|     | 103  |     | BRASIL   |   338  |     |     | SINGAPUR            |     |     |     |
|     | 104  |     | CANADÁ   | 339    |     |     | SRI LANKA (CEILAN)  |     |     |     |

80

| CÓDIGO  | DESCRIPCIÓN  | CÓDIGO  | DESCRIPCIÓN  |
| ------- | ------------ | ------- | ------------ |

| 105  | COLOMBIA    |   341  | VIETNAM                 |
| ---- | ----------- | ------ | ----------------------- |
| 106  | COSTA RICA  |   342  | YEMEN                   |
| 107  | CUBA        | 343    | ISLAS HEARD Y MCDONALD  |

| 108  | CHILE    |   344  | BRUNEI DARUSSALAM  |
| ---- | -------- | ------ | ------------------ |
| 109  | ANGUILA  | 346    | TURQUÍA            |

| 110  | ESTADOS UNIDOS  | 347  | AZERBAIJÁN  |
| ---- | --------------- | ---- | ----------- |

| 111  | GUATEMALA  |   348  | KAZAJSTÁN     |
| ---- | ---------- | ------ | ------------- |
| 112  | HAITÍ      | 349    | KIRGUIZISTÁN  |

| 113  | HONDURAS        |   350  | TAJIKISTAN    |
| ---- | --------------- | ------ | ------------- |
| 114  | JAMAICA         |   351  | TURKMENISTÁN  |
| 115  | MALVINAS ISLAS  | 352    | UZBEKISTÁN    |

| 116  | MÉXICO     |   353  | PALESTINA  |
| ---- | ---------- | ------ | ---------- |
| 117  | NICARAGUA  |   354  | HONG KONG  |
| 118  | PANAMÁ     | 355    | MACAO      |

| 119  | PARAGUAY     |   356  | ARMENIA       |
| ---- | ------------ | ------ | ------------- |
| 120  | PERÚ         |   382  | MONTENEGRO    |
| 121  | PUERTO RICO  | 402    | BURKINA FASO  |

| 122  | REPÚBLICA DOMINICANA  |   403  | ARGELIA  |
| ---- | --------------------- | ------ | -------- |
| 123  | EL SALVADOR           |   404  | BURUNDÍ  |
| 124  | TRINIDAD Y TOBAGO     | 405    | CAMERÚN  |

| 125  | URUGUAY    |   406  | CONGO    |
| ---- | ---------- | ------ | -------- |
| 126  | VENEZUELA  |   407  | ETIOPÍA  |
| 127  | CURAZAO    | 408    | GAMBIA   |

| 129  | BAHAMAS   |   409  | GUINEA   |
| ---- | --------- | ------ | -------- |
| 130  | BARBADOS  | 410    | LIBERIA  |

| 131  | GRANADA  | 412  | MADAGASCAR  |
| ---- | -------- | ---- | ----------- |

| 132  | GUYANA   |   413  | MALAWI  |
| ---- | -------- | ------ | ------- |
| 133  | SURINAM  | 414    | MALÍ    |

| 134  | ANTIGUA Y BARBUDA  |   415  | MARRUECOS   |
| ---- | ------------------ | ------ | ----------- |
| 135  | BELICE             |   416  | MAURITANIA  |
| 136  | DOMINICA           | 417    | NIGERIA     |

| 137  | SAN CRISTOBAL Y NEVIS      |   419  | ZIMBABWE (RHODESIA)  |
| ---- | -------------------------- | ------ | -------------------- |
| 138  | SANTA LUCÍA                |   420  | SENEGAL              |
| 139  | SAN VICENTE Y LAS GRANAD.  | 421    | SUDÁN                |

| 140  | ANTILLAS HOLANDESAS  |   422  | SUDAFRICA (CISKEI)  |
| ---- | -------------------- | ------ | ------------------- |
| 141  | ARUBA                |   423  | SIERRA LEONA        |
| 142  | BERMUDA              | 425    | TANZANIA            |

| 143  | GUADALUPE        |   426  | UGANDA         |
| ---- | ---------------- | ------ | -------------- |
| 144  | GUYANA FRANCESA  |   427  | ZAMBIA         |
| 145  | ISLAS CAIMÁN     | 428    | ÅLAND ISLANDS  |

| 146  | ISLAS VIRGENES (BRITANICAS)  |   429  | BENIN                     |
| ---- | ---------------------------- | ------ | ------------------------- |
| 147  | JOHNSTON ISLA                |   430  | BOTSWANA                  |
| 148  | MARTINICA                    | 431    | REPUBLICA CENTROAFRICANA  |

| 149  | MONTSERRAT ISLA        |   432  | COSTA DE MARFIL  |
| ---- | ---------------------- | ------ | ---------------- |
| 151  | TURCAS Y CAICOS ISLAS  | 433    | CHAD             |

| 152  | VIRGENES, ISLAS (NORT.AMER.)  |   434  | EGIPTO  |
| ---- | ----------------------------- | ------ | ------- |
| 201  | ALBANIA                       |   435  | GABON   |
| 202  | ALEMANIA                      | 436    | GHANA   |

| 203  | AUSTRIA   |   437  | GUINEA-BISSAU      |
| ---- | --------- | ------ | ------------------ |
| 204  | BÉLGICA   |   438  | GUINEA ECUATORIAL  |
| 205  | BULGARIA  | 439    | KENIA              |

| 207  | ALBORAN Y PEREJIL  |   440  | LESOTHO     |
| ---- | ------------------ | ------ | ----------- |
| 208  | DINAMARCA          |   441  | MAURICIO    |
| 209  | ESPAÑA             | 442    | MOZAMBIQUE  |

| 211  | FRANCIA      |   443  | MAYOTTE  |
| ---- | ------------ | ------ | -------- |
| 212  | FINLANDIA    |   444  | NIGER    |
| 213  | REINO UNIDO  | 445    | RWANDA   |

| 214  | GRECIA  |   446  | SEYCHELLES  |
| ---- | ------- | ------ | ----------- |

81

| CÓDIGO  | DESCRIPCIÓN  | CÓDIGO  | DESCRIPCIÓN  |
| ------- | ------------ | ------- | ------------ |

| 215  | PAISES BAJOS (HOLANDA)  |   447  | SAHARA OCCIDENTAL      |
| ---- | ----------------------- | ------ | ---------------------- |
| 216  | HUNGRÍA                 |   448  | SOMALIA                |
| 217  | IRLANDA                 | 449    | SANTO TOME Y PRINCIPE  |

| 218  | ISLANDIA  |   450  | SWAZILANDIA  |
| ---- | --------- | ------ | ------------ |
| 219  | ITALIA    | 451    | TOGO         |

| 220  | LUXEMBURGO  | 452  | TUNEZ  |
| ---- | ----------- | ---- | ------ |

| 221  | MALTA    |   453  | ZAIRE   |
| ---- | -------- | ------ | ------- |
| 222  | NORUEGA  | 454    | ANGOLA  |

| 223  | POLONIA   |   456  | CABO VERDE  |
| ---- | --------- | ------ | ----------- |
| 224  | PORTUGAL  |   458  | COMORAS     |
| 225  | RUMANIA   | 459    | DJIBOUTI    |

| 226  | SUECIA          |   460  | NAMIBIA  |
| ---- | --------------- | ------ | -------- |
| 227  | SUIZA           |   463  | ERITREA  |
| 228  | CANARIAS ISLAS  | 464    | MOROCCO  |

| 229  | UCRANIA     |   465  | REUNION      |
| ---- | ----------- | ------ | ------------ |
| 230  | RUSIA       |   466  | SANTA ELENA  |
| 231  | YUGOSLAVIA  | 499    | JERSEY       |

| 233  | ANDORRA        |   501  | AUSTRALIA         |
| ---- | -------------- | ------ | ----------------- |
| 234  | LIECHTENSTEIN  |   503  | NUEVA ZELANDA     |
| 235  | MÓNACO         | 504    | SAMOA OCCIDENTAL  |

| 237  | SAN MARINO             |   506  | FIJI                |
| ---- | ---------------------- | ------ | ------------------- |
| 238  | VATICANO (SANTA SEDE)  |   507  | PAPUA NUEVA GUINEA  |
| 239  | GIBRALTAR              | 508    | TONGA               |

| 241  | BELARUS               |   509  | PALAO (BELAU) ISLAS  |
| ---- | --------------------- | ------ | -------------------- |
| 242  | BOSNIA Y HERZEGOVINA  | 510    | KIRIBATI             |

| 243  | CROACIA  | 511  | MARSHALL ISLAS  |
| ---- | -------- | ---- | --------------- |

| 244  | ESLOVENIA  |   512  | MICRONESIA  |
| ---- | ---------- | ------ | ----------- |
| 245  | ESTONIA    | 513    | NAURU       |

| 246  | GEORGIA      |   514  | SALOMON ISLAS  |
| ---- | ------------ | ------ | -------------- |
| 247  | GROENLANDIA  |   515  | TUVALU         |
| 248  | LETONIA      | 516    | VANUATU        |

| 249  | LITUANIA   |   517  | GUAM                   |
| ---- | ---------- | ------ | ---------------------- |
| 250  | MOLDOVA    |   518  | ISLAS COCOS (KEELING)  |
| 251  | MACEDONIA  | 519    | ISLAS COOK             |

| 252  | ESLOVAQUIA                   |   520  | ISLAS NAVIDAD  |
| ---- | ---------------------------- | ------ | -------------- |
| 253  | ISLAS FAROE                  |   521  | MIDWAY ISLAS   |
| 260  | FRENCH SOUTHERN TERRITORIES  | 522    | NIUE ISLA      |

| 301  | AFGANISTAN       |   523  | NORFOLK ISLA     |
| ---- | ---------------- | ------ | ---------------- |
| 302  | ARABIA SAUDITA   |   524  | NUEVA CALEDONIA  |
| 303  | MYANMAR (BURMA)  | 525    | PITCAIRN, ISLA   |

| 304  | CAMBOYA         |   526  | POLINESIA FRANCESA  |
| ---- | --------------- | ------ | ------------------- |
| 306  | COREA NORTE     |   529  | TIMOR DEL ESTE      |
| 307  | TAIWAN (CHINA)  | 530    | TOKELAI             |

| 308  | FILIPINAS  |   531  | WAKE ISLA               |
| ---- | ---------- | ------ | ----------------------- |
| 309  | INDIA      | 532    | WALLIS Y FUTUNA, ISLAS  |

| 310  | INDONESIA                  |   590  | SAINT BARTHELEMY       |
| ---- | -------------------------- | ------ | ---------------------- |
| 311  | IRAK                       |   593  | ECUADOR                |
| 312  | IRÁN (REPÚBLICA ISLÁMICA)  | 594    | AGUAS INTERNACIONALES  |

| 313  | ISRAEL    |   595  | ALTO VOLTA    |
| ---- | --------- | ------ | ------------- |
| 314  | JAPÓN     |   596  | BIELORRUSIA   |
| 315  | JORDANIA  | 597    | COTE DÍVOIRE  |

| 316  | KUWAIT                  |   598  | CYPRUS            |
| ---- | ----------------------- | ------ | ----------------- |
| 317  | LAOS, REP. POP. DEMOC.  |   599  | REPÚBLICA CHECA   |
| 318  | LIBANO                  | 600    | FALKLAND ISLANDS  |

| 319  | MALASIA               |   601  | LATVIA                |
| ---- | --------------------- | ------ | --------------------- |
| 321  | MONGOLIA (MANCHURIA)  |   602  | LIBIA                 |
| 322  | PAKISTÁN              | 603    | NORTHERN MARIANA ISL  |

| 323  | SIRIA  |   604  | ST. PIERRE AND MIQUE  |
| ---- | ------ | ------ | --------------------- |

82

|     |         |     |              |     |         |     |     |              |     |     |
| --- | ------- | --- | ------------ | --- | ------- | --- | --- | ------------ | --- | --- |
|     | CÓDIGO  |     | DESCRIPCIÓN  |     | CÓDIGO  |     |     | DESCRIPCIÓN  |     |     |

|     | 325  |     | TAILANDIA      |     |   605  |                                 | SYRIAN ARAB REPUBLIC  |           |     |     |
| --- | ---- | --- | -------------- | --- | ------ | ------------------------------- | --------------------- | --------- | --- | --- |
|     | 327  |     | BAHREIN        |     |   606  | TERRITORIO ANTÁRTICO BRITÁNICO  |                       |           |     |     |
|     | 328  |     | BANGLADESH     |     |   607  | TERRITORIO BRITÁNICO OCÉANO IN  |                       |           |     |     |
|     | 329  |     | BUTÁN          |     |   688  |                                 |                       | SERBIA    |     |     |
|     | 330  |     | COREA DEL SUR  |     | 831    |                                 |                       | GUERNSEY  |     |     |

|     | 331  |                         | CHINA POPULAR  |     |   832  |     |     | JERSEY       |     |     |
| --- | ---- | ----------------------- | -------------- | --- | ------ | --- | --- | ------------ | --- | --- |
|     | 332  |                         | CHIPRE         |     |   833  |     |     | ISLE OF MAN  |     |     |
|     | 333  | EMIRATOS ARABES UNIDOS  |                |     |        |     |     |              |     |     |
|     |      |                         |                |     |        |     |     |              |     |     |

Los  códigos  establecidos  para  países  corresponden  al  Catálogo  de  Anexo
Transaccional  Simplificado,  publicado  en  la  página  web  www.sri.gob.ec:
Información sobre impuestos / Cómo declaro mis impuestos? / Anexos y guías.

| ANEXO  |     | 5   | -   | FORMATOS  |     |     | XML  |     | FACTURA  |     |
| ------ | --- | --- | --- | --------- | --- | --- | ---- | --- | -------- | --- |
REEMBOLSO APLICADO EN LAS VERSIONES
1.0.0 y 1.1.0

Incluyen los campos requeridos exclusivamente para rreembolso, caso contrario se
deberá utilizar los formatos de factura establecidos en el anexo 1 y anexo 3 según
corresponda.

FACTURA VERSIÓN 1.0.0

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                         |     |     |     |     |     |     |              |     | C A M P O   | F O R M A T O   |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8"?>  |     |     |     |     |     |     | Obligatorio  |     | -           | -               |
<factura id="comprobante" version="1.0.0">  Obligatorio  -  -
| <infoTributaria>  |     |     |     |     |     |     | Obligatorio  |     | -   | -   |
| ----------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
<ambiente>1 </ambiente>  Obligato ri o ,  c o nforme  Numérico  1

|     |     |     |     |     |     |     | ta  | b l a  4 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
<tipoEmision>1 </ tipoEmision>  Obligato ri o ,  c o nforme  Numérico  1
|     |     |     |     |     |     |     | ta  | b l a  2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
<razonSocial>CONTRIBUYENTE PRUEBA</razonSocial>  Obligatorio  Alfanumérico  Max 300
<nombreComercial>PRUEBA UNO</nombreComercial>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300
|                           |     |     |     |     |     |     | c o r r      | e s p o n d a   |           |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | --------- | --- |
| <ruc>1792261104001</ruc>  |     |     |     |     |     |     | Obligatorio  |                 | Numérico  | 13  |
< c la v eAcceso>0403201301179226110400110015010000000081234567816</claveAcc Obligato ri o ,  c o nforme  Numérico  49
| es o >   |     |     |     |     |     |     | ta  | b l a  1   |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
<codDoc>01</codDoc>  Obligato ri o ,  c o nforme  Numérico  2

|                       |     |     |     |     |     |     | ta           | b l a  3 |           |     |
| --------------------- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --------- | --- |
| <estab>001</estab>    |     |     |     |     |     |     | Obligatorio  |          | Numérico  | 3   |
| <ptoEmi>501</ptoEmi>  |     |     |     |     |     |     | Obligatorio  |          | Numérico  | 3   |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Alpallana</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     |     |     |     |     | Obligatorio  |     | -   | -   |
| ------------------ | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| <infoFactura>      |     |     |     |     |     |     | Obligatorio  |     | -   | -   |
<fechaEmision>04/03/2013</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
<dirEstablecimiento>Alpallana</dirEstablecimiento>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300

|     |     |     |     |     |     |     | c o r r | e s p o n d a |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --- |
<contribuyenteEspecial>5368</contribuyenteEspecial>  Obli g a t o r io ,  c u a n do  Alfanumérico  Min 3 Max 13
|     |     |     |     |     |     |     | c o r r | e s p o n d a   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --- |
<obligadoContabilidad>SI</ obligadoContabilidad >  Obli g a t o r io ,  c u a n do  Texto  SI/NO
|     |     |     |     |     |     |     | c o r r | e s p o n d a   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --- |
<tipoIdentificacionComprador>04</tipoIdentificacionComprador>  Obligato ri o ,  c o nforme  Numérico  2

|     |     |     |     |     |     |     | ta           | b l a  6            |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------- | --- | --- |
|     |     |     |     |     |     |     | Obli g a t o | r io ,  c u a n do  |     |     |
<guiaRemision>001-001-000000001</guiaRemision>  Numérico  15
|     |     |     |     |     |     |     | c o r r | e s p o n d a   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --- |
< ra z o n S oc ia l C o m p ra d o r> P R U E B A S  S ERVICIO DE RENTAS  Obligatorio  Alfanumérico  Max 300
| IN T E R | N A S < / ra z on S o c ia lC | o m p ra d o | r>   |     |     |     |     |     |     |     |
| -------- | ----------------------------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
<identificacionComprador>1760013210001</identificacionComprador>  Obligatorio  Numérico  Max 20
<direccionComprador>salinas y santiago</direccionComprador>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300
|     |     |     |     |     |     |     | c o r r | e s p o n d a   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --- |

83

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |           |               |
| --- | --- | --- | --------- | ------------- |
|     |     |     | C A M P O | F O R M A T O |
<totalSinImpuestos>150.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
Obligatorio cuando
| <codDocReemb>41</codDocReemb>  |     |     | Numérico  | 2   |
| ------------------------------ | --- | --- | --------- | --- |
corresponda a
Reembolso (41)
Obligatorio cuando
<codDocReemb>> sea
igual a 41, sumatoria
<totalComprobantesReembolso>150.00</totalComprobantesReembolso>  de  Numérico  Max 14
<totalBaseImponibleRe
embolso> y
<totalImpuestoReembol
so>.
Obligatorio cuando
<codDocReemb> sea
igual a 41, en base a la
<totalBaseImponibleReembolso>133.93</totalBaseImponibleReembolso>  información  Numérico  Max 14
<reembolsos>,
sumatoria de
<baseImponibleReemb
olso>.
Obligatorio cuando
<codDocReemb>> sea
igual a 41, en base a la
<totalImpuestoReembolso>16.07</totalImpuestoReembolso>  Numérico  Max 14
información
<reembolsos>
sumatoria de
<impuestoReembolso>.
| <totalConImpuesto>  | Obligatorio  |     | -   | -   |
| ------------------- | ------------ | --- | --- | --- |
| <totalImpuesto>     | Obligatorio  |     |     |     |
|                     |              |     | -   | -   |
<codigo>2</codigo>  Obligat o r io ,  c o n forme  Numérico  1
t a b la   1 6
<codigoPorcentaje>6</codigoPorcentaje>  Obligat o r io ,  c o n forme  Numérico  Min 1 Max 4

t a b la   1 7
<baseImponible>150.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>0.00<valor>      | Obligatorio  |     | Numérico  | Max 14  |
| ----------------------- | ------------ | --- | --------- | ------- |
| </totalImpuesto>        | Obligatorio  |     | -         | -       |
| </totalConImpuesto>     | Obligatorio  |     | -         | -       |
| <propina>0.00<propina>  | Obligatorio  |     | Numérico  | Max 14  |
<importeTotal>150.00<importeTotal>  Obligatorio  Numérico  Max 14
<moneda>DOLAR<moneda>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 15
c o r r e s p o n d a
| <pagos>  | Obligatorio  |     | -   | -   |
| -------- | ------------ | --- | --- | --- |
| <pago>   | Obligatorio  |     | -   | -   |
Obligat o r io ,  c o n forme
| <formaPago>01</formaPago>  |     |     | Numérico  | 2   |
| -------------------------- | --- | --- | --------- | --- |
t a b la   2 4
| <total>150</total>  | Obligatorio  |     | Numérico  | Max 14  |
| ------------------- | ------------ | --- | --------- | ------- |
<plazo>0<plazo>  Obli g a t o r io ,  c u a n do  Numérico  Max 14
c o r r e s p o n d a
<unidadTiempo>dias</unidadTiempo>  Obli g a t o r io ,  c u a n do  Texto  Max 10

c o r r e s p o n d a
| </pago>                          | Obligatorio  |     | -         | -       |
| -------------------------------- | ------------ | --- | --------- | ------- |
| </pagos>                         | Obligatorio  |     | -         | -       |
| <valorRetIva>0.00</valorRetIva>  | Opcional     |     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  |     | -   | -   |
| --------------- | ------------ | --- | --- | --- |
| <detalles>      | Obligatorio  |     | -   | -   |
| <detalle>       | Obligatorio  |     | -   | -   |
<codigoPrincipal>003</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
<codigoAuxiliar>001</codigoAuxiliar>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 25

c o r r e s p o n d a
<descripcion>REEMBOLSO DE GASTOS</descripcion>  Obligatorio  Alfanumérico  Max 300
| <cantidad>1</cantidad>  | Obligatorio  |     | Numérico  | Max 14  |
| ----------------------- | ------------ | --- | --------- | ------- |
<precioUnitario>150.00</precioUnitario>  Obligatorio  Numérico  Max 14
| <descuento>0</descuento>  | Obligatorio  |     | Numérico  | Max 14  |
| ------------------------- | ------------ | --- | --------- | ------- |
<precioTotalSinImpuestos>150.00</precioTotalSinImpuestos>  Obligatorio  Numérico  Max 14
Obli g a t o r io ,  c u a n do
| <detallesAdicionales>  |     |     | -   | -   |
| ---------------------- | --- | --- | --- | --- |
c o r r e s p o n d a
<detAdicional nombre="TECLADO DELL" valor="COMPRA DE REPUESTOS"/>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300
c o r r e s p o n d a
</detallesAdicionales>  Obli g a t o r io ,  c u a n do  -  -

c o r r e s p o n d a
| <impuestos>  | Obligatorio  |     | -   | -   |
| ------------ | ------------ | --- | --- | --- |
| <impuesto>   | Obligatorio  |     | -   | -   |
<codigo>2</codigo>  Obligat o r io ,  c o n forme  Numérico  1
t a b la   1 6
<codigoPorcentaje>6</codigoPorcentaje>  Obligat o r io ,  c o n forme  Numérico  Min 1 Max 4

t a b la   1 7

84

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |       |               |
| --- | --- | --- | ----- | ------------- |
|     |     | C A | M P O | F O R M A T O |
Min 1 Max 4
| <tarifa>0.00</ tarifa>  | Obligatorio  | Numérico  |     |     |
| ----------------------- | ------------ | --------- | --- | --- |
/ 2 enteros, 2
decimales
<baseImponible>150.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>0.00</valor>  | Obligatorio  | Numérico  |     | Max 14  |
| -------------------- | ------------ | --------- | --- | ------- |
| </impuesto>          | Obligatorio  |           | -   | -       |
| </impuestos>         | Obligatorio  |           | -   | -       |
| </detalle>           | Obligatorio  |           | -   | -       |
| </detalles>          | Obligatorio  |           | -   | -       |
Obligatorio cuando
| <reembolsos>  |                    |     |     |     |
| ------------- | ------------------ | --- | --- | --- |
|               | <codDocReemb> sea  |     | -   | -   |
igual a 41
Obligatorio cuando
| <reembolsoDetalle>  |                    |     |     |     |
| ------------------- | ------------------ | --- | --- | --- |
|                     | <codDocReemb> sea  |     | -   | -   |
igual a 41
Obligatorio cuando
<tipoIdentificacionProveedorReembolso>04</tipoIdentificacionProveedorReembol <codDocReemb>sea
| so>  | igual a 41, conforme  | Numérico |     | 2   |
| ---- | --------------------- | -------- | --- | --- |
tabla 6
Obligatorio cuando
<identificacionProveedorReembolso>1760013210001</identificacionProveedorRee <codD o cR e e m b > sea  Alfanumérico   Max 13
| mbolso>  |     |     |     |     |
| -------- | --- | --- | --- | --- |
ig u al  a   41
Obligatorio cuando
<codDocReemb> sea
<codPaisPagoProveedorReembolso>593</codPaisPagoProveedorReembolso>  Numérico   3
igual a 41, conforme
tabla 25
Obligatorio cuando
<tipoProveedorReembolso>01</tipoProveedorReembolso>  <codDocReemb> sea
|     | igual a 41, conforme  | Numérico |     | 2   |
| --- | --------------------- | -------- | --- | --- |
tabla 26
Obligatorio cuando
<codDocReemb> sea
<codDocReembolso>01</codDocReembolso>  igual a 41, conforme
|     |     | Numérico |     | Min 2 Max 3 |
| --- | --- | -------- | --- | ----------- |
documentos de
reembolso del catálogo
del ATS
Obligatorio cuando
<estabDocReembolso>001</estabDocReembolso>  <codDocReemb> sea  Numérico   3
igual a 41
Obligatorio cuando
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
<ptoEmiDocReembolso>501</ptoEmiDocReembolso>  <codDocReemb> sea  Numérico 3
igual a 41
Obligatorio cuando
<secuencialDocReembolso>000000008</secuencialDocReembolso>
|     | <codDocReemb> sea  | Numérico |     | 9   |
| --- | ------------------ | -------- | --- | --- |
igual a 41
Obligatorio cuando
<fechaEmisionDocReembolso>04/03/2013</fechaEmisionDocReembolso>
|     | <codDocReemb> sea  | Fecha |     | dd/mm/aaaa |
| --- | ------------------ | ----- | --- | ---------- |
igual a 41
Obligatorio cuando
<numeroautorizacionDocReemb>040320130117922611040011001501000000008123
4567816</numeroautorizacionDocReemb>  <codD o cR e e m b > sea  Numérico 10, 37 o 49

ig u al  a   41
Obligatorio cuando
| <detalleImpuestos>  |                    |     |     |     |
| ------------------- | ------------------ | --- | --- | --- |
|                     | <codDocReemb> sea  |     | -   | -   |
igual a 41
Obligatorio cuando
| <detalleImpuesto>  |                    |     |     |     |
| ------------------ | ------------------ | --- | --- | --- |
|                    | <codDocReemb> sea  |     | -   | -   |
igual a 41
Obligatorio cuando
| <codigo>2</codigo>  | <codDocReemb> sea     |          |     |     |
| ------------------- | --------------------- | -------- | --- | --- |
|                     | igual a 41, conforme  | Numérico |     | 1   |
tabla 16
Obligatorio cuando
<codigoPorcentaje>2</codigoPorcentaje>  <codDocReemb> sea
|     |     | Numérico |     | Min 1 Max 4 |
| --- | --- | -------- | --- | ----------- |
igual a 41, conforme
tabla 17
|                      | Obligatorio cuando  |          |     | Min 1 Max 4 / 2  |
| -------------------- | ------------------- | -------- | --- | ---------------- |
| <tarifa>12</tarifa>  |                     |          |     |                  |
|                      | <codDocReemb> sea   | Numérico |     | enteros, 2       |
|                      | igual a 41          |          |     | decimales        |
Obligatorio cuando
| <baseImponibleReembolso>133.93</baseImponibleReembolso>  |                    |          |     |        |
| -------------------------------------------------------- | ------------------ | -------- | --- | ------ |
|                                                          | <codDocReemb> sea  | Numérico |     | Max 14 |
igual a 41
Obligatorio cuando
| <impuestoReembolso>16.07</impuestoReembolso>  |                    |          |     |        |
| --------------------------------------------- | ------------------ | -------- | --- | ------ |
|                                               | <codDocReemb> sea  | Numérico |     | Max 14 |
igual a 41
Obligatorio cuando
| </detalleImpuesto>  |                    |     |     |     |
| ------------------- | ------------------ | --- | --- | --- |
|                     | <codDocReemb> sea  |     | -   | -   |
igual a 41
Obligatorio cuando
| </detalleImpuestos>  | <codDocReemb> sea  |     |     |     |
| -------------------- | ------------------ | --- | --- | --- |
|                      |                    |     | -   | -   |
igual a 41
| </reembolsoDetalle>  | Obligatorio cuando  |     |     |     |
| -------------------- | ------------------- | --- | --- | --- |
|                      | <codDocReemb> sea   |     | -   | -   |

85

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |     |     |     |           |               |
| --- | --- | --- | --- | --- | --- | --------- | ------------- |
|     |     |     |     |     |     | C A M P O | F O R M A T O |
igual a 41
Obligatorio cuando
| </reembolsos>  |     |     |     |                   |     |     |     |
| -------------- | --- | --- | --- | ----------------- | --- | --- | --- |
|                |     |     |     | <codDocReemb>sea  |     | -   | -   |
igual a 41
| <infoAdicional>  |     |     |     | Obl ig a t o ri o |  c u a n do  |     |     |
| ---------------- | --- | --- | --- | ----------------- | ------------ | --- | --- |
|                  |     |     |     |                   |              | -   | -   |
|                  |     |     |     | c o rr e s p      | o n d a      |     |     |
|                  |     |     |     | Obl ig a t o ri o |  c u a n do  |     |     |
<campoAdicional nombre="Codigo Impuesto ISD">4580</campoAdicional>  Alfanumérico   Max 300
|                   |     |     |     | c o rr e s p      | o n d a      |     |     |
| ----------------- | --- | --- | --- | ----------------- | ------------ | --- | --- |
| </infoAdicional>  |     |     |     | Obl ig a t o ri o |  c u a n do  |     |     |
|                   |     |     |     | c o rr e s p      | o n d a      | -   | -   |
|                   |     |     |     |                   |              |     |     |
| </factura>        |     |     |     | Obligatorio       |              | -   | -   |

FACTURA VERSIÓN 1.1.0

En esta versión se podrá utilizar de 2 a 6 decimales en los campos de cantidad y
precio unitario para contribuyentes que lo requieran.

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                          |     |     |     |              |     |           |               |
| ---------------------------------------- | --- | --- | --- | ------------ | --- | --------- | ------------- |
|                                          |     |     |     |              |     | C A M P O | F O R M A T O |
| <?xml version="1.0" encoding="UTF-8" ?>  |     |     |     | Obligatorio  |     | -         | -             |
<factura id="comprobante" version="1.1.0">  Obligatorio  -  -
| <infoTributaria>  |     |     |     | Obligatorio  |     | -   | -   |
| ----------------- | --- | --- | --- | ------------ | --- | --- | --- |
<ambiente>1 </ambiente>  Obligato ri o ,  c o nforme  Numérico  1

ta b l a  4
Obligato ri o ,  c o nforme
| <tipoEmision>1 </ tipoEmision>  |     |     |     |     |     | Numérico  | 1   |
| ------------------------------- | --- | --- | --- | --- | --- | --------- | --- |
ta b l a  2
< r a z o n S o cia l >E M P R E S A  P U B L IC A   D E HIDROCARBUROS DEL ECUADOR  Obligatorio  Alfanumérico  Max 300

| E P   P E T R O | E C U A D O R < /ra | z on S o ci al > |     |     |     |     |     |
| --------------- | ------------------- | ---------------- | --- | --- | --- | --- | --- |
< n o m b re C o m er ci al > E M P R E S A  P U B L I C A  D E  H ID R O C A R BUROS DEL  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300
|                           |                         |                         |                   |                    |     |           |     |
| ------------------------- | ----------------------- | ----------------------- | ----------------- | ------------------ | --- | --------- | --- |
| E C U A D O               | R   EP  P E T R O E C U | A D O R < /  n o m b re | C om e rc ia l  > | c o rr e s p o n d | a   |           |     |
| <ruc>1768153530001</ruc>  |                         |                         |                   | Obligatorio        |     | Numérico  | 13  |
< c la v e A c c e s o>0403201301179226110400110015010000000081234567816</cl Obligato ri o ,  c o nforme  Numérico  49
| av e A c c e s | o >   |     |     | ta b l a  1   |     |     |     |
| -------------- | ----- | --- | --- | ------------- | --- | --- | --- |
<codDoc>01</codDoc>  Obligato ri o ,  c o nforme  Numérico  2

ta b l a  3
| <estab>001</estab>    |     |     |     | Obligatorio  |     | Numérico  | 3   |
| --------------------- | --- | --- | --- | ------------ | --- | --------- | --- |
| <ptoEmi>501</ptoEmi>  |     |     |     | Obligatorio  |     | Numérico  | 3   |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Alpallana</dirMatriz>
|     |     |     |     | Obligatorio  |     | Alfanumérico  | Max 300  |
| --- | --- | --- | --- | ------------ | --- | ------------- | -------- |

| </infoTributaria>  |     |     |     | Obligatorio  |     | -   | -   |
| ------------------ | --- | --- | --- | ------------ | --- | --- | --- |
| <infoFactura>      |     |     |     | Obligatorio  |     | -   | -   |
<fechaEmision>04/03/2013</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
|     |     |     |     | Obli g a t o ri o   c u | an do  |     |     |
| --- | --- | --- | --- | ----------------------- | ------ | --- | --- |
<dirEstablecimiento>Alpallana</ dirEstablecimiento >  Alfanumérico  Max 300
c o rr e s p o n d a
<contribuyenteEspecial>5368</contribuyenteEspecial>  Obl ig a t o ri o  c u a n do  Alfanumérico  Min 3 Max 13
c o rr e s p o n d a
<obligadoContabilidad>SI</ obligadoContabilidad >  Obl ig a t o ri o  c u a n do  Texto  SI / NO

c o rr e s p o n d a
Obligato ri o ,  c o nforme
<tipoIdentificacionComprador>04</ tipoIdentificacionComprador >    Numérico  2
ta b l a  6
<guiaRemision>001-001-000000001</guiaRemision>  Obl ig a t o ri o  c u a n do  Numérico  15
c o rr e s p o n d a
< ra z o n S oc ia l C o m p ra d o r> P R U E B A S  S ERVICIO DE RENTAS  Obligatorio  Alfanumérico  Max 300

| IN T E R N A | S < / ra z on S o c ia lC | o m p r ad o r> |     |     |     |     |     |
| ------------ | ------------------------- | --------------- | --- | --- | --- | --- | --- |
<identificacionComprador>1760013210001</ identificacionComprador >  Obligatorio  Alfanumérico  Max 20
<direccionComprador>salinas y santiago</direccionComprador>  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300

c o rr e s p o n d a
<totalSinImpuestos>150.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
Obligatorio cuando
| <codDocReembolso>41</codDocReembolso>  |     |     |     |     |     | Numérico  | 2   |
| -------------------------------------- | --- | --- | --- | --- | --- | --------- | --- |
corresponda a Reembolso
(41)
Obligatorio cuando
<codDocReemb>> sea
<totalComprobantesReembolso>150.00</totalComprobantesReembolso>  igual a 41, sumatoria de  Numérico  Max 14
<totalBaseImponibleReemb
olso> y

86

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |     |           |               |
| --- | --- | --- | --- | --------- | ------------- |
|     |     |     |     | C A M P O | F O R M A T O |
<totalImpuestoReembolso>.
Obligatorio cuando
<codDocReemb> sea igual
a 41, en base a la
<totalBaseImponibleReembolso>133.93</totalBaseImponibleReembolso>  información <reembolsos>,  Numérico  Max 14
sumatoria de
<baseImponibleReembolso
>.
Obligatorio cuando
<codDocReemb>> sea
<totalImpuestoReembolso>16.07</totalImpuestoReembolso>  igual a 41, en base a la  Numérico  Max 14
información <reembolsos>
sumatoria de
<impuestoReembolso>.
| <totalConImpuestos>  |     | Obligatorio  |     | -   | -   |
| -------------------- | --- | ------------ | --- | --- | --- |
| <totalImpuesto>      |     | Obligatorio  |     | -   | -   |
<codigo>2</codigo >  Obligat o r io ,  c o n forme  Numérico  1

t a b la   1 6
|     |     | Obligat o r io ,  | c o n forme  |     |     |
| --- | --- | ----------------- | ------------ | --- | --- |
<codigoPorcentaje>6</ codigoPorcentaje>    Numérico  Min 1 M ax 4
t a b la   1 7
<descuentoAdicional>0.00</descuentoAdicional>  O p c io n a l ,  a p li c a   p a r a   Numérico  Max 14
|     |     | c ó d ig o   i m p | u e s t o   2 .   |     |     |
| --- | --- | ------------------ | ----------------- | --- | --- |
<baseImponible>150.00</ baseImponible >  Obligatorio  Numérico  Max 14
| <valor>0.00</valor >     |     | Obligatorio  |     | Numérico  | Max 14  |
| ------------------------ | --- | ------------ | --- | --------- | ------- |
| </totalImpuesto >        |     | Obligatorio  |     | -         | -       |
| </totalConImpuestos >    |     | Obligatorio  |     | -         | -       |
| <propina>0.00</propina>  |     | Obligatorio  |     | Numérico  | Max 14  |
<importeTotal>150.13</ importeTotal>  Obligatorio  Numérico  Max 14
<moneda>DOLAR</moneda>  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 15
|          |     | c o rr e s p | o n d a   |     |     |
| -------- | --- | ------------ | --------- | --- | --- |
| <pagos>  |     | Obligatorio  |           | -   |     |
| <pago>   |     | Obligatorio  |           | -   |     |

Obligatorio, cuando
| <formaPago>01</formaPago>  |     |     |     | Numérico  | 2   |
| -------------------------- | --- | --- | --- | --------- | --- |
corresponda conforme
tabla 24
| <total>150.13</total>  |     | Obligatorio  |     | Numérico  | Max 14  |
| ---------------------- | --- | ------------ | --- | --------- | ------- |
<plazo>0<plazo>  Obli g a t o r io ,  c u a n do  Numérico  Max 14
|     |     | c o r r e s p | o n d a   |     |     |
| --- | --- | ------------- | --------- | --- | --- |
<unidadTiempo>dias</unidadTiempo>  Obli g a t o r io ,  c u a n do  Texto  Max 10

|                                  |     | c o r r e s p | o n d a |           |         |
| -------------------------------- | --- | ------------- | ------- | --------- | ------- |
| </pago>                          |     | Obligatorio   |         | -         | -       |
| <pagos>                          |     | Obligatorio   |         | -         | -       |
| <valorRetIva>0.00</valorRetIva>  |     | Opcional      |         | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  |     | Obligatorio  |     | -   | -   |
| --------------- | --- | ------------ | --- | --- | --- |
| <detalles>      |     | Obligatorio  |     | -   | -   |
| <detalle>       |     | Obligatorio  |     | -   | -   |
<codigoPrincipal>003</codigoPrincipal >  Obligatorio  Alfanumérico  Max 25
<codigoAuxiliar>001</codigoAuxiliar>  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 25
|     |     | c o rr e s p | o n d a   |     |     |
| --- | --- | ------------ | --------- | --- | --- |
<descripcion> Reembolso de Gastos </descripcion>  Obligatorio  Alfanumérico  Max 300
Max 18,
<cantidad>1.000000</cantidad>  Obligatorio  Numérico  hasta 6
decimales
Max 18,
<precioUnitario>150.000000</precioUnitario>  Obligatorio  Numérico  hasta 6
decimales
| <descuento>0.00</descuento>  |     | Obligatorio  |     | Numérico  | Max 14  |
| ---------------------------- | --- | ------------ | --- | --------- | ------- |
<precioTotalSinImpuesto>150.00</ precioTotalSinImpuesto>  Obligatorio  Numérico  Max 14
| <detallesAdicionales>  |     | Obl ig a t o ri o |  c u a n do  | -   | -   |
| ---------------------- | --- | ----------------- | ------------ | --- | --- |

|     |     | c o rr e s p | o n d a |     |     |
| --- | --- | ------------ | ------- | --- | --- |
< d e t A d ici on a l  n o m b r e ="PARTES Y PIEZAS DE COMPUTADORA"  Obl ig a t o ri o  c u a n do
|                         |                  |                   |              | Alfanumérico  | Max 300  |
| ----------------------- | ---------------- | ----------------- | ------------ | ------------- | -------- |
| va l o r = "M O U       | S E   H P "/ >   | c o rr e s p      | o n d a      |               |          |
| </detallesAdicionales>  |                  | Obl ig a t o ri o |  c u a n do  | -             | -        |
|                         |                  | c o rr e s p      | o n d a      |               |          |
| <impuestos>             |                  | Obligatorio       |              | -             | -        |

87

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|             |     |     |     |              |     |           |               |
| ----------- | --- | --- | --- | ------------ | --- | --------- | ------------- |
|             |     |     |     |              |     | C A M P O | F O R M A T O |
| <impuesto>  |     |     |     | Obligatorio  |     | -         | -             |
<codigo>2</codigo>  Obligat o r io ,  c o n forme  Numérico  1

|     |     |     |     |         | t a b la   1 6         |     |     |
| --- | --- | --- | --- | ------- | ---------------------- | --- | --- |
|     |     |     |     | Obligat | o r io ,  c o n forme  |     |     |
<codigoPorcentaje>6</codigoPorcentaje>  Numérico  Min 1 Max 4
|     |     |     |     |     | t a b la   1 7   |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- |
Min 1 Max 4
| <tarifa>0</ tarifa>  |     |     |     | Obligatorio  |     | Numérico  |     |
| -------------------- | --- | --- | --- | ------------ | --- | --------- | --- |
/ 2 enteros, 2
decimales
<baseImponible>150.00</baseImponible>
|     |     |     |     | Obligatorio  |     | Numérico  | Max 14  |
| --- | --- | --- | --- | ------------ | --- | --------- | ------- |

| <valor>0.00</valor>  |     |     |     | Obligatorio  |     | Numérico  | Max 14  |
| -------------------- | --- | --- | --- | ------------ | --- | --------- | ------- |
| </impuesto>          |     |     |     | Obligatorio  |     | -         | -       |
| </impuestos>         |     |     |     | Obligatorio  |     | -         | -       |
| </detalle>           |     |     |     | Obligatorio  |     | -         | -       |
| </detalles>          |     |     |     | Obligatorio  |     | -         | -       |
Obligatorio cuando
| <reembolsos>  |     |     |     |     |     | -   | -   |
| ------------- | --- | --- | --- | --- | --- | --- | --- |
<codDocReemb> sea igual
a 41
Obligatorio cuando
| <reembolsoDetalle>  |     |     |     |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
<codDocReemb> sea igual
a 41
Obligatorio cuando
< ti po I d e n t if icacionProveedorReembolso>04</tipoIdentificacionProveedorR Numérico  2
|                |     |     |     | <c o d D o c R | e e m b > s e a   ig u al  |     |     |
| -------------- | --- | --- | --- | -------------- | -------------------------- | --- | --- |
| ee m b o l s o | >   |     |     | a   4 1,  c o  | n f o rm e   ta b l a  6   |     |     |
Obligatorio cuando
< i d e n t if ic a ci o n P roveedorReembolso>1760013210001</identificacionProvee Alfanumérico  Max 13
| d o r R e e m b | o l so >   |     |     | <codDocRe | e m b > sea igual  |     |     |
| --------------- | ---------- | --- | --- | --------- | ------------------ | --- | --- |
|                 |            |     |     |           | a   41             |     |     |
Obligatorio cuando
< co d PaisPagoProveedorReembolso>593</codPaisPagoProveedorReembol Numérico  3
| so >   |     |     |     | <c o d D o c R | e e m b >   s e a   i g ua    | l   |     |
| ------ | --- | --- | --- | -------------- | ----------------------------- | --- | --- |
|        |     |     |     | a  4 1 ,  c o  | n fo r m e  t a b l a   2 5   |     |     |
Obligatorio cuando
<tipoProveedorReembolso>01</tipoProveedorReembolso>  Numérico  2
<codDocReemb> sea igual
a 41, conforme tabla 26
Obligatorio cuando
<codDocReembolso>01</codDocReembolso>  <codDocReemb> sea igual  Numérico  2
a 41, conforme tabla 3
Obligatorio cuando
<estabDocReembolso>001</estabDocReembolso>  <codDocReemb> sea igual  Numérico  3
a 41
Obligatorio cuando
<ptoEmiDocReembolso>501</ptoEmiDocReembolso>  <codDocReemb> sea igual  Numérico  3
a 41
Obligatorio cuando
<secuencialDocReembolso>000000008</secuencialDocReembolso>  <codDocReemb> sea igual  Numérico  9
a 41
Obligatorio cuando
<fechaEmisionDocReembolso>04/03/2013</fechaEmisionDocReembolso>  <codDocReemb> sea igual  Fecha  dd/mm/aaaa
a 41
Obligatorio cuando
| < n u m e r o a | u t o r iz a c i o n D o c | R e e m b > 0 4 0 32 0     | 1 3 0 1 1 79 2 2 61104001100150100000 |           |                    |           |              |
| --------------- | -------------------------- | -------------------------- | ------------------------------------- | --------- | ------------------ | --------- | ------------ |
|                 |                            |                            |                                       | <codDocRe | e m b > sea igual  | Numérico  | 10, 37 o 49  |
| 00 0 8 1 2 3 4  | 5 6 7 8 1 6 < / n u m e r  | o a u to r iz a c io n D o | c R e e m b >                         |           |                    |           |              |
|                 |                            |                            |                                       |           | a   41             |           |              |
Obligatorio cuando
| <detalleImpuestos>  |     |     |     |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
<codDocReemb> sea igual
a 41
Obligatorio cuando
| <detalleImpuesto>  |     |     |     |     |     | -   | -   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
<codDocReemb> sea igual
a 41
Obligatorio cuando
| <codigo>2</codigo>  |     |     |     |     |     | Numérico  | 1   |
| ------------------- | --- | --- | --- | --- | --- | --------- | --- |
<codDocReemb> sea igual
a 41, conforme tabla 16
Obligatorio cuando
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
<codDocReemb> sea igual
a 41, conforme tabla 17
|                      |     |     |     | Obligatorio cuando       |       |           | Min 1 Max 4 /  |
| -------------------- | --- | --- | --- | ------------------------ | ----- | --------- | -------------- |
| <tarifa>12</tarifa>  |     |     |     |                          |       | Numérico  |                |
|                      |     |     |     | <codDocReemb> sea igual  |       |           | 2 enteros, 2   |
|                      |     |     |     |                          | a 41  |           | decimales      |
Obligatorio cuando
<baseImponibleReembolso>133.93</baseImponibleReembolso>  Numérico  Max 14
<codDocReemb> sea igual
a 41
Obligatorio cuando
<impuestoReembolso>16.07</impuestoReembolso>  Numérico  Max 14
<codDocReemb> sea igual
a 41
Obligatorio cuando
| </detalleImpuesto>  |     |     |     |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
<codDocReemb> sea igual
a 41
| </detalleImpuestos>  |     |     |     | Obligatorio cuando  |     | -   | -   |
| -------------------- | --- | --- | --- | ------------------- | --- | --- | --- |
<codDocReemb> sea igual

88

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /

|     |     |     |     |     |     |     | C A M P O | F O R M A T O |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- |
a 41
Obligatorio cuando
| </reembolsoDetalle>  |     |     |     |     |     |     | -   | -   |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
<codDocReemb> sea igual
a 41
Obligatorio cuando
| </reembolsos>  |     |     |     |     |     |     | -   | -   |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
<codDocReemb>sea igual
a 41
Obligatorio cuando
| <retenciones>  |     |     |     |     | corresponda. Aplica para  |     | -   | -   |
| -------------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
comercializadores de
Derivados de Petróleo.
| <retencion>  |     |     |     |     | Obl ig a t o ri | o  c u a n do  | -   | -   |
| ------------ | --- | --- | --- | --- | --------------- | -------------- | --- | --- |
|              |     |     |     |     | c o rr e s      | p o n d a      |     |     |
Obligatorio cuando
| <codigo>4</codigo>  |     |     |     |     |     |     | Numérico  | 1   |
| ------------------- | --- | --- | --- | --- | --- | --- | --------- | --- |
corresponda conforme
tabla 22
Obligatorio cuando
<codigoPorcentaje>327</codigoPorcentaje>  corresponda conforme  Numérico  Min 1 Max 3
tabla 23
Min 1 Max 5 /
|                        |     |     |     |     | Obl ig a t o ri | o  c u a n do  |           | 3 en t e r os,  |
| ---------------------- | --- | --- | --- | --- | --------------- | -------------- | --------- | --------------- |
| <tarifa>0.20</tarifa>  |     |     |     |     |                 |                | Numérico  |                 |
|                        |     |     |     |     | c o rr e s      | p o n d a      |           | d o s           |
decimales
Max 14 /12
<valor>0.13</valor>  Obl ig a t o ri o  c u a n do  Numérico
|     |     |     |     |     |            |           |     | e n te ro s ,  2   |
| --- | --- | --- | --- | --- | ---------- | --------- | --- | ------------------ |
|     |     |     |     |     | c o rr e s | p o n d a |     |                    |
d e c im a l e s
|                  |     |     |     |     | Obl ig a t o ri | o  c u a n do  |     |     |
| ---------------- | --- | --- | --- | --- | --------------- | -------------- | --- | --- |
| </retencion>     |     |     |     |     |                 |                | -   | -   |
|                  |     |     |     |     | c o rr e s      | p o n d a      |     |     |
| </retenciones>   |     |     |     |     | Obl ig a t o ri | o  c u a n do  | -   | -   |
|                  |     |     |     |     | c o rr e s      | p o n d a      |     |     |
| <infoAdicional>  |     |     |     |     | Obl ig a t o ri | o  c u a n do  | -   | -   |

|     |     |     |     |     | c o rr e s | p o n d a |     |     |
| --- | --- | --- | --- | --- | ---------- | --------- | --- | --- |
< c a m p o A d ic io n a l  n o m b re = " DESCRIPCION DE CARGA "> CAJAS DE 10  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300
|                 |                  |         |     |     |            |           |     |     |
| --------------- | ---------------- | ------- | --- | --- | ---------- | --------- | --- | --- |
| K IL O S   < /c | a m p o A d i ci | on a l> |     |     | c o rr e s | p o n d a |     |     |
< c a m p o A d ic io n a ln om b r e = "  IN F O R M A C I O N   B A N C ARIA "> NUMERO DE  Obl ig a t o ri o  c u a n do  Alfanumérico  Max 300
|                   |            |                     |                           |     |                 |                |     |     |
| ----------------- | ---------- | ------------------- | ------------------------- | --- | --------------- | -------------- | --- | --- |
| C U E N T A   D   | E  B A N C | O  1 2 4 3 5 46 < / | ca m p o A d ic i o na l> |     | c o rr e s      | p o n d a      |     |     |
| </infoAdicional>  |            |                     |                           |     | Obl ig a t o ri | o  c u a n do  | -   | -   |

|             |     |     |     |     | c o rr e s   | p o n d a |     |     |
| ----------- | --- | --- | --- | --- | ------------ | --------- | --- | --- |
| </factura>  |     |     |     |     | Obligatorio  |           | -   | -   |

TABLA 26: Tipo Proveedor de Reembolso

TIPO  CÓDIGO
|     |     |     | PERSONA NATURAL  | 01  |     |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
SOCIEDAD  02

| ANEXO      |     | 6   | -  FORMATOS  | XML  | FACTURA  |            |     | CON  |
| ---------- | --- | --- | ------------ | ---- | -------- | ---------- | --- | ---- |
| SUBSIDIOS  |     |     | APLICADO     | EN   | LAS      | VERSIONES  |     |      |
1.0.0 y 1.1.0

Incluyen los campos requeridos exclusivamente solo para subsidio; caso contrario
se deberá utilizar los formatos de factura establecidos en el anexo 1 y anexo 3
según corresponda12.

12 Resolución NAC-DGERCGC15-00003184, publicada en el Registro Oficial 661 de 4 de enero de 2016

89

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
FACTURA VERSIÓN 1.0.0

|                                          | ETIQUETAS O TAGS  | CARACTER     | T I P O  D E   | L O N G IT U D   |
| ---------------------------------------- | ----------------- | ------------ | -------------- | ---------------- |
|                                          |                   |              |                |                  |
|                                          |                   |              | C A M P O      | /  F O R M A T O |
| <?xml version="1.0" encoding="UTF-8" ?>  |                   | Obligatorio  | -              | -                |
-<factura id="comprobante" version="1.0.0">  Obligatorio  -  -
| - <infoTributaria>      |     | Obligatorio            | -         | -   |
| ----------------------- | --- | ---------------------- | --------- | --- |
| <ambiente>1</ambiente>  |     | O b li ga t o ri o ,   | Numérico  | 1   |
 4
con fo r m e   ta b l a
O b li ga t o ri o ,
| <tipoEmision>1</tipoEmision>  |     |  2  | Numérico  | 1   |
| ----------------------------- | --- | --- | --------- | --- |
con fo r m e   ta b l a
<razonSocial>SERVICIO DE RENTAS INTERNAS</razonSocial>  Obligatorio  Alfanumérico  Max 300
|     |     | Obli g a t o r io ,  c u a n do  |     |     |
| --- | --- | -------------------------------- | --- | --- |
<nombreComercial>SRI</nombreComercial>  Alfanumérico  Max 300
c o r r e s p o n d a
| <ruc>1760013210001</ruc>  |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | ------------ | --------- | --- |
<claveAcceso>0601201601176001321000110011230000000081234567817</claveAcceso>  O b l i ga t o ri o ,   Numérico  49
|                      |     | con f o r m e   ta b l a  1  |           |     |
| -------------------- | --- | ---------------------------- | --------- | --- |
| <codDoc>01</codDoc>  |     | O b li ga t o ri o ,         | Numérico  | 2   |
 3
con fo r m e   ta b l a
| <estab>001</estab>    |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | ------------ | --------- | --- |
| <ptoEmi>123</ptoEmi>  |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>SALINAS</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     | Obligatorio  | -   | -   |
| ------------------ | --- | ------------ | --- | --- |
| <infoFactura>      |     | Obligatorio  | -   | -   |
<fechaEmision>06/01/2016</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
<dirEstablecimiento>PÁEZ</dirEstablecimiento>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300
c o r r e s p o n d a
<contribuyenteEspecial>123A</contribuyenteEspecial>  Obli g a t o r io ,  c u a n do  Alfanumérico  Min  3  M ax
|     |     |                       |     |     |
| --- | --- | --------------------- | --- | --- |
|     |     | c o r r e s p o n d a |     | 1 3 |
<obligadoContabilidad>SI</obligadoContabilidad>  Obli g a t o r io ,  c u a n do  Texto  SI/NO

c o r r e s p o n d a
<tipoIdentificacionComprador>04</tipoIdentificacionComprador>  O b li ga t o ri o ,   Numérico  2
con fo r m e   ta b l a  6
<razonSocialComprador>EMPRESA ABC</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionComprador>1794567890001</identificacionComprador>  Obligatorio  Numérico  Max 13
|     |     | Obli g a t o r io ,  c u a n do  |     |     |
| --- | --- | -------------------------------- | --- | --- |
<direccionComprador>salinas y santiago</direccionComprador>    Alfanumérico  Max 300
c o r r e s p o n d a
<totalSinImpuestos>25.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
Opcional y se llenará
<totalSubsidio>10.00</totalSubsidio>  cuando exista el tag  Numérico  Max 14
<precioSinSubsidio>.
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  |     | Obligatorio           | -         | -   |
| -------------------- | --- | --------------------- | --------- | --- |
| <totalImpuesto>      |     | Obligatorio           | -         | -   |
| <codigo>2</codigo>   |     | O b lig a t o r io ,  | Numérico  | 1   |
con fo rm e   t a b la  16
<codigoPorcentaje>2</codigoPorcentaje>  O b lig a t o r io ,  Numérico  Min 1 Max 4
 17
con fo rm e   t a b la
<baseImponible>25.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>3.00</valor>      |     | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | --- | ------------ | --------- | ------- |
| </totalImpuesto>         |     | Obligatorio  | -         | -       |
| </totalConImpuestos>     |     | Obligatorio  | -         | -       |
| <propina>0.00</propina>  |     | Obligatorio  | Numérico  | Max 14  |
<importeTotal>28.00</importeTotal>  Obligatorio  Numérico  Max 14
<moneda>DOLAR</moneda>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 15
c o r r e s p o n d a
| <pagos>  |     | Obligatorio  | -   | -   |
| -------- | --- | ------------ | --- | --- |
| <pago>   |     | Obligatorio  | -   |     |

<formaPago>19</formaPago>  O b lig a t o r io ,  Numérico  2
 24
con fo rm e   t a b la
| <total>28,000</total>  |     | Obligatorio  | Numérico  | Max 14  |
| ---------------------- | --- | ------------ | --------- | ------- |
<plazo>30<plazo>  Obli g a t o r io ,  c u a n do  Numérico  Max 14

c o r r e s p o n d a
|                                    |     | Obli g a t o r io ,  c u a n do  |        |         |
| ---------------------------------- | --- | -------------------------------- | ------ | ------- |
| <unidadTiempo>dias</unidadTiempo>  |     |                                  | Texto  | Max 10  |
c o r r e s p o n d a

90

|           |                   |              |                |                  |
| --------- | ----------------- | ------------ | -------------- | ---------------- |
|           | ETIQUETAS O TAGS  | CARACTER     | T I P O  D E   | L O N G IT U D   |
|           |                   |              |                |                  |
|           |                   |              | C A M P O      | /  F O R M A T O |
| </pago>   |                   | Obligatorio  | -              | -                |
| </pagos>  |                   | Obligatorio  |                |                  |
<valorRetIva>10620.00</valorRetIva>  Opcional  Numérico  Max 14
<valorRetRenta>2950.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  |     | Obligatorio  | -   | -   |
| --------------- | --- | ------------ | --- | --- |
| <detalles>      |     | Obligatorio  | -   | -   |
| <detalle>       |     | Obligatorio  | -   | -   |
Obligatorio, (para
<codigoPrincipal>0011</codigoPrincipal>  Alfanumérico  Max 25
venta de combustible
ver tabla 30)
|     |     | Obli g a t o r io ,  c u a n do  |     |     |
| --- | --- | -------------------------------- | --- | --- |
<codigoAuxiliar>0011</codigoAuxiliar>    Alfanumérico  Max 25
c o r r e s p o n d a
Obligatorio, (para
<descripcion>COMBUSTIBLE</descripcion>  venta de combustible  Alfanumérico  Max 300
ver tabla 30)
| <cantidad>1</cantidad>  |     | Obligatorio  | Numérico  | Max 14  |
| ----------------------- | --- | ------------ | --------- | ------- |
<precioUnitario>25</precioUnitario>  Obligatorio  Numérico  Max 14
<precioSinSubsidio>35.00</precioSinSubsidio>  Obl ig a t o ri o ,  c u a n do  Numérico  Max 14

c o rr e s p o n d a .
| <descuento>0</descuento>  |     | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | --- | ------------ | --------- | ------- |
<precioTotalSinImpuesto>25.00</precioTotalSinImpuesto>  Obligatorio.  Numérico  Max 14
| <impuestos>         |     | Obligatorio           | -         | -   |
| ------------------- | --- | --------------------- | --------- | --- |
| <impuesto>          |     | Obligatorio           | -         | -   |
| <codigo>2</codigo>  |     | O b lig a t o r io ,  | Numérico  | 1   |
 16
con fo rm e   t a b la
O b lig a t o r io ,
<codigoPorcentaje>2</codigoPorcentaje>   17  Numérico  Min 1 Max 4
con fo rm e   t a b la
Min 1 Max
| <tarifa>12.00</tarifa>  |     | Obligatorio  | Numérico  | 4 / 2  |
| ----------------------- | --- | ------------ | --------- | ------ |
enteros, 2
decimales
<baseImponible>25.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>3.00</valor>  |     | Obligatorio  | Numérico  | Max 14  |
| -------------------- | --- | ------------ | --------- | ------- |
| </impuesto>          |     | Obligatorio  | -         | -       |
| </impuestos>         |     | Obligatorio  | -         | -       |
| </detalle>           |     | Obligatorio  | -         | -       |
| </detalles>          |     | Obligatorio  | -         | -       |
| </factura>           |     | Obligatorio  | -         | -       |

FACTURA VERSIÓN 1.1.0

En esta versión se podrá utilizar de 2 a 6 decimales en los campos de cantidad y
precio unitario para contribuyentes que lo requieran.

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                          |     |              | C A M P O   | F O R M A T O   |
| ---------------------------------------- | --- | ------------ | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8" ?>  |     | Obligatorio  | -           | -               |
-<factura id="comprobante" version="1.1.0">  Obligatorio  -  -
| - <infoTributaria>  |     | Obligatorio  | -   | -   |
| ------------------- | --- | ------------ | --- | --- |
O b li ga t o ri o ,
| <ambiente>1</ambiente>  |     |     | Numérico  | 1   |
| ----------------------- | --- | --- | --------- | --- |
con fo r m e   ta b l a  4
<tipoEmision>1</tipoEmision>  O b li ga t o ri o ,   Numérico  1
con fo r m e   ta b l a  2
<razonSocial>SERVICIO DE RENTAS INTERNAS</razonSocial>  Obligatorio  Alfanumérico  Max 300
<nombreComercial>SRI</nombreComercial>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300
c o r r e s p o n d a
| <ruc>1760013210001</ruc>  |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | ------------ | --------- | --- |
<claveAcceso>0601201601176001321000110011230000000081234567817</claveAcceso>  O b l i ga t o ri o ,   Numérico  49
|                      |     | con f o r m e   ta b l a  1  |           |     |
| -------------------- | --- | ---------------------------- | --------- | --- |
| <codDoc>01</codDoc>  |     | O b li ga t o ri o ,         | Numérico  | 2   |
 3
con fo r m e   ta b l a
| <estab>001</estab>    |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | ------------ | --------- | --- |
| <ptoEmi>123</ptoEmi>  |     | Obligatorio  | Numérico  | 3   |

91

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
<secuencial>000000008</secuencial>  Obligatorio  Numérico  9
<dirMatriz>SALINAS</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  | Obligatorio  | -   | -   |
| ------------------ | ------------ | --- | --- |
| <infoFactura>      | Obligatorio  | -   | -   |
<fechaEmision>06/01/2016</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
<dirEstablecimiento>PÁEZ</dirEstablecimiento>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300
c o r r e s p o n d a
<contribuyenteEspecial>123A</contribuyenteEspecial>  Obli g a t o r io ,  c u a n do  Alfanumérico  Min 3 Max 13

c o r r e s p o n d a
|     | Obli g a t o r io ,  c u a n do  |     |     |
| --- | -------------------------------- | --- | --- |
<obligadoContabilidad>SI</obligadoContabilidad>    Texto  SI/NO
c o r r e s p o n d a
<tipoIdentificacionComprador>04</tipoIdentificacionComprador>  O b li ga t o ri o ,   Numérico  2
con fo r m e   ta b l a  6
<razonSocialComprador>EMPRESA ABC</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionComprador>1794567890001</identificacionComprador>  Obligatorio  Numérico  Max 13
<direccionComprador>salinas y santiago</direccionComprador>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 300

c o r r e s p o n d a
<totalSinImpuestos>25.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
Opcional y se llenará
| <totalSubsidio>10.00</totalSubsidio>  |     | Numérico  | Max 14  |
| ------------------------------------- | --- | --------- | ------- |
cuando exista el tag
<precioSinSubsidio>.
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  | Obligatorio  | -   | -   |
| -------------------- | ------------ | --- | --- |
| <totalImpuesto>      | Obligatorio  | -   | -   |
O b lig a t o r io ,
| <codigo>2</codigo>  |  16  | Numérico  | 1   |
| ------------------- | ---- | --------- | --- |
con fo rm e   t a b la
<codigoPorcentaje>2</codigoPorcentaje>  O b lig a t o r io ,  Numérico  Min 1 Max 4
con fo rm e   t a b la  17
<baseImponible>25.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>3.00</valor>      | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </totalImpuesto>         | Obligatorio  | -         | -       |
| </totalConImpuestos>     | Obligatorio  | -         | -       |
| <propina>0.00</propina>  | Obligatorio  | Numérico  | Max 14  |
<importeTotal>28.00</importeTotal>  Obligatorio  Numérico  Max 14
<moneda>DOLAR</moneda>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 15

c o r r e s p o n d a
| <pagos>  | Obligatorio  | -   | -   |
| -------- | ------------ | --- | --- |
| <pago>   | Obligatorio  | -   |     |
<formaPago>20</formaPago>  O b lig a t o r io ,  Numérico  2
con fo rm e   t a b la  24
| <total>28,000</total>  | Obligatorio  | Numérico  | Max 14  |
| ---------------------- | ------------ | --------- | ------- |
<plazo>30<plazo>  Obli g a t o r io ,  c u a n do  Numérico  Max 14
c o r r e s p o n d a
<unidadTiempo>dias</unidadTiempo>  Obli g a t o r io ,  c u a n do  Texto  Max 10

c o r r e s p o n d a
| </pago>                          | Obligatorio  | -         | -       |
| -------------------------------- | ------------ | --------- | ------- |
| </pagos>                         | Obligatorio  | -         | -       |
| <valorRetIva>0.00</valorRetIva>  | Opcional     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |
| <detalles>      | Obligatorio  | -   | -   |
| <detalle>       | Obligatorio  | -   | -   |
Obligatorio, (para
<codigoPrincipal>0011</codigoPrincipal>  venta de combustible  Alfanumérico  Max 25
ver tabla 30)
<codigoAuxiliar>0011</codigoAuxiliar>  Obli g a t o r io ,  c u a n do  Alfanumérico  Max 25
c o r r e s p o n d a
Obligatorio, (para
<descripcion>COMBUSTIBLE</descripcion>  Alfanumérico  Max 300
venta de combustible
ver tabla 30)
Max 18,
| <cantidad>1</cantidad>  | Obligatorio  | Numérico  |     |
| ----------------------- | ------------ | --------- | --- |
hasta 6
decimales
Max 18,
| <precioUnitario>25</precioUnitario>  | Obligatorio  | Numérico  |     |
| ------------------------------------ | ------------ | --------- | --- |
hasta 6
decimales
<precioSinSubsidio>35.00</precioSinSubsidio>  Numérico  Max 14
Obligatorio, cuando

92

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
corresponda.
| <descuento>0</descuento>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
<precioTotalSinImpuesto>25.00</precioTotalSinImpuesto>  Obligatorio.  Numérico  Max 14
| <impuestos>         | Obligatorio           | -         | -   |
| ------------------- | --------------------- | --------- | --- |
| <impuesto>          | Obligatorio           | -         | -   |
| <codigo>2</codigo>  | O b lig a t o r io ,  | Numérico  | 1   |
con fo rm e   t a b la  16
<codigoPorcentaje>2</codigoPorcentaje>  O b lig a t o r io ,  Numérico  Min 1 Max 4
con fo rm e   t a b la  17
Min 1 Max 4
<tarifa>12.00</tarifa>  Obligatorio  Numérico  / 2 enteros, 2
decimales
<baseImponible>25.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>3.00</valor>  | Obligatorio  | Numérico  | Max 14  |
| -------------------- | ------------ | --------- | ------- |
| </impuesto>          | Obligatorio  | -         | -       |
| </impuestos>         | Obligatorio  | -         | -       |
| </detalle>           | Obligatorio  | -         | -       |
| </detalles>          | Obligatorio  | -         | -       |
| </factura>           | Obligatorio  | -         | -       |

93

ANEXO 7 – FORMATOS DE
REPRESENTACIÓN IMPRESA DE
DOCUMENTO ELECTRÓNICO CON SUBSIDIO
(RIDE)
Nota:
• El campo VALOR TOTAL SIN SUBSIDIO, corresponde a: precio sin subsidio + IVA según corresponda.
55.00 + 12% = $6.60
55.00 + 6.60 = $61.60
• El campo AHORRO POR SUBSIDIO, corresponde al subsidio + IVA según corresponda.
27.75 + 12% = $3.33
27.75 + 3.33 = $31.08
• La diferencia entre VALOR TOTAL SIN SUBSIDIO menos AHORRO POR SUBSIDIO es igual al valor total de la
factura, es decir: $30.52
94

| ANEXO   | 8  -  FORMATOS  | XML       | FACTURA  |     | CON  |
| ------- | --------------- | --------- | -------- | --- | ---- |
| RUBROS  | DE  TERCEROS    | APLICADO  |          | EN  | LAS  |
VERSIONES 2.0.0 y 2.1.0

Incluyen  los  campos  requeridos  exclusivamente  para  rubros  de  terceros,  caso
contrario se deberá utilizar los formatos de factura establecidos en el anexo 1 y
anexo 3 según corresponda13.

FACTURA VERSIÓN 2.0.0

ETIQUETAS O TAGS  CARACTER  T I P O  D E   L O N G IT U D   /
|                                         |     |     |              | C A M P O   | F O R M A T O   |
| --------------------------------------- | --- | --- | ------------ | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8"?>  |     |     | Obligatorio  | -           | -               |
<factura id="comprobante" version="2.0.0">  Obligatorio  -  -
| <infoTributaria>        |     |     | Obligatorio             | -         | -   |
| ----------------------- | --- | --- | ----------------------- | --------- | --- |
| <ambiente>1</ambiente>  |     |     | O b li ga t o ri o ,    | Numérico  | 1   |
|                         |     |     | con fo r m e   ta b l a |  4        |     |
<tipoEmision>1</tipoEmision>  O b li ga t o ri o ,   Numérico  1
 2
|     |     |     | con fo r m e   ta b l a |     |     |
| --- | --- | --- | ----------------------- | --- | --- |
<razonSocial>PRUEBA</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio,
<nombreComercial>PRUEBA 2</nombreComercial>  cuando  Alfanumérico  Max 300
corresponda
| <ruc>1760013210001</ruc>  |     |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2103201601176001321000110010010000000061234567816</claveAcceso>  Numérico  49
conforme tabla
1
| <codDoc>01</codDoc>  |     |     | O b li ga t o ri o ,   | Numérico  | 2   |
| -------------------- | --- | --- | ---------------------- | --------- | --- |
 3
|                       |     |     | con fo r m e   ta b l a |           |     |
| --------------------- | --- | --- | ----------------------- | --------- | --- |
| <estab>001</estab>    |     |     | Obligatorio             | Numérico  | 3   |
| <ptoEmi>001</ptoEmi>  |     |     | Obligatorio             | Numérico  | 3   |
<secuencial>000000006</secuencial>  Obligatorio  Numérico  9
<dirMatriz>SALINAS</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ------------------ | --- | --- | ------------ | --- | --- |
| <infoFactura>      |     |     | Obligatorio  | -   | -   |
<fechaEmision>21/03/2016</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio,
<dirEstablecimiento>PÁEZ</dirEstablecimiento>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<contribuyenteEspecial>12345</contribuyenteEspecial>  cuando  Alfanumérico  Min 3 Max 13
corresponda
Obligatorio,
<obligadoContabilidad>SI</obligadoContabilidad>  cuando  Texto  SI/NO
corresponda
<tipoIdentificacionComprador>07</tipoIdentificacionComprador>  O b li ga t o ri o ,   Numérico  2
|     |     |     | con fo r m e   ta b l a |  6  |     |
| --- | --- | --- | ----------------------- | --- | --- |
<razonSocialComprador>CONSUMIDOR FINAL</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionComprador>9999999999999</identificacionComprador>  Obligatorio  Numérico  Max 13
Obligatorio,
<direccionComprador>salinas y santiago</direccionComprador>  Alfanumérico  Max 300
cuando
corresponda
<totalSinImpuestos>50.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  |     |     | Obligatorio  | -   | -   |
| -------------------- | --- | --- | ------------ | --- | --- |
| <totalImpuesto>      |     |     | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  |     |     |     | Numérico  | 1   |
| ------------------- | --- | --- | --- | --------- | --- |
conforme tabla
16
<codigoPorcentaje>2</codigoPorcentaje>  Obligatorio,  Numérico  Min 1 Max 4

13 Resolución NAC-DGERCGC15-00003184, publicada en el Registro Oficial 661 de 4 de enero de 2016

95

ETIQUETAS O TAGS  CARACTER  T I P O  D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
conforme tabla
17
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>      | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </totalImpuesto>         | Obligatorio  | -         | -       |
| </totalConImpuestos>     | Obligatorio  | -         | -       |
| <propina>0.00</propina>  | Obligatorio  | Numérico  | Max 14  |
<importeTotal>61.00</importeTotal>  Obligatorio  Numérico  Max 14
Obligatorio,
| <moneda>DOLAR</moneda>  | cuando  | Alfanumérico  | Max 15  |
| ----------------------- | ------- | ------------- | ------- |
corresponda
Obligatorio,
| <pagos>  | cuando  | -   | -   |
| -------- | ------- | --- | --- |
corresponda
| <pago>  | Obligatorio  | -   |     |
| ------- | ------------ | --- | --- |

Obligatorio,
| <formaPago>19</formaPago>  |                 | Numérico  |     |
| -------------------------- | --------------- | --------- | --- |
|                            | conforme tabla  |           | 2   |
24
| <total>61,00</total>  | Obligatorio  | Numérico  | Max 14  |
| --------------------- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>30<plazo>  |         | Numérico  |         |
| ----------------- | ------- | --------- | ------- |
|                   | cuando  |           | Max 14  |
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |         | Texto  |         |
| ---------------------------------- | ------- | ------ | ------- |
|                                    | cuando  |        | Max 10  |
corresponda
| </pago>  | Obligatorio  | -   |     |
| -------- | ------------ | --- | --- |
-
| </pagos>                         | Obligatorio  | -         | -       |
| -------------------------------- | ------------ | --------- | ------- |
| <valorRetIva>0.00</valorRetIva>  | Opcional     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |
| <detalles>      | Obligatorio  | -   | -   |
| <detalle>       | Obligatorio  | -   | -   |
<codigoPrincipal>001</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
Obligatorio,
<codigoAuxiliar>0011</codigoAuxiliar>  cuando  Alfanumérico  Max 25
corresponda
<descripcion>BIEN</descripcion>  Obligatorio  Alfanumérico  Max 300
| <cantidad>1</cantidad>  | Obligatorio  | Numérico  | Max 14  |
| ----------------------- | ------------ | --------- | ------- |
<precioUnitario>50</precioUnitario>  Obligatorio  Numérico  Max 14
| <descuento>0</descuento>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
<precioTotalSinImpuesto>50.00</precioTotalSinImpuesto>  Obligatorio.  Numérico  Max 14
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |
| <impuesto>   | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  | conforme tabla  | Numérico  | 1   |
| ------------------- | --------------- | --------- | --- |
16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  conforme tabla  Numérico  Min 1 Max 4
17
Min 1 Max 4
| <tarifa>12.00</tarifa>  | Obligatorio  | Numérico  |     |
| ----------------------- | ------------ | --------- | --- |
/ 2 enteros, 2
decimales
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>    | Obligatorio  | Numérico  | Max 14  |
| ---------------------- | ------------ | --------- | ------- |
| </impuesto>            | Obligatorio  | -         | -       |
| </impuestos>           | Obligatorio  | -         | -       |
| </detalle>             | Obligatorio  | -         | -       |
| </detalles>            | Obligatorio  | -         | -       |
| <otrosRubrosTerceros>  | Obligatorio  | -         | -       |
| <rubro>                | Obligatorio  | -         | -       |
<concepto>CONCEPTO1</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>10</total>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| ------------------ | ------------ | --------- | ------------ |
| </rubro>           | Obligatorio  | -         | -            |
| <rubro>            | Obligatorio  | -         | -            |
<concepto>CONCEPTO2</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>12</total>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| ------------------ | ------------ | --------- | ------------ |
| </rubro>           | Obligatorio  | -         | -            |
| <rubro>            | Obligatorio  | -         | -            |

96

ETIQUETAS O TAGS  CARACTER  T I P O  D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
<concepto>CONCEPTO3</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>5</total>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| ----------------- | ------------ | --------- | ------------ |
| </rubro>          | Obligatorio  | -         | -            |
| <rubro>           | Obligatorio  | -         | -            |
<concepto>CONCEPTO4</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>25</total>       | Obligatorio  | Numérico  | Min 1 Max 4  |
| ----------------------- | ------------ | --------- | ------------ |
| </rubro>                | Obligatorio  | -         | -            |
| </otrosRubrosTerceros>  | Obligatorio  | -         | -            |
| </factura>              | Obligatorio  | -         | -            |

FACTURA VERSIÓN 2.1.0

En esta versión se podrá utilizar de 2 a 6 decimales en los campos de cantidad y
precio unitario para contribuyentes que lo requieran.

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                         |              |           |               |
| --------------------------------------- | ------------ | --------- | ------------- |
|                                         |              | C A M P O | F O R M A T O |
| <?xml version="1.0" encoding="UTF-8"?>  | Obligatorio  | -         | -             |
<factura id="comprobante" version="2.1.0">  Obligatorio  -  -
| <infoTributaria>  | Obligatorio  | -   | -   |
| ----------------- | ------------ | --- | --- |
Obligatorio,
| <ambiente>1</ambiente>  |     | Numérico  | 1   |
| ----------------------- | --- | --------- | --- |
conforme tabla
4
Obligatorio,
| <tipoEmision>1</tipoEmision>  |     | Numérico  | 1   |
| ----------------------------- | --- | --------- | --- |
conforme tabla
2
<razonSocial>PRUEBA</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio,
<nombreComercial>PRUEBA 2</nombreComercial>  Alfanumérico  Max 300
cuando
corresponda
| <ruc>1760013210001</ruc>  | Obligatorio  | Numérico  | 13  |
| ------------------------- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2103201601176001321000110010010000000061234567816</claveAcceso>  conforme  Numérico  49
tabla 1
Obligatorio,
| <codDoc>01</codDoc>  | conforme tabla  | Numérico  | 2   |
| -------------------- | --------------- | --------- | --- |
3
| <estab>001</estab>    | Obligatorio  | Numérico  | 3   |
| --------------------- | ------------ | --------- | --- |
| <ptoEmi>001</ptoEmi>  | Obligatorio  | Numérico  | 3   |
<secuencial>000000006</secuencial>  Obligatorio  Numérico  9
<dirMatriz>SALINAS</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  | Obligatorio  | -   | -   |
| ------------------ | ------------ | --- | --- |
| <infoFactura>      | Obligatorio  | -   | -   |
<fechaEmision>21/03/2016</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio,
<dirEstablecimiento>PÁEZ</dirEstablecimiento>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<contribuyenteEspecial>12345</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
Obligatorio,
<obligadoContabilidad>SI</obligadoContabilidad>  cuando  Texto  SI/NO
corresponda
Obligatorio,
<tipoIdentificacionComprador>07</tipoIdentificacionComprador>  conforme tabla  Numérico  2
6
<razonSocialComprador>CONSUMIDOR FINAL</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionComprador>9999999999999</identificacionComprador>  Obligatorio  Numérico  Max 13
Obligatorio,
<direccionComprador>salinas y santiago</direccionComprador>  Alfanumérico  Max 300
cuando
corresponda
<totalSinImpuestos>50.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  | Obligatorio  | -   | -   |
| -------------------- | ------------ | --- | --- |
| <totalImpuesto>      | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  |     | Numérico  | 1   |
| ------------------- | --- | --------- | --- |
conforme tabla

97

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme tabla
17
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>      | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </totalImpuesto>         | Obligatorio  | -         | -       |
| </totalConImpuestos>     | Obligatorio  | -         | -       |
| <propina>0.00</propina>  | Obligatorio  | Numérico  | Max 14  |
<importeTotal>61.00</importeTotal>  Obligatorio  Numérico  Max 14
Obligatorio,
| <moneda>DOLAR</moneda>  |     | Alfanumérico  | Max 15  |
| ----------------------- | --- | ------------- | ------- |
cuando
corresponda
| <pagos>  | Obligatorio  | -   | -   |
| -------- | ------------ | --- | --- |
| <pago>   | Obligatorio  | -   |     |

Obligatorio,
| <formaPago>19</formaPago>  | conforme tabla  | Numérico  | 2   |
| -------------------------- | --------------- | --------- | --- |
24
| <total>61,00</total>  | Obligatorio  | Numérico  | Max 14  |
| --------------------- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>30<plazo>  |     | Numérico  | Max 14  |
| ----------------- | --- | --------- | ------- |
cuando
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |     | Texto  | Max 10  |
| ---------------------------------- | --- | ------ | ------- |
cuando
corresponda
| </pago>                          | Obligatorio  | -         | -       |
| -------------------------------- | ------------ | --------- | ------- |
| </pagos>                         | Obligatorio  | -         | -       |
| <valorRetIva>0.00</valorRetIva>  | Opcional     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |
| <detalles>      | Obligatorio  | -   | -   |
| <detalle>       | Obligatorio  | -   | -   |
<codigoPrincipal>001</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
Obligatorio,
| <codigoAuxiliar>0011</codigoAuxiliar>  |     | Alfanumérico  | Max 25  |
| -------------------------------------- | --- | ------------- | ------- |
cuando
corresponda
<descripcion>BIEN</descripcion>  Obligatorio  Alfanumérico  Max 300
Max 18,
| <cantidad>1</cantidad>  | Obligatorio  | Numérico  |     |
| ----------------------- | ------------ | --------- | --- |
hasta 6
decimales
Max 18,
| <precioUnitario>50</precioUnitario>  | Obligatorio  | Numérico  |     |
| ------------------------------------ | ------------ | --------- | --- |
hasta 6
decimales
| <descuento>0</descuento>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
<precioTotalSinImpuesto>50.00</precioTotalSinImpuesto>  Obligatorio.  Numérico  Max 14
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |
| <impuesto>   | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  | conforme tabla  | Numérico  | 1   |
| ------------------- | --------------- | --------- | --- |
16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  conforme tabla  Numérico  Min 1 Max 4
17
Min 1 Max 4
| <tarifa>12.00</tarifa>  | Obligatorio  | Numérico  |     |
| ----------------------- | ------------ | --------- | --- |
/ 2 enteros, 2
decimales
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>    | Obligatorio  | Numérico  | Max 14  |
| ---------------------- | ------------ | --------- | ------- |
| </impuesto>            | Obligatorio  | -         | -       |
| </impuestos>           | Obligatorio  | -         | -       |
| </detalle>             | Obligatorio  | -         | -       |
| </detalles>            | Obligatorio  | -         | -       |
| <otrosRubrosTerceros>  | Obligatorio  | -         | -       |
| <rubro>                | Obligatorio  | -         | -       |

98

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
<concepto>CONCEPTO1</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>1</total>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| ----------------- | ------------ | --------- | ------------ |
| </rubro>          | Obligatorio  | -         | -            |
| <rubro>           | Obligatorio  | -         | -            |
<concepto>CONCEPTO2</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>1</total>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| ----------------- | ------------ | --------- | ------------ |
| </rubro>          | Obligatorio  | -         | -            |
| <rubro>           | Obligatorio  | -         | -            |
<concepto>CONCEPTO3</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>1</total>  | Obligatorio  | Numérico  | Min 1 Max 4  |
| ----------------- | ------------ | --------- | ------------ |
| </rubro>          | Obligatorio  | -         | -            |
| <rubro>           | Obligatorio  | -         | -            |
<concepto>CONCEPTO4</concepto>  Obligatorio  Alfanumérico  Max 300
| <total>1</total>        | Obligatorio  | Numérico  | Min 1 Max 4  |
| ----------------------- | ------------ | --------- | ------------ |
| </rubro>                | Obligatorio  | -         | -            |
| </otrosRubrosTerceros>  | Obligatorio  | -         | -            |
| </factura>              | Obligatorio  | -         | -            |

99

|              |       |           |       |      |           |     |
| ------------ | ----- | --------- | ----- | ---- | --------- | --- |
| ANEXO        | 9  -  | FORMATOS  |       | XML  | FACTURA   |     |
| SUSTITUTIVA  |       | DE        | GUÍA  | DE   | REMISIÓN  |     |
APLICADO EN LAS VERSIONES 2.0.0 y 2.1.0

Incluyen los campos requeridos exclusivamente para la factura sustitutiva de guía
de remisión, caso contrario se deberá utilizar los formatos de factura establecidos
en el anexo 1 y anexo 3 según corresponda14.

FACTURA VERSIÓN 2.0.0

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                         |     |     |     |              | C A M P O   | F O R M A T O   |
| --------------------------------------- | --- | --- | --- | ------------ | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8"?>  |     |     |     | Obligatorio  | -           | -               |
<factura id="comprobante" version="2.0.0">  Obligatorio  -  -
| <infoTributaria>        |     |     |     | Obligatorio       | -                  | -   |
| ----------------------- | --- | --- | --- | ----------------- | ------------------ | --- |
| <ambiente>1</ambiente>  |     |     |     | O b li ga t o     | ri o ,   Numérico  | 1   |
|                         |     |     |     | con fo r m e   ta | b l a  4           |     |
<tipoEmision>1</tipoEmision>  O b li ga t o ri o ,   Numérico  1
 2
|     |     |     |     | con fo r m e   ta | b l a |     |
| --- | --- | --- | --- | ----------------- | ----- | --- |
<razonSocial>PRUEBA</razonSocial>
|     |     |     |     | Obligatorio  | Alfanumérico  | Max 300  |
| --- | --- | --- | --- | ------------ | ------------- | -------- |

Obligatorio,
<nombreComercial>PRUEBA 2</nombreComercial>  cuando  Alfanumérico  Max 300
corresponda
| <ruc>1760013210001</ruc>  |     |     |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | --- | --- | ------------ | --------- | --- |
Obligatorio,
<claveAcceso>2203201601176001321000110010010000000101234567812</claveAcceso>  conforme tabla  Numérico  49
1
|                       |     |     |     | O b li ga t o     | ri o ,    |     |
| --------------------- | --- | --- | --- | ----------------- | --------- | --- |
| <codDoc>01</codDoc>   |     |     |     |                   | Numérico  | 2   |
|                       |     |     |     | con fo r m e   ta | b l a  3  |     |
| <estab>001</estab>    |     |     |     | Obligatorio       | Numérico  | 3   |
| <ptoEmi>001</ptoEmi>  |     |     |     | Obligatorio       | Numérico  | 3   |
<secuencial>000000010</secuencial>  Obligatorio  Numérico  9
<dirMatriz>SALINAS</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  |     |     |     | Obligatorio  | -   | -   |
| ------------------ | --- | --- | --- | ------------ | --- | --- |
| <infoFactura>      |     |     |     | Obligatorio  | -   | -   |
<fechaEmision>22/03/2016</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio,
<dirEstablecimiento>PÁEZ</dirEstablecimiento>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<contribuyenteEspecial>12345</contribuyenteEspecial>  Alfanumérico  Min 3 Max 13
cuando
corresponda
Obligatorio,
<obligadoContabilidad>SI</obligadoContabilidad>  Texto  SI/NO
cuando
corresponda
<tipoIdentificacionComprador>07</tipoIdentificacionComprador>  O b li ga t o ri o ,   Numérico  2
|     |     |     |     | con fo r m e   ta | b l a  6  |     |
| --- | --- | --- | --- | ----------------- | --------- | --- |
<razonSocialComprador>CONSUMIDOR FINAL</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionComprador>9999999999999</identificacionComprador>  Obligatorio  Numérico  Max 13
Obligatorio,
<direccionComprador>salinas y santiago</direccionComprador>  Alfanumérico  Max 300
cuando
corresponda
<totalSinImpuestos>50.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  |     |     |     | Obligatorio  | -   | -   |
| -------------------- | --- | --- | --- | ------------ | --- | --- |
| <totalImpuesto>      |     |     |     | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  |     |     |     |     | Numérico  | 1   |
| ------------------- | --- | --- | --- | --- | --------- | --- |
conforme tabla
16

14 Resolución NAC-DGERCGC15-00003184, publicada en el Registro Oficial 661 de 4 de enero de 2016

100

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  conforme tabla  Numérico  Min 1 Max 4
17
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>      | Obligatorio  | Numérico  | Max 14  |
| ------------------------ | ------------ | --------- | ------- |
| </totalImpuesto>         | Obligatorio  | -         | -       |
| </totalConImpuestos>     | Obligatorio  | -         | -       |
| <propina>0.00</propina>  | Obligatorio  | Numérico  | Max 14  |
<importeTotal>56.00</importeTotal>  Obligatorio  Numérico  Max 14
Obligatorio,
| <moneda>DOLAR</moneda>  | cuando  | Alfanumérico  | Max 15  |
| ----------------------- | ------- | ------------- | ------- |
corresponda
| <pagos>  | Obligatorio  | -   | -   |
| -------- | ------------ | --- | --- |
| <pago>   | Obligatorio  | -   |     |

Obligatorio,
| <formaPago>18</formaPago>  |     | Numérico  | 2   |
| -------------------------- | --- | --------- | --- |
conforme tabla
24
| <total>56,00</total>  | Obligatorio  | Numérico  | Max 14  |
| --------------------- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>30<plazo>  |     | Numérico  | Max 14  |
| ----------------- | --- | --------- | ------- |
cuando
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  |     | Texto  | Max 10  |
| ---------------------------------- | --- | ------ | ------- |
cuando
corresponda
| </pago>                          | Obligatorio  | -         | -       |
| -------------------------------- | ------------ | --------- | ------- |
| </pagos>                         | Obligatorio  | -         | -       |
| <valorRetIva>0.00</valorRetIva>  | Opcional     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |
| <detalles>      | Obligatorio  | -   | -   |
| <detalle>       | Obligatorio  | -   | -   |
<codigoPrincipal>001</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
Obligatorio,
<codigoAuxiliar>0011</codigoAuxiliar>  cuando  Alfanumérico  Max 25
corresponda
<descripcion>BIEN</descripcion>  Obligatorio  Alfanumérico  Max 300
| <cantidad>1</cantidad>  | Obligatorio  | Numérico  | Max 14  |
| ----------------------- | ------------ | --------- | ------- |
<precioUnitario>50</precioUnitario>  Obligatorio  Numérico  Max 14
| <descuento>0</descuento>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
<precioTotalSinImpuesto>50.00</precioTotalSinImpuesto>  Obligatorio.  Numérico  Max 14
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |
| <impuesto>   | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  | conforme tabla  | Numérico  | 1   |
| ------------------- | --------------- | --------- | --- |
16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
conforme tabla
17
Min 1 Max 4
<tarifa>12.00</tarifa>  Obligatorio  Numérico  / 2 enteros, 2
decimales
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>            | Obligatorio  | Numérico  | Max 14  |
| ------------------------------ | ------------ | --------- | ------- |
| </impuesto>                    | Obligatorio  | -         | -       |
| </impuestos>                   | Obligatorio  | -         | -       |
| </detalle>                     | Obligatorio  | -         | -       |
| </detalles>                    | Obligatorio  | -         | -       |
| <infoSustitutivaGuiaRemision>  | Obligatorio  | -         | -       |
Obligatorio,
<dirPartida>DIRECCION PARTIDA</dirPartida>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio,
<dirDestinatario>DESTINATARIO</dirDestinatario>  cuando  Alfanumérico  Max 300
corresponda

101

ETIQUETAS O TAGS CARACTER
T
C
I
A
PO
M P
D
O
E L
F
O
O
N
R
G
M
IT
A
U
T
D
O
/
Obligatorio,
<fechaIniTransporte>22/03/2016</fechaIniTransporte> cuando Fecha dd/mm/aaaa
corresponda
Obligatorio,
<fechaFinTransporte>22/03/2016</fechaFinTransporte> cuando Fecha dd/mm/aaaa
corresponda
Obligatorio,
<razonSocialTransportista>RAZON SOCIAL</razonSocialTransportista> cuando Alfanumérico Max 300
corresponda
Obligatorio,
<tipoIdentificacionTransportista>04</tipoIdentificacionTransportista>
cuando
Numérico 2
corresponda
conforme tabla 6
Obligatorio,
<rucTransportista>1002576302001</rucTransportista> cuando Numérico Max 13
corresponda
Obligatorio
cuando
<placa>PVB0341</placa>
corresponda
Alfanumérico Max 20
(para la venta de
combustible ver
tabla 29)
<destinos> Obligatorio - -
<destino> Obligatorio - -
Obligatorio,
<motivoTraslado>MOTIVO TRASLADO MERCADERIA 2</motivoTraslado> cuando Alfanumérico Max 300
corresponda
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico> cuando Alfanumérico Max 20
corresponda
Obligatorio,
<codEstabDestino>001</codEstabDestino> cuando Numérico 3
corresponda
Obligatorio,
<ruta>Quito - Cayambe- Otavalo</ruta> cuando Alfanumérico Max 300
corresponda
</destino> Obligatorio - -
<destino> Obligatorio - -
Obligatorio,
<motivoTraslado>MOTIVO TRASLADO MERCADERIA 3</motivoTraslado> cuando Alfanumérico Max 300
corresponda
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico> cuando Alfanumérico Max 20
corresponda
Obligatorio,
<codEstabDestino>001</codEstabDestino> cuando Numérico 3
corresponda
Obligatorio,
<ruta>Quito - Cayambe- Otavalo</ruta> cuando Alfanumérico Max 300
corresponda
</destino> Obligatorio - -
<destino> Obligatorio - -
Obligatorio,
<motivoTraslado>MOTIVO TRASLADO MERCADERIA 4</motivoTraslado> cuando Alfanumérico Max 300
corresponda
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico> cuando Alfanumérico Max 20
corresponda
Obligatorio,
<codEstabDestino>001</codEstabDestino> cuando Numérico 3
corresponda
Obligatorio,
<ruta>Quito - Cayambe- Otavalo</ruta> cuando Alfanumérico Max 300
corresponda
</destino> Obligatorio - -
</destinos> Obligatorio - -
</infoSustitutivaGuiaRemision> Obligatorio - -
</factura> Obligatorio - -
102

FACTURA VERSIÓN 2.1.0

En esta versión se podrá utilizar de 2 a 6 decimales en los campos de cantidad y
precio unitario para contribuyentes que lo requieran.

|     |     |     | T I P O  D E   | L O N G IT U D   /  |
| --- | --- | --- | -------------- | ------------------- |
ETIQUETAS O TAGS  CARACTER
|                                         |              |     | C A M P O   | F O R M A T O   |
| --------------------------------------- | ------------ | --- | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8"?>  | Obligatorio  |     | -           | -               |
<factura id="comprobante" version="2.1.0">  Obligatorio  -  -
| <infoTributaria>        | Obligatorio  |              | -         | -   |
| ----------------------- | ------------ | ------------ | --------- | --- |
|                         | O b li ga    | t o ri o ,   |           |     |
| <ambiente>1</ambiente>  |              |  4           | Numérico  | 1   |
con fo r m e   ta b l a
<tipoEmision>1</tipoEmision>  O b li ga t o ri o ,   Numérico  1
|     | con fo r m e |   ta b l a  2  |     |     |
| --- | ------------ | -------------- | --- | --- |
<razonSocial>PRUEBA</razonSocial>  Obligatorio  Alfanumérico  Max 300
Obligatorio,
<nombreComercial>PRUEBA 2</nombreComercial>  cuando  Alfanumérico  Max 300
corresponda
| <ruc>1760013210001</ruc>  | Obligatorio  |            | Numérico  | 13  |
| ------------------------- | ------------ | ---------- | --------- | --- |
|                           | O b li g at  | o r io ,   |           |     |
<claveAcceso>2203201601176001321000110010010000000101234567812</claveAcceso>  Numérico  49
|                      | co n fo r m | e   ta b l a  |           |     |
| -------------------- | ----------- | ------------- | --------- | --- |
|                      | 1           |               |           |     |
| <codDoc>01</codDoc>  | O b li ga   | t o ri o ,    | Numérico  | 2   |
 3
con fo r m e   ta b l a
| <estab>001</estab>    | Obligatorio  |     | Numérico  | 3   |
| --------------------- | ------------ | --- | --------- | --- |
| <ptoEmi>001</ptoEmi>  | Obligatorio  |     | Numérico  | 3   |
<secuencial>000000010</secuencial>  Obligatorio  Numérico  9
<dirMatriz>SALINAS</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>  | Obligatorio  |     | -   | -   |
| ------------------ | ------------ | --- | --- | --- |
| <infoFactura>      | Obligatorio  |     | -   | -   |
<fechaEmision>22/03/2016</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
Obligatorio,
<dirEstablecimiento>PÁEZ</dirEstablecimiento>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<contribuyenteEspecial>12345</contribuyenteEspecial>  cuando  Alfanumérico  Min 3 Max 13
corresponda
Obligatorio,
<obligadoContabilidad>SI</obligadoContabilidad>  cuando  Texto  SI/NO
corresponda
<tipoIdentificacionComprador>07</tipoIdentificacionComprador>  O b li ga t o ri o ,   Numérico  2
|     | con fo r m e |   ta b l a  6  |     |     |
| --- | ------------ | -------------- | --- | --- |
<razonSocialComprador>CONSUMIDOR FINAL</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionComprador>9999999999999</identificacionComprador>  Obligatorio  Numérico  Max 13
Obligatorio,
<direccionComprador>salinas y santiago</direccionComprador>  Alfanumérico  Max 300
cuando
corresponda
<totalSinImpuestos>50.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
| <totalConImpuestos>  | Obligatorio  |     | -   | -   |
| -------------------- | ------------ | --- | --- | --- |
| <totalImpuesto>      | Obligatorio  |     | -   | -   |
Obligatorio,
| <codigo>2</codigo>  | conforme tabla  |     | Numérico  | 1   |
| ------------------- | --------------- | --- | --------- | --- |
16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  conforme tabla  Numérico  Min 1 Max 4
17
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>      | Obligatorio  |     | Numérico  | Max 14  |
| ------------------------ | ------------ | --- | --------- | ------- |
| </totalImpuesto>         | Obligatorio  |     | -         | -       |
| </totalConImpuestos>     | Obligatorio  |     | -         | -       |
| <propina>0.00</propina>  | Obligatorio  |     | Numérico  | Max 14  |
<importeTotal>56.00</importeTotal>  Obligatorio  Numérico  Max 14
Obligatorio,
| <moneda>DOLAR</moneda>  | cuando  |     | Alfanumérico  | Max 15  |
| ----------------------- | ------- | --- | ------------- | ------- |
corresponda
| <pagos>  | Obligatorio  |     | -   | -   |
| -------- | ------------ | --- | --- | --- |
| <pago>   | Obligatorio  |     | -   |     |

Obligatorio,
| <formaPago>18</formaPago>  | cuando  |     | Numérico  | 2   |
| -------------------------- | ------- | --- | --------- | --- |
corresponda

103

ETIQUETAS O TAGS  CARACTER  T I P O  D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
conforme tabla
24
| <total>56,00</total>  | Obligatorio  | Numérico  | Max 14  |
| --------------------- | ------------ | --------- | ------- |
Obligatorio,
| <plazo>30<plazo>  | cuando  | Numérico  | Max 14  |
| ----------------- | ------- | --------- | ------- |
corresponda
Obligatorio,
| <unidadTiempo>dias</unidadTiempo>  | cuando  | Texto  | Max 10  |
| ---------------------------------- | ------- | ------ | ------- |
corresponda
| </pago>                          | Obligatorio  | -         | -       |
| -------------------------------- | ------------ | --------- | ------- |
| </pagos>                         | Obligatorio  | -         | -       |
| <valorRetIva>0.00</valorRetIva>  | Opcional     | Numérico  | Max 14  |
<valorRetRenta>0.00</valorRetRenta>  Opcional  Numérico  Max 14
| </infoFactura>  | Obligatorio  | -   | -   |
| --------------- | ------------ | --- | --- |
| <detalles>      | Obligatorio  | -   | -   |
| <detalle>       | Obligatorio  | -   | -   |
<codigoPrincipal>001</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
Obligatorio,
<codigoAuxiliar>0011</codigoAuxiliar>  cuando  Alfanumérico  Max 25
corresponda
<descripcion>BIEN</descripcion>  Obligatorio  Alfanumérico  Max 300
Max 18,
| <cantidad>1</cantidad>  | Obligatorio  | Numérico  | hasta 6  |
| ----------------------- | ------------ | --------- | -------- |
decimales
Max 18,
<precioUnitario>50</precioUnitario>  Obligatorio  Numérico  hasta 6
decimales
| <descuento>0</descuento>  | Obligatorio  | Numérico  | Max 14  |
| ------------------------- | ------------ | --------- | ------- |
<precioTotalSinImpuesto>50.00</precioTotalSinImpuesto>  Obligatorio.  Numérico  Max 14
| <impuestos>  | Obligatorio  | -   | -   |
| ------------ | ------------ | --- | --- |
| <impuesto>   | Obligatorio  | -   | -   |
Obligatorio,
| <codigo>2</codigo>  | conforme tabla  | Numérico  | 1   |
| ------------------- | --------------- | --------- | --- |
16
Obligatorio,
<codigoPorcentaje>2</codigoPorcentaje>  conforme tabla  Numérico  Min 1 Max 4
17
Min 1 Max 4
<tarifa>12.00</tarifa>  Obligatorio  Numérico  / 2 enteros, 2
decimales
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>            | Obligatorio  | Numérico  | Max 14  |
| ------------------------------ | ------------ | --------- | ------- |
| </impuesto>                    | Obligatorio  | -         | -       |
| </impuestos>                   | Obligatorio  | -         | -       |
| </detalle>                     | Obligatorio  | -         | -       |
| </detalles>                    | Obligatorio  | -         | -       |
| <infoSustitutivaGuiaRemision>  | Obligatorio  | -         | -       |
Obligatorio,
<dirPartida>DIRECCION PARTIDA</dirPartida>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<dirDestinatario>DESTINATARIO</dirDestinatario>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<fechaIniTransporte>22/03/2016</fechaIniTransporte>  Fecha  dd/mm/aaaa
cuando
corresponda
Obligatorio,
<fechaFinTransporte>22/03/2016</fechaFinTransporte>  Fecha  dd/mm/aaaa
cuando
corresponda
Obligatorio,
<razonSocialTransportista>RAZON SOCIAL</razonSocialTransportista>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
<tipoIdentificacionTransportista>04</tipoIdentificacionTransportista>  cuando  Numérico  2
corresponda
conforme tabla 6
Obligatorio,
<rucTransportista>1002576302001</rucTransportista>  cuando  Numérico  Max 13
corresponda
Obligatorio
| <placa>PVB0341</placa>  |     | Alfanumérico  | Max 20  |
| ----------------------- | --- | ------------- | ------- |
cuando
corresponda

104

ETIQUETAS O TAGS  CARACTER  T I P O  D E   L O N G IT U D   /
|     |     |           |               |
| --- | --- | --------- | ------------- |
|     |     | C A M P O | F O R M A T O |
(para la venta de
combustible ver
tabla 29)
| <destinos>  | Obligatorio  | -   | -   |
| ----------- | ------------ | --- | --- |
| <destino>   | Obligatorio  | -   | -   |
Obligatorio,
<motivoTraslado>MOTIVO TRASLADO MERCADERIA 1</motivoTraslado>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio,
| <codEstabDestino>001</codEstabDestino>  |     | Numérico  | 3   |
| --------------------------------------- | --- | --------- | --- |
cuando
corresponda
Obligatorio,
<ruta>Quito - Cayambe- Otavalo</ruta>  Alfanumérico  Max 300
cuando
corresponda
| </destino>  | Obligatorio  | -   | -   |
| ----------- | ------------ | --- | --- |
| <destino>   | Obligatorio  | -   | -   |
Obligatorio,
<motivoTraslado>MOTIVO TRASLADO MERCADERIA 2</motivoTraslado>  Alfanumérico  Max 300
cuando
corresponda
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico>  Alfanumérico  Max 20
cuando
corresponda
Obligatorio,
| <codEstabDestino>001</codEstabDestino>  |     | Numérico  | 3   |
| --------------------------------------- | --- | --------- | --- |
cuando
corresponda
Obligatorio,
<ruta>Quito - Cayambe- Otavalo</ruta>  Alfanumérico  Max 300
cuando
corresponda
| </destino>  | Obligatorio  | -   | -   |
| ----------- | ------------ | --- | --- |
| <destino>   | Obligatorio  | -   | -   |
Obligatorio,
<motivoTraslado>MOTIVO TRASLADO MERCADERIA 3</motivoTraslado>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico>  Alfanumérico  Max 20
cuando
corresponda
Obligatorio,
| <codEstabDestino>001</codEstabDestino>  |     | Numérico  | 3   |
| --------------------------------------- | --- | --------- | --- |
cuando
corresponda
Obligatorio,
<ruta>Quito - Cayambe- Otavalo</ruta>  Alfanumérico  Max 300
cuando
corresponda
| </destino>  | Obligatorio  | -   | -   |
| ----------- | ------------ | --- | --- |
| <destino>   | Obligatorio  | -   | -   |
Obligatorio,
<motivoTraslado>MOTIVO TRASLADO MERCADERIA 4</motivoTraslado>  cuando  Alfanumérico  Max 300
corresponda
Obligatorio
<docAduaneroUnico>0041324846887</docAduaneroUnico>  cuando  Alfanumérico  Max 20
corresponda
Obligatorio,
| <codEstabDestino>001</codEstabDestino>  | cuando  | Numérico  | 3   |
| --------------------------------------- | ------- | --------- | --- |
corresponda
Obligatorio,
<ruta>Quito - Cayambe- Otavalo</ruta>  Alfanumérico  Max 300
cuando
corresponda
| </destino>                      | Obligatorio  | -   | -   |
| ------------------------------- | ------------ | --- | --- |
| </destinos>                     | Obligatorio  | -   | -   |
| </infoSustitutivaGuiaRemision>  | Obligatorio  | -   | -   |
| </factura>                      | Obligatorio  | -   | -   |

105

|              |     |     |             |            |     |      |      |
| ------------ | --- | --- | ----------- | ---------- | --- | ---- | ---- |
| ANEXO        |     | 10  | -  FORMATO  |            |     | XML  | DE   |
| COMPROBANTE  |     |     | DE          | RETENCIÓN  |     |      | ATS  |
VERSIÓN 2.0.0

Esta versión de comprobante incluye la información que se reporta a través del
módulo de compras del Anexo Transaccional Simplificado (ATS).

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /

|                                          |     |     |     |     |              | C A M P | O F O R M A T O |
| ---------------------------------------- | --- | --- | --- | --- | ------------ | ------- | --------------- |
| <?xml version="1.0" encoding="UTF-8" ?>  |     |     |     |     | Obligatorio  | -       | -               |
<comprobanteRetencion id="comprobante" version="2.0.0">  Obligatorio  -  -
| <infoTributaria>  |     |     |     |     | Obligatorio  | -   | -   |
| ----------------- | --- | --- | --- | --- | ------------ | --- | --- |
Obligatorio, conforme
| <ambiente>1</ambiente>  |     |     |     |     |     | Numérico  | 1   |
| ----------------------- | --- | --- | --- | --- | --- | --------- | --- |
tabla 4 de la Ficha
Técnica Offline
Obligatorio, conforme
<tipoEmision>1</tipoEmision>  tabla 2 de la Ficha  Numérico  1
Técnica Offline
<razonSocial>Distribuidora de Suministros Nacional S.A.</razonSocial>  Obligatorio  Alfanumérico  Max 300
| < n o m b r e C           | o m e rc ia l > E m pr  | e s a  I m p o r t a d o r a y Exportadora de Piezas y Partes de  |     |     |              |               |          |
| ------------------------- | ----------------------- | ----------------------------------------------------------------- | --- | --- | ------------ | ------------- | -------- |
|                           |                         |                                                                   |     |     | Opcional     | Alfanumérico  | Max 300  |
| E q u ip o s  d           | e   Of ic in a < / n om | b r e C o m e r c i a l  >                                        |     |     |              |               |          |
| <ruc>1792146739001</ruc>  |                         |                                                                   |     |     | Obligatorio  | Numérico      | 13       |
< cl a v e A c c eso>2410201107179214673900110020010000000011234567815</clav
|     |     |     |     |     | Obligatorio  | Numérico  | 49  |
| --- | --- | --- | --- | --- | ------------ | --------- | --- |
eA c c e s o >
Obligatorio, conforme
| <codDoc>07</codDoc>  |     |     |     |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --- | --- | --- | --------- | --- |
tabla 3 de la Ficha
Técnica Offline
| <estab>002</estab>    |     |     |     |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | --- | --- | --- | ------------ | --------- | --- |
| <ptoEmi>001</ptoEmi>  |     |     |     |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000001</secuencial>  Obligatorio  Numérico  9
<dirMatriz>Enrique Guerrero Portilla OE1-34 AV. GALO PLAZA LASSO</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>    |     |     |     |     | Obligatorio  | -   | -   |
| -------------------- | --- | --- | --- | --- | ------------ | --- | --- |
| <infoCompRetencion>  |     |     |     |     | Obligatorio  | -   | -   |
<fechaEmision>15/01/2012</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
<dirEstablecimiento>Rodrigo Moreno S/N Francisco García</dirEstablecimiento >  Opcional  Alfanumérico  Max 300
<contribuyenteEspecial>5368</contribuyenteEspecial>  Opcional  Alfanumérico  Min 3 Max 13
<obligadoContabilidad>SI</obligadoContabilidad >  Opcional  Texto  SI/NO
Obligatorio, conforme
<tipoIdentificacionSujetoRetenido>04</tipoIdentificacionSujetoRetenido>  tabla 6 de la Ficha  Numérico  2
Técnica Offline
Obligatorio, conforme
tabla 14 Catalogo ATS. Si
el tipo de identificación
| <tipoSujetoRetenido>01</tipoSujetoRetenido>  |     |     |     |     |     | Numérico  | 2   |
| -------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- |
del Sujeto Retenido es
igual a IDENTIFICACION
DEL EXTERIOR
| <parteRel>SI</parteRel>  |                            |                                 |     |     | Obligatorio  | Alf a b ét    | ic o:  2  |
| ------------------------ | -------------------------- | ------------------------------- | --- | --- | ------------ | ------------- | --------- |
|                          |                            |                                 |     |     |              | S I /N        | O         |
| < r a z o n S o          | c ia l S u je t o R e te n | id o > J u a n  P a blo Chávez  |     |     |              |               |           |
|                          |                            |                                 |     |     | Obligatorio  | Alfanumérico  | Max 300   |
| N ú ñ e z < / ra         | z o n S o c i a lS u je to | R e t e n id o >                |     |     |              |               |           |
<identificacionSujetoRetenido>1713328506001</identificacionSujetoRetenido>  Obligatorio  Alfanumérico  Max 20
<periodoFiscal>03/2012</periodoFiscal>  Obligatorio  Fecha  mm/aaaa
| </infoCompRetencion>  |     |     |     |     | Obligatorio  | -   | -   |
| --------------------- | --- | --- | --- | --- | ------------ | --- | --- |
| <docsSustento>        |     |     |     |     | Obligatorio  | -   | -   |
| <docSustento>         |     |     |     |     | Obligatorio  |     |     |

106

ETIQUETAS O TAGS CARACTER
T
C
I
A
PO
M P
D
O
E L
F
O
O
N
R
G
M
IT
A
U
T
D
O
/
<codSustento>10</codSustento>
O
ta
b
b
l
l
i
a
g a
5
t o
C
r
a
io
t
,
á
c
lo
o
g
n
o
fo
A
rm
TS
e
Numérico 2
<codDocSustento>19</codDocSustento>
ta
O
bl
b
a
l i
4
g a
d
t
e
o
l
r i
C
o,
a
c
tá
o
lo
nf
g
o
o
r m
A
e
T S
Numérico Min 2, Max 3
<numDocSustento>002001000000001</numDocSustento> Opcional Numérico 15
<fechaEmisionDocSustento>20/01/2012</fechaEmisionDocSustento> Obligatorio Fecha dd/mm/aaaa
<fechaRegistroContable>15/03/2012</fechaRegistroContable> Opcional Fecha dd/mm/aaaa
<numAutDocSustento>2110201116</numAutDocSustento> Opcional Numérico 10 o 37 o 49
Obligatorio, conforme
<pagoLocExt>01</pagoLocExt> tabla 15 del Catálogo Numérico 2
ATS
Obligatorio cuando el
<tipoRegi>01</tipoRegi>
campo <pagoLocExt>
Numérico 2
sea igual 02. Tabla 19 del
Catálogo ATS
Se genera cuando el
código del campo
<pagoLocExt> sea igual
02, si <tipoReg> es igual
01 registrar el código de
la tabla 25 de la Ficha
Técnica Offline.
<paisEfecPago>212</paisEfecPago> Si <tipoReg> es igual 02 Numérico 3 o 4
registrar el país asociado
al paraíso fiscal tabla 17
Catálogo ATS.
Si <tipoReg> es igual 03
escoger códigos de la
tabla 16 del Catálogo
ATS, excepto código 593
Obligatorio cuando el
<aplicConvDobTrib>NO</aplicConvDobTrib> <pagoLocExt> sea igual Texto SI/NO
02 se llena el campo
Obligatorio el campo
<pagExtSujRetNorLeg>NO</pagExtSujRetNorLeg>
<aplicConvDobTrib> se
Texto SI/NO
haya escogido la opción
NO
Obligatorio cuando el
<pagoRegFis>SI</pagoRegFis> campo <pagoLocExt> SI 2
sea igual 02
Obligatorio, si
<codDocSustento> es
igual a 41, corresponde a
<totalComprobantesReembolso>141.01</totalComprobantesReembolso>
la suma de
Numérico Max 14
<totalBaseImponibleRee
mbolso> y
<totalImpuestoReembols
o>
Obligatorio, si
<codDocSustento> es
igual a 41, corresponde a
<totalBaseImponibleReembolso>120.75</totalBaseImponibleReembolso>
la sumatoria de las
Numérico Max 14
etiquetas
<baseImponibleReembol
so>, el cual es mayor o
igual a la sumatoria
Obligatorio, si
<codDocSustento> es
igual a 41, corresponde a
<totalImpuestoReembolso>20.26</totalImpuestoReembolso>
la sumatoria de las
Numérico Max 14
etiquetas
<impuestoReembolso>,
el cual es mayor o igual a
la sumatoria
<totalSinImpuestos>120.75</totalSinImpuestos> Obligatorio Numérico Max 14
<importeTotal>141.01</importeTotal> Obligatorio Numérico Max 14
<impuestosDocSustento> Obligatorio - -
<impuestoDocSustento> Obligatorio - -
107

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     | C A M P O   | F O R M A T O   |
| --- | --- | ----------- | --------------- |
Obligatorio, conforme
<codImpuestoDocSustento>2</codImpuestoDocSustento>  tabla 16 de la Ficha  Numérico  1
Técnica Offline
Obligatorio, conforme
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
tabla 17 o 18 de la Ficha
Técnica Offline
<baseImponible>125.90</baseImponible>  Obligatorio  Numérico  Max 14
M a x  3   e nt e r o s
| <tarifa>12</tarifa>  | Obligatorio  | Numérico  |     |
| -------------------- | ------------ | --------- | --- |
y  2  d e c im a l e s
<valorImpuesto>15.11</valorImpuesto>  Obligatorio  Numérico  Max 14
| </impuestoDocSustento>   | Obligatorio  | -   | -   |
| ------------------------ | ------------ | --- | --- |
| </impuestosDocSustento>  | Obligatorio  | -   | -   |
| <retenciones>            | Obligatorio  | -   | -   |
| <retencion>              | Obligatorio  | -   | -   |
Obligatorio, conforme
| <codigo >1</codigo>  |     | Numérico  | 1   |
| -------------------- | --- | --------- | --- |
tabla 19 de la Ficha
Técnica Offline
Obligatorio, conforme
<codigoRetencion>312</codigoRetencion>  tabla 20 de la Ficha  Numérico  Min 1 Max 5
Técnica Offline
<baseImponible>125.90</baseImponible>  Obligatorio  Numérico  Max 14
|     | Obligatorio, conforme  |     | Min 1 Max 5  |
| --- | ---------------------- | --- | ------------ |
<porcentajeRetener>1.75</porcentajeRetener>  tabla 20 de la Ficha  Numérico  entre enteros
|     | Técnica Offline  |     | y decimales  |
| --- | ---------------- | --- | ------------ |
Max 12
| <valorRetenido>2.20</valorRetenido>  | Obligatorio  | Numérico  |     |
| ------------------------------------ | ------------ | --------- | --- |
enteros y 2
decimales
Obligatorio cuando la
| <dividendos>15  |     | -   | -   |
| --------------- | --- | --- | --- |
etiqueta <codSustento>
es igual a 10
Obligatorio cuando la
<fechaPagoDiv>15/03/2012</fechaPagoDiv>  etiqueta <codSustento>  Fecha  dd/mm/aaaa
es igual a 10
|                                  | Obligatorio cuando la   |           | Max 14       |
| -------------------------------- | ----------------------- | --------- | ------------ |
| <imRentaSoc>102.54</imRentaSoc>  |                         | Numérico  |              |
|                                  | etiqueta <codSustento>  |           | enteros y 2  |
|                                  | es igual a 10           |           | decimales    |
Obligatorio cuando la
<ejerFisUtDiv>2012</ejerFisUtDiv>  etiqueta <codSustento>  Numérico  4
es igual a 10
Obligatorio cuando la
| </dividendos>  |     | -   | -   |
| -------------- | --- | --- | --- |
etiqueta <codSustento>
es igual a 10
| <compraCajBanano>  | Obl ig a t o ri | o  c u a n do  -  | -   |
| ------------------ | --------------- | ----------------- | --- |
|                    | c o rr e s      | p o n d a         |     |
Obligatorio cuando
corresponda. Debe
desplegarse solamente
<numCajBan>2012</numCajBan>  en el caso de que el  Numérico  Max 7 enteros
campo
<codigoRetencion> sea
igual a 338, 340, 341 y
342; 342A; 342B
Obligatorio cuando
corresponda. Debe
desplegarse solamente
Max 12
<precCajBan>2012</precCajBan>  en el caso de que el  Numérico
enteros y 2
|     | campo  |     | decimales  |
| --- | ------ | --- | ---------- |
<codigoRetencion> sea
igual a 338, 340, 341 y
342; 342A; 342B
| </compraCajBanano>  | Obl ig a t o ri | o  c u a n do  -  | -   |
| ------------------- | --------------- | ----------------- | --- |

|     | c o rr e s | p o n d a |     |
| --- | ---------- | --------- | --- |

15 Para efectos tributarios, se considerarán dividendos y tendrán el mismo tratamiento tributario todo tipo de participaciones en utilidades,
excedentes, beneficios o similares que se obtienen en razón de los derechos representativos de capital que el beneficiario mantiene, de
manera directa o indirecta.

108

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                 |     |     |     |              |     | C A M P O   | F O R M A T O   |
| --------------- | --- | --- | --- | ------------ | --- | ----------- | --------------- |
| </retencion>    |     |     |     | Obligatorio  |     | -           | -               |
| </retenciones>  |     |     |     | Obligatorio  |     | -           | -               |
Obligatorio cuando
| <reembolsos>  |     |     |     | <codDocSustento> sea  |     | -   | -   |
| ------------- | --- | --- | --- | --------------------- | --- | --- | --- |
igual a 41
| <reembolsoDetalle>  |     |     |     | Obligatorio  |     | -   | -   |
| ------------------- | --- | --- | --- | ------------ | --- | --- | --- |
Obligatorio cuando
<codDocSustento> sea
< t ip oIdentificacionProveedorReembolso>04</tipoIdentificacionProveedorReembols Numérico  2
|     |     |     |     | igual a 41, conforme tabla  |     |     |     |
| --- | --- | --- | --- | --------------------------- | --- | --- | --- |
o  >
6 de la Ficha Técnica
Offline
Obligatorio cuando
< id e n t if ic acionProveedorReembolso>1760013210001</identificacionProveedorRee
|                |     |     |     | <codDo c S | u s te n to > sea  Alfanumérico  |     | Max 20  |
| -------------- | --- | --- | --- | ---------- | -------------------------------- | --- | ------- |
| m b o ls o >   |     |     |     |            |                                  |     |         |
|                |     |     |     | ig u a     | l  a  4 1                        |     |         |
Obligatorio cuando
<codDocSustento> sea
<codPaisPagoProveedorReembolso>212</codPaisPagoProveedorReembolso>  igual a 41, conforme la  Numérico  3
tabla 25 de la Ficha
Técnica Offline
Obligatorio cuando
<codDocSustento> sea
<tipoProveedorReembolso>01</tipoProveedorReembolso>  Numérico  2
igual a 41, conforme tabla
26 de la Ficha Técnica
Offline
Obligatorio cuando
<codDocSustento> sea
| <codDocReembolso>01</codDocReembolso >  |     |     |     |     |     | Numérico  | 2   |
| --------------------------------------- | --- | --- | --- | --- | --- | --------- | --- |
igual a 41, validar
conforme tabla 4 del
Catálogo ATS
Obligatorio cuando
| <estabDocReembolso>001</estabDocReembolso>  |     |     |     |     |     | Numérico  | 3   |
| ------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- |
<codDocSustento> sea
igual a 41
Obligatorio cuando
<ptoEmiDocReembolso>501</ptoEmiDocReembolso>  <codDocSustento> sea  Numérico  3
igual a 41
Obligatorio cuando
<secuencialDocReembolso>000000008</secuencialDocReembolso>  <codDocSustento> sea  Numérico  9
igual a 41
Obligatorio cuando
<fechaEmisionDocReembolso>04/03/2013</fechaEmisionDocReembolso>  Fecha  dd/mm/aaaa
<codDocSustento> sea
igual a 41
Obligatorio cuando
| < n u m e r o A | u to r i z a cio n D o c R | e e m b > 0 4 0 3 2 0 | 1 30 1 1 7922611040011001501000000008 |            |                    |           |               |
| --------------- | -------------------------- | --------------------- | ------------------------------------- | ---------- | ------------------ | --------- | ------------- |
|                 |                            |                       |                                       | <codDo c S | u s te n to > sea  | Numérico  | 10 o 37 o 49  |
12 3 4 5 6 7 8 1 6 < / n u m e ro A u t or iz a c io n D o c R e e m b  >
|     |     |     |     | ig u a | l  a  4 1 |     |     |
| --- | --- | --- | --- | ------ | --------- | --- | --- |
Obligatorio cuando
| <detalleImpuestos>  |     |     |     |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
<codDocSustento> sea
igual a 41
Obligatorio cuando
| <detalleImpuesto>  |     |     |     | <codDocSustento> sea  |     | -   | -   |
| ------------------ | --- | --- | --- | --------------------- | --- | --- | --- |
igual a 41
Obligatorio cuando
| <codigo>2</codigo>  |     |     |     | <codDocSustento> sea  |     | Numérico  | 1   |
| ------------------- | --- | --- | --- | --------------------- | --- | --------- | --- |
igual a 41, tabla 16 de la
Ficha Técnica Offline
Obligatorio cuando
<codDocSustento> sea
<codigoPorcentaje>2</codigoPorcentaje>  Numérico  Min 1 Max 4
igual a 41, conforme tabla
17 o 18 de la Ficha
Técnica Offline
Obligatorio cuando
<tarifa>12</tarifa>  <codDocSustento> sea  Numérico  Min 1 Max 4
igual a 41
Obligatorio cuando
<baseImponibleReembolso>125.90</baseImponibleReembolso>  Numérico  Max 14
<codDocSustento> sea
igual a 41
Obligatorio cuando
<impuestoReembolso>15.11</impuestoReembolso >  <codDocSustento> sea  Numérico  Max 14
igual a 41
Obligatorio cuando
| </detalleimpuesto>  |     |     |     |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
<codDocSustento> sea
igual a 41

109

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     | C A M P O   | F O R M A T O   |
| --- | --- | --- | ----------- | --------------- |
Obligatorio cuando
| <detalleImpuesto>  |     | <codDocSustento> sea  | -   | -   |
| ------------------ | --- | --------------------- | --- | --- |
igual a 41
Obligatorio cuando
| <codigo>3</codigo>  |     | <codDocSustento> sea  | Numérico  | 1   |
| ------------------- | --- | --------------------- | --------- | --- |
igual a 41, tabla 16 de la
Ficha Técnica Offline
Obligatorio cuando
<codDocSustento> sea
<codigoPorcentaje>3011</codigoPorcentaje>  Numérico  Min 1 Max 4
igual a 41, conforme tabla
17 o 18 de la Ficha
Técnica Offline
Obligatorio cuando
<tarifa>0</tarifa>  <codDocSustento> sea  Numérico  Min 1 Max 4
igual a 41
Obligatorio cuando
<baseImponibleReembolso>0.00</baseImponibleReembolso>  Numérico  Max 14
<codDocSustento> sea
igual a 41
Obligatorio cuando
<impuestoReembolso>5.15</impuestoReembolso>  <codDocSustento> sea  Numérico  Max 14
igual a 41
Obligatorio cuando
| </detalleImpuesto>  |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- |
<codDocSustento> sea
igual a 41
Obligatorio cuando
| </detalleImpuestos>  |     | <codDocSustento> sea  | -   | -   |
| -------------------- | --- | --------------------- | --- | --- |
igual a 41
| </reembolsoDetalle>  |     | Obligatorio  | -   | -   |
| -------------------- | --- | ------------ | --- | --- |
Obligatorio cuando
| </reembolsos>  |     |     | -   | -   |
| -------------- | --- | --- | --- | --- |
<codDocSustento> sea
igual a 41
| <pagos>  |     | Obligatorio  | -   | -   |
| -------- | --- | ------------ | --- | --- |
| <pago>   |     | Obligatorio  | -   | -   |
Obligatorio, conforme
<formapago>01</formapago>  tabla 13 del Catálogo  Numérico  2
ATS
| <total>500</total>  |                   | Obligatorio  | Numérico      | Max 14  |
| ------------------- | ----------------- | ------------ | ------------- | ------- |
| </pago>             |                   | Obligatorio  | -             | -       |
| </pagos>            |                   | Obligatorio  | -             | -       |
| </docSustento>      |                   | Obligatorio  | -             | -       |
| </docsSustento>     |                   | Obligatorio  | -             | -       |
| <infoAdicional>     |                   | Opcional     | -             | -       |
| < ca m p o A        | d i c i o n a l   | Opcional     | Alfanumérico  | 1       |
adoIRsociedaddividendos">2000</campoAdicional>
| no m b re = "            | v a l o r p a g |              |           |              |
| ------------------------ | --------------- | ------------ | --------- | ------------ |
| </infoAdicional>         |                 | Opcional     | Numérico  | Min 1 Max 4  |
| </comprobanteRetencion>  |                 | Obligatorio  | Numérico  | Min 1 Max 4  |

Para registrar los códigos a utilizar, se recomienda revisar las tablas del catálogo
de  Anexo  Transaccional  Simplificado  (ATS),  publicado  en  la  página  web
www.sri.gob.ec:  Información  sobre  impuestos/Cómo  declaro  mis  impuestos?  /
Anexos  y  guías  o  directamente  a  través  del  siguiente  link:
http://www.sri.gob.ec/web/guest/formularios-e-instructivos1

Nota: El formato RIDE del comprobante de retención corresponderá al publicado
para la versión 1.0.0.

110

ANEXO 11 – REQUISITOS OBLIGATORIOS
PARA EL XML DE FACTURA COMERCIAL
NEGOCIABLE
Las facturas electrónicas comerciales negociables deberán contener la siguiente
información en la estructura del XML; caso contrario no podrán ser generadas
como negociables:
1. Dirección comprador:
<direccionComprador>salinas y santiago</direccionComprador>
2. Formas de pago:
<pagos>
<pago>
<formaPago>21</formaPago>
<total>56,00</total>
<plazo>30</plazo>
<unidadTiempo>dias</unidadTiempo>
</pago>
</pagos>
Para más información respecto a Factura Electrónica Comercial Negociable,
ingrese al siguiente link: http://www.sri.gob.ec/web/guest/facturacion-
electronica#informaci%C3%B3n
Únicamente para aquellos contribuyentes que se dedican a la negociación de
facturas electrónicas y que requieran realizar la notificación masiva de las facturas
mediante el servicio expuesto en el portal web en la opción de Comprobantes
Electrónicos / Ambientes Pruebas o Producción / Factura Comercial Negociable,
deberán incluir obligatoriamente en la estructura del archivo xml entre los tags
</detalles> e <infoAdicional> previa autorización del comprobante, la dirección de
correo electrónico del receptor, en los siguientes campos:
<tipoNegociable>
<correo>controldecalidad@sriprueba.ad</correo>
</tipoNegociable>
Si la notificación de las facturas comerciales negociables es de manera individual,
no se registrará la información mencionada.
111

ANEXO 12 – REQUISITO OBLIGATORIO PARA
EL XML DE FACTURA EN VENTA DE
COMBUSTIBLES LÍQUIDOS DERIVADOS DE
HIDROCARBUROS Y BIOCOMBUSTIBLES.
Las facturas electrónicas en venta de combustibles líquidos derivados de
hidrocarburos (CLDH) y biocombustibles deberán contener el tag placa en la
estructura del XML, esto entre los tags <moneda> y formas de pago para las
versiones 1.0.0, 1.1.0, 2.0.0, 2.1.0;
1. Placa
<moneda>DOLAR</moneda>
<placa>PCM4567</placa>
<pagos>
Para mayor información respecto a facturas para ventas de combustibles líquidos
derivados de hidrocarburos y biocombustibles, ingrese al siguiente link:
http://www.sri.gob.ec/web/guest/facturacion-electronica#informaci%C3%B3n
2. Llenado del campo Placa
El campo <placa> deberá llenarse considerando las siguientes especificaciones,
según lo dispuesto por el organismo regulador16:
TABLA 29: FORMATO DE LLENADO DEL CAMPO PLACA
Campo
Caso Descripción Observaciones
<placa>
Se deberá ingresar las letras y
1 Vehículo automotor de transporte terrestre <ABC1234>
números sin ningún espacio
Si existen solo tres dígitos se
2 Vehículo automotor de transporte terrestre <ABC0123> deberá anteponer el cero sin ningún
espacio
Las letras “CU” seguido de la parte
3 Cuantía doméstica <CU104634> numérica de la autorización de la
cuantía doméstica
Personas naturales o jurídicas sin vehículo que
Se deberá ingresar tres letras “Z” y
4 adquieran un volumen de despacho inferior a 5 <ZZZ9999>
cuatro números nueves (9)
galones en provincias no fronterizas
Personas naturales o jurídicas sin vehículo que
Se deberá ingresar tres letras “Z” y
5 adquieran un volumen de despacho inferior a 3 < ZZZ9999>
cuatro números nueves (9)
galones en frontera
Para el caso de venta de combustible a motos, <AB023C> Se deberá colocar la placa del
6 vehículos diplomáticos, régimen de internación <CD0123> vehículo asignada por la Agencia
temporal y otros que tienen placa asignada por <IT0123> Nacional de Transito, tal como
16 Disposiciones sobre el llenado del campo PLACA dadas a los distribuidores de combustible por la Agencia de Regulación y Control de
Energía y Recursos Naturales No Renovables mediante Oficio Nro. ARCERNNR-CTRCH-2024-0014-OF del 10 de enero de 2024.
112

Campo
Caso Descripción Observaciones
<placa>
la Agencia Nacional de Tránsito consta en
la matrícula.
Para el caso de venta de combustibles a Se deberá colocar la placa
7 <ABCD0123>
vehículos extranjeros. internacional del vehículo.
Para el caso de Equipo Caminero, Maquinaria Se debe ingresar en el campo placa
Pesada y Maquinaria Agrícola que tengan las Letras MAQN, y seguido del
8 <MAQN99999>
matricula asignada por el Ministerio de número completo de la matrícula
Transporte y Obras Publicas- MTOP. otorgado por el MTOP.
ANEXO 13 – REQUISITO OBLIGATORIO PARA
XML DE COMPROBANTES EMITIDOS DESDE
UNA MÁQUINA FISCAL
Los comprobantes factura, nota de crédito, nota de débito, guía de remisión y
comprobante de retención para todas sus versiones deberán contener los
siguientes tags: marca, modelo y serie en la estructura del XML como se muestra a
continuación:
</detalles>
<maquinaFiscal>
<marca>SISPAU</marca>
<modelo>ABC1234</modelo>
<serie>CGMC1405</serie>
</maquinaFiscal>
<infoAdicional>
ANEXO 14 – EJEMPLO FIRMA ELECTRÓNICA
BAJO ESTÁNDAR XADES_BES
<?xml 113escrip=”1.0” encoding=”UTF-8”?>
<factura id=”comprobante” 113escrip=”1.0.0”>
<infoTributaria>
<ambiente>1</ambiente>
<tipoEmision>1</tipoEmision>
<razonSocial>SERVICIO DE RENTAS INTERNAS</razonSocial>
<nombreComercial>LE HACE BIEN AL PAIS</nombreComercial>
<ruc>1760013210001</ruc>
<claveAcceso>0503201201176001321000110010030009900641234567814</claveAcceso>
<codDoc>01</codDoc>
<estab>001</estab>
<ptoEmi>003</ptoEmi>
<secuencial>000990064</secuencial>
<dirMatriz>AMAZONAS Y ROCA</dirMatriz>
</infoTributaria>
<infoFactura>
<fechaEmision>05/03/2012</fechaEmision>
<dirEstablecimiento>SALINAS Y SANTIAGO</dirEstablecimiento>
<contribuyenteEspecial>12345</contribuyenteEspecial>
<obligadoContabilidad>SI</obligadoContabilidad>
<tipoIdentificacionComprador>05</tipoIdentificacionComprador>
<razonSocialComprador>EGUIGUREN PENARRETA GABRIEL FERNANDO</razonSocialComprador>
<identificacionComprador>1103029144</identificacionComprador>
<totalSinImpuestos>100.00</totalSinImpuestos>
<totalDescuento>0.00</totalDescuento>
113

<totalConImpuestos>
<totalImpuesto>
<114escri>2</114escri>
<codigoPorcentaje>2</codigoPorcentaje>
<baseImponible>100.00</baseImponible>
<valor>12.00</valor>
</totalImpuesto>
</totalConImpuestos>
<propina>0.00</propina>
<importeTotal>112.00</importeTotal>
<moneda>DÓLAR</moneda>
</infoFactura>
<detalles>
<detalle>
<codigoPrincipal>001</codigoPrincipal>
<codigoAuxiliar>001</codigoAuxiliar>
<114escripción>SILLA DE MADERA</114escripción>
<cantidad>1.00</cantidad>
<precioUnitario>100.00</precioUnitario>
<descuento>0.00</descuento>
<precioTotalSinImpuesto>100.00</precioTotalSinImpuesto>
<impuestos>
<impuesto>
<114escri>2</114escri>
<codigoPorcentaje>2</codigoPorcentaje>
<tarifa>12.00</tarifa>
<baseImponible>100.00</baseImponible>
<valor>12.00</valor>
</impuesto>
</impuestos>
</detalle>
</detalles>
<infoAdicional>
<campoAdicional nombre=”Dirección”>LOS PERALES Y AV. ELOY ALFARO</campoAdicional>
<campoAdicional nombre=”Teléfono”>2123123</campoAdicional>
<campoAdicional nombre=”Email”>gfeguiguren@sri.gob.ec</campoAdicional>
</infoAdicional>
<!–INICIO DE LA FIRMA DIGITAL →
<ds:Signature xmlns:ds=”http://www.w3.org/2000/09/xmldsig#” xmlns:etsi=”http://uri.etsi.org/01903/v1.3.2#”
Id=”Signature620397”>
<ds:SignedInfo Id=”Signature-SignedInfo814463”>
<ds:CanonicalizationMethod Algorithm=”http://www.w3.org/TR/2001/REC-xml-c14n-
20010315”></ds:CanonicalizationMethod>
<ds:SignatureMethod Algorithm=”http://www.w3.org/2000/09/xmldsig#rsa-sha1”></ds:SignatureMethod>
<ds:Reference Id=”SignedPropertiesID157683” Type=”http://uri.etsi.org/01903#SignedProperties” URI=”#Signature620397-
SignedProperties24123”>
<ds:DigestMethod Algorithm=”http://www.w3.org/2000/09/xmldsig#sha1”></ds:DigestMethod>
<ds:DigestValue><!–HASH O DIGEST DEL ELEMENTO <etsi:SignedProperties> →</ds:DigestValue>
</ds:Reference>
<ds:Reference URI=”#Certificate1562780”>
<ds:DigestMethod Algorithm=”http://www.w3.org/2000/09/xmldsig#sha1”></ds:DigestMethod>
<ds:DigestValue><!–HASH O DIGEST DEL CERTIFICADO X509 →</ds:DigestValue>
</ds:Reference>
<ds:Reference Id=”Reference-ID-363558” URI=”#comprobante”>
<ds:Transforms>
<ds:Transform Algorithm=”http://www.w3.org/2000/09/xmldsig#enveloped-signature”></ds:Transform>
</ds:Transforms>
<ds:DigestMethod Algorithm=”http://www.w3.org/2000/09/xmldsig#sha1”></ds:DigestMethod>
<ds:DigestValue><!–HASH O DIGEST DE TODO EL ARCHIVO XML IDENTIFICADO POR EL
id=”comprobante”→</ds:DigestValue>
</ds:Reference>
</ds:SignedInfo>
<ds:SignatureValue Id=”SignatureValue398963”>
<!–VALOR DE LA FIRMA (ENCRIPTADO CON LA LLAVE PRIVADA DEL CERTIFICADO DIGITAL) →
</ds:SignatureValue>
<ds:KeyInfo Id=”Certificate1562780”>
<ds:X509Data>
<ds:X509Certificate>
<!–CERTIFICADO X509 CODIFICADO EN Base64 →
</ds:X509Certificate>
</ds:X509Data>
<ds:KeyValue>
<ds:RSAKeyValue>
<ds:Modulus>
114

<!–MODULO DEL CERTIFICADO X509 →
</ds:Modulus>
<ds:Exponent>AQAB</ds:Exponent>
</ds:RSAKeyValue>
</ds:KeyValue>
</ds:KeyInfo>
<ds:Object Id=”Signature620397-Object231987”><etsi:QualifyingProperties
Target=”#Signature620397”><etsi:SignedProperties Id=”Signature620397-
SignedProperties24123”><etsi:SignedSignatureProperties><etsi:SigningTime>2012-03-05T16:57:32-
05:00</etsi:SigningTime><etsi:SigningCertificate><etsi:Cert><etsi:CertDigest><ds:DigestMethod
Algorithm=”http://www.w3.org/2000/09/xmldsig#sha1”></ds:DigestMethod><ds:DigestValue>xUQewsj7MrjSfyMnhWz5DhQn
WJM=</ds:DigestValue></etsi:CertDigest><etsi:IssuerSerial><ds:X509IssuerName>CN=AC BANCO CENTRAL DEL
ECUADOR,L=QUITO,OU=ENTIDAD DE CERTIFICACION DE INFORMACION-ECIBCE,O=BANCO CENTRAL DEL
ECUADOR,C=EC</ds:X509IssuerName><ds:X509SerialNumber>1312833444</ds:X509SerialNumber></etsi:IssuerSerial></
etsi:Cert></etsi:SigningCertificate></etsi:SignedSignatureProperties><etsi:SignedDataObjectProperties><etsi:DataObjectFor
mat ObjectReference=”#Reference-ID-363558”><etsi:Description>contenido
comprobante</etsi:Description><etsi:MimeType>text/xml</etsi:MimeType></etsi:DataObjectFormat></etsi:SignedDataObject
Properties></etsi:SignedProperties></etsi:QualifyingProperties></ds:Object>
</ds:Signature>
<!–FIN DE LA FIRMA DIGITAL →
</factura>
Nota: Los archivos XML de comprobantes electrónicos se encuentran disponibles
en el portal web del SRI.
ANEXO 15 – COMPATIBILIDAD DISPOSITIVOS
PROVISTOS
BANCO CENTRAL DEL ECUADOR
Windows Windows Red Hat Enterprise Ubuntu MAC OS X
XP, Vista, 5.4 8.0.x LION (10.7)
Vista, 7 7 (32-bit and 64-bit) 9.0.x
(32-bits) (64-bits) en kernel 2.6
CentOS 5.4
(32-bit and 64-bit)
en kernel 2.6
SUSE Linux Enterprise
11 (32-bit) en kernel
2.6
Fedora 12 (32-bit)
Ubuntu 10.04 (32-bit
and 64 bit) en kernel
2.6
Ikey2032 ✓ ✓ × ✓ ×
(A) (1) (B) (2) (D) (3)
Aladin ✓ ✓ ✓ × ✓
etoken PRO (A) (1) (B) (2) (C) (3) (E) (5)
Driver SafeNet AuthenticationClient-x32-8.00.msi provisto por la página web del
•
B.C.E.
Driver SafeNet AuthenticationClient-x64-8.00.msi provisto por la página web del
•
B.C.E.
115

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Driver SafeNetAuthenticationClient_Linux_v8.0.zip  provisto por la página web
•
del B.C.E.
•  Driver BSecPKLinux-2.0.0.0007.zip  provisto por la página web del B.C.E.
•  Driver eToken_PKI_Client_4_55_Mac.zip provisto por la página web del B.C.E.
(1)  Requiere tener instalado el JRE de java versión 6.x (Java SE 6 Update 26 o
superior)
(2)  Requiere tener instalado el JRE de java versión 7.x (Java SE 7u3)
(3)  Requiere tener instalada el JRE SE 6.x respectivo a la versión que corresponda
de Linux
(4)  Requiere tener instalada el Java SE 6 correspondiente al MAC OS

| ANEXO  | 16  –  | REQUISITO  | OBLIGATORIO  |     | DE  |
| ------ | ------ | ---------- | ------------ | --- | --- |
LLENADO PARA EL XML DE FACTURA EN LA
| VENTA      | DE  | COMBUSTIBLES  |                | LÍQUIDOS  |     |
| ---------- | --- | ------------- | -------------- | --------- | --- |
| DERIVADOS  |     | DE            | HIDROCARBUROS  |           | Y   |
BIOCOMBUSTIBLES.

En la emisión del comprobante de venta tipo factura realizados por la venta de
combustibles líquidos derivados de hidrocarburos (CLDH) y biocombustibles, en la
sección  <detalles>,  para  el  llenado  de  los  campos  <codigoPrincipal>  y
<descripción> se deberán considerar la información del combustible conforme al
siguiente detalle:

TABLA 30

|     |     | <codigoPrincipal>  | <Descripción>     |     |     |
| --- | --- | ------------------ | ----------------- | --- | --- |
|     |     | 0103               | SÚPER             |     |     |
|     |     | 0101               | EXTRA             |     |     |
|     |     | 0174               | EXTRA CON ETANOL  |     |     |
|     |     | 0121               | DIESEL PREMIUM    |     |     |
|     |     | 0104               | DIESEL 2          |     |     |
*De conformidad con el Oficio Nro. ARCERNNR-CTRCH-2024-0014-OF emitido por la Agencia de Regulación y Control de Energía y
Recursos Naturales No Renovables

116

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

| ANEXO       | 17  –  | FORMATOS    |     | XML            | LIQUIDACIÓN  |     |     |
| ----------- | ------ | ----------- | --- | -------------- | ------------ | --- | --- |
| DE  COMPRA  |        | DE  BIENES  |     | Y  PRESTACIÓN  |              |     | DE  |
SERVICIOS EN LAS VERSIONES 1.0.0 Y 1.1.0

| LIQUIDACIÓN  | DE  | COMPRA  | DE  | BIENES  | Y  PRESTACIÓN  |     | DE  |
| ------------ | --- | ------- | --- | ------- | -------------- | --- | --- |
SERVICIOS VERSIÓN 1.0.0

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                         |     |     |     |              |     | C A M P O   | F O R M A T O   |
| --------------------------------------- | --- | --- | --- | ------------ | --- | ----------- | --------------- |
| <?xml version="1.0" encoding="UTF-8"?>  |     |     |     | Obligatorio  |     | -           | -               |
<liquidacionCompra id="comprobante" versión="1.0.0">  Obligatorio  -  -
| <infoTributaria>  |     |     |     | Obligatorio  |     | -   | -   |
| ----------------- | --- | --- | --- | ------------ | --- | --- | --- |
<ambiente>1</ambiente>  Ob l ig a t o r i o ,  c o n f o r m e   t a b la   4  Numérico  1

|                               |     |     |     | d e  l a  F i c h a    |   T é c n i c a  O f f l in e   |           |     |
| ----------------------------- | --- | --- | --- | ---------------------- | ------------------------------- | --------- | --- |
|                               |     |     |     | Ob l ig a t o r i o ,  | c o n f o r m e   t a b la   2  |           |     |
| <tipoEmision>1</tipoEmision>  |     |     |     |                        |                                 | Numérico  | 1   |
|                               |     |     |     | d e  l a  F i c h a    |   T é c n i c a  O f f l in e   |           |     |
<razonSocial>razonSocial0</razonSocial>  Obligatorio  Alfanumérico  Max 300
<nombreComercial>nombreComercial0</nombreComercial>  Opcional  Alfanumérico  Max 300
| <ruc>0000000000001</ruc>  |     |     |     | Obligatorio  |     | Numérico  | 13  |
| ------------------------- | --- | --- | --- | ------------ | --- | --------- | --- |
< c l a v e A c c e s o > 0000000000000000000000000000000000000000000000000< Obligatorio  Numérico  49
/c l a v e A c c e s o >
Obligatorio, conforme tabla 4
| <codDoc>03</codDoc>  |     |     |     |     |     | Numérico  | 2   |
| -------------------- | --- | --- | --- | --- | --- | --------- | --- |
de la Catálogo Técnica Anexo
ATS
| <estab>000</estab>    |     |     |     | Obligatorio  |     | Numérico  | 3   |
| --------------------- | --- | --- | --- | ------------ | --- | --------- | --- |
| <ptoEmi>000</ptoEmi>  |     |     |     | Obligatorio  |     | Numérico  | 3   |
<secuencial>000000000</secuencial>  Obligatorio  Numérico  9
<dirMatriz>dirMatriz0</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>         |     |     |     | Obligatorio  |     | -   | -   |
| ------------------------- | --- | --- | --- | ------------ | --- | --- | --- |
| -<infoLiquidacionCompra>  |     |     |     | Obligatorio  |     | -   | -   |
<fechaEmision>01/01/2000</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
<dirEstablecimiento>dirEstablecimiento0</dirEstablecimiento>  Opcional  Alfanumérico  Max 300
<contribuyenteEspecial>contribuyente</contribuyenteEspecial>  Opcional  Alfanumérico  Min 3 Max 13
<obligadoContabilidad>SI</obligadoContabilidad>  Opcional  Texto  SI/NO
|     |     |     |     | Opcio n a l  c o n | fo rm e   ta b l a   6  de la  |     |     |
| --- | --- | --- | --- | ------------------ | ------------------------------ | --- | --- |
<tipoIdentificacionProveedor>05</tipoIdentificacionProveedor>  Numérico  2
|     |     |     |     | F i c h a  T é | cn ica   O f fl i n e   |     |     |
| --- | --- | --- | --- | -------------- | ----------------------- | --- | --- |
<razonSocialProveedor>EMPRESA ABC</razonSocialComprador>  Obligatorio  Alfanumérico  Max 300
<identificacionProveedor>1794567890001</identificacionProveedor>  Obligatorio  Alfanumérico  20
<direccionProveedor>direccionComprador0</direccionProveedor>  Opcional  Alfanumérico  Max 300
<totalSinImpuestos>50.00</totalSinImpuestos>  Obligatorio  Numérico  Max 14
<totalDescuento>0.00</totalDescuento>  Obligatorio  Numérico  Max 14
Obligatorio, si
| <codDocReembolso>00</codDocReembolso>  |     |     |     |     |     | Numérico  | Max 2  |
| -------------------------------------- | --- | --- | --- | --- | --- | --------- | ------ |
<codDocReembolso> es igual a
41.
Obligatorio, si
<codDocReembolso> es igual a
<totalComprobantesReembolso>56.00</totalComprobantesReembolso>  Numérico  Max 14
41, corresponde a la suma de
<totalBaseImponibleReembolso
> y <totalImpuestoReembolso>

117

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     | C A M P O   | F O R M A T O   |
| --- | --- | ----------- | --------------- |
Obligatorio, si
<codDocReembolso> es igual a
<totalBaseImponibleReembolso>50.00</totalBaseImponibleReembolso>  Numérico  Max 14
41, corresponde a la suma de
<BaseImponibleReembolso>
Obligatorio, si
<codDocReembolso> es igual a
<totalImpuestoReembolso>6.00</totalImpuestoReembolso>  41, corresponde a la sumatoria  Numérico  Max 14
de los tags
<impuestoReembolso>, el cual
es mayor o igual a la sumatoria.
| <totalConImpuestos>  | Obligatorio  |     |     |
| -------------------- | ------------ | --- | --- |
| <totalImpuesto>      | Obligatorio  |     |     |
<codigo>2</codigo>  Ob li g a t o r i o ,  c o n fo r m e  t a b la  1 6  Numérico  Max 2

| d                                       | e   la   F i c h a   Té c n ic a  O f f lin e |           |        |
| --------------------------------------- | --------------------------------------------- | --------- | ------ |
| Ob li                                   | g a t o r i o ,  c o n fo r m e  t a b la     |  1 7      |        |
| <codigoPorcentaje>2</codigoPorcentaje>  |                                               | Numérico  | Max 2  |
| d                                       | e   la   F i c h a   Té c n ic a  O f f lin e |           |        |
<descuentoAdicional>0.00</descuentoAdicional>  Opcional  Numérico  Max 14
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
Min 1 Max 4 / 2
| <tarifa>12</tarifa>  | Obligatorio  | Numérico  |     |
| -------------------- | ------------ | --------- | --- |
enteros, 2
decimales
| <valor>6.00</valor>   | Obligatorio  | Numérico  | Max 14  |
| --------------------- | ------------ | --------- | ------- |
| </totalImpuesto>      | Obligatorio  | -         | -       |
| </totalConImpuestos>  | Obligatorio  | -         | -       |
Obligatorio corresponde a la
<importeTotal>56.00</importeTotal>  sumatoria de bases imponibles  Numérico  Max 14
e impuestos.
| <moneda>moneda0</moneda>  | Obligatorio  | Alfanumérico  | Max 14  |
| ------------------------- | ------------ | ------------- | ------- |
| <pagos>                   | Obligatorio  |               |         |
|                           |              |               |         |
| <pago>                    | Obligatorio  |               |         |
|                           |              |               |         |
<formaPago>01</formaPago>  Ob li g a to r i o .  C o n fo r m e  t a b la  2 4  Numérico  Max 2

| d                     | e   la  F i c h a  T é c n ic a  O f fl in e |           |         |
| --------------------- | -------------------------------------------- | --------- | ------- |
| <total>56.00</total>  | Obligatorio                                  | Numérico  | Max 14  |
| <plazo>30</plazo>     | Obligatorio                                  | Numérico  | Max 14  |
<unidadTiempo>unidadTiem</unidadTiempo>  Opcional  Texto  Max 10
| </pago>                   |              |     |     |
| ------------------------- | ------------ | --- | --- |
| </pagos>                  | Obligatorio  | -   | -   |
| </infoLiquidacionCompra>  | Obligatorio  | -   | -   |
| <detalles>                | Obligatorio  | -   | -   |
| <detalle>                 | Obligatorio  | -   | -   |
<codigoPrincipal>codigoPrincipal0</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
<codigoAuxiliar>codigoAuxiliar0</codigoAuxiliar>  Opcional  Alfanumérico  Max 25
<descripcion>descripcion0</descripcion>  Obligatorio  Alfanumérico  Max 300
<unidadMedida>unidadMedida0</unidadMedida>  Opcional  Alfanumérico  Max 50
| <cantidad>1</cantidad>  | Obligatorio  | Numérico  | Max 14  |
| ----------------------- | ------------ | --------- | ------- |
<precioUnitario>50.00</precioUnitario>  Obligatorio  Numérico  Max 14
| <descuento>0.00</descuento>  | Opcional                                   | Numérico  | Max 14  |
| ---------------------------- | ------------------------------------------ | --------- | ------- |
| Ob l ig                      | a to r i o ,  d e b e   m u l t ip l i c a | r  el     |         |
<precioTotalSinImpuesto>50.00</precioTotalSinImpuesto>    Numérico  Max 14
| c a                    | m p o   p r e c io   p o r  c a n t i d a d |     |     |
| ---------------------- | ------------------------------------------- | --- | --- |
| <detallesAdicionales>  | Opcional                                    | -   | -   |
<detAdicional nombre="nombre0" valor="valor0"/>  Opcional  Alfanumérico  Max 300
<detAdicional nombre="nombre1" valor="valor1"/>  Opcional  Alfanumérico  Max 300

118

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                         |     |              | C A M P O   | F O R M A T O   |
| ----------------------- | --- | ------------ | ----------- | --------------- |
| </detallesAdicionales>  |     | Opcional     | -           | -               |
| <impuestos>             |     | Obligatorio  | -           | -               |
| <impuesto>              |     | Obligatorio  | -           | -               |
<codigo>2</codigo>  Ob li g a t o r i o ,  c o n fo r m e  t a b la  1 6  Numérico  Max 2
|     |     | d e   la   F i c h a   Té c n ic a  O f f lin e   |     |     |
| --- | --- | ------------------------------------------------- | --- | --- |
<codigoPorcentaje>2</codigoPorcentaje>  Ob li g a t o r i o ,  c o n fo r m e  t a b la  1 7  Numérico  Max 2

|     |     | d e   la   F i c h a   Té c n ic a  O f f lin e |     |     |
| --- | --- | ----------------------------------------------- | --- | --- |
Min 1 Max 4 / 2
| <tarifa>12</tarifa>  |     | Obligatorio  | Numérico  |     |
| -------------------- | --- | ------------ | --------- | --- |
enteros, 2
decimales
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>  |     | Obligatorio  | Numérico  | Max 14  |
| -------------------- | --- | ------------ | --------- | ------- |
| </impuesto>          |     | Obligatorio  | -         | -       |
| </impuestos>         |     | Obligatorio  | -         | -       |
| </detalle>           |     | Obligatorio  | -         | -       |
| </detalles>          |     | Obligatorio  | -         | -       |
Obligatorio cuando
| <reembolsos>  |     |     | -   | -   |
| ------------- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| <reembolsoDetalle>  |     | <codDocReembolso> sea igual  | -   | -   |
| ------------------- | --- | ---------------------------- | --- | --- |
a 41
Obligatorio cuando
<codDocReembolso> sea igual
a   4 1
< t ip o Id e n tificacionProveedorReembolso>04</tipoIdentificacionProveedorRee Numérico  Max 2

| m b o ls o > |     | Validar cód i g o   de tipo de  |     |     |
| ------------ | --- | ------------------------------- | --- | --- |
identificación conforme tabla 6
de la Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso> sea igual
| < id e n t if ic a | c io n P ro v e edorReembolso>identificacionProvee</identificacionPro | a   4 1   |           |         |
| ------------------ | --------------------------------------------------------------------- | --------- | --------- | ------- |
|                    |                                                                       |           | Numérico  | Max 20  |
ve e d o r R e e m b o ls o >   Validar cód i g o   de tipo de
identificación conforme tabla
26 de la Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso> sea igual
<codPaisPagoProveedorReembolso>000</codPaisPagoProveedorReembolso>  a 41  Numérico  Max 3
Validar de acuerdo tabla 25 de
la Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso> sea igual
<tipoProveedorReembolso>01</tipoProveedorReembolso>  Numérico  Max 2
a 41, Validar con tabla 26 de la
Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso>00</codDocReembolso>  <codDocReembolso> sea igual  Numérico  Max 3
a 41, Validar tabla 4 de
Catálogo Anexo ATS
Obligatorio cuando
| <estabDocReembolso>000</estabDocReembolso>  |     |     | Numérico  | Max 3  |
| ------------------------------------------- | --- | --- | --------- | ------ |
<codDocReembolso> sea igual
a 41.
Obligatorio cuando
<ptoEmiDocReembolso>000</ptoEmiDocReembolso>  <codDocReembolso> sea igual  Numérico  Max 3
a 41
Obligatorio cuando
<secuencialDocReembolso>000000000</secuencialDocReembolso>  Numérico  Max 9
<codDocReembolso> sea igual
a 41
Obligatorio cuando
<fechaEmisionDocReembolso>01/01/2000</fechaEmisionDocReembolso>  Fecha  dd/mm/aaaa
<codDocReembolso> sea igual
a 41
<numeroautorizacionDocReemb>0000000000</numeroautorizacionDocRee Obligatorio cuando  Numérico  Max 10, 37 ó 49

119

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     | C A M P O   | F O R M A T O   |
| --- | --- | --- | ----------- | --------------- |
mb>
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| <detalleImpuestos>  |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| <detalleImpuesto>  | <codDocReembolso> sea igual  |     | -   | -   |
| ------------------ | ---------------------------- | --- | --- | --- |
a 41
Obligatorio cuando
<codDocReembolso> sea igual
| <codigo>2</codigo>  |     |     | Numérico  | Max 2  |
| ------------------- | --- | --- | --------- | ------ |
a 41. Conforme tabla 16 de la
Ficha Técnica Offline
Obligatorio cuando
<codigoPorcentaje>2</codigoPorcentaje>  <codDocReembolso> sea igual  Numérico  Max 2
a 41, conforme tabla 17 de la
Ficha Técnica Offline
Obligatorio cuando
Min   1   M a x   4   / 2
<codDocReembolso> sea igual
| <tarifa>12</tarifa>  |                                |     | Numérico  | e n t e ro s ,   2   |
| -------------------- | ------------------------------ | --- | --------- | -------------------- |
|                      | a 41, conforme tabla 17 de la  |     |           | decimales            |
Ficha Técnica Offline
Obligatorio cuando
<baseImponibleReembolso>50.00</baseImponibleReembolso>  <codDocReembolso> sea igual  Numérico  Max 14
a 41
Obligatorio cuando
<impuestoReembolso>50.00</impuestoReembolso>  Numérico  Max 14
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| </detalleImpuesto>  |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| </detalleImpuestos>  | <codDocReembolso> sea igual  |     | -   | -   |
| -------------------- | ---------------------------- | --- | --- | --- |
a 41
Obligatorio cuando
| </reembolsoDetalle>  | <codDocReembolso> sea igual  |     | -   | -   |
| -------------------- | ---------------------------- | --- | --- | --- |
a 41
Obligatorio cuando
| </reembolsos>  |     |     | -   | -   |
| -------------- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
|                  | Obl ig a t o r i o |  c u a n do  |     |     |
| ---------------- | ------------------ | ------------ | --- | --- |
| <maquinaFiscal>  |                    |              | -   | -   |
|                  | c o r r e s p      | o n d a      |     |     |
<marca>SISPAU</marca>  Obl ig a t o r i o  c u a n do  Alfanumérico  Min 1 Max 100
|     | c o r r e s p | o n d a   |     |     |
| --- | ------------- | --------- | --- | --- |
<modelo>ABC1234</modelo>  Obl ig a t o r i o  c u a n do  Alfanumérico  Min 1 Max 100

|                          | c o r r e s p      | o n d a      |               |         |
| ------------------------ | ------------------ | ------------ | ------------- | ------- |
|                          | Obl ig a t o r i o |  c u a n do  |               |         |
| <serie>CGMC1405</serie>  |                    |              | Alfanumérico  | Max 30  |
|                          | c o r r e s p      | o n d a      |               |         |
| </maquinaFiscal>         | Obl ig a t o r i o |  c u a n do  | -             | -       |

|                  | c o r r e s p | o n d a |     |     |
| ---------------- | ------------- | ------- | --- | --- |
| <infoAdicional>  | Opcional      |         | -   | -   |
<campoAdicional nombre="nombre4">campoAdicional0</campoAdicional>  Opcional  Alfanumérico  Max 300
<campoAdicional nombre="nombre5">campoAdicional1</campoAdicional>  Opcional  Alfanumérico  Max 300
| </infoAdicional>  | Opcional  |     | -   | -   |
| ----------------- | --------- | --- | --- | --- |

120

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

| LIQUIDACIÓN  | DE  COMPRA  | DE  BIENES  | Y  PRESTACIÓN  |     | DE  |
| ------------ | ----------- | ----------- | -------------- | --- | --- |
SERVICIOS VERSIÓN 1.1.0

En esta versión se podrá utilizar de 2 a 6 decimales en los campos de cantidad y
precio unitario para contribuyentes que lo requieran.

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|                                           |     |     |              | C A M P O   | F O R M A T O   |
| ----------------------------------------- | --- | --- | ------------ | ----------- | --------------- |
| <?xml version="1.1.0" encoding="UTF-8"?>  |     |     | Obligatorio  | -           | -               |
<liquidacionCompra id="comprobante" versión=”1.1.0”>  Obligatorio  -  -
| <infoTributaria>  |     |     | Obligatorio  | -   | -   |
| ----------------- | --- | --- | ------------ | --- | --- |
<ambiente>1</ambiente>  Ob l ig a t o r i o ,  c o n f o r m e   t a b la   4  Numérico  1

|                               |     | d    | e  l a  F i c h a   T é c n i c a  O f f l in e   |           |     |
| ----------------------------- | --- | ---- | ------------------------------------------------- | --------- | --- |
|                               |     | Ob l | ig a t o r i o ,  c o n f o r m e   t a b la   2  |           |     |
| <tipoEmision>1</tipoEmision>  |     |      |                                                   | Numérico  | 1   |
|                               |     | d    | e  l a  F i c h a   T é c n i c a  O f f l in e   |           |     |
<razonSocial>razonSocial0</razonSocial>  Obligatorio  Alfanumérico  Max 300
<nombreComercial>nombreComercial0</nombreComercial>  Opcional  Alfanumérico  Max 300
| <ruc>0000000000001</ruc>  |     |     | Obligatorio  | Numérico  | 13  |
| ------------------------- | --- | --- | ------------ | --------- | --- |
< c l a ve A c ce so > 0000000000000000000000000000000000000000000000000</
|     |     |     | Obligatorio  | Numérico  | 49  |
| --- | --- | --- | ------------ | --------- | --- |
cl a v e A cc e so >
<codDoc>03</codDoc>  Obliga to r i o ,  c o n f o r m e  t abla 4  Numérico  2

d e l   C a tá l o g o   AT S
| <estab>000</estab>    |     |     | Obligatorio  | Numérico  | 3   |
| --------------------- | --- | --- | ------------ | --------- | --- |
| <ptoEmi>000</ptoEmi>  |     |     | Obligatorio  | Numérico  | 3   |
<secuencial>000000000</secuencial>  Obligatorio  Numérico  9
<dirMatriz>dirMatriz0</dirMatriz>  Obligatorio  Alfanumérico  Max 300
| </infoTributaria>        |     |     | Obligatorio  | -   | -   |
| ------------------------ | --- | --- | ------------ | --- | --- |
| <infoLiquidacionCompra>  |     |     | Obligatorio  | -   | -   |
<fechaEmision>01/01/2000</fechaEmision>  Obligatorio  Fecha  dd/mm/aaaa
<dirEstablecimiento>dirEstablecimiento0</dirEstablecimiento>  Opcional  Alfanumérico  Max 300
<contribuyenteEspecial>contribuyente</contribuyenteEspecial>  Opcional  Alfanumérico  Min 3 Max 13
<obligadoContabilidad>SI</obligadoContabilidad>  Opcional  Texto  SI/NO
|     |     | Opcio | n a l  c o n fo rm e   ta b l a   6  de la  |     |     |
| --- | --- | ----- | ------------------------------------------- | --- | --- |
<tipoIdentificacionProveedor>05</tipoIdentificacionProveedor>  Numérico  2
|     |     |     | F i c h a  T é cn ica   O f fl i n e   |     |     |
| --- | --- | --- | -------------------------------------- | --- | --- |
<razonSocialProveedor>EMPRESA ABC</razonSocialProveedor>  Obligatorio  Alfanumérico  Max 300
<identificacionProveedor>1750863147</identificacionProveedor>  Obligatorio  Alfanumérico  Max 20
<direccionProveedor>direccionProveedor</direccionProveedor>  Opcional  Alfanumérico  Max 300
Obligatorio conforme sumatoria
<totalSinImpuestos>50.00</totalSinImpuestos>  Numérico  Max 14
de bases imponibles de
Detalles.
Opcional conforme sumatoria
| <totalDescuento>0.00</totalDescuento>  |     |     |     | Numérico  | Max 14  |
| -------------------------------------- | --- | --- | --- | --------- | ------- |
de campos descuentos de
Detalles.
Obligatorio, si
<codDocReembolso>00</codDocReembolso>  <codDocReembolso> es igual a  Numérico  Max 2
41.
Obligatorio, si
<codDocReembolso> es igual a
<totalComprobantesReembolso>56.00</totalComprobantesReembolso>  41, corresponde a la suma de  Numérico  Max 14
<totalBaseImponibleReembolso
> y <totalImpuestoReembolso>
Obligatorio, si
<totalBaseImponibleReembolso>50.00</totalBaseImponibleReembolso>  Numérico  Max 14
<codDocReembolso> es igual a
41, corresponde a la suma de

121

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     | C A M P O   | F O R M A T O   |
| --- | --- | ----------- | --------------- |
<BaseImponibleReembolso>
Obligatorio, si
<codDocReembolso> es igual a
41, corresponde a la sumatoria
<totalImpuestoReembolso>6.00</totalImpuestoReembolso>  Numérico  Max 14
de los tags
<impuestoReembolso>, el cual
es mayor o igual a la sumatoria.
| <totalConImpuestos>  | Obligatorio  | -   | -   |
| -------------------- | ------------ | --- | --- |
| <totalImpuesto>      | Obligatorio  | -   | -   |
<codigo>2</codigo>  Ob li g a t o r i o ,  c o n fo r m e  t a b la  1 6  Numérico  Max 2

| d                                       | e   la   F i c h a   Té c n ic a  O f f lin e |           |        |
| --------------------------------------- | --------------------------------------------- | --------- | ------ |
| Ob li                                   | g a t o r i o ,  c o n fo r m e  t a b la     |  1 7      |        |
| <codigoPorcentaje>2</codigoPorcentaje>  |                                               | Numérico  | Max 2  |
| d                                       | e   la   F i c h a   Té c n ic a  O f f lin e |           |        |
<descuentoAdicional>0.00</descuentoAdicional>  Opcional  Numérico  Max 14
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
Min 1 Max 4 / 2
| <tarifa>12</tarifa>  | Obligatorio  | Numérico  | enteros, 2  |
| -------------------- | ------------ | --------- | ----------- |
decimales
| <valor>6.00</valor>   | Obligatorio  | Numérico  | Max 14  |
| --------------------- | ------------ | --------- | ------- |
| </totalImpuesto>      | Obligatorio  | -         | -       |
| </totalConImpuestos>  | Obligatorio  | -         | -       |
Obligatorio corresponde a la
<importeTotal>56.00</importeTotal>  sumatoria de bases imponibles  Numérico  Max 14
e impuestos.
| <moneda>moneda0</moneda>   | Obligatorio                                  | Alfanumérico  | Max 14  |
| -------------------------- | -------------------------------------------- | ------------- | ------- |
| <pagos>                    | Obligatorio                                  | -             | -       |
| <pago>                     | Obligatorio                                  | -             | -       |
| Ob li                      | g a to r i o .  C o n fo r m e  t a b la     |  2 4          |         |
| <formaPago>01</formaPago>  |                                              | Numérico      | Max 2   |
| d                          | e   la  F i c h a  T é c n ic a  O f fl in e |               |         |
| <total>56.00</total>       | Obligatorio                                  | Numérico      | Max 14  |
| <plazo>30</plazo>          | Obligatorio                                  | Numérico      | Max 14  |
<unidadTiempo>unidadTiem</unidadTiempo>  Opcional  Texto  Max 10
| </pago>                   | Obligatorio  | -   | -   |
| ------------------------- | ------------ | --- | --- |
| </pagos>                  | Obligatorio  | -   | -   |
| </infoLiquidacionCompra>  | Obligatorio  | -   | -   |
| <detalles>                | Obligatorio  | -   | -   |
| <detalle>                 | Obligatorio  | -   | -   |
<codigoPrincipal>codigoPrincipal0</codigoPrincipal>  Obligatorio  Alfanumérico  Max 25
<codigoAuxiliar>codigoAuxiliar0</codigoAuxiliar>  Opcional  Alfanumérico  Max 25
<descripcion>descripcion0</descripcion>  Obligatorio  Alfanumérico  Max 300
<unidadMedida>unidadMedida0</unidadMedida>  Opcional  Alfanumérico  Max 50
<cantidad>1.000000</cantidad>  Obligatorio  Numérico  Max 14
<precioUnitario>50.000000</precioUnitario>  Obligatorio  Numérico  Max 14
| <descuento>0.00</descuento>  | Opcional  | Numérico  | Max 14  |
| ---------------------------- | --------- | --------- | ------- |
<precioTotalSinImpuesto>50.00</precioTotalSinImpuesto>  Ob l ig a to r i o ,  d e b e   m u l t ip l i c a r  el  Numérico  Max 14

| c a                    | m p o   p r e c io   p o r  c a n t i d a d |     |     |
| ---------------------- | ------------------------------------------- | --- | --- |
| <detallesAdicionales>  | Opcional                                    | -   | -   |
<detAdicional nombre="nombre0" valor="valor0" />  Opcional  Alfanumérico  Max 300
<detAdicional nombre="nombre1" valor="valor1" />  Opcional  Alfanumérico  Max 300
| </detallesAdicionales>  | Opcional     | -   | -   |
| ----------------------- | ------------ | --- | --- |
| <impuestos>             | Obligatorio  | -   | -   |

122

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|             |              |     | C A M P O   | F O R M A T O   |
| ----------- | ------------ | --- | ----------- | --------------- |
| <impuesto>  | Obligatorio  |     | -           | -               |
<codigo>2</codigo>  Ob li g a t o r i o ,  c o n fo r m e  t a b la  1 6  Numérico  Max 2
|     | d e   la   F i c | h a   Té c n ic a  O f f lin e   |     |     |
| --- | ---------------- | -------------------------------- | --- | --- |
<codigoPorcentaje>2</codigoPorcentaje>  Ob li g a t o r i o ,  c o n fo r m e  t a b la  1 7  Numérico  Max 2

|     | d e   la   F i c | h a   Té c n ic a  O f f lin e |     |     |
| --- | ---------------- | ------------------------------ | --- | --- |
Obligatorio cuando
|                      | <codDocReembolso> sea igual    |     |           | Min   1   M a x   4   / 2  |
| -------------------- | ------------------------------ | --- | --------- | -------------------------- |
| <tarifa>12</tarifa>  |                                |     | Numérico  | e n t e ro s ,   2         |
|                      | a 41, conforme tabla 17 de la  |     |           | decimales                  |
Ficha Técnica Offline
<baseImponible>50.00</baseImponible>  Obligatorio  Numérico  Max 14
| <valor>6.00</valor>  | Obligatorio  |     | Numérico  | Max 14  |
| -------------------- | ------------ | --- | --------- | ------- |
| </impuesto>          | Obligatorio  |     | -         | -       |
| </impuestos>         | Obligatorio  |     | -         | -       |
| </detalle>           | Obligatorio  |     | -         | -       |
| </detalles>          | Obligatorio  |     | -         | -       |
Obligatorio cuando
| <reembolsos>  | <codDocReembolso> sea igual  |     | -   | -   |
| ------------- | ---------------------------- | --- | --- | --- |
a 41
Obligatorio cuando
| <reembolsoDetalle>  |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
Obligatorio cuando
<codDocReembolso> sea igual
| < t ip o Id e n tificacionProveedorReembolso>04</tipoIdentificacionProveedorRee |             | a   4 1             |           |        |
| ------------------------------------------------------------------------------- | ----------- | ------------------- | --------- | ------ |
|                                                                                 |             |                     | Numérico  | Max 2  |
| m b o ls o >                                                                    | Validar cód | i g o   de tipo de  |           |        |
identificación conforme tabla 6
de la Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso> sea igual

< id e n t if ic a c io n P ro v e edorReembolso>identificacionProvee</identificacionPro a   4 1 Numérico  Max 20

ve e d o r R e e m b o ls o > Validar cód i g o   de tipo de
identificación conforme tabla
26 de la Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso> sea igual
<codPaisPagoProveedorReembolso>000</codPaisPagoProveedorReembolso>  a 41  Numérico  Max 3
Validar de acuerdo tabla 25 de
la Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso> sea igual
<tipoProveedorReembolso>01</tipoProveedorReembolso>  Numérico  Max 2
a 41, Validar con tabla 26 de la
Ficha Técnica Offline
Obligatorio cuando
<codDocReembolso> sea igual
| <codDocReembolso>00</codDocReembolso>  |     |     | Numérico  | Max 3  |
| -------------------------------------- | --- | --- | --------- | ------ |
a 41, Validar tabla 3 de Ficha
Técnica
Obligatorio cuando
| <estabDocReembolso>000</estabDocReembolso>  |     |     | Numérico  | Max 3  |
| ------------------------------------------- | --- | --- | --------- | ------ |
<codDocReembolso> sea igual
a 41, conforme tabla 4
Obligatorio cuando
<ptoEmiDocReembolso>000</ptoEmiDocReembolso>  Numérico  Max 3
<codDocReembolso> sea igual
a 41
Obligatorio cuando
<secuencialDocReembolso>000000000</secuencialDocReembolso>  <codDocReembolso> sea igual  Numérico  Max 9
a 41
Obligatorio cuando
<fechaEmisionDocReembolso>01/01/2000</fechaEmisionDocReembolso>  <codDocReembolso> sea igual  Fecha  dd/mm/aaaa
a 41
Obligatorio cuando
< n u m eroautorizacionDocReemb>0000000000</numeroautorizacionDocRee Numérico  Max 10, 37 ó 49
|       | <codDocReem | b o l so> sea igual  |     |     |
| ----- | ----------- | -------------------- | --- | --- |
| m b > |             |                      |     |     |
a  4 1

123

ETIQUETAS O TAGS  CARACTER  T I PO   D E   L O N G IT U D   /
|     |     |     |     | C A M P O |   F O R M A T O   |
| --- | --- | --- | --- | --------- | ----------------- |
Obligatorio cuando
| <detalleImpuestos>  | <codDocReembolso> sea igual  |     |     | -   | -   |
| ------------------- | ---------------------------- | --- | --- | --- | --- |
a 41
Obligatorio cuando
| <detalleImpuesto>  |     |     |     | -   | -   |
| ------------------ | --- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
Obligatorio cuando
<codigo>2</codigo>  <codDocReembolso> sea igual  Numérico  Max 2
a 41
Obligatorio cuando
<codDocReembolso> sea igual
| <codigoPorcentaje>2</codigoPorcentaje>  |     |     |     | Numérico  | Max 2  |
| --------------------------------------- | --- | --- | --- | --------- | ------ |
a 41, conforme tabla 17 de la
Ficha Técnica Offline
|                      | Ob li | g a t o r i o ,  c | o n fo r m e  t a b la     |  1 7      | Min   1   M a x   4   / 2  |
| -------------------- | ----- | ------------------ | -------------------------- | --------- | -------------------------- |
| <tarifa>12</tarifa>  |       |                    |                            | Numérico  |                            |
|                      | d     | e   la   F i c h a |   Té c n ic a  O f f lin e |           | e n t e ro s ,   2         |
d e c im a l e s
Obligatorio cuando
<baseImponibleReembolso>50.00</baseImponibleReembolso>  <codDocReembolso> sea igual  Numérico  Max 14
a 41
Obligatorio cuando
<impuestoReembolso>6.00</impuestoReembolso>  Numérico  Max 14
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| </detalleImpuesto>  |     |     |     | -   | -   |
| ------------------- | --- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| </detalleImpuestos>  | <codDocReembolso> sea igual  |     |     | -   | -   |
| -------------------- | ---------------------------- | --- | --- | --- | --- |
a 41
Obligatorio cuando
| </reembolsoDetalle>  |     |     |     | -   | -   |
| -------------------- | --- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
Obligatorio cuando
| </reembolsos>  |     |     |     | -   | -   |
| -------------- | --- | --- | --- | --- | --- |
<codDocReembolso> sea igual
a 41
|                  |     | Obl ig a | t o r i o  c u a n do  |     |     |
| ---------------- | --- | -------- | ---------------------- | --- | --- |
| <maquinaFiscal>  |     |          |                        | -   | -   |
|                  |     | c o r    | r e s p o n d a        |     |     |
<marca>SISPAU</marca>  Obl ig a t o r i o  c u a n do  Alfanumérico  Min 1 Max 100

|     |     | c o r | r e s p o n d a |     |     |
| --- | --- | ----- | --------------- | --- | --- |
<modelo>ABC1234</modelo>  Obl ig a t o r i o  c u a n do  Alfanumérico  Min 1 Max 100

|                          |     | c o r    | r e s p o n d a        |               |         |
| ------------------------ | --- | -------- | ---------------------- | ------------- | ------- |
|                          |     | Obl ig a | t o r i o  c u a n do  |               |         |
| <serie>CGMC1405</serie>  |     |          |                        | Alfanumérico  | Max 30  |
|                          |     | c o r    | r e s p o n d a        |               |         |
| </maquinaFiscal>         |     | Obl ig a | t o r i o  c u a n do  | -             | -       |

|                  |     | c o r     | r e s p o n d a |     |     |
| ---------------- | --- | --------- | --------------- | --- | --- |
| <infoAdicional>  |     | Opcional  |                 | -   | -   |
<campoAdicional nombre="nombre4">campoAdicional0</campoAdicional>  Opcional  Alfanumérico  Max 300
<campoAdicional nombre="nombre5">campoAdicional1</campoAdicional>  Opcional  Alfanumérico  Max 300
| </infoAdicional>      |     | Opcional     |     | -   | -   |
| --------------------- | --- | ------------ | --- | --- | --- |
| </liquidacionCompra>  |     | Obligatorio  |     | -   | -   |

124

ANEXO 18 – REQUISITOS OBLIGATORIOS DE
LLENADO EN LA FACTURA ELECTRÓNICA
POR LA ENTREGA DE FUNDAS PLÁSTICAS
Aplica para establecimientos de comercio con tres (3) o más establecimientos
abiertos y, al franquiciador y sus franquiciados, independientemente del número de
sus establecimientos que entreguen fundas o bolsas plásticas tipo acarreo o
camiseta al adquiriente o consumidor, para cargar o llevar los productos adquiridos.
En la emisión del comprobante de venta tipo factura, en la sección <detalles> para
el llenado de los campos <cantidad>, <codigoPrincipal> y <descripcion> se deberá
llenar el número, código y la descripción de las fundas plásticas gravadas con ICE,
como un producto adicional a los vendidos, conforme el siguiente detalle:
<codigoPrin
<cantidad> <descripcion> <precioUnitario>
cipal>
ICE-FPN-01 Funda/bolsa plástica
Funda/bolsa plástica con rebaja 50% (aplicable para
Número de fundas o ICE-FPR-02
fundas biodegradables y compostables).
bolsas plásticas tipo 0,00*
camiseta o acarreo. Funda/bolsa plástica exenta (aplicable para fundas con
ICE-FPE-03 un mínimo de adición del 50% de materia prima
reciclada post consumo).
(*) Es importante recalcar que los agentes de percepción del ICE por concepto de
fundas plásticas no deberán establecer un precio de venta al público sugerido para
este bien, salvo que lo tuvieren.
El ICE corresponderá a la tarifa específica vigente multiplicada por la cantidad. (Ver
Tabla 18 – TARIFA DEL ICE).
El valor del ICE formará parte de la base imponible del IVA de conformidad con el
artículo 58 de la Ley de Régimen Tributario Interno.
Ejemplo de la estructura XML:
125

ANEXO 19 – APLICACIÓN DE LAS
AUTORETENCIONES
En el llenado del comprobante de retención que se emita por concepto de
autoretenciones de conformidad con la normativa correspondiente para cada caso,
se deberá considerar lo siguiente:
• Código y porcentaje para llenar en el comprobante de retención
Porcentaje de
Código de Concepto retención en la fuente de Impuesto a la
retención
retención Renta
(Desde 01/04/2020)
350 Otras autoretenciones 1,50 ó 1,75
3481 Autorretenciones Sociedades Grandes Contribuyentes Varios porcentajes
• El comprobante de retención se emite a nombre del mismo agente de retención,
esto es en el campo <identificacionSujetoRetenido> y
<razonSocialSujetoRetenido>
• En cuanto al campo <codDocSustento> se considerará:
➢ En la versión 1.0 del comprobante de retención electrónico se utilizará el
código de documento 42 (Documento retención presuntiva y retención
emitida por propio vendedor o por intermediario. (Ver Ejemplo 1 a
continuación).
➢ En la versión 2.0 del comprobante de retención electrónico se utilizará el
código de documento 42 (Documento retención presuntiva y retención
emitida por propio vendedor o por intermediario y el código de sustento de la
operación 12 (Impuestos y retenciones presuntivos). (Ver Ejemplo 2 a
continuación).
• En el campo <numDocSustento> ubicar el mismo número de comprobante de
retención por la autoretención que se está realizando.
Estas consideraciones aplican debido a que dicha retención no opera sobre compras
a terceros sino sobre sus propios ingresos.
126

Ejemplo 1 de la estructura XML – Comprobante de retención código 350:
Ejemplo 2 de la estructura XML – Comprobante de retención ATS versión
2.0.0 código 350:
127

Ejemplo 1 de la estructura XML – Comprobante de retención código 3481:
Ejemplo 2 de la estructura XML – Comprobante de retención ATS versión
2.0.0 código 3481:
128

ANEXO 20 – REQUISITO PARA LA
APLICACIÓN DE LA DEVOLUCIÓN
AUTOMÁTICA DEL IVA EN EL XML DE
FACTURAS, NOTAS DE CRÉDITO Y NOTAS
DE DÉBITO.
Las facturas, notas de crédito y notas de débito electrónicas deberá contener la
siguiente información en la estructura del XML, cuando aplique devolución del IVA,
cuyo valor deberá ser igual al autorizado por los servicios web – DIG, para el caso
de las notas de crédito deberá corresponder al valor que aplique al documento de
sustento:
• Campo Devolución IVA en la cabecera del XML:
<totalConImpuestos>
<totalImpuesto>
<codigo>2</codigo>
<codigoPorcentaje>0</codigoPorcentaje>
<descuentoAdicional>0.00</descuentoAdicional>
<baseImponible>50.00</baseImponible>
<tarifa>12.00</tarifa>
<valor>6.00</valor>
<valorDevolucionIva>6.00</valorDevolucionIva>
</totalImpuesto>
• Validaciones: Las validaciones en comprobantes electrónicos que se aplicarán al
campo son las siguientes:
➢ Tipo identificación del comprador o cliente según Tabla 6: Cédula (Código
05)
➢ Si el campo <valorDevolucionIva> es un valor mayor a cero, la clave de
acceso deberá estar registrada en el control de saldos del beneficiario y el
monto deberá ser igual al autorizado por el servicio web - DIG.
➢ El valor registrado en el campo <valorDevolucionIva> debe ser mayor o igual
a cero y menor o igual al campo <valor> de la misma sección. En caso de
que el campo se envíe con valor cero no aplica validación.
➢ Los campos que totalizan la factura <importeTotal>, nota de crédito
<valorModificacion> y débito <valorTotal>, deberán restar el valor
consignado en el campo <valorDevolucionIva>.
➢ Las facturas y notas de débito utilizarán los servicios web - DIG para el
registro del valor en el campo <valorDevolucionIva>.
129

ANEXO 21 – REQUISITO OBLIGATORIO PARA
COMPROBANTES ELECTRÓNICOS EMITIDOS
POR CONTRIBUYENTES DESIGNADOS COMO
AGENTES DE RETENCIÓN.
Los comprobantes de venta, retención y documentos complementarios electrónicos
deberán contener la leyenda Agente de Retención en la estructura del XML,
conforme las siguientes especificaciones:
• Agente de retención
Nombre de la etiqueta: <agenteRetencion>
Formato: Numérico
Caracteres: Máximo 8
Número de la resolución, omitiendo los ceros a la
Contenido:
izquierda
Entre la etiqueta <regimenMicroempresas> y
Ubicación:
</infoTributaria>
Ejemplo 1 – Contribuyente designado Agente de Retención
130

Ejemplo 2 – Formato RIDE
Nota: Se incluirán únicamente las etiquetas que correspondan al contribuyente.
ANEXO 22 – REQUISITO OBLIGATORIO PARA
COMPROBANTES ELECTRÓNICOS EMITIDOS
POR CONTRIBUYENTES RIMPE.
Los comprobantes de venta, retención y documentos complementarios electrónicos
deberán contener la leyenda CONTRIBUYENTE RÉGIMEN RIMPE o
CONTRIBUYENTE NEGOCIO POPULAR - RÉGIMEN RIMPE, conforme las
siguientes especificaciones:
• RIMPE
Nombre de la etiqueta: <contribuyenteRimpe>
Formato: Texto
Caracteres: 27 (Incluidos espacios)
Contenido: CONTRIBUYENTE RÉGIMEN RIMPE
Ubicación: Entre la etiqueta <agenteRetencion> y </infoTributaria>
131

Ejemplo 1 – Contribuyente RIMPE y Agente de Retención
Ejemplo 2 – Contribuyente RIMPE
132

Ejemplo 3 – Formato RIDE Contribuyente RIMPE
• Negocio popular
Nombre de la etiqueta: <contribuyenteRimpe>
Formato: Texto
Caracteres: 45 (Incluidos espacios)
Contenido: CONTRIBUYENTE NEGOCIO POPULAR - RÉGIMEN RIMPE
Ubicación: Entre la etiqueta <agenteRetencion> y </infoTributaria>
Ejemplo 4 – Contribuyente Negocio Popular
133

Ejemplo 5 – Formato RIDE Contribuyente Negocio Popular
ANEXO 23 – REQUISITO OBLIGATORIO EL
LLENADO PARA EL XML DE
COMPROBANTES DE VENTA EN LA
TRANSFERENCIA LOCAL DE MATERIALES
DE CONSTRUCCIÓN.
En la emisión de comprobantes por la transferencia local de materiales de
construcción establecidos en la Resolución No. NAC-DGERCGC24-00000013, en
la sección <detalles>, en el campo <codigoAuxiliar> se deberá colocar
obligatoriamente los siguientes códigos de manera exacta:
TABLA 31
<codigoAuxiliar> Subcategoría material de construcción
VARILLA LAMINADA CORRUGADA AS42 DE 8MM, 10MM Y 12MM
F010101
DE DIÁMETRO
F010201 ARCILLA
F010202 ARENA
F010203 CAL
F010204 CALIZA
F010205 PÉTROS
134

F010301 HORMIGÓN PREMEZCLADO
F010401 CEMENTO Y SUS DERIVADOS
F010402 RESIDUO CEMENTO
F010501 CHATARRA FERROSA
F010601 MORTERS
F010701 CLINKER
F010702 PUZOLANA
F010703 YESO
F010801 ADOQUÍN
F010802 BLOQUES
F010803 LADRILLOS
F010804 PRODUCTOS DE HORMIGÓN PREFABRICADO
ANEXO 24 – REQUISITO OBLIGATORIO PARA
COMPROBANTES ELECTRÓNICOS EMITIDOS
POR GRANDES CONTRIBUYENTES.
Los comprobantes de venta, notas de crédito y notas de débito electrónicos
deberán contener la leyenda “Gran Contribuyente” y el número de la resolución
mediante la cual fueron calificados como tal, en la estructura del XML, conforme las
siguientes especificaciones:
• Gran Contribuyente
Nombre de la etiqueta: <campoadicional>
Formato: Alfanumérico
Caracteres: Máximo 300
Contenido: Leyenda “Gran Contribuyente” y número de resolución
Ubicación: Entre las etiquetas <infoAdicional> y </infoAdicional>
Ejemplo 1 – Contribuyente designado gran contribuyente
135

Ejemplo 2 – Formato RIDE
ANEXO 25 – REQUISITO OBLIGATORIO DE
LLENADO PARA EL XML DE FACTURAS
EMITIDAS POR OPERADORAS TRANSPORTE
COMERCIAL (NO APLICA PARA TAXIS Y
SOCIOS O ACCIONISTAS DE TAXIS).
De conformidad con el artículo 57 de la Ley de Transporte Terrestre Tránsito y
Seguridad Vial, el cual establece que los servicios de transporte comercial deben
ser prestados únicamente por operadoras de transporte terrestre autorizadas
para tal objeto, y el artículo 189 del Reglamento a la Ley de Régimen Tributario
Interno que señala que la contratación de servicios terrestre comercial, salvo los
prestados por taxis, será realizado únicamente por las operadoras
debidamente autorizadas por el organismo de tránsito competente.
La Circular No. NAC-DGECCGC24-00000005 establece que, solamente los
servicios de transporte terrestre comercial que estén sustentados en
comprobantes de venta emitidos por las operadoras de transporte terrestre
comercial, excepto taxis, autorizadas por la autoridad competente, pueden
considerarse como deducibles para determinar la base imponible del impuesto a
la renta. Así mismo únicamente en estos casos, el servicio se encuentra gravado
con tarifa 0% del impuesto al valor agregado.
Requisito: En las facturas electrónicas emitidas por la prestación de servicios de
transporte comercial, excepto taxis, por parte de las operadoras de transporte
debidamente autorizadas, así como en aquellas emitidas por parte de sus socios o
accionistas, en la sección <detalles>, para el llenado del campo <codigoAuxiliar>
de las facturas electrónicas se deberá considerar la información conforme al
siguiente detalle:
136

TABLA 32
<codigoAuxiliar> Caso Observación
Aplica en las facturas emitidas
por la operadora de transporte
Facturas emitidas por comercial (excepto taxis)
H492001
la operadora al cliente debidamente autorizada, a sus
clientes por la prestación de
servicio de transporte
Facturas emitidas por Aplica en las facturas emitidas
H492002
el socio o accionista
o
p
p
o
e
r
r a
e
d
l
o
s
r
o
a
c
d
io
e
o
tr a
a
n
c
s
c
p
io
or
n
te
is
p
ta
o
,
r
a
s u
la
s
a la operadora de
servicios
transporte
Los códigos arriba detallados deberán incluirse en la factura electrónica en el campo
<codigoAuxiliar> de cada ítem que corresponda a la actividad de transporte comercial.
Nota: Este requisito puede ser implementado desde su publicación en la Ficha Técnica
de Comprobantes Electrónicos, sin embargo, para efectos de ajustes en los sistemas
tecnológicos de los sujetos pasivos emisores de comprobantes electrónicos, este
requisito será obligatorio desde el 01 de noviembre de 2025.
15. Glosario de términos
ARCHIVOS PLANOS:
Son archivos que están compuestos únicamente por texto sin formato, sólo caracteres.
AMPERSAND (&):
El signo & (ampersand), deberá incorporarse en los comprobantes electrónicos de la
siguiente manera “&amp;” caso contrario al solicitar la autorización se rechazará con
motivo de mal estructurado.
COMERCIO ELECTRÓNICO:
Es toda transacción comercial realizada en parte o en su totalidad, a través de redes
electrónicas de información.
DBF:
(Data Base File). Es la extensión que corresponde a un tipo de fichero de bases de
datos, originalmente utilizado por el SGBD Dbase, pero que es frecuente encontrar en
todo tipo de aplicaciones como el Lenguaje de Programación FOX PRO.
DOCUMENTO ELECTRÓNICO:
Es la emisión mediante mensaje de datos (documentos desmaterializados) de los
comprobantes de venta, retención y documentos complementarios.
137

ETIQUETAS O TAGS:
Etiqueta en lenguaje marcado. Es una marca con tipo que delimita una región en los
lenguajes basados en XML.
ESQUEMA OFFLINE:
En este esquema el número de autorización es la clave de acceso generada por el
emisor y los archivos XML contendrán únicamente la cave de acceso (49 dígitos).
Normativa: Resolución No. NAC-DGERCGC14-00790.
INTERFACES (Plural de interfaz):
En informática, es un elemento de conexión que facilita el intercambio de datos.
También se lo define como el conjunto de métodos para lograr interactividad entre un
usuario y una computadora.
LOG:
Registro oficial de eventos durante un rango de tiempo en particular. En seguridad
informática es usado para registrar datos o información sobre quién, qué, cuándo, dónde
y por qué un evento ocurre para un dispositivo en particular o aplicación.
MENSAJES DE DATOS:
Es toda información creada, generada, procesada, enviada, recibida, comunicada o
archivada por medios electrónicos, que puede ser intercambiada por cualquier medio.
Serán considerados como mensajes de datos, sin que esta enumeración limite su
definición, los siguientes documentos electrónicos, registros electrónicos, correo
electrónico, servicios web, telegrama, télex, fax e intercambio electrónico de datos.
MÓDULO:
Componente auto controlado de un sistema, dicho componente posee una interfaz bien
definida hacia otros componentes; algo es modular si está construido de manera tal que
se facilite su ensamblaje, acomodamiento flexible y reparación de sus componentes.
PASSWORD:
Clave de acceso. Es una forma de autentificación que utiliza información secreta para
controlar el acceso hacia algún recurso.
PKCS:
En criptografía, PKCS se refiere a un grupo de estándares de criptografía de clave
pública concebidos y publicados por los laboratorios de RSA en California.
RCVRYDC:
Reglamento de Comprobantes de Venta, Retención y Documentos Complementarios,
publicado en el Registro Oficial 247, del 30 de Julio de 2010 y sus reformas.
SERVICIO ELECTRÓNICO:
Es toda actividad realizada a través de redes electrónicas de información.
SGBD:
Siglas de Sistema Gestor de Base de Datos; programas que permiten almacenar y
posteriormente acceder a los datos de forma rápida y estructurada.
138

SISTEMA DE INFORMACIÓN:
Es todo dispositivo físico o lógico utilizado para crear, generar, enviar, recibir, procesar,
comunicar o almacenar, de cualquier forma, mensajes de datos.
USERNAME:
Nombre de usuario de un sistema computarizado que obedece a un perfil o roles
asignados por un Administrador.
UTF-8:
UTF-8 (8-bit Unicode Transformation Format) es un formato de codificación de
caracteres Unicode e ISO 10646 utilizando símbolos de longitud variable, capaz de
representar cualquier CARACTER Unicode.
WEB SERVICE:
Un servicio web (en inglés, Web service) es una pieza de software que utiliza un
conjunto de protocolos y estándares que sirven para intercambiar datos entre
aplicaciones. Distintas aplicaciones de software desarrolladas en lenguajes de
programaciones diferentes y ejecutadas sobre cualquier plataforma pueden utilizar los
servicios web para intercambiar datos en redes de ordenadores como Internet.
XAdES:
Firma electrónica avanzada XML. Es un conjunto de extensiones a las recomendaciones
XML-DSig haciéndolas adecuadas para la firma electrónica avanzada.
XML:
Siglas en inglés de EXtensible Markup Language (lenguaje de marcas extensible); es un
estándar para el intercambio de información estructurada entre diferentes plataformas.
XSD:
XML Schema es un lenguaje de esquema utilizado para describir la estructura y las
restricciones de los contenidos de los documentos XML de una forma muy precisa.
139

16. Preguntas técnicas frecuentes
Pregunta Solución
Hay dos tipos de firmado: uno que firma el archivo completo y otro el
nodo especifico; se debe revisar el archivo XML y verificar que esté
firmado el nodo como en el siguiente ejemplo:
Firma inválida- El nodo comprobante
no está firmado.
Se puede validar el firmado con herramientas auxiliares de validación,
como la herramienta XOLIDOSIGN. Link de descarga:
Firma inválida- La estructura de la
http://www.xolido.com/lang/productosxolidosign/xolidosignescritorio
firma es incorrecta.
/modulo/?refbol=xolidosign-escritorio&refsec=xolidosign-
escritorio_descargas
Se puede validar el firmado con herramientas auxiliares de validación,
como la herramienta XOLIDOSIGN. Link de descarga:
http://www.xolido.com/lang/productosxolidosign/xolidosignescritorio
Firma inválida- La firma no
/modulo/?refbol=xolidosign-escritorio&refsec=xolidosign-
corresponde con el contenido del
escritorio_descargas
documento.
Generalmente estos errores se deben a que en el documento existen
caracteres extraños, el contribuyente debe verificar en los campos de
descripción o tipo texto del XML.
Favor re-enviar todos los comprobantes que no fueron autorizados por
"[Firma inválida. La fecha contenida en la firma es posterior a la
actual]". Al respecto la fecha y hora de nuestros servidores están
configurados con un servidor NTP.
Firma inválida- La fecha de la firma es
posterior a la actual.
server 0.south-america.pool.ntp.org maxpoll 12
server 1.south-america.pool.ntp.org maxpoll 12
server 2.south-america.pool.ntp.org maxpoll 12
Se puede validar el firmado con herramientas auxiliares de validación,
como la herramienta XOLIDOSIGN. Link de descarga:
http://www.xolido.com/lang/productosxolidosign/xolidosignescritorio
Firma inválida- No existe el RUC en el /modulo/?refbol=xolidosign-escritorio&refsec=xolidosign-
certificado digital. escritorio_descargas
En la herramienta muestra el certificado con el que fue firmado el
archivo.
PASOS para validar:
140

Pregunta Solución
1. Seleccionar el archivo, clic en verificar.
2. Clic en el botón certificado.
3. Clic en detalles y luego en el tag que contiene el dato del RUC.
141

Pregunta Solución
Revisar en la página web del SRI si la clave de acceso ya fue
Clave de acceso registrada.
autorizada.
Es responsabilidad del emisor controlar la no generación de un mismo
secuencial para un mismo tipo de comprobante (cabe recordar que
Secuencial registrado.
estos casos debieron ser detectados y corregidos en el ambiente de
pruebas).
El RUC ingresado en la identificación del receptor no consta en la base
RUC no existe.
de RUC, esto se puede validar en la página Web del SRI.
Verificar que todos los datos ingresados para la anulación sean
correctos; debe coincidir con los datos del comprobante a anular, se
No se pueden anular comprobantes.
puede consultar en la página WEB del SRI o en Intranet en la opción
de Consultas.
Comprobantes no autorizados por
Abrir el XML y revisar que todos los cálculos estén correctos.
error en diferencias.
Validar si el RUC del emisor presenta alertas de Infracciones en la
RUC clausurado.
aplicación de RUC o consultar con el área de Infracciones.
Revisar el uso correcto de las versiones de los archivos XML:
Número de decimales en la estructura
Pueden utilizar dos decimales en la versión 1.0.0 y seis decimales en la
del XML del comprobante.
versión 1.1.0.
142

Pregunta Solución
Revisar en las consultas públicas mediante el portal web
Validar el estado del Comprobante.
www.sri.gob.ec, el estado del comprobante.
Un comprobante en estado no autorizado está atado a un mensaje de
Que quiere decir comprobante no rechazo, puede ser cualquiera de los errores detallados en esta ficha
autorizado. técnica. Es importante notar que pueden existir varias respuestas en
estado no autorizado y una única respuesta en estado autorizado.
143