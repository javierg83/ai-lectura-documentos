-- =============================================================
-- MODELO DE BASE DE DATOS PARA GESTIÓN DE LICITACIONES (v2026)
-- =============================================================
-- Este archivo contiene la creación completa de todas las tablas del sistema
-- de licitaciones, incluyendo adjudicación, homologación, trazabilidad y
-- almacenamiento de evidencias (OC y cotizaciones).
--
-- Cada tabla contiene:
-- • Una descripción funcional del concepto
-- • Descripción de cada campo y su propósito
-- • Claves UUID + ID interno incremental (para uso interfaz)
-- • Borrado lógico mediante campo `obsoleto`
--
-- Requiere extensión: pgcrypto (para gen_random_uuid())
-- =============================================================

CREATE EXTENSION IF NOT EXISTS "pgcrypto";


-- =============================================
-- Tabla: licitaciones
-- =============================================
-- CONCEPTO: Representa una licitación publicada por un organismo.
-- Describe la solicitud formal de adquisición de bienes o servicios.
-- =============================================
-- Campos:
-- - id: UUID único para referencia interna
-- - id_interno: Número incremental visible para usuarios
-- - codigo_licitacion: Código oficial de la licitación
-- - titulo: Título descriptivo
-- - descripcion: Detalle general del proceso
-- - organismo: Institución que publica
-- - unidad_solicitante: Área interna que realiza la solicitud
-- - forma_pago / plazo_pago / moneda: Condiciones comerciales
-- - presupuesto_maximo: Monto máximo aceptado
-- - estado: Activa, Cerrada, Adjudicada, etc.
-- - usuario: Responsable asignado
-- - fecha_publicacion / cierre / adjudicacion: Fechas clave
-- - obsoleto: Indicador de borrado lógico
CREATE TABLE licitaciones (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    codigo_licitacion TEXT,
    titulo TEXT,
    descripcion TEXT,
    organismo TEXT,
    unidad_solicitante TEXT,
    forma_pago TEXT,
    plazo_pago TEXT,
    moneda TEXT,
    presupuesto_maximo NUMERIC,
    estado TEXT,
    usuario TEXT,
    fecha_publicacion DATE,
    fecha_cierre DATE,
    fecha_adjudicacion DATE,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: licitacion_archivos
-- =============================================
-- CONCEPTO: Archivos asociados a la licitación (Bases, Anexos, etc.).
-- Permite gestión individual de extracción y embedding.
-- =============================================
-- Campos:
-- - licitacion_id: FK obligatoria
-- - estado_procesamiento: Control de flujo ETL (PENDIENTE, EXTRAYENDO...)
-- - estado_embedding: Si ya está en vector DB
-- =============================================
CREATE TABLE licitacion_archivos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    licitacion_id UUID NOT NULL REFERENCES licitaciones(id),
    nombre_archivo_org TEXT NOT NULL,
    ruta_almacenamiento TEXT,
    tipo_contenido TEXT,
    peso_bytes BIGINT,
    hash_md5 TEXT,
    clasificacion_archivo TEXT,
    estado_procesamiento TEXT DEFAULT 'PENDIENTE',
    estado_embedding BOOLEAN DEFAULT FALSE,
    id_job_procesamiento TEXT,
    mensaje_error TEXT,
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_procesado TIMESTAMP,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: items_licitacion
-- =============================================
-- CONCEPTO: Ítems o productos solicitados dentro de una licitación.
-- Cada fila representa una línea de pedido o requerimiento específico.
-- =============================================
-- Campos:
-- - licitacion_id: FK a licitaciones
-- - descripcion: Detalle del producto o servicio requerido
-- - cantidad / unidad: Número y unidad solicitada
-- - sku: Código interno opcional
-- - adjudicado / proveedor / precio_unitario: Resultado del proceso
-- - comentario_adjudicacion: Observaciones finales del ítem
CREATE TABLE items_licitacion (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    licitacion_id UUID REFERENCES licitaciones(id),
    descripcion TEXT,
    cantidad NUMERIC,
    unidad TEXT,
    sku TEXT,
    archivo_origen_id UUID REFERENCES licitacion_archivos(id),
    adjudicado BOOLEAN DEFAULT FALSE,
    proveedor TEXT,
    precio_unitario NUMERIC,
    comentario_adjudicacion TEXT,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: especificaciones_tecnicas
-- =============================================
-- CONCEPTO: Condiciones técnicas requeridas para un ítem.
-- Se agrupan por tipo: obligatoria, recomendada o general.
-- =============================================
-- Campos:
-- - item_id: FK a ítem
-- - tipo: Tipo de especificación
-- - descripcion: Detalle técnico
CREATE TABLE especificaciones_tecnicas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    item_id UUID REFERENCES items_licitacion(id),
    tipo TEXT,
    descripcion TEXT,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: finanzas_licitacion
-- =============================================
-- CONCEPTO: Información financiera asociada a la licitación.
-- Incluye fuente, glosa, tipo documento y montos involucrados.
-- =============================================
-- Campos:
-- - licitacion_id: FK
-- - tipo_documento / descripcion / documento_origen: Caracterización
-- - monto / fuente_financiamiento / glosa: Valores económicos
CREATE TABLE finanzas_licitacion (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    licitacion_id UUID REFERENCES licitaciones(id),
    tipo_documento TEXT,
    descripcion TEXT,
    monto NUMERIC,
    documento_origen TEXT,
    fuente_financiamiento TEXT,
    glosa TEXT,
    archivo_origen_id UUID REFERENCES licitacion_archivos(id),
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: homologaciones_productos
-- =============================================
-- CONCEPTO: Resultado del proceso de homologación de un ítem solicitado.
-- Registra razonamiento del modelo y uso de tokens IA.
-- =============================================
CREATE TABLE homologaciones_productos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    item_id UUID REFERENCES items_licitacion(id),
    razonamiento TEXT,
    input_tokens INTEGER,
    output_tokens INTEGER,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: candidatos_homologacion
-- =============================================
-- CONCEPTO: Alternativas propuestas por el modelo para un ítem.
-- Asociadas a una homologación específica.
-- =============================================
CREATE TABLE candidatos_homologacion (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    homologacion_id UUID REFERENCES homologaciones_productos(id),
    nombre_producto TEXT,
    descripcion TEXT,
    score_similitud NUMERIC,
    razonamiento TEXT,
    ranking INTEGER,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: adjudicaciones_licitacion
-- =============================================
-- CONCEPTO: Representa el acto de adjudicar una licitación.
-- Incluye información general, monto y comentarios.
-- =============================================
CREATE TABLE adjudicaciones_licitacion (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    licitacion_id UUID REFERENCES licitaciones(id),
    usuario TEXT,
    monto_total_adjudicado NUMERIC,
    sucursal_envio_oc TEXT,
    fecha_adjudicacion DATE,
    comentario TEXT,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: archivos_cotizaciones
-- =============================================
-- CONCEPTO: Archivos subidos como cotización del proceso.
-- Se asocian a la adjudicación como respaldo.
-- =============================================
-- Campos:
-- - adjudicacion_id: FK
-- - nombre_archivo / url_archivo / formato / peso: Archivo
-- - sucursal_destino: Sucursal que lo recibió
-- - usuario_subio: Quién subió el archivo
-- - fecha_subida: Cuándo fue subido
CREATE TABLE archivos_cotizaciones (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    adjudicacion_id UUID REFERENCES adjudicaciones_licitacion(id),
    nombre_archivo TEXT,
    url_archivo TEXT,
    formato TEXT,
    peso_archivo_kb NUMERIC,
    sucursal_destino TEXT,
    usuario_subio TEXT,
    fecha_subida TIMESTAMP,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: archivos_ordenes_compra
-- =============================================
-- CONCEPTO: Archivos subidos como orden de compra oficial.
-- Parte del respaldo formal del proceso adjudicado.
-- =============================================
CREATE TABLE archivos_ordenes_compra (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    adjudicacion_id UUID REFERENCES adjudicaciones_licitacion(id),
    nombre_archivo TEXT,
    url_archivo TEXT,
    formato TEXT,
    peso_archivo_kb NUMERIC,
    sucursal_destino TEXT,
    usuario_subio TEXT,
    fecha_subida TIMESTAMP,
    obsoleto BOOLEAN DEFAULT FALSE
);


-- =============================================
-- Tabla: auditoria_eventos
-- =============================================
-- CONCEPTO: Registro semiestructurado de cualquier cambio en el sistema.
-- Permite trazabilidad de acciones por entidad, usuario y contenido JSON.
-- =============================================
CREATE TABLE auditoria_eventos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_interno SERIAL UNIQUE,
    entidad TEXT NOT NULL,
    entidad_id UUID NOT NULL,
    tipo_evento TEXT NOT NULL,
    evento TEXT NOT NULL,
    fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    datos_json JSONB NOT NULL,
    usuario TEXT
);