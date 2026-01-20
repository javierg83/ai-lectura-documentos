# ai_extractor_pdf.py

import base64
import time
from datetime import datetime
import os
from image_filters import enhance_image_contrast  # NUEVO: mejora binarización imagen
from pdf_utils import extract_page_image
from services.ai_engine.factory import AIProviderFactory
from services.ai_engine.prompt_loader import PromptLoader

# Ruta al prompt externalizado
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "prompts", "extraction", "pdf_page_analysis_v1.txt")

# Contador global de llamadas (para debug)
_request_count = 0

def analyze_page_with_gpt(pdf_path: str, page_number: int, timeout: float = 60.0, enhance_contrast: bool = True):
    """
    Envía la página completaa una IA Vision (OpenAI/Gemini/etc).
    Retorna: elementos (lista), raw (JSON limpio), tokens_in, tokens_out.
    """
    global _request_count
    _request_count += 1

    print(f"\n[Extractor] ({_request_count}) → {datetime.now():%H:%M:%S} "
          f"Iniciando análisis de página {page_number+1} de '{pdf_path}'")

    # 1) Extraer imagen original
    img_bytes = extract_page_image(pdf_path, page_number)
    print(f"[Extractor]   • Imagen original obtenida (bytes={len(img_bytes)})")

    # 2) Mejorar contraste visual (binarización)
    if enhance_contrast:
        img_bytes = enhance_image_contrast(img_bytes)
        print(f"[Extractor]   • Mejora de contraste aplicada (binarización adaptativa)")
    else:
        print(f"[Extractor]   • Mejora de contraste DESACTIVADA")

    # 3) Codificar a Base64
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')
    print(f"[Extractor]   • Imagen convertida a base64 (largo={len(img_b64)} caracteres)")
    
    # 4) Cargar Prompt y Configuración
    print(f"[Extractor]   • Cargando prompt de visión desde: {PROMPT_PATH}")
    config_dict, system_msg = PromptLoader.load_prompt(PROMPT_PATH)
    
    # Overrides dinámicos
    if timeout:
        config_dict["timeout"] = timeout

    print(f"[Extractor]   • Configuración IA: Engine={config_dict.get('engine')} | Model={config_dict.get('model')}")

    # 5) Instanciar Proveedor
    provider = AIProviderFactory.get_provider(config_dict)
    
    # 6) Ejecutar
    user_msg_text = f"Página {page_number+1}: analiza esta imagen."
    
    try:
        elementos, raw_response, t_in, t_out = provider.analyze_image(
            image_b64=img_b64,
            prompt=user_msg_text,
            system_prompt=system_msg,
            config=config_dict
        )
        
        print(f"[Extractor]   ✅ Análisis OK: elementos detectados = {len(elementos)}")
        if not elementos:
             print(f"[Extractor]   ⚠️  Advertencia: respuesta vacía en página {page_number+1}")
        else:
             tipos = set(el.get("tipo", "¿?") for el in elementos)
             print(f"[Extractor]   🔍 Tipos encontrados: {sorted(tipos)}")
             
        print(f"[Extractor]   • Tokens → in={t_in}, out={t_out}")
        
        return elementos, raw_response, t_in, t_out

    except Exception as e:
        print(f"[Extractor]   ✖ Error en llamada IA #{_request_count}: {e}")
        return [], "{}", 0, 0

if __name__ == "__main__":
    from utils.logger import setup_full_console_logging
    setup_full_console_logging()
    
    # Ejemplo de uso simple si se corre directo
    print("Corriendo extractor como script...")
    # analyze_page_with_gpt("ruta/al/pdf.pdf", 0)
