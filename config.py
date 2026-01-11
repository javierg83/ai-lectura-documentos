# config.py
from dotenv import load_dotenv
load_dotenv()

import os

# Clave OpenAI
# AI CONFIG
API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DEFAULT_AI_PROVIDER = "openai" # "openai" or "gemini"
if not API_KEY:
    raise ValueError("La variable OPENAI_API_KEY no está definida en el entorno")

# Parámetros de Redis
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_DB = os.getenv("REDIS_DB", "0")
REDIS_USERNAME = os.getenv("REDIS_USERNAME", "")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")

MODEL_EMBEDDING = "text-embedding-3-small"

# REDIS_PROTOCOL = "rediss"  ← ESTE NO
REDIS_PROTOCOL = os.getenv("REDIS_PROTOCOL", "redis")  # ✅ usa este


# Construir URL de Redis con esquema válido
if REDIS_USERNAME and REDIS_PASSWORD:
    REDIS_URL = f"{REDIS_PROTOCOL}://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
elif REDIS_PASSWORD:
    REDIS_URL = f"{REDIS_PROTOCOL}://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
else:
    REDIS_URL = f"{REDIS_PROTOCOL}://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
