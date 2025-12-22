-- ==========================================
-- EXTENSIONES (UUID)
-- ==========================================
create extension if not exists "pgcrypto";

-- ==========================================
-- TABLA: licitaciones
-- ==========================================
create table if not exists public.licitaciones (
  id uuid primary key default gen_random_uuid(),
  codigo_licitacion text null,
  nombre text null,
  descripcion text null,
  fecha_carga timestamptz not null default now(),
  estado text not null default 'ACTIVA',
  -- opcional: para multi-tenant si después lo necesitas
  tenant_id uuid null
);

create index if not exists idx_licitaciones_codigo on public.licitaciones (codigo_licitacion);
create index if not exists idx_licitaciones_fecha on public.licitaciones (fecha_carga);

-- ==========================================
-- TABLA: documentos (archivos asociados a la licitación)
-- ==========================================
create table if not exists public.documentos (
  id uuid primary key default gen_random_uuid(),
  licitacion_id uuid not null references public.licitaciones(id) on delete cascade,
  nombre_archivo text not null,
  tipo_documento text null, -- ej: BASES_TECNICAS, BASES_ADMIN, ANEXOS, etc.
  total_paginas int null,
  hash_archivo text null,   -- opcional: sha1/sha256 si lo tienes
  creado_en timestamptz not null default now()
);

create index if not exists idx_documentos_licitacion on public.documentos (licitacion_id);

-- ==========================================
-- TABLA: semantic_runs (una ejecución del extractor por concepto)
-- concepto fijo por ahora: ITEMS_LICITACION
-- ==========================================
create table if not exists public.semantic_runs (
  id uuid primary key default gen_random_uuid(),
  licitacion_id uuid not null references public.licitaciones(id) on delete cascade,
  concepto text not null, -- 'ITEMS_LICITACION'
  is_current boolean not null default true,

  -- control / auditoría
  estado text not null default 'OK', -- OK | ERROR
  mensaje_error text null,

  -- versionado del prompt / pipeline
  prompt_version text null,
  extractor_version text null,

  -- métricas operativas
  top_k int null,
  min_score numeric(10,6) null,

  creado_en timestamptz not null default now()
);

create index if not exists idx_semantic_runs_licitacion_concepto on public.semantic_runs (licitacion_id, concepto);
create index if not exists idx_semantic_runs_current on public.semantic_runs (licitacion_id, concepto, is_current);

-- ÚNICO "vigente" por licitación + concepto
create unique index if not exists uq_semantic_runs_one_current
on public.semantic_runs (licitacion_id, concepto)
where is_current = true;

-- ==========================================
-- TABLA: semantic_results (JSON bruto generado por IA)
-- 1 a 1 con semantic_runs (para simplificar)
-- ==========================================
create table if not exists public.semantic_results (
  id uuid primary key default gen_random_uuid(),
  semantic_run_id uuid not null unique references public.semantic_runs(id) on delete cascade,
  concepto text not null,
  resultado_json jsonb not null, -- salida completa IA por concepto
  confianza_global numeric(10,6) null,
  creado_en timestamptz not null default now()
);

create index if not exists idx_semantic_results_concepto on public.semantic_results (concepto);

-- ==========================================
-- TABLA: semantic_evidences (huella exacta: fragmentos Redis usados)
-- ==========================================
create table if not exists public.semantic_evidences (
  id uuid primary key default gen_random_uuid(),
  semantic_run_id uuid not null references public.semantic_runs(id) on delete cascade,

  -- enlace a Redis (clave exacta)
  redis_key text not null,

  -- trazabilidad documental
  documento_id uuid null references public.documentos(id) on delete set null,
  pagina int null,

  -- score devuelto por vector search
  score_similitud numeric(10,6) null,

  -- snapshot del texto usado (importante para auditoría)
  texto_fragmento text not null,

  creado_en timestamptz not null default now()
);

create index if not exists idx_semantic_evidences_run on public.semantic_evidences (semantic_run_id);
create index if not exists idx_semantic_evidences_doc_pagina on public.semantic_evidences (documento_id, pagina);

-- ==========================================
-- TABLAS DOMINIO: ITEMS (normalizado)
-- ==========================================
create table if not exists public.items_licitados (
  id uuid primary key default gen_random_uuid(),
  licitacion_id uuid not null references public.licitaciones(id) on delete cascade,
  semantic_run_id uuid not null references public.semantic_runs(id) on delete cascade,

  -- campos base del ítem
  nombre_item text not null,
  cantidad numeric(14,4) null,
  unidad text null,
  descripcion text null,
  observaciones text null,

  -- trazabilidad "soft" (puede ayudar en UI)
  fuente_resumen text null, -- ej: "Bases Técnicas p.12-13"

  creado_en timestamptz not null default now()
);

create index if not exists idx_items_licitacion on public.items_licitados (licitacion_id);
create index if not exists idx_items_run on public.items_licitados (semantic_run_id);

-- Si quieres evitar duplicados exactos dentro de una corrida:
create unique index if not exists uq_items_run_nombre
on public.items_licitados (semantic_run_id, nombre_item);

create table if not exists public.item_especificaciones (
  id uuid primary key default gen_random_uuid(),
  item_id uuid not null references public.items_licitados(id) on delete cascade,
  especificacion text not null,
  creado_en timestamptz not null default now()
);

create index if not exists idx_item_specs_item on public.item_especificaciones (item_id);

-- ==========================================
-- OPCIONAL: vínculo fino de evidencia ↔ ítem (si quieres justificar cada ítem)
-- (lo recomiendo, pero puedes partir sin esto)
-- ==========================================
create table if not exists public.item_evidences (
  id uuid primary key default gen_random_uuid(),
  item_id uuid not null references public.items_licitados(id) on delete cascade,
  evidence_id uuid not null references public.semantic_evidences(id) on delete cascade,
  creado_en timestamptz not null default now(),
  unique(item_id, evidence_id)
);

create index if not exists idx_item_evidences_item on public.item_evidences (item_id);
