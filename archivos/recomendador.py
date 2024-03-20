import streamlit as st
from funciones.funciones import *
from funciones.funcionesGastronomia import *




def mostrar_recomendador():
    escribeTitulo("Proyecto Gastronomia : ",'center')
    espacio(4)
    escribeSubTitulo("Proyecto de Clustering, Recomendación y Predicción de Ratings para Restaurantes",'center')
    espacio(2)
   

    escribeSubSubTitulo("Clustering de Restaurantes en Madrid",'center')
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Se aplican técnicas de clustering utilizando el algoritmo DBSCAN y KMeans para agrupar restaurantes en Madrid. 
    Los distintos clusters se forman en base a diversas características, principalmente el tipo de cocina, y se diferencian
    principalmente por el rango de precios. Esta parte del proyecto ofrece una visión estructurada de la diversidad de 
    restaurantes en la ciudad y a quién van dirigidos.
    </div>
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(3)

    escribeSubSubTitulo("Recomendadores de Restaurantes",'center')
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Desarrollamos dos recomendadores de restaurantes, uno centrado en Madrid y otro en México, 
    mediante una aplicación web interactiva creada con la biblioteca Streamlit. Estos recomendadores se basan en las puntuaciones 
    que los usuarios otorgan a una serie de restaurantes. Utilizando esta información, el sistema recomienda otros restaurantes similares en 
    función de sus características. Esta funcionalidad proporciona a los usuarios sugerencias personalizadas basadas en sus preferencias gastronómicas. 
    El recomendador de México inlcuye una nuevo algoritmo de recomendacion creado por el equipo.
    </div>
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(3)


    escribeSubSubTitulo("Modelo Predictivo de Ratings",'center')
    espacio(1)
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Implementamos un modelo predictivo para estimar las calificaciones de los restaurantes según las revisiones proporcionadas por los usuarios. Logramos una tasa de predicción de más del 50%, lo que proporciona información valiosa sobre cómo los usuarios evalúan diferentes restaurantes.
    Este proyecto refleja nuestro interés en explorar y aplicar técnicas de aprendizaje no supervisado, recomendación y predicción en el contexto de la industria de restaurantes, brindando perspectivas útiles y soluciones prácticas.
    </div>
    """
    st.markdown(texto,unsafe_allow_html=True)

    espacio(5)
    escribeTexto("Comparto los resultados obtenidos mediante una presentación: ")
   
 
    if "indice_diapositiva2" not in st.session_state:
        st.session_state.indice_diapositiva2 = 0
    col1,col2,col3 = st.columns([0.2,1.2,0.2])
    with col1:
        # Botón "Anterior"
        if st.button("Anterior") and st.session_state.indice_diapositiva2 > 0:
            st.session_state.indice_diapositiva2 -= 1
    with col2:
        # Botón "Siguiente"
        if st.button("Siguiente") and st.session_state.indice_diapositiva2 < len(imagenes_diapositivas) - 1:
            st.session_state.indice_diapositiva2 += 1

    # Mostrar la diapositiva actual
    mostrar_diapositiva(st.session_state.indice_diapositiva2)








