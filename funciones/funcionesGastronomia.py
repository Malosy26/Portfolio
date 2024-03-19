import streamlit as st
from PIL import Image

# Ruta de la carpeta que contiene las imágenes de las diapositivas
ruta_carpeta = r"D:\bootcamp\Streamlit\Portafolio\imagenesGastronomia"

# Crear una lista con las rutas de todas las imágenes de las diapositivas
imagenes_diapositivas = [f"{ruta_carpeta}\\Diapositiva{i}.JPG" for i in range(1, 27)]

# Función para cargar y mostrar la imagen
def mostrar_diapositiva(indice):
    imagen = Image.open(imagenes_diapositivas[indice])
    st.image(imagen, caption=f"Diapositiva {indice+1}/{len(imagenes_diapositivas)}",use_column_width=True)
