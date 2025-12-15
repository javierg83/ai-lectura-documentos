# borrar_todo_redis.py

from utils.redis_utils import r  # Usa la conexión ya configurada
import sys

def borrar_todo_redis():
    print("⚠️ Este script eliminará todas las claves de la base de datos Redis configurada.")
    confirmacion = input("¿Estás seguro que quieres continuar? (sí/no): ").strip().lower()

    if confirmacion != "sí":
        print("❌ Operación cancelada.")
        return

    try:
        total = r.dbsize()
        print(f"🔍 Claves encontradas: {total}")

        if total == 0:
            print("✅ No hay claves que borrar.")
            return

        r.flushdb()
        print("🧹 Todas las claves han sido eliminadas exitosamente.")
    except Exception as e:
        print(f"❌ Error al conectar o borrar en Redis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    borrar_todo_redis()
