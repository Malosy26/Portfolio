import streamlit as st
from funciones.funciones import *
from funciones.funMonedas import *
opciones = [
    'AUD Australian Dollar',
    'BGN Bulgarian Lev',
    'BRL Brazilian Real',
    'CAD Canadian Dollar',
    'CHF Swiss Franc',
    'CNY Chinese Renminbi Yuan',
    'CZK Czech Koruna',
    'DKK Danish Krone',
    'EUR Euro',
    'GBP British Pound',
    'HKD Hong Kong Dollar',
    'HUF Hungarian Forint',
    'IDR Indonesian Rupiah',
    'ILS Israeli New Sheqel',
    'INR Indian Rupee',
    'ISK Icelandic Króna',
    'JPY Japanese Yen',
    'KRW South Korean Won',
    'MXN Mexican Peso',
    'MYR Malaysian Ringgit',
    'NOK Norwegian Krone',
    'NZD New Zealand Dollar',
    'PHP Philippine Peso',
    'PLN Polish Złoty',
    'RON Romanian Leu',
    'SEK Swedish Krona',
    'SGD Singapore Dollar',
    'THB Thai Baht',
    'TRY Turkish Lira',
    'USD United States Dollar',
    'ZAR South African Rand'
]



def monedas():
    escribeTitulo("Conversion de Monedas",'center')
    espacio(1)
    escribeTexto("A continuación expondré un ejercicio de conversión de monedas. Se utiliza una api para la obtención de los datos. En este primer ejemplo va a elegir dos monedas y obtendra un gráfico comparativo entre las dos.")

    col1,col2 = st.columns(2)
    with col1:
        seleccion1 = st.selectbox("Seleccione la moneda principal",opciones)
    with col2:
        seleccion2 = st.selectbox("Seleccione la moneda para realizar la comparativa",opciones)
    cantidad = st.slider('Seleccione la cantidad a convertir :',1,50,1 )
    if seleccion1 == seleccion2:
        st.error("Por favor seleccione dos monedas diferentes")
    else:
        conversion(seleccion1,seleccion2,cantidad)