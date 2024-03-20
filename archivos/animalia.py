import streamlit as st
from funciones.funciones import *
from funciones.funcionesAnimalia import *



def mostrar_proyecto1():
    escribeTitulo("Proyecto Animalia",'Center')
    # escribeTexto("El proyecto Animalia es un proyecto de un estudio científico sobre las características de los diferentes tipos de animales de nuestra base de datos.")
    # escribeTexto("Características como su taxonomia ,habitat ,principales ,amenazas para su especie, pelaje,genes ect. El estudio en si es bastante extenso. ")
    # escribeTexto("Por lo que voy a explicar los desafios a los que nos enfrentamos y luego mostrare los resultados.")
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    El proyecto Animalia es un proyecto de un estudio científico sobre las características de los diferentes tipos de animales de nuestra base de datos. Características como su taxonomia ,habitat principales amenazas para su especie, pelaje,genes ect. El estudio en si es bastante extenso.
    Por lo que voy a explicar los desafios a los que nos enfrentamos y luego mostrare los resultados.


    </div>
    """
    st.markdown(texto,unsafe_allow_html=True)
    espacio(3)
    escribeSubTitulo("Principales desafios:",'center')
    espacio(2)
    escribeTexto("- Adquisición de los datos:")
    texto ="""
    <div style='text-align: justify; font-size: 18px;'>
    Para la adquisición de los datos utilizamos varias Apis, debido a el máximo de datos posibles por petición y la forma en la que podían extraer,
    tuvimos que improvisar para poder adquirir todos los datos de la base, la petición respondia por letras por lo que hicimos un bucle para 
    extraer toda la informacion guardandola en un nuevo df y en paralelo a un set para que si en el set ya estaba ese animal no volver a incluirlo en el df.
    </div>"""
    st.markdown(texto,unsafe_allow_html=True)
    espacio(1)
    escribeTexto("- Transformación  de los datos:")
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Esta parte se llevó la mayoría de horas del proyecto. Una vez formado el dataframe completo, procedimos a separarlo por categorías del reino animal. 
    El resultado fueron 4 dataframes. Para no explayarnos mucho, voy a comentar lo que, a mi parecer, fue lo más complicado.<br>
    </div>
    <div style='text-align: justify; font-size: 18px;'>
    Primero, al tener datos de diferentes fuentes, existían columnas con valores NaN, por lo que tuvimos que elegir las columnas con los datos que nos interesaban y limpiarlas.
    Luego, tuvimos que enfrentarnos a formatear las columnas con unidades para que estuvieran en la misma unidad. Os pongo un ejemplo: <br>
    </div>
    <div style='text-align: justify; font-size: 18px;'>
    En la columna de peso y altura, algunas venían con texto, otras con unidades, otras con la combinación de ambas y, por supuesto, en diferentes unidades de medida.
    Por lo que utilizar comandos regex y filtros fue una ardua tarea para conseguir que todos los datos estuvieran en la misma unidad.<br>
    </div>
    <div style='text-align: justify; font-size: 18px;'>
    Y como último ejemplo, la columna de amenazas o pérdida y de hábitat. Estas venían siempre en texto, pero algunas tenían solo datos de una amenaza o de un hábitat,
    mientras que otras tenían dos o tres datos con diferente formato. Todo esto, viniendo de lo ya comentado, supuso un aprendizaje extenso en la conversión de datos.
    </div>
"""
    st.markdown(texto, unsafe_allow_html=True)
    espacio(2)
    escribeTexto("- ¿Que datos queremos mostrar y con que tipo de gráficas? ")
    texto = """
    <div style='text-align: justify; font-size: 18px;'>
    Finalmente, llegó el momento de exponer los datos y las conclusiones. Como analistas, aspirábamos a presentar gráficamente las características y extraer conclusiones precisas de las mismas. Sin embargo, la tarea no resultó tan sencilla debido a la alta complejidad de los datos. Tuvimos que adquirir conocimientos sobre características de las cuales no teníamos previamente conocimiento. Pero, con mucho trabajo, estudio y esfuerzo, creo que logramos plasmar adecuadamente el contenido que teníamos, adaptándonos para alcanzar nuestra meta.
    </div>
"""

    st.markdown(texto, unsafe_allow_html=True)
    espacio(4)
    # escribeTexto("Os dejo el enlace para que la visualizacion de la presentación del proyecto y sus conclusiones.")
    # link = "[Haz clic aquí para ver la presentación](https://es.slideshare.net/DanielVillaRayo/proyectoestudiodeanimalespptx)"
    # st.markdown(link, unsafe_allow_html=True)
    escribeTexto("Os muestro la presentación del trabajo realizado: ")
    espacio(3)
    
    col1,col2,col3 = st.columns([0,2,1,0,2])
    if "indice_diapositiva" not in st.session_state:
        st.session_state.indice_diapositiva = 0
    with col1:
        # Botón "Anterior"
        if st.button("Anterior") and st.session_state.indice_diapositiva > 0:
            st.session_state.indice_diapositiva -= 1
    with col3:
        # Botón "Siguiente"
        if st.button("Siguiente") and st.session_state.indice_diapositiva < len(imagenes_diapositivas) - 1:
            st.session_state.indice_diapositiva += 1

    # Mostrar la diapositiva actual
    mostrar_diapositiva(st.session_state.indice_diapositiva)




