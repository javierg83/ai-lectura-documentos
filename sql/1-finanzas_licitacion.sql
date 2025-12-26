-- =========================================================
-- EXTENSION REQUERIDA (UUID)
-- =========================================================
create extension if not exists "pgcrypto";

-- =========================================================
-- TABLA: finanzas_licitacion
-- =========================================================
create table if not exists public.finanzas_licitacion (
  id uuid primary key default gen_random_uuid(),

  licitacion_id uuid not null
    references public.licitaciones(id)
    on delete cascade,

  presupuesto_referencial numeric null,
  moneda text null,

  forma_pago text null,
  plazo_pago text null,

  fuente_financiamiento text null,
  observaciones text null,

  fecha_extraccion timestamptz not null default now(),

  unique (licitacion_id)
);

create index if not exists idx_finanzas_licitacion_licitacion
  on public.finanzas_licitacion (licitacion_id);

-- =========================================================
-- TABLA: finanzas_garantias
-- =========================================================
create table if not exists public.finanzas_garantias (
  id uuid primary key default gen_random_uuid(),

  finanzas_licitacion_id uuid not null
    references public.finanzas_licitacion(id)
    on delete cascade,

  tipo text not null,              -- ej: SERIEDAD_OFERTA, FIEL_CUMPLIMIENTO
  monto numeric null,
  moneda text null,
  vigencia text null,
  descripcion text null
);

create index if not exists idx_finanzas_garantias_finanzas
  on public.finanzas_garantias (finanzas_licitacion_id);

-- =========================================================
-- TABLA: finanzas_multas
-- =========================================================
create table if not exists public.finanzas_multas (
  id uuid primary key default gen_random_uuid(),

  finanzas_licitacion_id uuid not null
    references public.finanzas_licitacion(id)
    on delete cascade,

  descripcion text not null,
  monto numeric null,
  moneda text null,
  condicion_aplicacion text null
);

create index if not exists idx_finanzas_multas_finanzas
  on public.finanzas_multas (finanzas_licitacion_id);
