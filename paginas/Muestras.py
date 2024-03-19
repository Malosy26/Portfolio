import streamlit as st
from archivos.monedas import *
from archivos.creditos import *
from archivos.animalia import *
from archivos.recomendador import *
from archivos.ecoMovilidad import *




def Muestras():

    seleccion = st.sidebar.selectbox("Eliga la opción que desea ver: ",["ConversiónMonedas","MLCrédito","Animalia","Gastronomia","EcoMovilidad"])

    if seleccion == "ConversiónMonedas":
        monedas()
    elif seleccion == "MLCrédito":
        mostrar_creditos()
    elif seleccion == "Animalia":
        mostrar_proyecto1()
    elif seleccion == 'Gastronomia':
        mostrar_recomendador()
    elif seleccion == "EcoMovilidad":
        mostrar_ecoMovilidad()

    
    