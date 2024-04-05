import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np
import seaborn as sns
import calendar

st.page_link("Home.py", label="🏠 Volver a Inicio")
st.markdown('* Análisis de casos fatales por comuna')

# Importo el dataframe 
fatales = pd.DataFrame(pd.read_csv('hechos_fatales.csv'))

# Calcular la cantidad de hechos por comuna
hechos_por_comuna = fatales['COMUNA'].value_counts()

# Crear el histograma
fig, ax = plt.subplots()
hechos_por_comuna.plot(kind='bar')
plt.xlabel('Comuna')
plt.ylabel('Cantidad de hechos')
plt.title('Cantidad de hechos por comuna')

# Mostrar el histograma en Streamlit
st.pyplot(fig)

st.write('* Podemos observar que la comuna con más incidentes es la comuna número 1, que corresponden con los barrios de Retiro, Constitución, Monserrat, San Nicolás, San Telmo y Puerto Madero')
st.write('* Estos son barrios comerciales y administrativos. Haré un análisis por franja horaria de los hechos ocurridos, solo en la comuna 1')

#Crear histograma por horas
fatales_comuna_1 = fatales[fatales['COMUNA']==1]
hechos_por_horas = fatales_comuna_1['HH'].value_counts()
fig, ax = plt.subplots()
hechos_por_horas.plot(kind='bar')
plt.xlabel('Franja Horaria')
plt.ylabel('Cantidad de hechos')
plt.title('Hechos por franja horaria')
#Muestro el histograma en streamlit
st.pyplot(fig)


st.write('Ahora haremos un análisis para saber qué dias ocurren los accidentes solamente en la comuna 1')

# Filtrar los datos para obtener solo los accidentes en la comuna 1
accidentes_comuna_1 = fatales[fatales['COMUNA'] == 1]

# Convertir la columna 'fecha' al tipo de datos datetime
accidentes_comuna_1['FECHA'] = pd.to_datetime(accidentes_comuna_1['FECHA'])

# Extraer el día de la semana de cada fecha
accidentes_comuna_1['dia_semana'] = accidentes_comuna_1['FECHA'].dt.dayofweek

# Obtener los nombres de los días de la semana en español
nombres_dias_semana = [calendar.day_name[i] for i in range(7)]

# Contar la cantidad de accidentes por día de la semana
conteo_accidentes_por_dia = accidentes_comuna_1['dia_semana'].value_counts().sort_index()

# Crear el gráfico
plt.figure(figsize=(10, 6))
sns.barplot(x=conteo_accidentes_por_dia.index, y=conteo_accidentes_por_dia.values, palette="viridis")
plt.title("Distribución de accidentes por día de la semana en la comuna 1")
plt.xlabel("Día de la semana")
plt.ylabel("Cantidad de accidentes")

# Cambiar el texto del eje x a español
plt.xticks(range(7), nombres_dias_semana, rotation=45)

plt.tight_layout()

# Mostrar el gráfico en Streamlit
st.pyplot(plt)