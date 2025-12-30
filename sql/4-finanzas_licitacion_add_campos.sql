ALTER TABLE finanzas_licitacion
ADD COLUMN garantias TEXT,
ADD COLUMN multas TEXT,
ADD COLUMN otros TEXT,
ADD COLUMN resumen TEXT,
ADD COLUMN updated_at TIMESTAMP DEFAULT now();
