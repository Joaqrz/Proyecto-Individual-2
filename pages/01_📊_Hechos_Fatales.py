import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np

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