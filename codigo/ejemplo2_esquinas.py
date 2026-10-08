import os
import cv2
import numpy as np

# Nahum Flores NC 0065
# Obtener la ruta exacta del directorio donde está ESTE archivo de Python
directorio_actual = os.path.dirname(os.path.abspath(__file__))


ruta_imagen = os.path.join(directorio_actual, "../imagenes/nutria.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

# Verificar que la imagen exista
if imagen is None:
    print(f"Error: no se pudo cargar la imagen desde: {ruta_imagen}")
    print("Asegúrate de que 'venado.jpg' esté guardada en la misma carpeta que este script.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a tipo float32
gris_float = np.float32(gris)

# Detectar esquinas mediante Harris
esquinas = cv2.cornerHarris(gris_float, 2, 3, 0.04)

# Dilatar para hacer visibles las esquinas
esquinas = cv2.dilate(esquinas, None)

# Crear copia para dibujar resultados
resultado = imagen.copy()

# Umbral para identificar esquinas
umbral = 0.01 * esquinas.max()

# Marcar esquinas en rojo
resultado[esquinas > umbral] = [0, 0, 255]

# Mostrar resultados
cv2.imshow("vnutria 0065 Imagen original", imagen)
cv2.imshow("nutria 0065 Esquinas detectadas", resultado)

# Contar esquinas aproximadas
cantidad_esquinas = np.sum(esquinas > umbral)

print("Detección de esquinas terminada.")
print("Cantidad aproximada de puntos detectados:", cantidad_esquinas)

# Esperar una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Nahum Flores NC 0065")


import os
import cv2
import numpy as np

# Nahum Flores NC 0065
# Obtener la ruta exacta del directorio donde está ESTE archivo de Python
directorio_actual = os.path.dirname(os.path.abspath(__file__))

ruta_imagen = os.path.join(directorio_actual, "../imagenes/nutria.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

# Verificar que la imagen exista
if imagen is None:
    print(f"Error: no se pudo cargar la imagen desde: {ruta_imagen}")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a tipo float32
gris_float = np.float32(gris)

# Detectar esquinas mediante Harris
# Consejo: Subir 'blockSize' (de 2 a 3 o 4) también ayuda a detectar menos puntos
esquinas = cv2.cornerHarris(gris_float, 2, 3, 0.04)

# Dilatar para hacer visibles las esquinas
esquinas = cv2.dilate(esquinas, None)

# Crear copia para dibujar resultados
resultado = imagen.copy()

# --- CAMBIO PRINCIPAL ---
# Aumentamos el umbral para ser más estrictos.
# Un valor más alto (ej. 0.05 o 0.10) filtrará las esquinas débiles y reducirá la cantidad total de puntos.
umbral = 0.05 * esquinas.max()

# Marcar esquinas en rojo
resultado[esquinas > umbral] = [0, 0, 255]

# Mostrar resultados
cv2.imshow("nutria 0065 Imagen original", imagen)
cv2.imshow("nutria 0065 Esquinas detectadas", resultado)

# Contar esquinas aproximadas
cantidad_esquinas = np.sum(esquinas > umbral)

print("Detección de esquinas terminada.")
print("Cantidad aproximada de puntos detectados:", cantidad_esquinas)

# Esperar una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Nahum Flores NC 0065")


import os
import cv2
import numpy as np

# Nahum Flores NC 0065
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(directorio_actual, "../imagenes/nutria.jpg")

imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print(f"Error: no se pudo cargar la imagen desde: {ruta_imagen}")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 1. Aplicar un filtro Blur para eliminar ruido fino y texturas
gris_suave = cv2.GaussianBlur(gris, (5, 5), 0)

gris_float = np.float32(gris_suave)

# 2. Aumentar blockSize (de 2 a 5) para tomar áreas más grandes
esquinas = cv2.cornerHarris(gris_float, 5, 3, 0.04)

esquinas = cv2.dilate(esquinas, None)
resultado = imagen.copy()

# 3. Subir drásticamente el umbral (de 0.01/0.05 a 0.15)
umbral = 0.15 * esquinas.max()

# Marcar esquinas en rojo
resultado[esquinas > umbral] = [0, 0, 255]

cv2.imshow("nutria 0065 Imagen original", imagen)
cv2.imshow("nutria 0065 Esquinas detectadas", resultado)

cantidad_esquinas = np.sum(esquinas > umbral)

print("Detección de esquinas terminada.")
print("Cantidad aproximada de puntos detectados:", cantidad_esquinas)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Nahum Flores NC 0065")