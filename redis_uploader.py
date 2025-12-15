import os, json
from config import REDIS_URL

# Comprobación e import
try:
    import redis
    try:
        _redis = redis.from_url(REDIS_URL)
        HAS_REDIS = True
    except Exception as e:
        print(f"[RedisUploader][Error] Conexión fallida: {e}")
        HAS_REDIS = False
except ImportError:
    print("[RedisUploader][Error] Redis no instalado. Módulo desactivado.")
    HAS_REDIS = False

def upload_json_to_redis(json_path: str, key: str) -> None:
    if not HAS_REDIS:
        print("[RedisUploader] Subida desactivada.")
        return
    try:
        print(f"[RedisUploader] Leyendo {json_path}...")
        data=json.load(open(json_path,'r',encoding='utf-8'))
        print(f"[RedisUploader] Subiendo a '{key}'...")
        _redis.set(key,json.dumps(data,ensure_ascii=False))
        print("[RedisUploader] Subida exitosa.")
    except Exception as e:
        print(f"[RedisUploader][Error] {e}")