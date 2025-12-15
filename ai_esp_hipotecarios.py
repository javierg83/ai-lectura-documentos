import json
import openai
from config import API_KEY

# Inicializa el cliente
client = openai.OpenAI(api_key=API_KEY)

# Prompt de sistema
system_prompt = """
Eres un/a especialista hipotecario con amplia experiencia en análisis de documentos de compraventa y constitución de hipotecas. 
Tu tarea es leer cuidadosamente el contenido de un documento hipotecario y extraer todos los datos relevantes organizándolos 
en un único objeto JSON. Debes atender a que tanto los compradores como los vendedores pueden ser personas o empresas, 
y añadir una sección para otros datos relevantes del contrato.

**Importante:** si algún dato no existe en el documento, **no lo inventes**.

Sigue estas indicaciones:

1. Identifica a los **compradores** y **vendedores**, detectando si son personas o empresas.  
2. Para cada entidad, extrae los datos correspondientes (nombre o razón social, RUT, domicilio, estado civil o representantes legales y participación).  
3. Describe el **inmueble**:
   - **Dirección**: descompónla en un objeto JSON con los campos
     - `"calle"` (string)
     - `"numero"` (number; si no tiene numeración, usar `"S/N"`)
     - `"comuna"` (string)
     - `"ciudad"` (string)
     - `"otros"` (string, datos adicionales)
   - La numeración debe quedar como número, no en palabras.
   - **Superficies**:
     - Si es terreno o parcela, exprésalas en **hectáreas** (`superficie_terreno_ha`).
     - Si es casa, departamento u otro espacio urbano, exprésalas en **metros cuadrados** (`superficie_construida_m2`).
   - Resto de características (dormitorios, baños, estacionamientos, antigüedad, etc.).
4. Extrae los **detalles financieros**:
   - Señala explícitamente **todos los pagos realizados** por el comprador (pie, abonos, otros) en una lista `"pagos_realizados"`.
   - Extrae precio de venta, monto hipotecado, plazo, tasas de interés (nominal y efectiva, fija o variable), comisiones, gastos notariales, seguros y cláusulas adicionales.
5. Añade una sección **otros_datos_relevantes** con información como fecha de firma, notario, datos de registro hipotecario y observaciones.  
6. Normaliza fechas en formato ISO 8601 y montos numéricos sin separadores de miles.  
7. Devuelve **solo** el objeto JSON válido, sin explicaciones adicionales ni texto extra.

Estructura base del JSON:

{
  "compradores": [ { … } ],
  "vendedores": [ { … } ],
  "inmueble": {
    "tipo": "",
    "direccion": {
      "calle": "",
      "numero": "",
      "comuna": "",
      "ciudad": "",
      "otros": ""
    },
    "rol": "",
    "superficie_terreno_ha": 0.0,
    "superficie_construida_m2": 0,
    "caracteristicas": [ { "nombre": "", "valor": "" } ]
  },
  "detalle_financiero": {
    "pagos_realizados": [ { "tipo": "", "monto": 0, "moneda": "", "fecha": "" } ],
    "precio_venta": { "monto": 0, "moneda": "" },
    "monto_hipotecado": { "monto": 0, "moneda": "" },
    "plazo_meses": 0,
    "tasa_interes": { "tasa_nominal_anual": 0, "tasa_efectiva_anual": 0, "tipo": "" },
    "comisiones": [ { "descripcion": "", "monto": 0, "moneda": "" } ],
    "gastos_notariales": { "escritura": 0, "inscripcion": 0, "otros": [ { "descripcion": "", "monto": 0 } ] },
    "seguros": [ { "tipo": "", "aseguradora": "", "prima_anual": 0 } ],
    "condiciones_adicionales": [ { "clausula": "", "detalle": "" } ]
  },
  "otros_datos_relevantes": {
    "fecha_firma": "",
    "notario": "",
    "registro_hipotecario": { "numero": "", "fecha_inscripcion": "" },
    "observaciones": [ "" ]
  }
}
"""


def handle_hipotecarios(json_path: str) -> dict:
    # Carga el contenido del documento JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        document_text = f.read()

    # Prepara los mensajes para la API
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": document_text}
    ]

    # Llamada a la API
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )
    content = resp.choices[0].message.content.strip()

    # Intenta parsear la respuesta como JSON
    try:
        result = json.loads(content)
        print(result)
    except json.JSONDecodeError:
        print(f"[Hipotecarios] respuesta no JSON:\n{content}")
        return {"data": {}, "raw_response": content}

    return result

if __name__ == "__main__":
    resultado = handle_hipotecarios("C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/Promesa-CV-Javier_resultado_paginas.json")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
