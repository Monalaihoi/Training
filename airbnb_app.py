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

#defining side bar
st.sidebar.header("Filters:")

#placing filters in the sidebar using unique values.
neighbourhood = st.sidebar.multiselect(
    "Select Neighbourhood:",
    options=data["neighbourhood"].unique(),
    default=data["neighbourhood"].unique()
)
#placing filters in the sidebar using unique values.
room_type = st.sidebar.multiselect(
    "Select room_type:",
    options=data["room_type"].unique(),
    default=data["room_type"].unique()
)
# Imprimir los valores únicos de la columna 'minimum_nights'
print(data['minimum_nights'].unique())
#print(data.columns)

def get_minimum_nights_group(nights):
    """Function for generating minimum nights grouping based on number of nights."""
    if 1 <= nights <= 5:
        return "1 to 5 nights"
    elif 6 <= nights <= 14:
        return "6 to 14 nights"
    elif 15 <= nights <= 30:
        return "15 to 30 nights"
    elif 31 <= nights <= 90:
        return "30 to 90 nights"
    else:
        return "Over 90 nights"

# Aplicar la función a la columna 'minimum_nights' y crear una nueva columna 'nights_group'
data['minimum_nights_group'] = data['minimum_nights'].apply(get_minimum_nights_group)

# Ahora puedes ver los resultados
print(data[['minimum_nights', 'minimum_nights_group']])

#taking the filtered dataframe created in a previous step and applying a query
df_selection = data.query(
    "`neighbourhood`== @neighbourhood & `room_type` == @room_type"
)

#defining our metrics
total_apartments = df_selection["id"].value_counts().sum()
nights_5 = df_selection[df_selection["minimum_nights_group"]=="1 to 5 nights"].value_counts().sum()
nights_15 = df_selection[df_selection["minimum_nights_group"]=="6 to 14 nights"].value_counts().sum()
nights_30 = df_selection[df_selection["minimum_nights_group"]=="15 to 30 nights"].value_counts().sum()
nights_90 = df_selection[df_selection["minimum_nights_group"]=="30 to 90 nights"].value_counts().sum()
nights_100 = df_selection[df_selection["minimum_nights_group"]=="Over 90 nights"].value_counts().sum()

#placing our metrics within columns in the dashboard
col1,col2,col3,col4,col5,col6=st.columns(6)
col1.metric(label="Total Apartments",value=total_apartments)
col2.metric(label="1 to 5 nights",value=nights_5)
col3.metric(label="6 to 14 nights",value=nights_15)
col4.metric(label="15 to 30 nights",value=nights_30)
col5.metric(label="30 to 90 nights",value=nights_90)
col6.metric(label="Over 90 nights",value=nights_100)

#a dividing line
st.divider()

st.header('Casas Airbnb en Madrid')

st.map(data, zoom=10)

