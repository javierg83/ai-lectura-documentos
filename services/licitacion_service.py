# ==============================================
# Archivo: services/licitacion_service.py (unificado)
# ==============================================

import psycopg2
import os
import uuid
from datetime import datetime

DATABASE_URL = os.getenv("DATABASE_URL")

def get_pg_conn():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL no configurado")
    return psycopg2.connect(DATABASE_URL)

# --------------------------------------------------
# FUNCIONES DE CONSULTA
# --------------------------------------------------

def obtener_licitacion_por_id(licitacion_id: str) -> dict | None:
    conn = get_pg_conn()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT id, codigo_licitacion, nombre, descripcion, estado, fecha_carga
            FROM licitaciones
            WHERE id = %s
        """, (str(licitacion_id),)
        )
        row = cur.fetchone()
        if not row:
            return None
        return {
            "id": row[0],
            "codigo_licitacion": row[1],
            "nombre": row[2],
            "descripcion": row[3],
            "estado": row[4],
            "fecha_carga": row[5].isoformat() if row[5] else None
        }
    finally:
        cur.close()
        conn.close()

def obtener_todas_las_licitaciones() -> list[dict]:
    conn = get_pg_conn()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT id, codigo_licitacion, nombre, descripcion, estado, fecha_carga
            FROM licitaciones
            ORDER BY fecha_carga DESC
        """)
        rows = cur.fetchall()
        return [
            {
                "id": r[0],
                "codigo_licitacion": r[1],
                "nombre": r[2],
                "descripcion": r[3],
                "estado": r[4],
                "fecha_carga": r[5].isoformat() if r[5] else None
            }
            for r in rows
        ]
    finally:
        cur.close()
        conn.close()

def obtener_items_por_licitacion(licitacion_id: str) -> list[dict]:
    conn = get_pg_conn()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT nombre_item, cantidad, unidad, descripcion
            FROM items_licitados
            WHERE licitacion_id = %s
            ORDER BY nombre_item
        """, (str(licitacion_id),))
        rows = cur.fetchall()
        return [
            {
                "nombre_item": r[0],
                "cantidad": r[1],
                "unidad": r[2],
                "descripcion": r[3]
            }
            for r in rows
        ]
    finally:
        cur.close()
        conn.close()

# --------------------------------------------------
# FUNCIÓN PARA EXTRACCIÓN SEMÁNTICA
# --------------------------------------------------

def get_or_create_licitacion(nombre_archivo: str) -> str:
    """
    Crea o recupera licitación según nombre del archivo PDF.
    Guarda el nombre como campo 'nombre' en la tabla licitaciones.
    """
    conn = get_pg_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id FROM licitaciones WHERE nombre = %s", (nombre_archivo,))
        row = cur.fetchone()
        if row:
            return str(row[0])

        nuevo_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO licitaciones (id, nombre, estado, fecha_carga)
            VALUES (%s, %s, 'ACTIVA', now())
        """, (nuevo_id, nombre_archivo))
        conn.commit()
        return nuevo_id
    finally:
        cur.close()
        conn.close()


def guardar_items_licitacion(conn, licitacion_id, items: list[dict]):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM items_licitacion WHERE licitacion_id = %s", (licitacion_id,))
        for item in items:
            cur.execute("""
                INSERT INTO items_licitacion (licitacion_id, item_key, nombre_item, cantidad, unidad, descripcion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                licitacion_id,
                item.get("item_key"),
                item.get("nombre_item"),
                item.get("cantidad"),
                item.get("unidad"),
                item.get("descripcion")
            ))
        conn.commit()


def guardar_finanzas_licitacion(conn, licitacion_id, finanzas: dict):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM finanzas_licitacion WHERE licitacion_id = %s", (licitacion_id,))
        cur.execute("""
            INSERT INTO finanzas_licitacion (
                licitacion_id,
                presupuesto_referencial,
                moneda,
                forma_pago,
                plazo_pago,
                fuente_financiamiento,
                garantias,
                multas
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            licitacion_id,
            finanzas.get("presupuesto_referencial"),
            finanzas.get("moneda"),
            finanzas.get("forma_pago"),
            finanzas.get("plazo_pago"),
            finanzas.get("fuente_financiamiento"),
            finanzas.get("garantias"),
            finanzas.get("multas")
        ))
        conn.commit()
