import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt

st.page_link('Home.py',label='🏠 Inicio')
st.page_link('pages/07_Analisis_Geografico_Fatal.py',label='⬅️ Volver')
    
st.title("Análisis Geográfico de Hechos No Fatales")

#Traigo el dataset hechos no fatales
No_Fatales = pd.DataFrame(pd.read_csv('src/No_fatales.csv'))
Total_Casos = len(No_Fatales)
# Convertir la columna 'fecha' de str a datetime
No_Fatales['Fecha'] = pd.to_datetime(No_Fatales['Fecha'])

# GRÁFICO DE CASOS POR COMUNA
comuna = No_Fatales['Comuna'].value_counts()
Porcentaje_Comuna_Lesiones = (comuna / Total_Casos) * 100
#Grafico 
fig,ax= plt.subplots(figsize=(8,4))
Porcentaje_Comuna_Lesiones.plot(kind='bar',color='skyblue',ax=ax)
ax.set_title('Distribución de Lesiones por comuna')
ax.set_xlabel('Comuna')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y', linestyle='--', alpha=0.7)
# Anotar los valores exactos de cada barra
for i in range(len(Porcentaje_Comuna_Lesiones)):
    plt.annotate(f"{Porcentaje_Comuna_Lesiones.iloc[i]:.1f}%", 
                xy=(i,Porcentaje_Comuna_Lesiones.iloc[i]), 
                ha='center', va='bottom')
plt.xticks(rotation=0)
st.pyplot(fig)

# GRAFICO DE CASOS POR COMUNA Y HORA
# Obtener las opciones únicas de la columna COMUNA y ordenarlas
opciones_comunas = sorted(No_Fatales['Comuna'].unique())

Comuna_seleccionada = st.selectbox('Seleccione Una Comuna:', opciones_comunas)

# Filtrar el DataFrame por la comuna seleccionada
Comuna_Filtrada = No_Fatales[No_Fatales['Comuna'] == Comuna_seleccionada]

# Calcular el total de casos en la comuna seleccionada
Total_Comuna_Filtrada = len(Comuna_Filtrada)

# Contar los casos por hora en la comuna seleccionada
Comuna_Filtrada_por_Hora = Comuna_Filtrada['HH'].value_counts()

# Calcular el porcentaje de casos por hora en la comuna seleccionada
Porcentaje_Comuna_Hora = (Comuna_Filtrada_por_Hora / Total_Comuna_Filtrada) * 100
Porcentaje_Comuna_Hora = Porcentaje_Comuna_Hora.sort_index()

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
Porcentaje_Comuna_Hora.plot(kind='bar', color='skyblue', ax=ax, width=0.5)
ax.set_title('Distribución de lesiones por hora en la comuna seleccionada')
ax.set_xlabel('Hora')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Anotar los valores exactos de cada barra
for i in range(len(Porcentaje_Comuna_Hora)):
    plt.annotate(f"{Porcentaje_Comuna_Hora.iloc[i]:.1F}%", 
                 xy=(i, Porcentaje_Comuna_Hora.iloc[i]), 
                 ha='center', va='bottom',
                 rotation = 45
                 )
plt.xticks(rotation=0)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# GRAFICO POR COMUNA Y DIA

# Contar los casos por dia en la comuna seleccionada
Comuna_Filtrada_por_Dia = Comuna_Filtrada['Fecha'].dt.day_name().value_counts()

# Calcular el porcentaje de casos por dia en la comuna seleccionada
Porcentaje_Comuna_Dia = (Comuna_Filtrada_por_Dia / Total_Comuna_Filtrada) * 100

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
Porcentaje_Comuna_Dia.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución de Lesiones por día en la comuna seleccionada')
ax.set_xlabel('Día')
ax.set_ylabel('Porcentaje de casos')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Anotar los valores exactos de cada barra
for i in range(len(Porcentaje_Comuna_Dia)):
    plt.annotate(f"{Porcentaje_Comuna_Dia.iloc[i]:.1F}%", 
                 xy=(i, Porcentaje_Comuna_Dia.iloc[i]), 
                 ha='center', va='bottom',
                 )
plt.xticks(rotation=0)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


#GRAFICO DE TIPO DE VEHICULO VICTIMA 
# Definir un diccionario de colores para cada tipo de vehículo
colors = {
    'auto': 'blue',
    'moto': 'red',
    'camion':'purple',
    'ciclista': 'green',
    'transporte_publico':'pink',
    # Añade más tipos de vehículo y colores según sea necesario
}




Comuna_Filtrada_por_Victima = Comuna_Filtrada['Vehiculo Victima'].value_counts()

# Calcular el porcentaje de casos por dia en la comuna seleccionada
Porcentaje_Comuna_Victima = (Comuna_Filtrada_por_Victima / Total_Comuna_Filtrada) * 100

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
Porcentaje_Comuna_Victima.plot(kind='bar', color=[colors.get(vehicle, 'gray') for vehicle in Porcentaje_Comuna_Victima.index], ax=ax)
ax.set_title('Casos por tipo de vehículo en la comuna seleccionada')
ax.set_xlabel('Vehículo')
ax.set_ylabel('Porcentaje de casos')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Anotar los valores exactos de cada barra
for i in range(len(Porcentaje_Comuna_Victima)):
    plt.annotate(f"{Porcentaje_Comuna_Victima.iloc[i]:.1F}%", 
                 xy=(i, Porcentaje_Comuna_Victima.iloc[i]), 
                 ha='center', va='bottom',
                 )
plt.xticks(rotation=0)
st.pyplot(fig)



# CREO EL MAPA DE VISUALIZACION DE LOS CASOS 

#Primero filtro

mapa_filtro = No_Fatales[No_Fatales['Comuna']==Comuna_seleccionada]

#Titulo del mapa
st.header('Ubicación Geográfica de los casos')



# Crear un mapa centrado en una ubicación inicial
m = folium.Map(location=[-34.6037, -58.3816], zoom_start=12)

# Añadir marcadores para cada par de coordenadas de longitud y latitud
for index, row in mapa_filtro.iterrows():
    lat = row['Lat']
    lon = row['Long']
    edad = row['Edad']
    sexo = row['Sexo']
    tipo_vehiculo = row['Vehiculo Victima']
    hora = row['HH']
    color = colors.get(tipo_vehiculo, 'gray')
    # Crear el texto del pop-up
    popup_text = f"Edad: {edad}<br>Sexo: {sexo}<br>Vehículo: {tipo_vehiculo}<br>Hora: {hora}"
    folium.Marker([lat, lon], icon=folium.Icon(color=color),popup=popup_text).add_to(m)

# Mostrar el mapa usando folium_static

Mostrar_Mapa = st.checkbox('Mostrar Mapa')

if Mostrar_Mapa:
    folium_static(m)






st.page_link('pages/09_KPI.py',label='➡️ Siguiente')