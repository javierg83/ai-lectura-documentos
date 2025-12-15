# create_index.py
# --------------------------------
# Requisitos:
#   pip install redis python-dotenv
#
# Este script crea (si no existe) el índice `idx:documents`
# sobre hashes con prefijo `doc:` y campos `filename` y `content`.

from redis import Redis
import redis
import config

# 1. Conéctate a tu Redis Cloud
r = Redis.from_url(config.REDIS_URL)

# 2. Intenta obtener info del índice
try:
    r.execute_command('FT.INFO', 'idx:documents')
    print("Índice 'idx:documents' ya existe.")
except redis.exceptions.ResponseError:
    # 3. Si no existe, créalo:
    #    FT.CREATE idx:documents ON HASH PREFIX 1 doc: SCHEMA filename TEXT SORTABLE content TEXT
    r.execute_command(
        'FT.CREATE', 'idx:documents',
        'ON', 'HASH',
        'PREFIX', '1', 'doc:',
        'SCHEMA',
          'filename', 'TEXT', 'SORTABLE',
          'content',  'TEXT'
    )
    print("Índice 'idx:documents' creado con éxito.")
