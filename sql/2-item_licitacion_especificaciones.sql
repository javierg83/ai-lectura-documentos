
-- ==========================================================
-- TABLA: items_licitacion
-- ==========================================================

CREATE TABLE IF NOT EXISTS public.items_licitacion (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  licitacion_id TEXT NOT NULL,
  semantic_run_id UUID NOT NULL REFERENCES public.semantic_runs(id) ON DELETE CASCADE,
  item_key TEXT, -- Clave lógica para trazabilidad entre ítem y especificaciones
  nombre_item TEXT,
  cantidad NUMERIC,
  unidad TEXT,
  descripcion TEXT,
  observaciones TEXT,
  fuente_resumen TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
  incompleto BOOLEAN DEFAULT false,
  incompleto_motivos TEXT[],
  tiene_descripcion_tecnica BOOLEAN DEFAULT false
);

CREATE INDEX IF NOT EXISTS idx_items_licitacion_licitacion_id ON public.items_licitacion(licitacion_id);
CREATE INDEX IF NOT EXISTS idx_items_licitacion_semantic_run_id ON public.items_licitacion(semantic_run_id);
CREATE INDEX IF NOT EXISTS idx_items_licitacion_item_key ON public.items_licitacion(item_key);

-- ==========================================================
-- TABLA: item_licitacion_especificaciones
-- ==========================================================

CREATE TABLE IF NOT EXISTS public.item_licitacion_especificaciones (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  semantic_run_id UUID NOT NULL REFERENCES public.semantic_runs(id) ON DELETE CASCADE,
  item_id UUID NOT NULL REFERENCES public.items_licitacion(id) ON DELETE CASCADE,
  especificacion TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_item_licitacion_especificaciones_item ON public.item_licitacion_especificaciones(item_id);
CREATE INDEX IF NOT EXISTS idx_item_licitacion_especificaciones_semantic_run ON public.item_licitacion_especificaciones(semantic_run_id);
