-- ==============================================
-- TABLA: homologaciones_productos
-- ==============================================
CREATE TABLE IF NOT EXISTS public.homologaciones_productos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  licitacion_id UUID NOT NULL REFERENCES public.licitaciones(id) ON DELETE CASCADE,
  item_key TEXT NOT NULL,
  descripcion_detectada TEXT NOT NULL,
  razonamiento_general TEXT,
  tokens_input INT,
  tokens_output INT,
  tokens_total INT,
  modelo_usado TEXT,
  fecha_homologacion TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_homologaciones_licitacion ON public.homologaciones_productos(licitacion_id);


-- ==============================================
-- TABLA: candidatos_homologacion
-- ==============================================
CREATE TABLE IF NOT EXISTS public.candidatos_homologacion (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  homologacion_id UUID NOT NULL REFERENCES public.homologaciones_productos(id) ON DELETE CASCADE,
  ranking INT NOT NULL,
  producto_codigo TEXT NOT NULL,
  producto_nombre TEXT NOT NULL,
  producto_descripcion TEXT,
  stock_disponible INT,
  ubicacion_stock TEXT,
  score_similitud FLOAT NOT NULL,
  razonamiento TEXT
);

CREATE INDEX IF NOT EXISTS idx_candidatos_homologacion_hid ON public.candidatos_homologacion(homologacion_id);