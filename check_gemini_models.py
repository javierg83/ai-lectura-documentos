import google.generativeai as genai
import os
from dotenv import load_dotenv

# Re-load env vars just in case
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in environment.")
else:
    genai.configure(api_key=api_key)
    print("✅ GEMINI_API_KEY found. Listing models...")
    with open("available_models.txt", "w", encoding="utf-8") as f:
        try:
            count = 0
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    print(f"- {m.name}")
                    f.write(f"{m.name}\n")
                    count += 1
            if count == 0:
                print("⚠️ No models found with 'generateContent' support.")
                f.write("No models found.\n")
        except Exception as e:
            print(f"❌ Error listing models: {e}")
            f.write(f"Error: {e}\n")
