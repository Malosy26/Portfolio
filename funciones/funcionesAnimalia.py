import streamlit as st
from PIL import Image
import os

# Ruta de la carpeta que contiene las imágenes de las diapositivas
ruta_carpeta = "imagenesAnimalia"

# Crear una lista con las rutas de todas las imágenes de las diapositivas
imagenes_diapositivas = [os.path.join(ruta_carpeta, f"Diapositiva{i}.JPG") for i in range(1, 68)]

# Función para cargar y mostrar la imagen
def mostrar_diapositiva(indice):
    imagen = Image.open(imagenes_diapositivas[indice])
    st.image(imagen, caption=f"Diapositiva {indice+1}/{len(imagenes_diapositivas)}", use_column_width=True)