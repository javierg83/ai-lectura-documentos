print("✅ Script iniciado correctamente")

from services.semantic_extraction.extractors.items_licitacion.items_licitacion_extractor import ItemsLicitacionExtractor

contexto_manual = """
ADQUISICION DE ESTANQUE MAS BOMBA CENTRIFUGA Y KIT DE INSTALACION.
Se requiere la adquisición de un estanque vertical para ser posicionado en la cancha de la localidad de la playa,
el estanque deberá contener una bomba de impulsión para abastecer la red de agua.
"""

if __name__ == "__main__":
    print("🚀 Entrando a ejecución principal (__main__)")

    extractor = ItemsLicitacionExtractor(licitacion_id="test-123")

    print("🧱 Construyendo prompt...")
    prompt = extractor.build_prompt(context=contexto_manual, licitacion_id="test-123")
    print("\n====== PROMPT FINAL ENVIADO A LLM ======\n")
    print(prompt[:3000])

    print("\n====== EJECUTANDO LLM ======")
    try:
        from services.llm_service import run_llm_raw
        raw_output = run_llm_raw(prompt)
    except Exception as e:
        print(f"[❌ ERROR LLM] {e}")
        exit(1)

    print("\n====== RESPUESTA CRUDA DEL MODELO ======\n")
    print(raw_output)

    print("\n====== PARSEANDO SALIDA ======\n")
    try:
        resultado = extractor.parse_output(raw_output)
        import json
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"[❌ ERROR PARSEANDO SALIDA] {e}")
