# Data visualization
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

#Abrir csv
# 1. Leemos los datos de Airbnb
## Utilizar el path completo
data= pd.read_csv("C:/Users/Mona/Desktop/Data-analyysi/Training/madrid_airbnb_data_2023.csv")

# 2. Titulo general para la aplicacion
st.title("Datos de Airbnb de Madrid en 2023")

# 3. Barplot de precios promedios por barrio por tipo de habitacion
### Agrupamos el dataset por 'room_type', 'neighbourhood'
### Agrupacion con el metodo groupby
df_neigborhood = data.groupby(['neighbourhood', 'room_type']).price.mean().reset_index() # dataset grupado

# Titulo para grafico de barras
st.subheader("Precios promedios de Airbnb en barrios de Madrid durante 2023")

#Barplot Precios medios por barrio por tipo de habitación.
fig_bar = px.bar(df_neigborhood, x='neighbourhood', y='price', color='room_type', hover_name='room_type')
st.plotly_chart(fig_bar)

# Titulo para grafico de barras
st.subheader("Conteo inmuebles por barrio por tipo de habitacion en Madrid durante el ano 2023")

# 4. Countplot: conteo imuebles por barrio por tipo de habitacion
fig_count_plot = px.histogram(data, x='neighbourhood', color = 'room_type', hover_name='room_type')
st.plotly_chart(fig_count_plot)

