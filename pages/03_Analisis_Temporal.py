import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np
import seaborn as sns
import calendar

# Traigo los datasets para ser analizados
Fatales = pd.DataFrame(pd.read_csv('src/fatales.csv'))
No_Fatales = pd.DataFrame(pd.read_csv('src/No_fatales.csv'))


col1, col2 = st.columns(2)

with col1:
    st.page_link('Home.py',label='🏠 Inicio')
with col2: 
    st.page_link('pages/02_Objetivo.py',label='⬅️ Volver')

fig, ax= plt.subplots()

# Convertir la columna 'fecha' de str a datetime
Fatales['Fecha'] = pd.to_datetime(Fatales['Fecha'])

with col1: 
    # Agrupar los casos por año y contar el número de casos por año
    casos_por_año = Fatales['Fecha'].dt.year.value_counts().sort_index()

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(8, 4))
    casos_por_año.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Casos de incidentes fatales por año')
    ax.set_xlabel('Año')
    ax.set_ylabel('Número de casos')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    # Anotar los valores exactos de cada barra
    for i in range(len(casos_por_año)):
        plt.annotate(str(casos_por_año.iloc[i]), 
                    xy=(i, casos_por_año.iloc[i]), 
                    ha='center', va='bottom')
        plt.tight_layout()
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

with col2:
    # Agrupar los casos por año y contar el número de casos por año
    casos_por_año = Fatales['Fecha'].dt.year.value_counts().sort_index()

    # Calcular la cantidad de casos en el año 2016
    casos_2016 = casos_por_año.loc[2016]

    # Calcular la variación porcentual con respecto al año 2016
    variacion_porcentual = (casos_por_año / casos_2016 - 1) * 100

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = variacion_porcentual.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Variación porcentual de casos fatales con respecto al año 2016')
    ax.set_xlabel('Año')
    ax.set_ylabel('Variación porcentual (%)')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)

    # Anotar los valores exactos de cada barra
    for i in range(len(variacion_porcentual)):
        plt.annotate(f"{variacion_porcentual.iloc[i]:.2f}%", 
                    xy=(i, variacion_porcentual.iloc[i]), 
                    ha='center', va='bottom')

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    
st.write('* Como podemos observar en el grafico de la izquierda, el año con más casos fatales fue el año 2018')
st.write('* El gráfico de la izquierda es la variación de la cantidad de casos con respecto al año 2016, el primero en nuestro análisis')
st.write('* El año 2020 es el que mayor reducción de casos tiene, sin embargo hay que recordar que la circulación en el año 2020 estaba restingida por la pandemida del COVID-19')

    
    
st.page_link('pages/04_Analisis_por_Victima_Fatal.py',label='➡️ Siguiente')