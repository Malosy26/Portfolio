import streamlit as st
from funciones.funciones import * 




def mostrar_ecoMovilidad():
    escribeTitulo("Proyecto EcoMovilidad",'center')
    espacio(2)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    El proyecto EcoMovilidad tiene varios objetivos que desglosaremos a continuación, explicando cada una de las pestañas de nuestra página web.
    </div>
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(4)
    escribeSubTitulo("EcoInicio",'left')
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Al abrir nuestra página, encontrarás esta pestaña inicial que proporciona una introducción al proyecto, sus objetivos y los temas que se tratarán.
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(4)
    escribeSubTitulo("EcoMovilidad",'left')
    escribeTexto("La pestaña con mayor contenido es donde podremos ver el contenido del proyecto en sí. Se divide en tres pestañas, las cuales explicaremos a continuación: ")
    espacio(1)
    escribeSubSubTitulo("EcoEstudio",'left')
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    En la pestaña EcoEstudio, encontrarás un análisis de los vehículos de nuestra base de datos. El propósito es conocer más sobre los tipos de vehículos en nuestra base de datos y sus características. De esta manera, si el usuario está pensando en cambiar de vehículo, podrá conocer las características de los diferentes tipos de vehículos y tomar una decisión más informada.
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(1)
    escribeSubSubTitulo("EcoViaje",'left')
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    La aplicación principal tiene varias funciones interactivas con el cliente. La primera es un comparador de vehículos donde al usuario se le permite elegir un vehículo de cada tipo (híbridos, eléctrico puro, gasolina y diésel) a partir de las  características que elija. Se realiza una comparativa del consumo y las emisiones.
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    La siguiente función es una aplicación con un mapa interactivo. El usuario introduce el código postal y un radio en kilómetros y elige si desea visualizar las gasolineras cercanas o los puntos de carga. Al hacer clic en el mapa, se muestran las características del punto de carga seleccionado, los modelos admitidos, su precio y un índice necesario para la siguiente funcionalidad.
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Finalmente, una vez que el usuario ha elegido un punto de carga, deberá introducir el índice del mismo y los kilómetros que desea recorrer. Se mostrará por pantalla el precio de la carga en función de los kilómetros seleccionados. Además, se utiliza la selección del usuario de los cuatro vehículos comparados para calcular el costo de recorrer esos mismos kilómetros con los diferentes vehículos preseleccionados. Se proporciona un precio de la gasolina para los híbridos y para los vehículos de gasoil y gasolina. Este precio se obtiene mediante una predicción que realizamos en la pestaña EcoHistórico, la cual se explicará a continuación.
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(1)
    escribeSubSubTitulo("EcoHistórico",'left')
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Esta pestaña se centra en el estudio de las fluctuaciones en el precio del gasoil y la gasolina. En primer lugar, se presenta un gráfico que muestra estas fluctuaciones. Posteriormente, se identifican y explican los momentos más destacados de estas variaciones. Finalmente, se utiliza el entrenamiento de modelos predictivos basados en redes neuronales utilizando series temporales. Se muestran las métricas del modelo obtenidas y se analizan. A través de la entrada de datos del usuario, que puede introducir el precio de la gasolina y/o del gasoil, se muestra el precio predicho para la próxima semana según el modelo.

    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(2)
    escribeSubTitulo("EcoFaqs y EcoEncuesta",'left')
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
   En EcoFaqs encontrarás las preguntas frecuentes que el usuario pueda tener, presentadas de manera desplegable para que puedas visualizar las respuestas fácilmente.
   En EcoEncuesta, se realiza una encuesta con el objetivo de informar al usuario si posee los conocimientos adecuados sobre la contaminación actual. Al finalizar la encuesta, se muestran emoticonos en pantalla, tanto si se responde correctamente como si no.
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(2)
    escribeTexto("A continuación les dejo el enlace de la pagina cabe destacar que también tienes un boton para cambiar la página a ingles:")
    espacio(1)
    st.markdown("[ecomovilidad.streamlit.app](https://ecomovilidad.streamlit.app)")
   





    
    