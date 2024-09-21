import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

st.title('Análisis Interactivo de Datos de Venta de Vehículos Usados')

st.write('Esta aplicación permite explorar un conjunto de datos de vehículos usados en venta a través de dos gráficos interactivos: un histograma y un gráfico de dispersión. Usa los botones a continuación para generar los gráficos.')

if hist_button: # al hacer clic en el botón

            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

scatter_botton=st.button('Construir gráfico de dispersión')
if scatter_botton: # al hacer clic en el botón
            
            st.write('Creación de una gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig1 = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig1, use_container_width=True)
