import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt

st.page_link('Home.py',label='🏠 Inicio')
st.page_link('pages/06_Analisis_por_Victima_No_Fatal.py',label='⬅️ Volver')

st.title("Análisis Geográfico de Hechos Fatales")

#Traigo el dataset hechos fatales
Fatales = pd.DataFrame(pd.read_csv('src/fatales.csv'))
Total_Casos = len(Fatales)


# GRÁFICO DE CASOS POR COMUNA
comuna = Fatales['Comuna'].value_counts()
Porcentaje_Comuna = (comuna / Total_Casos) * 100
#Grafico 
fig,ax= plt.subplots(figsize=(8,4))
Porcentaje_Comuna.plot(kind='bar',color='skyblue',ax=ax)
ax.set_title('Distribución de casos por comuna')
ax.set_xlabel('Comuna')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y', linestyle='--', alpha=0.7)
# Anotar los valores exactos de cada barra
for i in range(len(Porcentaje_Comuna)):
    plt.annotate(f"{Porcentaje_Comuna.iloc[i]:.1f}%", 
                xy=(i,Porcentaje_Comuna.iloc[i]), 
                ha='center', va='bottom')
plt.xticks(rotation=0)
st.pyplot(fig)

# GRAFICO DE CASOS POR COMUNA Y HORA
# Obtener las opciones únicas de la columna COMUNA y ordenarlas
opciones_comunas = sorted(Fatales['Comuna'].unique())

Comuna_seleccionada = st.selectbox('Seleccione Una Comuna:', opciones_comunas)

# Filtrar el DataFrame por la comuna seleccionada
Comuna_Filtrada = Fatales[Fatales['Comuna'] == Comuna_seleccionada]

# Calcular el total de casos en la comuna seleccionada
Total_Comuna_Filtrada = len(Comuna_Filtrada)

# Contar los casos por hora en la comuna seleccionada
Comuna_Filtrada_por_Hora = Comuna_Filtrada['HH'].value_counts()

# Calcular el porcentaje de casos por hora en la comuna seleccionada
Porcentaje_Comuna_Hora = (Comuna_Filtrada_por_Hora / Total_Comuna_Filtrada) * 100

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
Porcentaje_Comuna_Hora.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución de casos por hora en la comuna seleccionada')
ax.set_xlabel('Hora')
ax.set_ylabel('Porcentaje de casos')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Anotar los valores exactos de cada barra
for i in range(len(Porcentaje_Comuna_Hora)):
    plt.annotate(f"{Porcentaje_Comuna_Hora.iloc[i]:.1F}%", 
                 xy=(i, Porcentaje_Comuna_Hora.iloc[i]), 
                 ha='center', va='bottom',
                 rotation = 90)
plt.xticks(rotation=0)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)





# Mostrar el widget multiselect con las opciones ordenadas
comunas_seleccionadas = st.multiselect("Seleccionar comunas", opciones_comunas)

# Widget para seleccionar tipo de vehículo de la víctima
tipos_vehiculo = st.multiselect("Seleccionar tipo de vehículo de la víctima", Fatales['Vehiculo Victima'].unique())

# Imprimir las opciones seleccionadas para depurar
st.write("Comunas seleccionadas:", comunas_seleccionadas)

# Filtrar el DataFrame según los filtros seleccionados
homicidios_filtrados = Fatales
if comunas_seleccionadas:
    homicidios_filtrados = homicidios_filtrados[homicidios_filtrados['Comuna'].isin(comunas_seleccionadas)]

if tipos_vehiculo:
    homicidios_filtrados = homicidios_filtrados[homicidios_filtrados['Vehiculo Victima'].isin(tipos_vehiculo)]

# Crear un mapa centrado en una ubicación inicial
m = folium.Map(location=[-34.6037, -58.3816], zoom_start=12)

# Añadir marcadores para cada par de coordenadas de longitud y latitud
for index, row in homicidios_filtrados.iterrows():
    lat = row['Lat']
    lon = row['Long']
    folium.Marker([lat, lon]).add_to(m)

# Mostrar el mapa usando folium_static
folium_static(m)


st.page_link('pages/08_Analisis_Geografico_No_Fatal.py',label='➡️ Siguiente')