import cv2
import numpy as np
from PIL import Image
from io import BytesIO

def enhance_image_contrast(image_bytes: bytes) -> bytes:
    """
    Convierte la imagen a blanco y negro binarizado para mejorar el contraste.
    Ideal para mejorar lectura OCR/visión de tablas sin bordes definidos.
    """
    # Cargar imagen en escala de grises
    pil_img = Image.open(BytesIO(image_bytes)).convert('L')
    np_img = np.array(pil_img)

    # Aplicar umbral adaptativo para binarización
    img_thresh = cv2.adaptiveThreshold(
        np_img,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY,
        blockSize=15,  # Debe ser impar. Prueba también 11 o 17
        C=10           # Constante que ajusta el umbral local
    )

    # Convertir de nuevo a PNG en memoria
    pil_out = Image.fromarray(img_thresh)
    buffer = BytesIO()
    pil_out.save(buffer, format="PNG")
    return buffer.getvalue()
