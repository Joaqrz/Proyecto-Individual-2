import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static

#Traigo el dataset hechos fatales
homicidios = pd.DataFrame(pd.read_csv('hechos_fatales.csv'))

#Título del mapa
st.title("Mapa interactivo de CABA")
# Obtener las opciones únicas de la columna COMUNA y ordenarlas
opciones_comunas = sorted(homicidios['COMUNA'].unique())

# Mostrar el widget multiselect con las opciones ordenadas
comunas_seleccionadas = st.multiselect("Seleccionar comunas", opciones_comunas)

# Widget para seleccionar tipo de vehículo de la víctima
tipos_vehiculo = st.multiselect("Seleccionar tipo de vehículo de la víctima", homicidios['VICTIMA'].unique())

# Imprimir las opciones seleccionadas para depurar
st.write("Comunas seleccionadas:", comunas_seleccionadas)

# Filtrar el DataFrame según los filtros seleccionados
homicidios_filtrados = homicidios
if comunas_seleccionadas:
    homicidios_filtrados = homicidios_filtrados[homicidios_filtrados['COMUNA'].isin(comunas_seleccionadas)]

if tipos_vehiculo:
    homicidios_filtrados = homicidios_filtrados[homicidios_filtrados['VICTIMA'].isin(tipos_vehiculo)]

# Crear un mapa centrado en una ubicación inicial
m = folium.Map(location=[-34.6037, -58.3816], zoom_start=12)

# Añadir marcadores para cada par de coordenadas de longitud y latitud
for index, row in homicidios_filtrados.iterrows():
    lat = row['pos y']
    lon = row['pos x']
    folium.Marker([lat, lon]).add_to(m)

# Mostrar el mapa usando folium_static
folium_static(m)
