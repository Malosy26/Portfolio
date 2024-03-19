import streamlit as st
from funciones.funciones import *
from paginas.SobreMi import *
from paginas.Muestras import *


st.set_page_config(layout = "wide")

def main():
   
    # st.sidebar.markdown("Paginas del portafolio : ")
    seleccion_pagina = st.sidebar.radio(label=" Paginas del Portfolio", options = ["SobreMi","Proyectos"])

    if seleccion_pagina == "SobreMi":
        SobreMi()
    elif seleccion_pagina == "Proyectos":
        Muestras()


    












if  __name__ == "__main__":
    main()
