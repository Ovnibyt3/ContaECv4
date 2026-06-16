#!/bin/bash
# Download SRI XSD schema files for XML validation
# Run this on the server with internet access
# Source: https://sri.gob.ec

XSD_DIR="$(dirname "$0")"

echo "Downloading SRI XSD schemas..."

curl -sS -o "${XSD_DIR}/factura_V1.1.0.xsd" "https://sri.gob.ec/images/sri/ws/factura_V1.1.0.xsd"
curl -sS -o "${XSD_DIR}/notaCredito_V1.1.0.xsd" "https://sri.gob.ec/images/sri/ws/notaCredito_V1.1.0.xsd"
curl -sS -o "${XSD_DIR}/notaDebito_V1.1.0.xsd" "https://sri.gob.ec/images/sri/ws/notaDebito_V1.1.0.xsd"
curl -sS -o "${XSD_DIR}/comprobanteRetencion_V1.1.0.xsd" "https://sri.gob.ec/images/sri/ws/comprobanteRetencion_V1.1.0.xsd"
curl -sS -o "${XSD_DIR}/guiaRemision_V1.1.0.xsd" "https://sri.gob.ec/images/sri/ws/guiaRemision_V1.1.0.xsd"
curl -sS -o "${XSD_DIR}/liquidacionCompra_V1.1.0.xsd" "https://sri.gob.ec/images/sri/ws/liquidacionCompra_V1.1.0.xsd"

# Verify downloads
for f in factura notaCredito notaDebito comprobanteRetencion guiaRemision liquidacionCompra; do
  if [ -s "${XSD_DIR}/${f}_V1.1.0.xsd" ]; then
    echo "OK: ${f}_V1.1.0.xsd ($(wc -c < "${XSD_DIR}/${f}_V1.1.0.xsd") bytes)"
  else
    echo "MISSING: ${f}_V1.1.0.xsd - check internet connection"
  fi
done
