import streamlit as st
from funciones.funciones import *
from PIL import Image


def SobreMi():
    colbeg1,colbeg2,colbeg3 =st.columns(3)
    with colbeg1:
        st.markdown("<span style='display: block; text-align: left; font-size: 50px; font-weight: bold; margin: 0; padding-left: 0;'>SobreMi</span>", unsafe_allow_html=True)
        espacio(6)
        foto_python = Image.open("imagenesSobreMi/python.png")
        st.image(foto_python,width = 200)
    with colbeg2:
        espacio(9)
        foto_st = Image.open("imagenesSobreMi/streamlit.png")
        st.image(foto_st,use_column_width=True)

    with colbeg3:
        foto_dani = Image.open("imagenesSobreMi/foto_dani.png")
        st.image(foto_dani,width = 300)
    espacio(4)
    col1,col2,col3 = st.columns([0.5,0.85,1])
    
    with col1:
        st.markdown("<span style='display: block; text-align: left; font-size: 40px; font-weight: bold; margin: 0; padding-left: 0;'>Daniel Villa </span>", unsafe_allow_html=True)
        st.markdown("<span style='display: block; text-align: left; font-size: 30px; font-weight: bold; margin: 0; padding-left: 0;'>Cientifico de Datos</span>", unsafe_allow_html=True)  
    
    
    with col2:
        st.markdown("<span style='display: block; text-align: left; font-size: 30px; font-weight: bold; margin: 0; padding-left: 0;'>Redes Sociales y correo</span>", unsafe_allow_html=True)
        
        colaux1,colaux2 = st.columns([0.2,0.8])
        with colaux1:
            foto_linkdn = Image.open("imagenesSobreMi/linkdncolor1.png")
            st.image(foto_linkdn,width = 50 )
            espacio(1)
            foto_correo = Image.open ("imagenesSobreMi/gmail1.png")
            st.image(foto_correo, width = 50 )
            espacio(1)
            foto_gitlab = Image.open ("imagenesSobreMi/gitlab1.png")
            st.image(foto_gitlab, width = 50 )
            espacio(1)
            foto_github = Image.open ("imagenesSobreMi/github1.png")
            st.image(foto_github, width = 50 )


        with colaux2:
           st.write("https://www.linkedin.com/in/dvr0001/")
           espacio(4)
           st.write ("danielvillarayo@gmail.com")
           espacio(3)
           st.write("https://gitlab.com/danielvillarayo/RepositorioDeMuestras")
           espacio(3)
           st.write("https://github.com/Malosy26/Repositorio-de-Muestras")
        
    
    
    
    
    with col3:
        st.markdown(" ")
        texto = """
                    <div style='text-align: justify;font-size:22px'>
                    ¡Hola, soy Daniel!

                """

            
        st.markdown(texto, unsafe_allow_html=True)
        st.markdown(" ")
        texto = """
                    <div style='text-align: justify;font-size:18px'>
                Un apasionado de la programación. Comencé con microcontroladores y ensamblador, luego exploré C y Java, 
                donde aprendí programación orientada a objetos. 
                Ahora estoy inmerso en Python, un lenguaje versátil y poderoso. Desde el desarrollo web hasta la ciencia de datos,
                Python me ofrece un mundo de posibilidades. Siempre estoy buscando nuevos desafíos y oportunidades para crecer como programador.


                """

            
        st.markdown(texto, unsafe_allow_html=True)
    espacio(10)
    st.markdown("<span style='display: block; text-align: center; font-size: 30px; font-weight: bold; margin: 0; padding-left: 0;'>Librerías de Python con las que tengo experiencia</span>", unsafe_allow_html=True)
    espacio(4)
    col5,col6,col7 = st.columns([0.2,0.5,0.5])
    
    with col6:
        foto_machine_learning = Image.open("imagenesSobreMi/Beutiful1.png")
        st.image(foto_machine_learning,width = 200)
        espacio(1)
        foto_matplotlib = Image.open("imagenesSobreMi/matplotlib1.png")
        st.image(foto_matplotlib,width = 200)
        espacio(1)
        foto_sql = Image.open("imagenesSobreMi/sql1.png")
        st.image(foto_sql,width = 200)
        espacio(1)
        foto_tf = Image.open("imagenesSobreMi/tensorflow1.png")
        st.image(foto_tf,width = 200)
    with col7: 
        foto_numpy = Image.open("imagenesSobreMi/numpy.png")
        st.image(foto_numpy,width = 200)
        espacio(1)
        foto_pandas = Image.open("imagenesSobreMi/pandas1.png")
        st.image(foto_pandas,width = 200)
        espacio(1)
        foto_pyspark = Image.open("imagenesSobreMi/pyspark1.png")
        st.image(foto_pyspark,width = 200)
        espacio(1)
        foto_ml = Image.open("imagenesSobreMi/machinelearning.png")
        st.image(foto_ml,width = 200)
        espacio(1)



    #     espacio(3)
    #     st.write("La librería BeautifulSoup en Python se utiliza para extraer datos de archivos HTML y XML, permitiendo el análisis y la manipulación de estos datos de manera sencilla.")
    #     espacio(6)
    #     st.write("NumPy es una librería de Python que proporciona soporte para grandes matrices y arrays multidimensionales, junto con una amplia colección de funciones matemáticas de alto rendimiento para operar con estos arrays.")
    #     espacio(3)
    #     st.write("Matplotlib es una librería de Python que permite la creación de gráficos en dos dimensiones, ofreciendo una amplia gama de formatos y personalizaciones.")
    #     espacio(5)
    #     st.write("Pandas es una librería de Python que proporciona estructuras de datos potentes y flexibles diseñadas para trabajar con datos estructurados de manera eficiente.")
    #     espacio(4)
    #     st.write ("MySQL Connector es una librería de Python que permite a los programas de Python acceder a las bases de datos MySQL mediante una API que cumple con la especificación de la API de la base de datos de Python. ")
    #     espacio(5)
    #     st.write("PySpark es una biblioteca de Python que permite el procesamiento de grandes conjuntos de datos utilizando Apache Spark y su capacidad de computación distribuida.")
    #     espacio(4)
    #     st.write ("Scikit-learn (o sklearn) es una librería de Python que se utiliza ampliamente para el aprendizaje automático. Proporciona una variedad de algoritmos para modelos supervisados (como clasificación y regresión) y no supervisados (como clustering). Además, sklearn ofrece una serie de métricas para evaluar la precisión y el rendimiento de los modelos entrenados. También proporciona herramientas para el preprocesamiento de datos, la selección de características, y la optimización de parámetros, entre otras funcionalidades.") 
    #     espacio(6)
    #     st.write("TensorFlow es una librería de Python que se utiliza principalmente para programar sistemas de aprendizaje automático y redes neuronales de manera eficiente. Permite a los desarrolladores crear modelos de aprendizaje profundo, que son una clase de modelos de aprendizaje automático que utilizan redes neuronales con muchas capas.")