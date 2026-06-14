'use client';

import { Shield } from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';

export function LOPDPolicy() {
  return (
    <Card>
      <CardHeader>
        <div className="rounded-lg bg-blue-100 dark:bg-blue-900/30 w-12 h-12 flex items-center justify-center mb-3">
          <Shield className="h-6 w-6 text-blue-600" />
        </div>
        <CardTitle>L.O.P.D — Ley Organica de Proteccion de Datos Personales</CardTitle>
        <CardDescription>Republica del Ecuador</CardDescription>
      </CardHeader>
      <CardContent className="prose prose-sm dark:prose-invert max-w-none space-y-4">
        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">1. Objeto de la Ley</h3>
          <p className="text-sm text-muted-foreground">
            La presente Ley tiene por objeto garantizar y proteger el ejercicio del derecho a la proteccion de datos de caracter personal, asi como la libre circulacion de estos datos, en el territorio ecuatoriano, con el fin de fortalecer el derecho a la autodeterminacion informativa.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">2. Ambito de Aplicacion</h3>
          <p className="text-sm text-muted-foreground">
            Esta ley se aplica a todo tratamiento de datos personales realizado en el Ecuador, independientemente de donde resida el titular de los datos. ContaEC, como sistema de facturacion electronica, recopila y procesa datos personales de usuarios, clientes y empresas en cumplimiento de esta normativa.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">3. Datos que Recopilamos</h3>
          <ul className="text-sm text-muted-foreground space-y-1 list-disc ml-4">
            <li>Informacion de registro: nombre completo, correo electronico, telefono</li>
            <li>Informacion empresarial: RUC, razon social, direccion de empresa</li>
            <li>Informacion de facturacion: datos de clientes, comprobantes electronicos</li>
            <li>Informacion tecnica: direccion IP, navegador, dispositivo de acceso</li>
            <li>Datos de uso: funcionalidades utilizadas, frecuencia de acceso</li>
          </ul>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">4. Derechos del Titular</h3>
          <p className="text-sm text-muted-foreground mb-2">Como titular de datos personales, usted tiene derecho a:</p>
          <ul className="text-sm text-muted-foreground space-y-1 list-disc ml-4">
            <li><strong>Acceso:</strong> Conocer que datos personales suyos estan siendo tratados</li>
            <li><strong>Rectificacion:</strong> Solicitar la correccion de datos inexactos o incompletos</li>
            <li><strong>Cancelacion (supresion):</strong> Solicitar la eliminacion de sus datos cuando ya no sean necesarios</li>
            <li><strong>Oposicion:</strong> Oponerse al tratamiento de sus datos personales</li>
            <li><strong>Revocacion:</strong> Retirar el consentimiento otorgado para el tratamiento de sus datos</li>
          </ul>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">5. Seguridad de los Datos</h3>
          <p className="text-sm text-muted-foreground">
            ContaEC implementa medidas tecnicas y organizativas adecuadas para proteger los datos personales contra el tratamiento no autorizado o ilicito, su perdida, destruccion o dano accidental. Estas incluyen: cifrado de datos en transito y en reposo, controles de acceso basados en roles, auditoria de acciones del sistema y copias de seguridad regulares.
          </p>
        </div>

        <div className="rounded-lg border p-4 bg-muted/50">
          <h3 className="text-base font-semibold mb-2">6. Contacto</h3>
          <p className="text-sm text-muted-foreground">
            Para ejercer cualquiera de sus derechos o para consultas relacionadas con la proteccion de sus datos personales, puede contactarnos en: <strong>info@tymtechnology.shop</strong> o al telefono <strong>0960068866</strong>.
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
