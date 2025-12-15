import io
from PIL import Image
import pytesseract


def image_to_text(image_bytes: bytes, lang: str = 'spa') -> str:
    img = Image.open(io.BytesIO(image_bytes))
    return pytesseract.image_to_string(img, lang=lang)