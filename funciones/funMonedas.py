import streamlit as st
import time
from datetime import datetime
import requests
from pprint import pprint
import plotly.express as px
import pandas as pd


url = "https://api.frankfurter.app"

def conversion(seleccion1, seleccion2,cantidad):
    try:
        
        seleccion1 = seleccion1.split(" ")[0]
        seleccion2 = seleccion2.split(" ")[0]
     
        from_currency = seleccion1
        to_currency = seleccion2
        date_1 = '2023-01-01'
        cantidad = cantidad
        
        # Realizar la solicitud a la API de conversión de moneda
        endpoint = f"{url}/{date_1}..?amount={cantidad}&from={from_currency}&to={to_currency}"
        response = requests.get(endpoint)
        data = response.json()
        
        # Obtener las fechas y los valores de las tasas de cambio
        fechas = list(data['rates'].keys())
        fechas = sorted([datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas])
        monedasCon = [data['rates'][fecha.strftime("%Y-%m-%d")][seleccion2] for fecha in fechas]
        
        # Crear un DataFrame con los datos
        df = pd.DataFrame({'Fechas': fechas, seleccion2: monedasCon})
        
        # Encontrar el máximo y el mínimo
        max_index = monedasCon.index(max(monedasCon))
        min_index = monedasCon.index(min(monedasCon))
        max_fecha = fechas[max_index]
        min_fecha = fechas[min_index]
        
        # Crear el gráfico con Plotly Express
        fig = px.line(df, x='Fechas', y=seleccion2, title=f'Relación de {cantidad} {from_currency} : {cantidad} {to_currency} desde 01/01/2023 hasta {max(fechas).strftime("%d-%m-%Y")}')
        fig.add_scatter(x=[max_fecha], y=[max(monedasCon)], mode='markers', marker=dict(color='red', size=10), name=f"max: {max(monedasCon)}")
        fig.add_scatter(x=[min_fecha], y=[min(monedasCon)], mode='markers', marker=dict(color='blue', size=10), name=f"min: {min(monedasCon)}")
        
        # Configurar el eje x para mostrar el mes y el año
        fig.update_xaxes(
        tickmode='linear',
        tick0=0,
        dtick='M1',  # Intervalo de 1 mes
        tickformat='%b %Y'  # Formato de mes abreviado
                        )
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)
    
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")