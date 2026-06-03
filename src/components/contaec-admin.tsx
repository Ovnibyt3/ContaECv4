'use client';

import { useState, useEffect, useCallback } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Label } from '@/components/ui/label';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import {
  ArrowLeft,
  AlertTriangle,
  CheckCircle2,
  Database,
  Heart,
  Loader2,
  Shield,
  ShieldAlert,
  ShieldCheck,
  Users,
  Settings,
  Key,
  Activity,
  RefreshCw,
  UserCheck,
  UserX,
} from 'lucide-react';
import { toast } from 'sonner';
import {
  getAdminStats,
  getAdminUsers,
  modifyUserLicense,
  toggleUserActive,
  getSystemHealth,
  getSecurityIssues,
  type AdminStats,
  type AdminUser,
} from '@/lib/api';

interface ContaECAdminProps {
  onBack: () => void;
}

export function ContaECAdmin({ onBack }: ContaECAdminProps) {
  const [activeTab, setActiveTab] = useState('overview');
  const [stats, setStats] = useState<AdminStats | null>(null);
  const [users, setUsers] = useState<AdminUser[]>([]);
  const [health, setHealth] = useState<{
    system: Record<string, unknown>;
    database: Record<string, unknown>;
    application: Record<string, unknown>;
  } | null>(null);
  const [securityData, setSecurityData] = useState<{
    expired_active_licenses: Array<{ user_id: string; email: string; full_name: string; license_end_date: string | null; days_expired: number | null }>;
    users_without_config: Array<{ user_id: string; email: string; full_name: string }>;
  } | null>(null);
  const [loading, setLoading] = useState(true);

  // License modification dialog
  const [licenseDialogOpen, setLicenseDialogOpen] = useState(false);
  const [selectedUser, setSelectedUser] = useState<AdminUser | null>(null);
  const [licenseForm, setLicenseForm] = useState({ license_type: '' });
  const [modifying, setModifying] = useState(false);

  const loadAdminData = useCallback(async () => {
    setLoading(true);
    try {
      const results = await Promise.allSettled([
        getAdminStats(),
        getAdminUsers(),
        getSystemHealth(),
        getSecurityIssues(),
      ]);

      if (results[0].status === 'fulfilled') setStats(results[0].value);
      if (results[1].status === 'fulfilled') setUsers(results[1].value);
      if (results[2].status === 'fulfilled') setHealth(results[2].value);
      if (results[3].status === 'fulfilled') setSecurityData(results[3].value);
    } catch {
      toast.error('Error al cargar datos de administracion');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadAdminData();
  }, [loadAdminData]);

  async function handleModifyLicense() {
    if (!selectedUser) return;
    setModifying(true);
    try {
      await modifyUserLicense(selectedUser.id, { license_type: licenseForm.license_type });
      const updatedUsers = await getAdminUsers();
      setUsers(updatedUsers);
      setLicenseDialogOpen(false);
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al modificar licencia');
    } finally {
      setModifying(false);
    }
  }

  async function handleToggleUserActive(user: AdminUser) {
    try {
      await toggleUserActive(user.id, !user.is_active);
      setUsers((prev) =>
        prev.map((u) => (u.id === user.id ? { ...u, is_active: !u.is_active } : u))
      );
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al cambiar estado del usuario');
    }
  }

  function openLicenseDialog(user: AdminUser) {
    setSelectedUser(user);
    setLicenseForm({
      license_type: user.license_type || '',
    });
    setLicenseDialogOpen(true);
  }

  const securityIssuesCount =
    (securityData?.expired_active_licenses?.length ?? 0) +
    (securityData?.users_without_config?.length ?? 0);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center gap-4">
        <Button variant="ghost" size="icon" onClick={onBack}>
          <ArrowLeft className="h-4 w-4" />
        </Button>
        <div>
          <h2 className="text-2xl font-bold flex items-center gap-2">
            <Settings className="h-6 w-6 text-primary" />
            Panel de Administracion
          </h2>
          <p className="text-muted-foreground">
            Gestion del sistema ContaEC
          </p>
        </div>
      </div>

      {/* Admin Tabs */}
      <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-4">
        <TabsList>
          <TabsTrigger value="overview" className="gap-2">
            <Activity className="h-4 w-4" />
            Resumen
          </TabsTrigger>
          <TabsTrigger value="users" className="gap-2">
            <Users className="h-4 w-4" />
            Usuarios
          </TabsTrigger>
          <TabsTrigger value="health" className="gap-2">
            <Heart className="h-4 w-4" />
            Sistema
          </TabsTrigger>
          <TabsTrigger value="security" className="gap-2">
            <Shield className="h-4 w-4" />
            Seguridad
          </TabsTrigger>
        </TabsList>

        {/* Overview Tab */}
        <TabsContent value="overview">
          <div className="grid grid-cols-2 lg:grid-cols-3 gap-4">
            {stats && (
              <>
                <Card>
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs text-muted-foreground">Total Usuarios</span>
                      <Users className="h-4 w-4 text-primary" />
                    </div>
                    <div className="text-2xl font-bold">{stats.total_users}</div>
                    <p className="text-xs text-muted-foreground">
                      {stats.active_users} activos
                    </p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs text-muted-foreground">Empresas</span>
                      <Database className="h-4 w-4 text-primary" />
                    </div>
                    <div className="text-2xl font-bold">{stats.total_companies}</div>
                    <p className="text-xs text-muted-foreground">registradas</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs text-muted-foreground">Clientes</span>
                      <Activity className="h-4 w-4 text-primary" />
                    </div>
                    <div className="text-2xl font-bold">{stats.total_clients ?? 0}</div>
                    <p className="text-xs text-muted-foreground">registrados</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs text-muted-foreground">Licencias Expiradas</span>
                      <Key className="h-4 w-4 text-destructive" />
                    </div>
                    <div className="text-2xl font-bold">{stats.expired_licenses ?? 0}</div>
                    <p className="text-xs text-muted-foreground">de {stats.total_users} usuarios</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs text-muted-foreground">Por Expirar</span>
                      <AlertTriangle className="h-4 w-4 text-yellow-600" />
                    </div>
                    <div className="text-2xl font-bold">{stats.expiring_licenses}</div>
                    <p className="text-xs text-muted-foreground">en los proximos 30 dias</p>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs text-muted-foreground">Problemas Seguridad</span>
                      <ShieldAlert className="h-4 w-4 text-destructive" />
                    </div>
                    <div className="text-2xl font-bold">
                      {securityIssuesCount}
                    </div>
                    <p className="text-xs text-muted-foreground">sin resolver</p>
                  </CardContent>
                </Card>
              </>
            )}
            {!stats && (
              <div className="col-span-full text-center py-8">
                <p className="text-muted-foreground">No se pudieron cargar las estadisticas</p>
                <Button variant="outline" className="mt-2" onClick={loadAdminData}>
                  <RefreshCw className="mr-2 h-4 w-4" />
                  Reintentar
                </Button>
              </div>
            )}
          </div>
        </TabsContent>

        {/* Users Tab */}
        <TabsContent value="users">
          <Card>
            <CardHeader>
              <CardTitle className="text-base flex items-center gap-2">
                <Users className="h-4 w-4 text-primary" />
                Gestion de Usuarios
              </CardTitle>
              <CardDescription>
                Administre usuarios y sus licencias
              </CardDescription>
            </CardHeader>
            <CardContent>
              {users.length > 0 ? (
                <ScrollArea className="max-h-96">
                  <Table>
                    <TableHeader>
                      <TableRow>
                        <TableHead>Nombre</TableHead>
                        <TableHead>Correo</TableHead>
                        <TableHead>Licencia</TableHead>
                        <TableHead>Estado</TableHead>
                        <TableHead>Expira</TableHead>
                        <TableHead className="text-right">Acciones</TableHead>
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {users.map((u) => (
                        <TableRow key={u.id}>
                          <TableCell>
                            <div className="flex items-center gap-2">
                              {u.is_admin && (
                                <Shield className="h-3.5 w-3.5 text-primary" />
                              )}
                              <span className="font-medium">{u.full_name}</span>
                            </div>
                          </TableCell>
                          <TableCell className="text-muted-foreground text-xs">
                            {u.email}
                          </TableCell>
                          <TableCell className="text-xs">
                            <Badge variant="outline" className="text-xs">{u.license_type || '-'}</Badge>
                          </TableCell>
                          <TableCell>
                            <Badge
                              variant={u.is_active ? 'default' : 'secondary'}
                              className={u.is_active ? 'bg-primary' : ''}
                            >
                              {u.is_active ? 'Activo' : 'Inactivo'}
                            </Badge>
                          </TableCell>
                          <TableCell className="text-xs">
                            {u.license_end_date
                              ? new Date(u.license_end_date).toLocaleDateString('es-EC')
                              : '-'}
                          </TableCell>
                          <TableCell className="text-right">
                            <div className="flex justify-end gap-1">
                              <Button
                                variant="outline"
                                size="sm"
                                className="h-7 text-xs"
                                onClick={() => openLicenseDialog(u)}
                              >
                                <Key className="mr-1 h-3 w-3" />
                                Licencia
                              </Button>
                              <Button
                                variant={u.is_active ? 'destructive' : 'default'}
                                size="sm"
                                className="h-7 text-xs"
                                onClick={() => handleToggleUserActive(u)}
                              >
                                {u.is_active ? (
                                  <>
                                    <UserX className="mr-1 h-3 w-3" />
                                    Desactivar
                                  </>
                                ) : (
                                  <>
                                    <UserCheck className="mr-1 h-3 w-3" />
                                    Activar
                                  </>
                                )}
                              </Button>
                            </div>
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </ScrollArea>
              ) : (
                <div className="text-center py-8">
                  <Users className="h-8 w-8 mx-auto text-muted-foreground mb-2" />
                  <p className="text-sm text-muted-foreground">
                    No se pudieron cargar los usuarios
                  </p>
                </div>
              )}
            </CardContent>
          </Card>
        </TabsContent>

        {/* Health Tab */}
        <TabsContent value="health">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <Card>
              <CardHeader>
                <CardTitle className="text-base flex items-center gap-2">
                  <Heart className="h-4 w-4 text-primary" />
                  Estado del Sistema
                </CardTitle>
              </CardHeader>
              <CardContent>
                {health ? (
                  <div className="space-y-4">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-muted-foreground">Version</span>
                      <span className="text-sm font-mono">{(health.application as Record<string, string>)?.version ?? 'N/A'}</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-muted-foreground">Ambiente</span>
                      <span className="text-sm font-medium">{(health.application as Record<string, string>)?.environment ?? 'N/A'}</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-muted-foreground">CPU</span>
                      <span className="text-sm font-medium">
                        {String((health.system as Record<string, unknown>)?.cpu_percent ?? 'N/A')}
                        {typeof (health.system as Record<string, unknown>)?.cpu_percent === 'number' ? '%' : ''}
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-muted-foreground">Memoria</span>
                      <span className="text-sm font-medium">
                        {String((health.system as Record<string, unknown>)?.memory_percent ?? 'N/A')}
                        {typeof (health.system as Record<string, unknown>)?.memory_percent === 'number' ? '%' : ''}
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-muted-foreground">Disco</span>
                      <span className="text-sm font-medium">
                        {String((health.system as Record<string, unknown>)?.disk_percent ?? 'N/A')}
                        {typeof (health.system as Record<string, unknown>)?.disk_percent === 'number' ? '%' : ''}
                      </span>
                    </div>
                  </div>
                ) : (
                  <p className="text-sm text-muted-foreground text-center py-4">
                    No se pudo obtener el estado del sistema
                  </p>
                )}
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="text-base flex items-center gap-2">
                  <Database className="h-4 w-4 text-primary" />
                  Base de Datos
                </CardTitle>
              </CardHeader>
              <CardContent>
                {health ? (
                  <div className="space-y-3">
                    <div className="flex items-center justify-between p-3 rounded-lg border">
                      <div className="flex items-center gap-2">
                        <Users className="h-4 w-4 text-muted-foreground" />
                        <span className="text-sm">Total Usuarios</span>
                      </div>
                      <span className="text-sm font-medium">
                        {(health.database as Record<string, number>)?.total_users ?? 'N/A'}
                      </span>
                    </div>
                    <div className="flex items-center justify-between p-3 rounded-lg border">
                      <div className="flex items-center gap-2">
                        <Database className="h-4 w-4 text-muted-foreground" />
                        <span className="text-sm">Total Empresas</span>
                      </div>
                      <span className="text-sm font-medium">
                        {(health.database as Record<string, number>)?.total_companies ?? 'N/A'}
                      </span>
                    </div>
                    <div className="flex items-center justify-between p-3 rounded-lg border">
                      <div className="flex items-center gap-2">
                        <Activity className="h-4 w-4 text-muted-foreground" />
                        <span className="text-sm">Total Clientes</span>
                      </div>
                      <span className="text-sm font-medium">
                        {(health.database as Record<string, number>)?.total_clients ?? 'N/A'}
                      </span>
                    </div>
                  </div>
                ) : (
                  <p className="text-sm text-muted-foreground text-center py-4">
                    No se pudo obtener el estado de la base de datos
                  </p>
                )}
              </CardContent>
            </Card>
          </div>
        </TabsContent>

        {/* Security Tab */}
        <TabsContent value="security">
          <Card>
            <CardHeader>
              <CardTitle className="text-base flex items-center gap-2">
                <Shield className="h-4 w-4 text-primary" />
                Problemas de Seguridad
              </CardTitle>
              <CardDescription>
                Alertas y problemas de seguridad detectados
              </CardDescription>
            </CardHeader>
            <CardContent>
              {securityData && securityIssuesCount > 0 ? (
                <ScrollArea className="max-h-96">
                  <div className="space-y-3">
                    {securityData.expired_active_licenses.map((item) => (
                      <div key={item.user_id} className="rounded-lg border p-4 border-destructive/30">
                        <div className="flex items-start gap-3">
                          <ShieldAlert className="h-5 w-5 text-destructive mt-0.5" />
                          <div className="flex-1 min-w-0">
                            <h4 className="text-sm font-medium">Licencia expirada - {item.full_name}</h4>
                            <p className="text-xs text-muted-foreground">
                              {item.email} - Expirada hace {item.days_expired} dias
                            </p>
                          </div>
                        </div>
                      </div>
                    ))}
                    {securityData.users_without_config.map((item) => (
                      <div key={item.user_id} className="rounded-lg border p-4 border-yellow-500/30">
                        <div className="flex items-start gap-3">
                          <AlertTriangle className="h-5 w-5 text-yellow-600 mt-0.5" />
                          <div className="flex-1 min-w-0">
                            <h4 className="text-sm font-medium">Sin configuracion - {item.full_name}</h4>
                            <p className="text-xs text-muted-foreground">
                              {item.email} - No tiene configuracion de usuario
                            </p>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </ScrollArea>
              ) : (
                <div className="text-center py-8">
                  <ShieldCheck className="h-12 w-12 mx-auto text-green-600 mb-3" />
                  <h3 className="text-lg font-medium">Todo en orden</h3>
                  <p className="text-muted-foreground text-sm mt-1">
                    No se detectaron problemas de seguridad
                  </p>
                </div>
              )}
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>

      {/* License Modification Dialog */}
      <Dialog open={licenseDialogOpen} onOpenChange={setLicenseDialogOpen}>
        <DialogContent className="sm:max-w-md">
          <DialogHeader>
            <DialogTitle>Modificar Licencia</DialogTitle>
            <DialogDescription>
              Modificar la licencia del usuario {selectedUser?.full_name}
            </DialogDescription>
          </DialogHeader>
          <div className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="mod-license-type">Tipo de Licencia</Label>
              <select
                id="mod-license-type"
                className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                value={licenseForm.license_type}
                onChange={(e) => setLicenseForm({ ...licenseForm, license_type: e.target.value })}
              >
                <option value="">Seleccionar...</option>
                <option value="monthly">Mensual - $15.00</option>
                <option value="quarterly">Trimestral - $40.00</option>
                <option value="semiannual">Semestral - $75.00</option>
                <option value="annual">Anual - $130.00</option>
              </select>
            </div>
            <div className="flex justify-end gap-2">
              <Button variant="outline" onClick={() => setLicenseDialogOpen(false)}>
                Cancelar
              </Button>
              <Button onClick={handleModifyLicense} disabled={modifying || !licenseForm.license_type}>
                {modifying ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Guardando...
                  </>
                ) : (
                  'Guardar Cambios'
                )}
              </Button>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
