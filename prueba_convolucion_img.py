import cv2
import numpy as np

def rgb_to_gray_manual(img_bgr: np.ndarray) -> np.ndarray:
    """
    Convierte una imagen BGR a escala de grises usando combinación lineal:
        Gray = 0.299 R + 0.587 G + 0.114 B
    """
    b = img_bgr[:, :, 0].astype(np.float32)
    g = img_bgr[:, :, 1].astype(np.float32)
    r = img_bgr[:, :, 2].astype(np.float32)

    gray = 0.299 * r + 0.587 * g + 0.114 * b
    return np.clip(gray, 0, 255).astype(np.uint8)

def convolve2d_gray(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Aplica convolución 2D a imagen en escala de grises usando filtro manual.
    """
    image = image.astype(np.float32)
    kernel = kernel.astype(np.float32)

    img_h, img_w = image.shape
    k_h, k_w = kernel.shape

    kernel_flipped = np.flipud(np.fliplr(kernel))

    pad_h = k_h // 2
    pad_w = k_w // 2

    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode="reflect")
    output = np.zeros_like(image, dtype=np.float32)

    for i in range(img_h):
        for j in range(img_w):
            region = padded[i:i + k_h, j:j + k_w]
            output[i, j] = np.sum(region * kernel_flipped)

    return np.clip(output, 0, 255).astype(np.uint8)


if __name__ == "__main__":

    # --- Ruta de imagen (ajusta el nombre del archivo si cambia) ---
    image_path = r"C:\Desarrollo\IA\Proyectos\ai-lectura-documentos\Imagenes Ejemplo Convolucion\pag2.jpg"

    # --- Salidas ---
    output_gray = r"C:\Desarrollo\IA\Proyectos\ai-lectura-documentos\Imagenes Ejemplo Convolucion\salida_gris.png"
    output_conv = r"C:\Desarrollo\IA\Proyectos\ai-lectura-documentos\Imagenes Ejemplo Convolucion\salida_convolucion.png"

    # --- Cargar imagen ---
    img_color = cv2.imread(image_path)
    if img_color is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {image_path}")

    # --- Convertir a gris ---
    img_gray = rgb_to_gray_manual(img_color)

    # --- Kernel de convolución (realce / bordes) ---
    kernel = np.array([
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ], dtype=np.float32)

    # --- Aplicar convolución ---
    img_gray_conv = convolve2d_gray(img_gray, kernel)

    # --- Guardar imágenes ---
    cv2.imwrite(output_gray, img_gray)
    cv2.imwrite(output_conv, img_gray_conv)

    print("Procesamiento completado.")
    print(f"Imagen gris guardada en: {output_gray}")
    print(f"Imagen con convolución guardada en: {output_conv}")
