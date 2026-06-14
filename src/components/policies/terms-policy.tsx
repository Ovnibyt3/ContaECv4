'use client';

import { FileText } from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';

export function TermsPolicy() {
  return (
    <Card>
      <CardHeader>
        <div className="rounded-lg bg-emerald-100 dark:bg-emerald-900/30 w-12 h-12 flex items-center justify-center mb-3">
          <FileText className="h-6 w-6 text-emerald-600" />
        </div>
        <CardTitle>Terminos y Condiciones de Uso</CardTitle>
        <CardDescription>Acuerdo entre el usuario y T&M Technology Ec para el uso de ContaEC</CardDescription>
      </CardHeader>
      <CardContent className="prose prose-sm dark:prose-invert max-w-none space-y-4">
        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">1. Aceptacion de los Terminos</h3>
          <p className="text-sm text-muted-foreground">
            Al registrarse y utilizar el sistema ContaEC, el usuario acepta plenamente los presentes Terminos y Condiciones. Si no esta de acuerdo con alguno de estos terminos, le solicitamos que no utilice el servicio. T&M Technology Ec se reserva el derecho de modificar estos terminos en cualquier momento, notificando a los usuarios de cambios significativos.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">2. Descripcion del Servicio</h3>
          <p className="text-sm text-muted-foreground">
            ContaEC es un sistema de facturacion electronica y gestion contable disenado para empresas ecuatorianas. El servicio incluye: emision de comprobantes electronicos (facturas, notas de credito, notas de debito, retenciones, guias de remision), gestion de empresas, clientes, productos, inventario, reportes contables, y herramientas de gestion empresarial.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">3. Registro y Cuenta de Usuario</h3>
          <ul className="text-sm text-muted-foreground space-y-1 list-disc ml-4">
            <li>El usuario debe proporcionar informacion veraz y actualizada durante el registro</li>
            <li>Cada usuario es responsable de mantener la confidencialidad de sus credenciales de acceso</li>
            <li>Se permite una cuenta por usuario; el compartir cuentas esta prohibido</li>
            <li>T&M Technology Ec se reserva el derecho de suspender cuentas que violen estos terminos</li>
          </ul>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">4. Licencia de Uso</h3>
          <p className="text-sm text-muted-foreground">
            El acceso a ContaEC se otorga bajo un modelo de licencia por suscripcion. Los limites de uso (numero de empresas, usuarios, comprobantes, etc.) varian segun el plan adquirido. La licencia es personal e intransferible. El usuario no puede copiar, modificar, distribuir o reverse-engineer el software.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">5. Obligaciones del Usuario</h3>
          <ul className="text-sm text-muted-foreground space-y-1 list-disc ml-4">
            <li>Utilizar el sistema de acuerdo con las leyes ecuatorianas vigentes</li>
            <li>No utilizar el sistema para actividades ilicitas o fraudulentas</li>
            <li>Mantener actualizada la informacion de su empresa y datos fiscales</li>
            <li>No intentar acceder a datos de otros usuarios o a funciones administrativas no autorizadas</li>
            <li>Reportar cualquier vulnerabilidad de seguridad descubierta</li>
          </ul>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">6. Limitacion de Responsabilidad</h3>
          <p className="text-sm text-muted-foreground">
            T&M Technology Ec no se responsabiliza por interrupciones temporales del servicio por mantenimiento, fallas de terceros, o casos de fuerza mayor. El usuario es responsable de la veracidad de la informacion ingresada al sistema y del cumplimiento de sus obligaciones tributarias ante el SRI.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">7. Contacto</h3>
          <p className="text-sm text-muted-foreground">
            Para consultas sobre estos terminos: <strong>info@tymtechnology.shop</strong> | <strong>0960068866</strong>
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
