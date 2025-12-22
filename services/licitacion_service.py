import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
    )

def obtener_licitacion_por_id(licitacion_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM licitaciones WHERE id = %s", (str(licitacion_id),))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0],
            'codigo_licitacion': row[1],
            'nombre': row[2],
            'descripcion': row[3],
            'fecha_carga': row[4],
            'estado': row[5],
            'tenant_id': row[6]
        }
    return None

def obtener_todas_las_licitaciones():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM licitaciones ORDER BY fecha_carga DESC")
    rows = cursor.fetchall()
    conn.close()

    licitaciones = []
    for row in rows:
        licitaciones.append({
            'id': row[0],
            'codigo_licitacion': row[1],
            'nombre': row[2],
            'descripcion': row[3],
            'fecha_carga': row[4],
            'estado': row[5],
            'tenant_id': row[6]
        })
    return licitaciones

def obtener_items_por_licitacion(licitacion_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nro_item, producto, cantidad, unidad, descripcion
        FROM licitacion_items
        WHERE licitacion_id = %s
        ORDER BY nro_item
    """, (str(licitacion_id),))
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "nro_item": row[0],
            "producto": row[1],
            "cantidad": row[2],
            "unidad": row[3],
            "descripcion": row[4],
        }
        for row in rows
    ]

def get_or_create_licitacion(codigo_licitacion, nombre=None, descripcion=None, tenant_id=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Buscar si ya existe
    cursor.execute("""
        SELECT * FROM licitaciones WHERE codigo_licitacion = %s
    """, (codigo_licitacion,))
    row = cursor.fetchone()

    if row:
        conn.close()
        return {
            'id': row[0],
            'codigo_licitacion': row[1],
            'nombre': row[2],
            'descripcion': row[3],
            'fecha_carga': row[4],
            'estado': row[5],
            'tenant_id': row[6]
        }

    # Si no existe, crear una nueva
    import uuid
    nueva_id = str(uuid.uuid4())

    cursor.execute("""
        INSERT INTO licitaciones (id, codigo_licitacion, nombre, descripcion, tenant_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (nueva_id, codigo_licitacion, nombre, descripcion, tenant_id))

    conn.commit()
    conn.close()

    return {
        'id': nueva_id,
        'codigo_licitacion': codigo_licitacion,
        'nombre': nombre,
        'descripcion': descripcion,
        'fecha_carga': None,
        'estado': 'ACTIVA',
        'tenant_id': tenant_id
    }
