# utils/redis_utils.py

import redis
import json
import os
from dotenv import load_dotenv

# Cargar variables desde .env si existe
load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)
REDIS_USERNAME = os.getenv("REDIS_USERNAME", None)
REDIS_SSL = os.getenv("REDIS_USE_SSL", "false").lower() == "true"

print(f"[redis_utils] 🧩 REDIS_HOST: {REDIS_HOST}")
print(f"[redis_utils] 🧩 REDIS_PORT: {REDIS_PORT}")
print(f"[redis_utils] 🧩 REDIS_DB: {REDIS_DB}")
print(f"[redis_utils] 🧩 REDIS_USERNAME: {REDIS_USERNAME}")
print(f"[redis_utils] 🧩 REDIS_SSL: {REDIS_SSL}")

# Conexión global
try:
    redis_params = {
        "host": REDIS_HOST,
        "port": REDIS_PORT,
        "db": REDIS_DB,
        "decode_responses": True,
    }

    if REDIS_PASSWORD:
        redis_params["password"] = REDIS_PASSWORD
        print("[redis_utils] 🔑 Usando contraseña para Redis")

    if REDIS_USERNAME:
        redis_params["username"] = REDIS_USERNAME
        print("[redis_utils] 👤 Usando usuario para Redis")

    if REDIS_SSL:
        redis_params["ssl"] = True
        print("[redis_utils] 🔐 Conexión con SSL ACTIVADA")
    else:
        print("[redis_utils] 🛡️ Conexión sin SSL")

    print(f"[redis_utils] 🚀 Conectando a Redis con parámetros: {redis_params}")

    r = redis.Redis(**redis_params)
    r.ping()
    print("[redis_utils] ✅ Conexión exitosa a Redis")

except Exception as e:
    print(f"[redis_utils] ❌ Error conectando a Redis: {e}")
    import traceback
    traceback.print_exc()
    r = None


def guardar_en_redis(clave, datos):
    """
    Guarda un diccionario como hash en Redis.
    Convierte automáticamente valores que sean listas o diccionarios a JSON string.
    """
    if r is None:
        print(f"[redis_utils] ⚠️ Redis no está conectado. No se puede guardar {clave}")
        return

    try:
        print(f"[redis_utils] 💾 Guardando clave: {clave}")
        datos_serializados = {
            k: json.dumps(v) if isinstance(v, (dict, list)) else v
            for k, v in datos.items()
        }
        r.hset(clave, mapping=datos_serializados)
        print(f"[redis_utils] ✅ Guardado en Redis: {clave}")
    except Exception as e:
        print(f"[redis_utils] ❌ Error guardando {clave}: {e}")
        import traceback
        traceback.print_exc()


def leer_hash(clave):
    """Lee un hash de Redis y deserializa campos JSON si aplica"""
    if r is None:
        print(f"[redis_utils] ⚠️ Redis no está conectado. No se puede leer {clave}")
        return {}

    try:
        print(f"[redis_utils] 📥 Leyendo hash: {clave}")
        data = r.hgetall(clave)
        for k, v in data.items():
            try:
                data[k] = json.loads(v)
            except Exception:
                pass  # Mantener valor como string si no es JSON
        return data
    except Exception as e:
        print(f"[redis_utils] ❌ Error al leer {clave}: {e}")
        import traceback
        traceback.print_exc()
        return {}


import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD, REDIS_USERNAME

def get_redis_connection() -> redis.Redis:
    """
    Devuelve una conexión directa a Redis para operaciones como scan_iter.
    """
    return redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        decode_responses=True,
        username=REDIS_USERNAME,
        password=REDIS_PASSWORD,
        ssl=False  # conexión sin SSL
    )