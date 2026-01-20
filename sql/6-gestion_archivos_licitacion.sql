-- =============================================================
-- Script 6: Gestión de Archivos por Licitación
-- Fecha: 2026-01-20
-- Descripción:
-- 1. Crea la tabla 'licitacion_archivos' para manejar múltiples documentos.
-- 2. Agrega referencias en 'items_licitacion' y 'finanzas_licitacion'.
-- NOTA: Se asume existencia de datos previos, por lo que los nuevos campos FK son NULLABLE.
-- =============================================================

-- 1. Tabla: licitacion_archivos
-- Centraliza los documentos (PDF, Docx, etc.) asociados a una licitación antes de la adjudicación.
CREATE TABLE IF NOT EXISTS licitacion_archivos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    licitacion_id UUID NOT NULL REFERENCES licitaciones(id),
    nombre_archivo_org TEXT NOT NULL,
    ruta_almacenamiento TEXT,
    tipo_contenido TEXT, -- e.g. 'application/pdf'
    peso_bytes BIGINT,
    hash_md5 TEXT,
    clasificacion_archivo TEXT, -- 'Bases', 'TDR', 'Anexos', etc.
    estado_procesamiento TEXT DEFAULT 'PENDIENTE', -- 'PENDIENTE', 'EXTRAYENDO', 'COMPLETADO', 'ERROR'
    estado_embedding BOOLEAN DEFAULT FALSE,
    id_job_procesamiento TEXT,
    mensaje_error TEXT,
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_procesado TIMESTAMP,
    obsoleto BOOLEAN DEFAULT FALSE
);

-- Indice para facilitar búsquedas por licitación
CREATE INDEX IF NOT EXISTS idx_licitacion_archivos_licitacion_id ON licitacion_archivos(licitacion_id);

-- 2. Modificación: items_licitacion
-- Se agrega referencia al archivo origen del ítem.
-- Es NULLABLE porque existen ítems previos sin archivo asociado explícito en este modelo.
ALTER TABLE items_licitacion 
ADD COLUMN IF NOT EXISTS archivo_origen_id UUID REFERENCES licitacion_archivos(id);

-- 3. Modificación: finanzas_licitacion
-- Se agrega referencia al archivo origen del dato financiero.
ALTER TABLE finanzas_licitacion 
ADD COLUMN IF NOT EXISTS archivo_origen_id UUID REFERENCES licitacion_archivos(id);
