import os
import sys
from services.ai_engine.factory import AIProviderFactory
from services.ai_engine.prompt_loader import PromptLoader
import config

# Mock configs regarding API keys if they are not set, just to test factory logic
# (Assuming user has keys set in env or config, but we can catch errors)

def test_prompt_loader():
    print("--- Testing PromptLoader ---")
    prompt_path = os.path.join("services", "semantic_extraction", "prompts", "items_licitacion", "prompt_items_licitacion_v1.txt")
    if not os.path.exists(prompt_path):
        print(f"❌ Prompt file not found: {prompt_path}")
        return

    try:
        conf, text = PromptLoader.load_prompt(prompt_path)
        print(f"✅ Loaded prompt: {prompt_path}")
        print(f"   Config: {conf}")
        print(f"   Text length: {len(text)}")
        if "engine" in conf:
            print(f"   Engine found: {conf['engine']}")
        else:
             print("❌ 'engine' not found in config")
    except Exception as e:
        print(f"❌ Error loading prompt: {e}")

def test_factory():
    print("\n--- Testing AIProviderFactory ---")
    
    # Test OpenAI instantiation
    try:
        if not config.OPENAI_API_KEY:
            config.OPENAI_API_KEY = "sk-mock-key" # Mock for factory test if not present
            
        print("Attempting to create OpenAI provider...")
        provider_openai = AIProviderFactory.get_provider({"engine": "openai"})
        print(f"✅ OpenAI Provider created: {type(provider_openai).__name__}")
    except Exception as e:
        print(f"❌ Error creating OpenAI provider: {e}")

    # Test Gemini instantiation
    try:
        if not config.GEMINI_API_KEY:
             config.GEMINI_API_KEY = "mock-key"
             
        print("Attempting to create Gemini provider...")
        provider_gemini = AIProviderFactory.get_provider({"engine": "gemini"})
        print(f"✅ Gemini Provider created: {type(provider_gemini).__name__}")
    except Exception as e:
        print(f"❌ Error creating Gemini provider: {e}")

if __name__ == "__main__":
    test_prompt_loader()
    test_factory()
