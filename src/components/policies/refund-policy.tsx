'use client';

import { DollarSign } from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';

export function RefundPolicy() {
  return (
    <Card>
      <CardHeader>
        <div className="rounded-lg bg-amber-100 dark:bg-amber-900/30 w-12 h-12 flex items-center justify-center mb-3">
          <DollarSign className="h-6 w-6 text-amber-600" />
        </div>
        <CardTitle>Politica de Reembolso</CardTitle>
        <CardDescription>Condiciones de devolucion y reembolso de ContaEC</CardDescription>
      </CardHeader>
      <CardContent className="prose prose-sm dark:prose-invert max-w-none space-y-4">
        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">1. Periodo de Garantia</h3>
          <p className="text-sm text-muted-foreground">
            ContaEC ofrece un periodo de garantia de <strong>7 dias calendario</strong> a partir de la fecha de compra de cualquier plan de licencia. Durante este periodo, si el usuario no esta satisfecho con el servicio, puede solicitar un reembolso completo sin necesidad de justificacion.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">2. Condiciones para el Reembolso</h3>
          <ul className="text-sm text-muted-foreground space-y-1 list-disc ml-4">
            <li>La solicitud debe realizarse dentro de los 7 dias posteriores a la compra</li>
            <li>El usuario no debe haber emitido mas de <strong>10 comprobantes electronicos</strong> durante el periodo de prueba</li>
            <li>No debe haber habido uso fraudulento o violacion de los terminos y condiciones</li>
            <li>El reembolso aplica solo para la ultima transaccion de compra de licencia</li>
          </ul>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">3. Exclusiones</h3>
          <p className="text-sm text-muted-foreground">No aplican reembolso los siguientes casos:</p>
          <ul className="text-sm text-muted-foreground space-y-1 list-disc ml-4">
            <li>Solicitudes realizadas despues del periodo de 7 dias</li>
            <li>Usuarios que hayan excedido el limite de comprobantes permitido</li>
            <li>Cuentas suspendidas por violacion de terminos y condiciones</li>
            <li>Licencias ya utilizadas para emision comprobantes en produccion con el SRI</li>
          </ul>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">4. Proceso de Reembolso</h3>
          <ol className="text-sm text-muted-foreground space-y-1 list-decimal ml-4">
            <li>Enviar solicitud por correo a <strong>info@tymtechnology.shop</strong> indicando: nombre completo, correo de la cuenta, tipo de licencia adquirida y motivo del reembolso</li>
            <li>El equipo de T&M Technology Ec evaluara la solicitud en un plazo de <strong>5 dias habiles</strong></li>
            <li>Si es aprobada, el reembolso se procesara al mismo metodo de pago utilizado en la compra</li>
            <li>El tiempo de acreditacion del reembolso depende del procesador de pago (generalmente 7-15 dias habiles)</li>
          </ol>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">5. Cancelacion de Suscripcion</h3>
          <p className="text-sm text-muted-foreground">
            El usuario puede cancelar su suscripcion en cualquier momento desde su perfil. La cancelacion impide la renovacion automatica de la licencia, pero el usuario mantendra acceso hasta la fecha de expiracion de la licencia vigente. No se realizan reembolsos proporcionales por tiempo no utilizado fuera del periodo de garantia.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">6. Contacto</h3>
          <p className="text-sm text-muted-foreground">
            Para solicitar un reembolso: <strong>info@tymtechnology.shop</strong> | <strong>0960068866</strong>
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
