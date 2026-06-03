'use client';

import { useState, useEffect, useCallback } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
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
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Textarea } from '@/components/ui/textarea';
import {
  Kanban,
  Users,
  Target,
  Phone,
  Mail,
  CalendarClock,
  Layers,
  Zap,
  TrendingUp,
  DollarSign,
  BarChart3,
  Plus,
  RefreshCw,
  Loader2,
  Pencil,
  Trash2,
  ArrowRight,
  CheckCircle2,
  Clock,
  Filter,
} from 'lucide-react';
import { toast } from 'sonner';
import {
  getCRMStats,
  getCRMOpportunities,
  createCRMOpportunity,
  updateCRMOpportunity,
  moveCRMOpportunity,
  deleteCRMOpportunity,
  getCRMActivities,
  createCRMActivity,
  updateCRMActivity,
  completeCRMActivity,
  getCRMSegments,
  createCRMSegment,
  deleteCRMSegment,
  getCRMAutomations,
  createCRMAutomation,
  toggleCRMAutomation,
  deleteCRMAutomation,
  getCRMPipelines,
  getCRMLeads,
  createCRMLead,
  updateCRMLead,
  convertCRMLead,
  getClients,
  type CRMOpportunity,
  type CRMActivity as CRMActivityType,
  type CRMSegment,
  type CRMAutomation,
  type CRMStats,
  type CRMPipeline,
  type CRMLead,
  type User,
  type Company,
  type ClientResponse,
} from '@/lib/api';

function formatCurrency(amount: number): string {
  return `$${amount.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

function formatDate(dateStr: string | null | undefined): string {
  if (!dateStr) return '-';
  return new Date(dateStr).toLocaleDateString('es-EC', { year: 'numeric', month: 'short', day: 'numeric' });
}

const ETAPAS_PIPELINE = [
  { key: 'prospecto', label: 'Prospecto', color: 'bg-slate-400', textColor: 'text-slate-600' },
  { key: 'calificacion', label: 'Calificación', color: 'bg-sky-500', textColor: 'text-sky-600' },
  { key: 'propuesta', label: 'Propuesta', color: 'bg-amber-500', textColor: 'text-amber-600' },
  { key: 'negociacion', label: 'Negociación', color: 'bg-orange-500', textColor: 'text-orange-600' },
  { key: 'cierre_ganado', label: 'Cierre Ganado', color: 'bg-emerald-600', textColor: 'text-emerald-600' },
  { key: 'cierre_perdido', label: 'Cierre Perdido', color: 'bg-red-500', textColor: 'text-red-600' },
] as const;

const FUENTES = [
  { key: 'web', label: 'Web' },
  { key: 'referido', label: 'Referido' },
  { key: 'llamado', label: 'Llamado' },
  { key: 'email', label: 'Email' },
  { key: 'redes', label: 'Redes Sociales' },
  { key: 'otro', label: 'Otro' },
] as const;

const TIPOS_ACTIVIDAD = [
  { key: 'llamada', label: 'Llamada', icon: Phone },
  { key: 'email', label: 'Email', icon: Mail },
  { key: 'reunion', label: 'Reunión', icon: Users },
  { key: 'tarea', label: 'Tarea', icon: CheckCircle2 },
  { key: 'nota', label: 'Nota', icon: Layers },
] as const;

const ESTADOS_ACTIVIDAD = [
  { key: 'pendiente', label: 'Pendiente', badgeClass: 'bg-slate-400' },
  { key: 'completada', label: 'Completada', badgeClass: 'bg-emerald-600' },
  { key: 'cancelada', label: 'Cancelada', badgeClass: 'bg-red-500' },
] as const;

const ESTADOS_LEAD = [
  { key: 'nuevo', label: 'Nuevo', badgeClass: 'bg-sky-500' },
  { key: 'contactado', label: 'Contactado', badgeClass: 'bg-amber-500' },
  { key: 'calificado', label: 'Calificado', badgeClass: 'bg-emerald-600' },
  { key: 'no_calificado', label: 'No Calificado', badgeClass: 'bg-red-500' },
  { key: 'convertido', label: 'Convertido', badgeClass: 'bg-purple-600' },
] as const;

function getEtapaBadge(etapa: string) {
  const e = ETAPAS_PIPELINE.find((x) => x.key === etapa);
  if (e) return <Badge className={`${e.color} text-white`}>{e.label}</Badge>;
  return <Badge variant="outline">{etapa}</Badge>;
}

function getActividadBadge(estado: string) {
  const e = ESTADOS_ACTIVIDAD.find((x) => x.key === estado);
  if (e) return <Badge className={`${e.badgeClass} text-white text-xs`}>{e.label}</Badge>;
  return <Badge variant="outline">{estado}</Badge>;
}

function getLeadStatusBadge(status: string) {
  const e = ESTADOS_LEAD.find((x) => x.key === status);
  if (e) return <Badge className={`${e.badgeClass} text-white text-xs`}>{e.label}</Badge>;
  return <Badge variant="outline">{status}</Badge>;
}

function getActividadTipoBadge(tipo: string) {
  const t = TIPOS_ACTIVIDAD.find((x) => x.key === tipo);
  if (t) return <Badge variant="outline" className="gap-1">{<t.icon className="h-3 w-3" />}{t.label}</Badge>;
  return <Badge variant="outline">{tipo}</Badge>;
}

interface ContaECCRMProps {
  user: User;
  companies: Company[];
}

export function ContaECCRM({ user, companies }: ContaECCRMProps) {
  const [selectedCompanyId, setSelectedCompanyId] = useState<string>(() =>
    companies.length > 0 ? companies[0].id : ''
  );

  if (companies.length === 0) {
    return (
      <div className="space-y-6">
        <div>
          <h2 className="text-2xl font-bold">CRM</h2>
          <p className="text-muted-foreground">Gestión de relaciones con clientes</p>
        </div>
        <Card>
          <CardContent className="py-12 text-center">
            <Kanban className="h-12 w-12 mx-auto text-muted-foreground mb-3" />
            <h3 className="text-lg font-medium">Sin empresas</h3>
            <p className="text-muted-foreground text-sm mt-1">Registre una empresa para comenzar</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-2xl font-bold">CRM</h2>
          <p className="text-muted-foreground">Gestión de relaciones con clientes</p>
        </div>
        {companies.length > 1 && (
          <div className="flex items-center gap-2">
            <Label className="text-sm whitespace-nowrap">Empresa:</Label>
            <Select value={selectedCompanyId} onValueChange={setSelectedCompanyId}>
              <SelectTrigger className="w-[220px]">
                <SelectValue placeholder="Empresa" />
              </SelectTrigger>
              <SelectContent>
                {companies.map((c) => (
                  <SelectItem key={c.id} value={c.id}>{c.razon_social}</SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        )}
      </div>

      <Tabs defaultValue="pipeline" className="space-y-4">
        <TabsList className="flex flex-wrap h-auto gap-1">
          <TabsTrigger value="pipeline" className="gap-1.5"><Kanban className="h-3.5 w-3.5" /><span className="hidden sm:inline">Pipeline</span></TabsTrigger>
          <TabsTrigger value="leads" className="gap-1.5"><Users className="h-3.5 w-3.5" /><span className="hidden sm:inline">Leads</span></TabsTrigger>
          <TabsTrigger value="oportunidades" className="gap-1.5"><Target className="h-3.5 w-3.5" /><span className="hidden sm:inline">Oportunidades</span></TabsTrigger>
          <TabsTrigger value="actividades" className="gap-1.5"><CalendarClock className="h-3.5 w-3.5" /><span className="hidden sm:inline">Actividades</span></TabsTrigger>
          <TabsTrigger value="segmentos" className="gap-1.5"><Layers className="h-3.5 w-3.5" /><span className="hidden sm:inline">Segmentos</span></TabsTrigger>
          <TabsTrigger value="automatizaciones" className="gap-1.5"><Zap className="h-3.5 w-3.5" /><span className="hidden sm:inline">Automatizaciones</span></TabsTrigger>
        </TabsList>
        <TabsContent value="pipeline"><PipelineTab companyId={selectedCompanyId} /></TabsContent>
        <TabsContent value="leads"><LeadsTab companyId={selectedCompanyId} /></TabsContent>
        <TabsContent value="oportunidades"><OportunidadesTab companyId={selectedCompanyId} /></TabsContent>
        <TabsContent value="actividades"><ActividadesTab companyId={selectedCompanyId} /></TabsContent>
        <TabsContent value="segmentos"><SegmentosTab companyId={selectedCompanyId} /></TabsContent>
        <TabsContent value="automatizaciones"><AutomatizacionesTab companyId={selectedCompanyId} /></TabsContent>
      </Tabs>
    </div>
  );
}

// ─── Pipeline Tab ────────────────────────────────────────────

function PipelineTab({ companyId }: { companyId: string }) {
  const [stats, setStats] = useState<CRMStats | null>(null);
  const [opportunities, setOpportunities] = useState<CRMOpportunity[]>([]);
  const [pipelines, setPipelines] = useState<CRMPipeline[]>([]);
  const [loading, setLoading] = useState(true);
  const [movingId, setMovingId] = useState<string | null>(null);

  const loadData = useCallback(async () => {
    if (!companyId) return;
    setLoading(true);
    try {
      const [st, opps, pipes] = await Promise.all([
        getCRMStats(companyId),
        getCRMOpportunities({ company_id: companyId }),
        getCRMPipelines(companyId),
      ]);
      setStats(st);
      setOpportunities(opps);
      setPipelines(pipes);
    } catch {
      toast.error('Error al cargar pipeline');
    } finally {
      setLoading(false);
    }
  }, [companyId]);

  useEffect(() => { loadData(); }, [loadData]);

  async function handleMoveStage(id: string, etapa: string) {
    setMovingId(id);
    try {
      await moveCRMOpportunity(id, etapa);
      toast.success('Oportunidad movida');
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al mover');
    } finally {
      setMovingId(null);
    }
  }

  if (loading) return <div className="flex items-center justify-center h-48"><Loader2 className="h-8 w-8 animate-spin text-primary" /></div>;

  // Group opportunities by etapa
  const pipelineStages = ETAPAS_PIPELINE.map((etapa) => ({
    ...etapa,
    opportunities: opportunities.filter((o) => o.etapa === etapa.key),
    totalValue: opportunities.filter((o) => o.etapa === etapa.key).reduce((sum, o) => sum + o.valor_estimado, 0),
  }));

  return (
    <div className="space-y-4">
      {/* Stats Row */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2 mb-1">
              <Target className="h-4 w-4 text-muted-foreground" />
              <p className="text-xs text-muted-foreground">Oportunidades</p>
            </div>
            <p className="text-2xl font-bold">{stats?.total_oportunidades ?? 0}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2 mb-1">
              <DollarSign className="h-4 w-4 text-sky-500" />
              <p className="text-xs text-muted-foreground">Pipeline</p>
            </div>
            <p className="text-2xl font-bold">{formatCurrency(stats?.valor_pipeline ?? 0)}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2 mb-1">
              <TrendingUp className="h-4 w-4 text-emerald-500" />
              <p className="text-xs text-muted-foreground">Ganado</p>
            </div>
            <p className="text-2xl font-bold text-emerald-600">{formatCurrency(stats?.valor_ganado ?? 0)}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2 mb-1">
              <BarChart3 className="h-4 w-4 text-amber-500" />
              <p className="text-xs text-muted-foreground">Tasa Conversión</p>
            </div>
            <p className="text-2xl font-bold">{(stats?.tasa_conversion ?? 0).toFixed(1)}%</p>
          </CardContent>
        </Card>
      </div>

      <div className="flex justify-end">
        <Button variant="outline" size="icon" onClick={loadData}><RefreshCw className="h-4 w-4" /></Button>
      </div>

      {/* Pipeline Columns */}
      <div className="flex gap-4 overflow-x-auto pb-4">
        {pipelineStages.map((stage) => (
          <div key={stage.key} className="min-w-[250px] flex-1">
            <div className={`${stage.color} text-white rounded-t-lg px-3 py-2 flex items-center justify-between`}>
              <span className="font-medium text-sm">{stage.label}</span>
              <Badge variant="secondary" className="bg-white/20 text-white">{stage.opportunities.length}</Badge>
            </div>
            <div className="bg-muted/50 rounded-b-lg p-2 space-y-2 min-h-[200px] border border-t-0">
              <div className="text-xs text-muted-foreground text-center font-medium">
                {formatCurrency(stage.totalValue)}
              </div>
              {stage.opportunities.map((opp) => (
                <Card key={opp.id} className="cursor-pointer hover:shadow-md transition-shadow">
                  <CardContent className="p-3">
                    <div className="space-y-1">
                      <p className="font-medium text-sm truncate">{opp.titulo}</p>
                      {opp.cliente_razon_social && (
                        <p className="text-xs text-muted-foreground">{opp.cliente_razon_social}</p>
                      )}
                      <div className="flex items-center justify-between">
                        <span className="text-sm font-semibold">{formatCurrency(opp.valor_estimado)}</span>
                        <span className="text-xs text-muted-foreground">{opp.probabilidad}%</span>
                      </div>
                      <div className="flex gap-1 pt-1">
                        {ETAPAS_PIPELINE.filter((e) => e.key !== stage.key).slice(0, 3).map((e) => (
                          <Button
                            key={e.key}
                            variant="ghost"
                            size="sm"
                            className="h-6 px-1.5 text-xs"
                            onClick={() => handleMoveStage(opp.id, e.key)}
                            disabled={!!movingId}
                          >
                            <ArrowRight className="h-3 w-3" />
                          </Button>
                        ))}
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
              {stage.opportunities.length === 0 && (
                <p className="text-xs text-muted-foreground text-center py-4">Sin oportunidades</p>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Pipelines Config */}
      {pipelines.length > 0 && (
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm">Pipelines Configurados</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {pipelines.map((p) => (
                <div key={p.id} className="rounded-lg border p-3">
                  <div className="flex items-center justify-between">
                    <span className="font-medium text-sm">{p.name}</span>
                    {p.is_default && <Badge className="bg-primary text-white text-xs">Default</Badge>}
                  </div>
                  {p.description && <p className="text-xs text-muted-foreground mt-1">{p.description}</p>}
                  {p.stages && p.stages.length > 0 && (
                    <div className="flex flex-wrap gap-1 mt-2">
                      {p.stages.sort((a, b) => a.order - b.order).map((s) => (
                        <Badge key={s.id} variant="outline" className="text-xs" style={{ borderColor: s.color, color: s.color }}>{s.name} ({s.probability_percentage}%)</Badge>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

// ─── Leads Tab ───────────────────────────────────────────────

function LeadsTab({ companyId }: { companyId: string }) {
  const [leads, setLeads] = useState<CRMLead[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreate, setShowCreate] = useState(false);
  const [editLead, setEditLead] = useState<CRMLead | null>(null);
  const [showConvert, setShowConvert] = useState<CRMLead | null>(null);
  const [operating, setOperating] = useState(false);
  const [filterStatus, setFilterStatus] = useState<string>('all');

  const loadData = useCallback(async () => {
    if (!companyId) return;
    setLoading(true);
    try {
      const data = await getCRMLeads(companyId);
      setLeads(data);
    } catch {
      toast.error('Error al cargar leads');
    } finally {
      setLoading(false);
    }
  }, [companyId]);

  useEffect(() => { loadData(); }, [loadData]);

  async function handleConvert(lead: CRMLead, titulo: string, valorEstimado: string) {
    setOperating(true);
    try {
      await convertCRMLead(lead.id, {
        company_id: companyId,
        titulo,
        valor_estimado: valorEstimado ? parseFloat(valorEstimado) : undefined,
      });
      toast.success('Lead convertido a oportunidad');
      setShowConvert(null);
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al convertir');
    } finally {
      setOperating(false);
    }
  }

  const filteredLeads = leads.filter((l) => filterStatus === 'all' || l.status === filterStatus);

  if (loading) return <div className="flex items-center justify-center h-48"><Loader2 className="h-8 w-8 animate-spin text-primary" /></div>;

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-2">
        <Select value={filterStatus} onValueChange={setFilterStatus}>
          <SelectTrigger className="w-[160px]"><SelectValue placeholder="Estado" /></SelectTrigger>
          <SelectContent>
            <SelectItem value="all">Todos</SelectItem>
            {ESTADOS_LEAD.map((e) => (<SelectItem key={e.key} value={e.key}>{e.label}</SelectItem>))}
          </SelectContent>
        </Select>
        <Button variant="outline" size="icon" onClick={loadData}><RefreshCw className="h-4 w-4" /></Button>
        <div className="flex-1" />
        <Button onClick={() => { setEditLead(null); setShowCreate(true); }}><Plus className="mr-2 h-4 w-4" /> Nuevo Lead</Button>
      </div>

      {filteredLeads.length > 0 ? (
        <Card>
          <CardContent className="p-0">
            <ScrollArea className="max-h-[500px]">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Nombre</TableHead>
                    <TableHead>Email</TableHead>
                    <TableHead>Teléfono</TableHead>
                    <TableHead>Fuente</TableHead>
                    <TableHead>Estado</TableHead>
                    <TableHead className="text-right">Valor Est.</TableHead>
                    <TableHead>Sig. Seguimiento</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {filteredLeads.map((lead) => (
                    <TableRow key={lead.id}>
                      <TableCell className="font-medium">{lead.first_name} {lead.last_name}</TableCell>
                      <TableCell className="text-sm">{lead.email || '-'}</TableCell>
                      <TableCell className="text-sm">{lead.phone || '-'}</TableCell>
                      <TableCell>
                        <Badge variant="outline" className="text-xs">
                          {FUENTES.find((f) => f.key === lead.source)?.label || lead.source}
                        </Badge>
                      </TableCell>
                      <TableCell>{getLeadStatusBadge(lead.status)}</TableCell>
                      <TableCell className="text-right">{lead.estimated_value ? formatCurrency(lead.estimated_value) : '-'}</TableCell>
                      <TableCell className="text-sm">{formatDate(lead.next_follow_up)}</TableCell>
                      <TableCell className="text-right">
                        <div className="flex justify-end gap-1">
                          <Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => setEditLead(lead)}>
                            <Pencil className="h-3.5 w-3.5" />
                          </Button>
                          {!lead.converted_to_opportunity && lead.status === 'calificado' && (
                            <Button variant="ghost" size="sm" className="h-8 text-xs text-emerald-600" onClick={() => setShowConvert(lead)}>
                              <ArrowRight className="h-3.5 w-3.5 mr-1" /> Convertir
                            </Button>
                          )}
                        </div>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ScrollArea>
          </CardContent>
        </Card>
      ) : (
        <Card>
          <CardContent className="py-12 text-center">
            <Users className="h-12 w-12 mx-auto text-muted-foreground mb-3" />
            <h3 className="text-lg font-medium">Sin leads</h3>
            <p className="text-muted-foreground text-sm mt-1">Agregue leads para comenzar</p>
          </CardContent>
        </Card>
      )}

      <CreateLeadDialog open={showCreate} onOpenChange={setShowCreate} companyId={companyId} onCreated={loadData} />
      {editLead && (
        <EditLeadDialog lead={editLead} open={!!editLead} onOpenChange={(open) => { if (!open) setEditLead(null); }} onUpdated={loadData} />
      )}
      {showConvert && (
        <ConvertLeadDialog lead={showConvert} open={!!showConvert} onOpenChange={(open) => { if (!open) setShowConvert(null); }} onConvert={handleConvert} operating={operating} />
      )}
    </div>
  );
}

// ─── Oportunidades Tab ───────────────────────────────────────

function OportunidadesTab({ companyId }: { companyId: string }) {
  const [opportunities, setOpportunities] = useState<CRMOpportunity[]>([]);
  const [clients, setClients] = useState<ClientResponse[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreate, setShowCreate] = useState(false);
  const [editOpp, setEditOpp] = useState<CRMOpportunity | null>(null);
  const [operating, setOperating] = useState(false);
  const [filterEtapa, setFilterEtapa] = useState<string>('all');

  const loadData = useCallback(async () => {
    if (!companyId) return;
    setLoading(true);
    try {
      const [opps, cls] = await Promise.all([
        getCRMOpportunities({ company_id: companyId }),
        getClients(companyId),
      ]);
      setOpportunities(opps);
      setClients(cls);
    } catch {
      toast.error('Error al cargar oportunidades');
    } finally {
      setLoading(false);
    }
  }, [companyId]);

  useEffect(() => { loadData(); }, [loadData]);

  async function handleMoveStage(id: string, etapa: string) {
    setOperating(true);
    try {
      await moveCRMOpportunity(id, etapa);
      toast.success('Etapa actualizada');
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al mover');
    } finally {
      setOperating(false);
    }
  }

  async function handleDelete(id: string) {
    if (!confirm('¿Está seguro de eliminar esta oportunidad?')) return;
    setOperating(true);
    try {
      await deleteCRMOpportunity(id);
      toast.success('Oportunidad eliminada');
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al eliminar');
    } finally {
      setOperating(false);
    }
  }

  const filteredOpps = opportunities.filter((o) => filterEtapa === 'all' || o.etapa === filterEtapa);

  if (loading) return <div className="flex items-center justify-center h-48"><Loader2 className="h-8 w-8 animate-spin text-primary" /></div>;

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-2">
        <Select value={filterEtapa} onValueChange={setFilterEtapa}>
          <SelectTrigger className="w-[180px]"><SelectValue placeholder="Etapa" /></SelectTrigger>
          <SelectContent>
            <SelectItem value="all">Todas</SelectItem>
            {ETAPAS_PIPELINE.map((e) => (<SelectItem key={e.key} value={e.key}>{e.label}</SelectItem>))}
          </SelectContent>
        </Select>
        <Button variant="outline" size="icon" onClick={loadData}><RefreshCw className="h-4 w-4" /></Button>
        <div className="flex-1" />
        <Button onClick={() => { setEditOpp(null); setShowCreate(true); }}><Plus className="mr-2 h-4 w-4" /> Nueva Oportunidad</Button>
      </div>

      {filteredOpps.length > 0 ? (
        <Card>
          <CardContent className="p-0">
            <ScrollArea className="max-h-[500px]">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Nombre</TableHead>
                    <TableHead>Cliente</TableHead>
                    <TableHead>Etapa</TableHead>
                    <TableHead className="text-right">Monto Est.</TableHead>
                    <TableHead>Prob.</TableHead>
                    <TableHead>Fecha Cierre</TableHead>
                    <TableHead>Cambiar Etapa</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {filteredOpps.map((opp) => (
                    <TableRow key={opp.id}>
                      <TableCell className="font-medium">{opp.titulo}</TableCell>
                      <TableCell className="text-sm">{opp.cliente_razon_social || '-'}</TableCell>
                      <TableCell>{getEtapaBadge(opp.etapa)}</TableCell>
                      <TableCell className="text-right">{formatCurrency(opp.valor_estimado)}</TableCell>
                      <TableCell className="text-center">{opp.probabilidad}%</TableCell>
                      <TableCell className="text-sm">{formatDate(opp.fecha_cierre_estimada)}</TableCell>
                      <TableCell>
                        <Select value={opp.etapa} onValueChange={(v) => handleMoveStage(opp.id, v)} disabled={operating}>
                          <SelectTrigger className="w-[140px] h-8 text-xs"><SelectValue /></SelectTrigger>
                          <SelectContent>
                            {ETAPAS_PIPELINE.map((e) => (<SelectItem key={e.key} value={e.key}>{e.label}</SelectItem>))}
                          </SelectContent>
                        </Select>
                      </TableCell>
                      <TableCell className="text-right">
                        <div className="flex justify-end gap-1">
                          <Button variant="ghost" size="icon" className="h-8 w-8" onClick={() => setEditOpp(opp)}>
                            <Pencil className="h-3.5 w-3.5" />
                          </Button>
                          <Button variant="ghost" size="icon" className="h-8 w-8 text-destructive" onClick={() => handleDelete(opp.id)} disabled={operating}>
                            <Trash2 className="h-3.5 w-3.5" />
                          </Button>
                        </div>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ScrollArea>
          </CardContent>
        </Card>
      ) : (
        <Card>
          <CardContent className="py-12 text-center">
            <Target className="h-12 w-12 mx-auto text-muted-foreground mb-3" />
            <h3 className="text-lg font-medium">Sin oportunidades</h3>
            <p className="text-muted-foreground text-sm mt-1">Cree una oportunidad para comenzar</p>
          </CardContent>
        </Card>
      )}

      <CreateOpportunityDialog open={showCreate} onOpenChange={setShowCreate} companyId={companyId} clients={clients} onCreated={loadData} />
      {editOpp && (
        <EditOpportunityDialog opportunity={editOpp} open={!!editOpp} onOpenChange={(open) => { if (!open) setEditOpp(null); }} clients={clients} onUpdated={loadData} />
      )}
    </div>
  );
}

// ─── Actividades Tab ─────────────────────────────────────────

function ActividadesTab({ companyId }: { companyId: string }) {
  const [activities, setActivities] = useState<CRMActivityType[]>([]);
  const [opportunities, setOpportunities] = useState<CRMOpportunity[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreate, setShowCreate] = useState(false);
  const [filterOpp, setFilterOpp] = useState<string>('all');
  const [completingId, setCompletingId] = useState<string | null>(null);

  const loadData = useCallback(async () => {
    if (!companyId) return;
    setLoading(true);
    try {
      const [acts, opps] = await Promise.all([
        getCRMActivities({ company_id: companyId }),
        getCRMOpportunities({ company_id: companyId }),
      ]);
      setActivities(acts);
      setOpportunities(opps);
    } catch {
      toast.error('Error al cargar actividades');
    } finally {
      setLoading(false);
    }
  }, [companyId]);

  useEffect(() => { loadData(); }, [loadData]);

  async function handleComplete(id: string) {
    setCompletingId(id);
    try {
      await completeCRMActivity(id);
      toast.success('Actividad completada');
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al completar');
    } finally {
      setCompletingId(null);
    }
  }

  const filteredActivities = activities.filter((a) => filterOpp === 'all' || a.opportunity_id === filterOpp);

  if (loading) return <div className="flex items-center justify-center h-48"><Loader2 className="h-8 w-8 animate-spin text-primary" /></div>;

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-2">
        <Select value={filterOpp} onValueChange={setFilterOpp}>
          <SelectTrigger className="w-[220px]"><SelectValue placeholder="Oportunidad" /></SelectTrigger>
          <SelectContent>
            <SelectItem value="all">Todas</SelectItem>
            {opportunities.map((o) => (<SelectItem key={o.id} value={o.id}>{o.titulo}</SelectItem>))}
          </SelectContent>
        </Select>
        <Button variant="outline" size="icon" onClick={loadData}><RefreshCw className="h-4 w-4" /></Button>
        <div className="flex-1" />
        <Button onClick={() => setShowCreate(true)}><Plus className="mr-2 h-4 w-4" /> Nueva Actividad</Button>
      </div>

      {filteredActivities.length > 0 ? (
        <Card>
          <CardContent className="p-0">
            <ScrollArea className="max-h-[500px]">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Tipo</TableHead>
                    <TableHead>Asunto</TableHead>
                    <TableHead>Descripción</TableHead>
                    <TableHead>Fecha</TableHead>
                    <TableHead>Estado</TableHead>
                    <TableHead>Oportunidad</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {filteredActivities.map((act) => (
                    <TableRow key={act.id}>
                      <TableCell>{getActividadTipoBadge(act.tipo)}</TableCell>
                      <TableCell className="font-medium">{act.asunto}</TableCell>
                      <TableCell className="text-sm text-muted-foreground max-w-[200px] truncate">{act.descripcion || '-'}</TableCell>
                      <TableCell className="text-sm">{formatDate(act.fecha_actividad)}</TableCell>
                      <TableCell>{getActividadBadge(act.estado)}</TableCell>
                      <TableCell className="text-sm">{act.oportunidad_titulo || '-'}</TableCell>
                      <TableCell className="text-right">
                        {act.estado === 'pendiente' && (
                          <Button variant="ghost" size="sm" className="h-8 text-xs" onClick={() => handleComplete(act.id)} disabled={!!completingId}>
                            {completingId === act.id ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <CheckCircle2 className="h-3.5 w-3.5 mr-1" />}
                            Completar
                          </Button>
                        )}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ScrollArea>
          </CardContent>
        </Card>
      ) : (
        <Card>
          <CardContent className="py-12 text-center">
            <CalendarClock className="h-12 w-12 mx-auto text-muted-foreground mb-3" />
            <h3 className="text-lg font-medium">Sin actividades</h3>
            <p className="text-muted-foreground text-sm mt-1">Cree una actividad para comenzar</p>
          </CardContent>
        </Card>
      )}

      <CreateActivityDialog open={showCreate} onOpenChange={setShowCreate} companyId={companyId} opportunities={opportunities} onCreated={loadData} />
    </div>
  );
}

// ─── Segmentos Tab ───────────────────────────────────────────

function SegmentosTab({ companyId }: { companyId: string }) {
  const [segments, setSegments] = useState<CRMSegment[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreate, setShowCreate] = useState(false);
  const [operating, setOperating] = useState(false);

  const loadData = useCallback(async () => {
    if (!companyId) return;
    setLoading(true);
    try {
      const data = await getCRMSegments(companyId);
      setSegments(data);
    } catch {
      toast.error('Error al cargar segmentos');
    } finally {
      setLoading(false);
    }
  }, [companyId]);

  useEffect(() => { loadData(); }, [loadData]);

  async function handleDelete(id: string) {
    if (!confirm('¿Está seguro de eliminar este segmento?')) return;
    setOperating(true);
    try {
      await deleteCRMSegment(id);
      toast.success('Segmento eliminado');
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al eliminar');
    } finally {
      setOperating(false);
    }
  }

  if (loading) return <div className="flex items-center justify-center h-48"><Loader2 className="h-8 w-8 animate-spin text-primary" /></div>;

  return (
    <div className="space-y-4">
      <div className="flex justify-end gap-2">
        <Button variant="outline" size="icon" onClick={loadData}><RefreshCw className="h-4 w-4" /></Button>
        <Button onClick={() => setShowCreate(true)}><Plus className="mr-2 h-4 w-4" /> Nuevo Segmento</Button>
      </div>

      {segments.length > 0 ? (
        <Card>
          <CardContent className="p-0">
            <ScrollArea className="max-h-[500px]">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Nombre</TableHead>
                    <TableHead>Tipo</TableHead>
                    <TableHead>Reglas</TableHead>
                    <TableHead>Color</TableHead>
                    <TableHead className="text-center">Clientes</TableHead>
                    <TableHead>Estado</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {segments.map((seg) => (
                    <TableRow key={seg.id}>
                      <TableCell className="font-medium">{seg.nombre}</TableCell>
                      <TableCell className="text-sm">{seg.criterio ? 'Dinámico' : 'Manual'}</TableCell>
                      <TableCell className="text-sm text-muted-foreground max-w-[200px] truncate">{seg.criterio || '-'}</TableCell>
                      <TableCell>
                        {seg.color ? (
                          <div className="flex items-center gap-2">
                            <div className="h-4 w-4 rounded-full" style={{ backgroundColor: seg.color }} />
                            <span className="text-xs">{seg.color}</span>
                          </div>
                        ) : '-'}
                      </TableCell>
                      <TableCell className="text-center">{seg.cliente_count}</TableCell>
                      <TableCell>
                        <Badge variant={seg.is_active ? 'default' : 'secondary'} className={seg.is_active ? 'bg-emerald-600' : ''}>
                          {seg.is_active ? 'Activo' : 'Inactivo'}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-right">
                        <Button variant="ghost" size="icon" className="h-8 w-8 text-destructive" onClick={() => handleDelete(seg.id)} disabled={operating}>
                          <Trash2 className="h-3.5 w-3.5" />
                        </Button>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ScrollArea>
          </CardContent>
        </Card>
      ) : (
        <Card>
          <CardContent className="py-12 text-center">
            <Layers className="h-12 w-12 mx-auto text-muted-foreground mb-3" />
            <h3 className="text-lg font-medium">Sin segmentos</h3>
            <p className="text-muted-foreground text-sm mt-1">Cree segmentos para agrupar clientes</p>
          </CardContent>
        </Card>
      )}

      <CreateSegmentDialog open={showCreate} onOpenChange={setShowCreate} companyId={companyId} onCreated={loadData} />
    </div>
  );
}

// ─── Automatizaciones Tab ────────────────────────────────────

function AutomatizacionesTab({ companyId }: { companyId: string }) {
  const [automations, setAutomations] = useState<CRMAutomation[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreate, setShowCreate] = useState(false);
  const [operating, setOperating] = useState(false);

  const loadData = useCallback(async () => {
    if (!companyId) return;
    setLoading(true);
    try {
      const data = await getCRMAutomations(companyId);
      setAutomations(data);
    } catch {
      toast.error('Error al cargar automatizaciones');
    } finally {
      setLoading(false);
    }
  }, [companyId]);

  useEffect(() => { loadData(); }, [loadData]);

  async function handleToggle(id: string, isActive: boolean) {
    setOperating(true);
    try {
      await toggleCRMAutomation(id, !isActive);
      toast.success(isActive ? 'Automatización desactivada' : 'Automatización activada');
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al cambiar estado');
    } finally {
      setOperating(false);
    }
  }

  async function handleDelete(id: string) {
    if (!confirm('¿Está seguro de eliminar esta automatización?')) return;
    setOperating(true);
    try {
      await deleteCRMAutomation(id);
      toast.success('Automatización eliminada');
      loadData();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al eliminar');
    } finally {
      setOperating(false);
    }
  }

  const TRIGGERS: Record<string, string> = {
    nueva_oportunidad: 'Nueva Oportunidad',
    cambio_etapa: 'Cambio de Etapa',
    actividad_vencida: 'Actividad Vencida',
    nuevo_lead: 'Nuevo Lead',
    lead_convertido: 'Lead Convertido',
  };

  if (loading) return <div className="flex items-center justify-center h-48"><Loader2 className="h-8 w-8 animate-spin text-primary" /></div>;

  return (
    <div className="space-y-4">
      <div className="flex justify-end gap-2">
        <Button variant="outline" size="icon" onClick={loadData}><RefreshCw className="h-4 w-4" /></Button>
        <Button onClick={() => setShowCreate(true)}><Plus className="mr-2 h-4 w-4" /> Nueva Automatización</Button>
      </div>

      {automations.length > 0 ? (
        <Card>
          <CardContent className="p-0">
            <ScrollArea className="max-h-[500px]">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Nombre</TableHead>
                    <TableHead>Trigger</TableHead>
                    <TableHead>Acciones</TableHead>
                    <TableHead className="text-center">Ejecuciones</TableHead>
                    <TableHead>Estado</TableHead>
                    <TableHead className="text-right">Acciones</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {automations.map((auto) => (
                    <TableRow key={auto.id}>
                      <TableCell className="font-medium">{auto.nombre}</TableCell>
                      <TableCell>
                        <Badge variant="outline" className="text-xs">
                          {TRIGGERS[auto.evento_disparador] || auto.evento_disparador}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-sm text-muted-foreground max-w-[200px] truncate">{auto.acciones}</TableCell>
                      <TableCell className="text-center">{auto.ejecuciones_count}</TableCell>
                      <TableCell>
                        <Badge variant={auto.is_active ? 'default' : 'secondary'} className={auto.is_active ? 'bg-emerald-600' : ''}>
                          {auto.is_active ? 'Activo' : 'Inactivo'}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-right">
                        <div className="flex justify-end gap-1">
                          <Button variant="ghost" size="sm" className="h-8 text-xs" onClick={() => handleToggle(auto.id, auto.is_active)} disabled={operating}>
                            {auto.is_active ? 'Desactivar' : 'Activar'}
                          </Button>
                          <Button variant="ghost" size="icon" className="h-8 w-8 text-destructive" onClick={() => handleDelete(auto.id)} disabled={operating}>
                            <Trash2 className="h-3.5 w-3.5" />
                          </Button>
                        </div>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ScrollArea>
          </CardContent>
        </Card>
      ) : (
        <Card>
          <CardContent className="py-12 text-center">
            <Zap className="h-12 w-12 mx-auto text-muted-foreground mb-3" />
            <h3 className="text-lg font-medium">Sin automatizaciones</h3>
            <p className="text-muted-foreground text-sm mt-1">Cree automatizaciones para optimizar su CRM</p>
          </CardContent>
        </Card>
      )}

      <CreateAutomationDialog open={showCreate} onOpenChange={setShowCreate} companyId={companyId} onCreated={loadData} />
    </div>
  );
}

// ─── Dialogs ─────────────────────────────────────────────────

function CreateLeadDialog({ open, onOpenChange, companyId, onCreated }: {
  open: boolean; onOpenChange: (open: boolean) => void; companyId: string; onCreated: () => void;
}) {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [source, setSource] = useState('web');
  const [estimatedValue, setEstimatedValue] = useState('');
  const [notes, setNotes] = useState('');
  const [nextFollowUp, setNextFollowUp] = useState('');
  const [creating, setCreating] = useState(false);

  async function handleCreate() {
    if (!firstName || !lastName) {
      toast.error('Complete los campos requeridos (nombre, apellido)');
      return;
    }
    setCreating(true);
    try {
      await createCRMLead({
        company_id: companyId,
        first_name: firstName,
        last_name: lastName,
        email: email || undefined,
        phone: phone || undefined,
        source,
        estimated_value: estimatedValue ? parseFloat(estimatedValue) : undefined,
        notes: notes || undefined,
        next_follow_up: nextFollowUp || undefined,
      });
      toast.success('Lead creado exitosamente');
      onOpenChange(false);
      setFirstName(''); setLastName(''); setEmail(''); setPhone('');
      setSource('web'); setEstimatedValue(''); setNotes(''); setNextFollowUp('');
      onCreated();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al crear lead');
    } finally {
      setCreating(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Nuevo Lead</DialogTitle>
          <DialogDescription>Registre un nuevo lead en el CRM</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Nombre *</Label><Input value={firstName} onChange={(e) => setFirstName(e.target.value)} placeholder="Juan" /></div>
            <div className="space-y-2"><Label>Apellido *</Label><Input value={lastName} onChange={(e) => setLastName(e.target.value)} placeholder="Pérez" /></div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Email</Label><Input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="juan@ejemplo.com" /></div>
            <div className="space-y-2"><Label>Teléfono</Label><Input value={phone} onChange={(e) => setPhone(e.target.value)} placeholder="0991234567" /></div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Fuente</Label><Select value={source} onValueChange={setSource}><SelectTrigger /><SelectContent>{FUENTES.map((f) => (<SelectItem key={f.key} value={f.key}>{f.label}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Valor Estimado ($)</Label><Input type="number" value={estimatedValue} onChange={(e) => setEstimatedValue(e.target.value)} placeholder="0.00" /></div>
          </div>
          <div className="space-y-2"><Label>Siguiente Seguimiento</Label><Input type="date" value={nextFollowUp} onChange={(e) => setNextFollowUp(e.target.value)} /></div>
          <div className="space-y-2"><Label>Notas</Label><Textarea value={notes} onChange={(e) => setNotes(e.target.value)} rows={2} placeholder="Notas sobre el lead" /></div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={handleCreate} disabled={creating}>{creating ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}Crear Lead</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function EditLeadDialog({ lead, open, onOpenChange, onUpdated }: {
  lead: CRMLead; open: boolean; onOpenChange: (open: boolean) => void; onUpdated: () => void;
}) {
  const [firstName, setFirstName] = useState(lead.first_name);
  const [lastName, setLastName] = useState(lead.last_name);
  const [email, setEmail] = useState(lead.email || '');
  const [phone, setPhone] = useState(lead.phone || '');
  const [source, setSource] = useState(lead.source);
  const [status, setStatus] = useState(lead.status);
  const [estimatedValue, setEstimatedValue] = useState(lead.estimated_value?.toString() || '');
  const [notes, setNotes] = useState(lead.notes || '');
  const [nextFollowUp, setNextFollowUp] = useState(lead.next_follow_up?.split('T')[0] || '');
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    setFirstName(lead.first_name);
    setLastName(lead.last_name);
    setEmail(lead.email || '');
    setPhone(lead.phone || '');
    setSource(lead.source);
    setStatus(lead.status);
    setEstimatedValue(lead.estimated_value?.toString() || '');
    setNotes(lead.notes || '');
    setNextFollowUp(lead.next_follow_up?.split('T')[0] || '');
  }, [lead]);

  async function handleSave() {
    setSaving(true);
    try {
      await updateCRMLead(lead.id, {
        first_name: firstName,
        last_name: lastName,
        email: email || undefined,
        phone: phone || undefined,
        source,
        status,
        estimated_value: estimatedValue ? parseFloat(estimatedValue) : undefined,
        notes: notes || undefined,
        next_follow_up: nextFollowUp || undefined,
      });
      toast.success('Lead actualizado');
      onOpenChange(false);
      onUpdated();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al actualizar');
    } finally {
      setSaving(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Editar Lead</DialogTitle>
          <DialogDescription>Modifique los datos del lead</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Nombre</Label><Input value={firstName} onChange={(e) => setFirstName(e.target.value)} /></div>
            <div className="space-y-2"><Label>Apellido</Label><Input value={lastName} onChange={(e) => setLastName(e.target.value)} /></div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Email</Label><Input value={email} onChange={(e) => setEmail(e.target.value)} /></div>
            <div className="space-y-2"><Label>Teléfono</Label><Input value={phone} onChange={(e) => setPhone(e.target.value)} /></div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Fuente</Label><Select value={source} onValueChange={setSource}><SelectTrigger /><SelectContent>{FUENTES.map((f) => (<SelectItem key={f.key} value={f.key}>{f.label}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Estado</Label><Select value={status} onValueChange={setStatus}><SelectTrigger /><SelectContent>{ESTADOS_LEAD.map((e) => (<SelectItem key={e.key} value={e.key}>{e.label}</SelectItem>))}</SelectContent></Select></div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Valor Estimado ($)</Label><Input type="number" value={estimatedValue} onChange={(e) => setEstimatedValue(e.target.value)} /></div>
            <div className="space-y-2"><Label>Siguiente Seguimiento</Label><Input type="date" value={nextFollowUp} onChange={(e) => setNextFollowUp(e.target.value)} /></div>
          </div>
          <div className="space-y-2"><Label>Notas</Label><Textarea value={notes} onChange={(e) => setNotes(e.target.value)} rows={2} /></div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={handleSave} disabled={saving}>{saving ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}Guardar</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function ConvertLeadDialog({ lead, open, onOpenChange, onConvert, operating }: {
  lead: CRMLead; open: boolean; onOpenChange: (open: boolean) => void; onConvert: (lead: CRMLead, titulo: string, valorEstimado: string) => void; operating: boolean;
}) {
  const defaultTitulo = `${lead.first_name} ${lead.last_name} - Oportunidad`;
  const defaultValor = lead.estimated_value?.toString() || '';
  const [titulo, setTitulo] = useState(defaultTitulo);
  const [valorEstimado, setValorEstimado] = useState(defaultValor);

  // Reset when lead changes using key prop on Dialog parent is better, but we handle it here
  if (titulo !== defaultTitulo && defaultTitulo) {
    // Only update if the derived value differs (lead changed)
    const currentDerived = `${lead.first_name} ${lead.last_name} - Oportunidad`;
    if (!titulo.startsWith(lead.first_name)) {
      setTitulo(currentDerived);
      setValorEstimado(lead.estimated_value?.toString() || '');
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Convertir Lead a Oportunidad</DialogTitle>
          <DialogDescription>Convierta el lead &quot;{lead.first_name} {lead.last_name}&quot; en una oportunidad de venta</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="space-y-2"><Label>Título de la Oportunidad *</Label><Input value={titulo} onChange={(e) => setTitulo(e.target.value)} /></div>
          <div className="space-y-2"><Label>Valor Estimado ($)</Label><Input type="number" value={valorEstimado} onChange={(e) => setValorEstimado(e.target.value)} placeholder="0.00" /></div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={() => onConvert(lead, titulo, valorEstimado)} disabled={operating || !titulo}>
              {operating ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : <ArrowRight className="mr-2 h-4 w-4" />}
              Convertir
            </Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function CreateOpportunityDialog({ open, onOpenChange, companyId, clients, onCreated }: {
  open: boolean; onOpenChange: (open: boolean) => void; companyId: string; clients: ClientResponse[]; onCreated: () => void;
}) {
  const [titulo, setTitulo] = useState('');
  const [clientId, setClientId] = useState('');
  const [valorEstimado, setValorEstimado] = useState('');
  const [probabilidad, setProbabilidad] = useState('50');
  const [etapa, setEtapa] = useState('prospecto');
  const [fechaCierre, setFechaCierre] = useState('');
  const [fuente, setFuente] = useState('web');
  const [responsable, setResponsable] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [creating, setCreating] = useState(false);

  async function handleCreate() {
    if (!titulo) {
      toast.error('El título es requerido');
      return;
    }
    setCreating(true);
    try {
      await createCRMOpportunity({
        company_id: companyId,
        titulo,
        client_id: clientId || undefined,
        valor_estimado: parseFloat(valorEstimado) || 0,
        probabilidad: parseInt(probabilidad) || undefined,
        etapa,
        fecha_cierre_estimada: fechaCierre || undefined,
        fuente,
        responsable: responsable || undefined,
        descripcion: descripcion || undefined,
      });
      toast.success('Oportunidad creada exitosamente');
      onOpenChange(false);
      setTitulo(''); setClientId(''); setValorEstimado(''); setProbabilidad('50');
      setEtapa('prospecto'); setFechaCierre(''); setFuente('web'); setResponsable(''); setDescripcion('');
      onCreated();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al crear oportunidad');
    } finally {
      setCreating(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-2xl max-h-[80vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle>Nueva Oportunidad</DialogTitle>
          <DialogDescription>Cree una nueva oportunidad de venta</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2 col-span-2"><Label>Título *</Label><Input value={titulo} onChange={(e) => setTitulo(e.target.value)} placeholder="Nombre de la oportunidad" /></div>
            <div className="space-y-2"><Label>Cliente</Label><Select value={clientId} onValueChange={setClientId}><SelectTrigger><SelectValue placeholder="Seleccionar cliente" /></SelectTrigger><SelectContent>{clients.map((c) => (<SelectItem key={c.id} value={c.id}>{c.razon_social}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Etapa</Label><Select value={etapa} onValueChange={setEtapa}><SelectTrigger /><SelectContent>{ETAPAS_PIPELINE.map((e) => (<SelectItem key={e.key} value={e.key}>{e.label}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Valor Estimado ($) *</Label><Input type="number" value={valorEstimado} onChange={(e) => setValorEstimado(e.target.value)} placeholder="0.00" /></div>
            <div className="space-y-2"><Label>Probabilidad (%)</Label><Input type="number" min="0" max="100" value={probabilidad} onChange={(e) => setProbabilidad(e.target.value)} /></div>
            <div className="space-y-2"><Label>Fecha Cierre Estimada</Label><Input type="date" value={fechaCierre} onChange={(e) => setFechaCierre(e.target.value)} /></div>
            <div className="space-y-2"><Label>Fuente</Label><Select value={fuente} onValueChange={setFuente}><SelectTrigger /><SelectContent>{FUENTES.map((f) => (<SelectItem key={f.key} value={f.key}>{f.label}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Responsable</Label><Input value={responsable} onChange={(e) => setResponsable(e.target.value)} placeholder="Nombre del responsable" /></div>
            <div className="space-y-2 col-span-2"><Label>Descripción</Label><Textarea value={descripcion} onChange={(e) => setDescripcion(e.target.value)} rows={2} placeholder="Descripción de la oportunidad" /></div>
          </div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={handleCreate} disabled={creating}>{creating ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}Crear Oportunidad</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function EditOpportunityDialog({ opportunity, open, onOpenChange, clients, onUpdated }: {
  opportunity: CRMOpportunity; open: boolean; onOpenChange: (open: boolean) => void; clients: ClientResponse[]; onUpdated: () => void;
}) {
  const [titulo, setTitulo] = useState(opportunity.titulo);
  const [clientId, setClientId] = useState(opportunity.client_id || '');
  const [valorEstimado, setValorEstimado] = useState(opportunity.valor_estimado.toString());
  const [probabilidad, setProbabilidad] = useState(opportunity.probabilidad.toString());
  const [etapa, setEtapa] = useState(opportunity.etapa);
  const [fechaCierre, setFechaCierre] = useState(opportunity.fecha_cierre_estimada?.split('T')[0] || '');
  const [fuente, setFuente] = useState(opportunity.fuente || 'web');
  const [responsable, setResponsable] = useState(opportunity.responsable || '');
  const [descripcion, setDescripcion] = useState(opportunity.descripcion || '');
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    setTitulo(opportunity.titulo);
    setClientId(opportunity.client_id || '');
    setValorEstimado(opportunity.valor_estimado.toString());
    setProbabilidad(opportunity.probabilidad.toString());
    setEtapa(opportunity.etapa);
    setFechaCierre(opportunity.fecha_cierre_estimada?.split('T')[0] || '');
    setFuente(opportunity.fuente || 'web');
    setResponsable(opportunity.responsable || '');
    setDescripcion(opportunity.descripcion || '');
  }, [opportunity]);

  async function handleSave() {
    setSaving(true);
    try {
      await updateCRMOpportunity(opportunity.id, {
        titulo,
        client_id: clientId || undefined,
        valor_estimado: parseFloat(valorEstimado) || undefined,
        probabilidad: parseInt(probabilidad) || undefined,
        etapa,
        fecha_cierre_estimada: fechaCierre || undefined,
        fuente,
        responsable: responsable || undefined,
        descripcion: descripcion || undefined,
      });
      toast.success('Oportunidad actualizada');
      onOpenChange(false);
      onUpdated();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al actualizar');
    } finally {
      setSaving(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-2xl max-h-[80vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle>Editar Oportunidad</DialogTitle>
          <DialogDescription>Modifique los datos de la oportunidad</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2 col-span-2"><Label>Título *</Label><Input value={titulo} onChange={(e) => setTitulo(e.target.value)} /></div>
            <div className="space-y-2"><Label>Cliente</Label><Select value={clientId} onValueChange={setClientId}><SelectTrigger><SelectValue placeholder="Seleccionar cliente" /></SelectTrigger><SelectContent>{clients.map((c) => (<SelectItem key={c.id} value={c.id}>{c.razon_social}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Etapa</Label><Select value={etapa} onValueChange={setEtapa}><SelectTrigger /><SelectContent>{ETAPAS_PIPELINE.map((e) => (<SelectItem key={e.key} value={e.key}>{e.label}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Valor Estimado ($)</Label><Input type="number" value={valorEstimado} onChange={(e) => setValorEstimado(e.target.value)} /></div>
            <div className="space-y-2"><Label>Probabilidad (%)</Label><Input type="number" min="0" max="100" value={probabilidad} onChange={(e) => setProbabilidad(e.target.value)} /></div>
            <div className="space-y-2"><Label>Fecha Cierre Estimada</Label><Input type="date" value={fechaCierre} onChange={(e) => setFechaCierre(e.target.value)} /></div>
            <div className="space-y-2"><Label>Fuente</Label><Select value={fuente} onValueChange={setFuente}><SelectTrigger /><SelectContent>{FUENTES.map((f) => (<SelectItem key={f.key} value={f.key}>{f.label}</SelectItem>))}</SelectContent></Select></div>
            <div className="space-y-2"><Label>Responsable</Label><Input value={responsable} onChange={(e) => setResponsable(e.target.value)} /></div>
            <div className="space-y-2 col-span-2"><Label>Descripción</Label><Textarea value={descripcion} onChange={(e) => setDescripcion(e.target.value)} rows={2} /></div>
          </div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={handleSave} disabled={saving}>{saving ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}Guardar</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function CreateActivityDialog({ open, onOpenChange, companyId, opportunities, onCreated }: {
  open: boolean; onOpenChange: (open: boolean) => void; companyId: string; opportunities: CRMOpportunity[]; onCreated: () => void;
}) {
  const [tipo, setTipo] = useState('llamada');
  const [asunto, setAsunto] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [fechaActividad, setFechaActividad] = useState(new Date().toISOString().slice(0, 10));
  const [opportunityId, setOpportunityId] = useState('');
  const [creating, setCreating] = useState(false);

  async function handleCreate() {
    if (!asunto) {
      toast.error('El asunto es requerido');
      return;
    }
    setCreating(true);
    try {
      await createCRMActivity({
        company_id: companyId,
        tipo,
        asunto,
        descripcion: descripcion || undefined,
        fecha_actividad: fechaActividad,
        opportunity_id: opportunityId || undefined,
        estado: 'pendiente',
      });
      toast.success('Actividad creada');
      onOpenChange(false);
      setTipo('llamada'); setAsunto(''); setDescripcion('');
      setFechaActividad(new Date().toISOString().slice(0, 10)); setOpportunityId('');
      onCreated();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al crear actividad');
    } finally {
      setCreating(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Nueva Actividad</DialogTitle>
          <DialogDescription>Registre una nueva actividad en el CRM</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label>Tipo *</Label>
              <Select value={tipo} onValueChange={setTipo}>
                <SelectTrigger><SelectValue /></SelectTrigger>
                <SelectContent>
                  {TIPOS_ACTIVIDAD.map((t) => (<SelectItem key={t.key} value={t.key}>{t.label}</SelectItem>))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label>Oportunidad</Label>
              <Select value={opportunityId} onValueChange={setOpportunityId}>
                <SelectTrigger><SelectValue placeholder="Sin oportunidad" /></SelectTrigger>
                <SelectContent>
                  {opportunities.map((o) => (<SelectItem key={o.id} value={o.id}>{o.titulo}</SelectItem>))}
                </SelectContent>
              </Select>
            </div>
          </div>
          <div className="space-y-2"><Label>Asunto *</Label><Input value={asunto} onChange={(e) => setAsunto(e.target.value)} placeholder="Asunto de la actividad" /></div>
          <div className="space-y-2"><Label>Descripción</Label><Textarea value={descripcion} onChange={(e) => setDescripcion(e.target.value)} rows={2} placeholder="Detalles de la actividad" /></div>
          <div className="space-y-2"><Label>Fecha Programada</Label><Input type="date" value={fechaActividad} onChange={(e) => setFechaActividad(e.target.value)} /></div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={handleCreate} disabled={creating}>{creating ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}Crear Actividad</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function CreateSegmentDialog({ open, onOpenChange, companyId, onCreated }: {
  open: boolean; onOpenChange: (open: boolean) => void; companyId: string; onCreated: () => void;
}) {
  const [nombre, setNombre] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [color, setColor] = useState('#3b82f6');
  const [criterio, setCriterio] = useState('');
  const [creating, setCreating] = useState(false);

  async function handleCreate() {
    if (!nombre) {
      toast.error('El nombre es requerido');
      return;
    }
    setCreating(true);
    try {
      await createCRMSegment({
        company_id: companyId,
        nombre,
        descripcion: descripcion || undefined,
        color,
        criterio: criterio || undefined,
      });
      toast.success('Segmento creado');
      onOpenChange(false);
      setNombre(''); setDescripcion(''); setColor('#3b82f6'); setCriterio('');
      onCreated();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al crear segmento');
    } finally {
      setCreating(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Nuevo Segmento</DialogTitle>
          <DialogDescription>Cree un segmento para agrupar clientes</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="space-y-2"><Label>Nombre *</Label><Input value={nombre} onChange={(e) => setNombre(e.target.value)} placeholder="Nombre del segmento" /></div>
          <div className="space-y-2"><Label>Descripción</Label><Textarea value={descripcion} onChange={(e) => setDescripcion(e.target.value)} rows={2} placeholder="Descripción del segmento" /></div>
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2"><Label>Color</Label><div className="flex items-center gap-2"><Input type="color" value={color} onChange={(e) => setColor(e.target.value)} className="w-10 h-10 p-1" /><span className="text-sm text-muted-foreground">{color}</span></div></div>
            <div className="space-y-2"><Label>Tipo</Label><Badge variant="outline">{criterio ? 'Dinámico' : 'Manual'}</Badge></div>
          </div>
          <div className="space-y-2"><Label>Reglas (JSON)</Label><Textarea value={criterio} onChange={(e) => setCriterio(e.target.value)} rows={2} placeholder='{"campo": "valor"}' /></div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={handleCreate} disabled={creating}>{creating ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}Crear Segmento</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function CreateAutomationDialog({ open, onOpenChange, companyId, onCreated }: {
  open: boolean; onOpenChange: (open: boolean) => void; companyId: string; onCreated: () => void;
}) {
  const [nombre, setNombre] = useState('');
  const [eventoDisparador, setEventoDisparador] = useState('nueva_oportunidad');
  const [condiciones, setCondiciones] = useState('');
  const [acciones, setAcciones] = useState('');
  const [isActive, setIsActive] = useState(true);
  const [creating, setCreating] = useState(false);

  const TRIGGERS = [
    { key: 'nueva_oportunidad', label: 'Nueva Oportunidad' },
    { key: 'cambio_etapa', label: 'Cambio de Etapa' },
    { key: 'actividad_vencida', label: 'Actividad Vencida' },
    { key: 'nuevo_lead', label: 'Nuevo Lead' },
    { key: 'lead_convertido', label: 'Lead Convertido' },
  ];

  async function handleCreate() {
    if (!nombre || !acciones) {
      toast.error('Complete los campos requeridos (nombre, acciones)');
      return;
    }
    setCreating(true);
    try {
      await createCRMAutomation({
        company_id: companyId,
        nombre,
        evento_disparador: eventoDisparador,
        condiciones: condiciones || undefined,
        acciones,
        is_active: isActive,
      });
      toast.success('Automatización creada');
      onOpenChange(false);
      setNombre(''); setEventoDisparador('nueva_oportunidad'); setCondiciones(''); setAcciones(''); setIsActive(true);
      onCreated();
    } catch (err) {
      toast.error(err instanceof Error ? err.message : 'Error al crear automatización');
    } finally {
      setCreating(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Nueva Automatización</DialogTitle>
          <DialogDescription>Configure una automatización del CRM</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="space-y-2"><Label>Nombre *</Label><Input value={nombre} onChange={(e) => setNombre(e.target.value)} placeholder="Nombre de la automatización" /></div>
          <div className="space-y-2">
            <Label>Trigger *</Label>
            <Select value={eventoDisparador} onValueChange={setEventoDisparador}>
              <SelectTrigger><SelectValue /></SelectTrigger>
              <SelectContent>
                {TRIGGERS.map((t) => (<SelectItem key={t.key} value={t.key}>{t.label}</SelectItem>))}
              </SelectContent>
            </Select>
          </div>
          <div className="space-y-2"><Label>Condiciones (JSON)</Label><Textarea value={condiciones} onChange={(e) => setCondiciones(e.target.value)} rows={2} placeholder='{"campo": "valor"}' /></div>
          <div className="space-y-2"><Label>Acciones (JSON) *</Label><Textarea value={acciones} onChange={(e) => setAcciones(e.target.value)} rows={3} placeholder='[{"tipo": "enviar_email", "destino": "cliente"}]' /></div>
          <div className="flex items-center gap-2">
            <input type="checkbox" checked={isActive} onChange={(e) => setIsActive(e.target.checked)} className="rounded" />
            <Label>Activar inmediatamente</Label>
          </div>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => onOpenChange(false)}>Cancelar</Button>
            <Button onClick={handleCreate} disabled={creating}>{creating ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}Crear Automatización</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}
