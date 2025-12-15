import json
import openai
from config import API_KEY

# Inicializa el cliente
client = openai.OpenAI(api_key=API_KEY)

# Prompt de sistema
system_prompt = """
Eres un/a especialista en estudio de títulos con amplia experiencia en análisis de documentos registrales, notariales y catastros.  
Tu tarea es leer cuidadosamente el contenido de un documento de estudio de títulos y extraer **toda** la información relevante organizándola en un único objeto JSON.  
**Importante:** si algún dato no existe en el documento, **no lo inventes**.

Sigue estas indicaciones:

1. Identifica a los **propietarios** actuales y anteriores, indicando para cada uno:
   - Nombre o razón social
   - RUT o identificación
   - Tipo de titular (persona natural o jurídica)
   - Porcentaje de participación o cuota
   - Fechas de adquisición y transmisión

2. Extrae los **antecedentes registrales**:
   - Número de inscripción o folio real
   - Conservador de bienes raíces y fecha de inscripción
   - Número de rol o matrícula inmobiliaria

3. Si existen **subdivisiones**, extrae los datos de cada una:
   - Número de lote
   - Superficie de cada subdivisión
   - Rol o matrícula correspondiente

4. Describe el **inmueble** y el **lote objeto de compraventa**:
   - Identifica claramente el lote objeto de compraventa con sus campos:
     - `"numero_lote"` (string o number)
     - `"rol_lote"` (string)
   - **Dirección completa** desglosada en:
     - `"calle"` (string)
     - `"numero"` (number o `"S/N"`)
     - `"comuna"` (string)
     - `"ciudad"` (string)
     - `"otros"` (string, datos adicionales)
   - **Superficie** en metros cuadrados (`superficie_m2`) o hectáreas (`superficie_ha`)
   - Límites y deslindes (norte, sur, este, oeste)

5. Identifica y detalla las **cargas y gravámenes**:
   - Hipotecas vigentes y canceladas (monto, fecha, acreedor)
   - Embargos, prohibiciones de enajenar o gravar
   - Hipotechuras y sus condiciones (plazo, tasa, garantía)

6. Señala las **servidumbres** y limitaciones:
   - Servidumbres activas y pasivas (tipo, beneficiario, fecha)
   - Restricciones de uso (zonificación, áreas verdes, derecho de paso)

7. Añade una sección **otros_datos_relevantes** con:
   - Fecha de redactación o estudio del título
   - Notario autorizante y protocolo
   - Observaciones, reservas o cláusulas especiales

8. Normaliza fechas en formato ISO 8601 (`YYYY-MM-DD`) y montos numéricos sin separadores de miles.

9. Devuelve **solo** el objeto JSON válido, sin explicaciones ni texto adicional.

Estructura base del JSON:

{
  "propietarios": [
    {
      "nombre": "",
      "identificacion": "",
      "tipo_titular": "",
      "participacion_pct": 0.0,
      "fecha_adquisicion": "",
      "fecha_transmision": ""
    }
  ],
  "antecedentes_registrales": {
    "inscripcion_numero": "",
    "conservador": "",
    "fecha_inscripcion": "",
    "rol_inmobiliario": ""
  },
  "subdivisiones": [
    {
      "numero_lote": "",
      "superficie_m2": 0,
      "rol": ""
    }
  ],
  "inmueble": {
    "numero_lote": "",
    "rol_lote": "",
    "direccion": {
      "calle": "",
      "numero": "",
      "comuna": "",
      "ciudad": "",
      "otros": ""
    },
    "superficie_m2": 0,
    "superficie_ha": 0.0,
    "limites": {
      "norte": "",
      "sur": "",
      "este": "",
      "oeste": ""
    }
  },
  "cargas_gravamenes": [
    {
      "tipo": "",
      "monto": 0,
      "moneda": "",
      "acreedor": "",
      "fecha": "",
      "estado": ""
    }
  ],
  "servidumbres_limitaciones": [
    {
      "tipo": "",
      "beneficiario": "",
      "fecha": "",
      "detalle": ""
    }
  ],
  "otros_datos_relevantes": {
    "fecha_estudio": "",
    "notario": "",
    "protocolo": "",
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
    resultado = handle_hipotecarios("C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/informe de titulos GALLARDO JIMENEZ_resultado_paginas.json")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
