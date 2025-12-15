import os
from redis import Redis
import json
import config

# Configuración: carpeta donde están los JSON generados
DOCS_FOLDER = os.getenv('DOCS_FOLDER', 'archivos_texto')

# Conexión a Redis Cloud
db = Redis.from_url(config.REDIS_URL)

# Iterar sobre archivos JSON que terminen en '_resultado_paginas.json'
for fname in os.listdir(DOCS_FOLDER):
    if not fname.endswith('_resultado_paginas.json'):
        continue
    full_path = os.path.join(DOCS_FOLDER, fname)
    with open(full_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Convertimos el JSON a texto para indexar
    doc_text = json.dumps(data, ensure_ascii=False)
    # Obtener nombre original del archivo procesado (antes de '_resultado_paginas')
    base_name = fname.replace('_resultado_paginas.json', '')
    original_filename = f"{base_name}.pdf"
    key = f"doc:{base_name}"
    # Guardar en hash: filename, content y original
    db.hset(key, mapping={
        'filename': fname,
        'original': original_filename,
        'content': doc_text
    })
    print(f"Indexado JSON {fname} bajo clave {key}, original: {original_filename}.")