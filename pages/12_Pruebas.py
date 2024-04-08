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





st.page_link('Home.py',label='🏠 Inicio')

st.page_link('pages/02_Objetivo.py',label='⬅️ Volver')

fig, ax= plt.subplots()

# Convertir la columna 'fecha' de str a datetime
Fatales['Fecha'] = pd.to_datetime(Fatales['Fecha'])


with st.container():    
    # Agrupar los casos por año y contar el número de casos por año
    casos_por_año = Fatales['Fecha'].dt.year.value_counts().sort_index()

    # Calcular el promedio de casos por año
    promedio_casos_por_año = casos_por_año.mean()

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

    # Agregar una línea horizontal para mostrar el promedio
    plt.axhline(y=promedio_casos_por_año, color='red', linestyle='--', label=f'Promedio: {promedio_casos_por_año:.2f}')
    plt.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)



with st.container():
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





with st.container():
    # Crear una columna nueva con el día de la semana
    Fatales['Dia_semana'] = Fatales['Fecha'].dt.day_name()

    # Contar la cantidad de casos por día de la semana
    casos_por_dia = Fatales['Dia_semana'].value_counts()

    # Calcular el porcentaje de casos por día de la semana
    porcentaje_por_dia = casos_por_dia / casos_por_dia.sum() * 100

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = porcentaje_por_dia.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Distribución porcentual de casos por día de la semana')
    ax.set_xlabel('Día de la semana')
    ax.set_ylabel('Porcentaje de casos')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)

    # Anotar los valores de porcentaje en cada barra
    for i in range(len(porcentaje_por_dia)):
        plt.annotate(f'{porcentaje_por_dia.iloc[i]:.2f}%', 
                    xy=(i, porcentaje_por_dia.iloc[i]), 
                    ha='center', va='bottom')

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


# Suponiendo que tienes un DataFrame llamado 'accidentes' con una columna 'franja_horaria'

# Calcular el número de accidentes por franja horaria
accidentes_por_franja = Fatales['HH'].value_counts()

# Calcular el porcentaje de accidentes para cada franja horaria
porcentaje_accidentes = accidentes_por_franja / len(Fatales) * 100

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(8, 4))
porcentaje_accidentes.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución porcentual de accidentes por franja horaria')
ax.set_xlabel('Franja horaria')
ax.set_ylabel('Porcentaje de accidentes (%)')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)

# Anotar los valores exactos de cada barra
for i in range(len(porcentaje_accidentes)):
    value = porcentaje_accidentes.iloc[i]
    plt.annotate(f"{value:.2f}%", 
                xy=(i, value), 
                xytext=(0, 3),  # Ajuste vertical
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)



st.divider()
# -------------------------------------------------------------------------------------------------




# Convertir la columna 'fecha' de str a datetime
No_Fatales['Fecha'] = pd.to_datetime(No_Fatales['Fecha'])


with st.container():    
# Agrupar los casos por año y contar el número de casos por año
    casos_por_año = No_Fatales['Fecha'].dt.year.value_counts().sort_index()

    # Calcular el promedio de casos por año
    promedio_casos_por_año = casos_por_año.mean()

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

    # Agregar una línea horizontal para mostrar el promedio
    plt.axhline(y=promedio_casos_por_año, color='red', linestyle='--', label=f'Promedio: {promedio_casos_por_año:.2f}')
    plt.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)



with st.container():
    # Agrupar los casos por año y contar el número de casos por año
    casos_por_año = No_Fatales['Fecha'].dt.year.value_counts().sort_index()

    # Calcular la cantidad de casos en el año 2016
    casos_2016 = casos_por_año.loc[2019]

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





with st.container():
    # Crear una columna nueva con el día de la semana
    No_Fatales['Dia_semana'] = No_Fatales['Fecha'].dt.day_name()

    # Contar la cantidad de casos por día de la     semana
    casos_por_dia = No_Fatales['Dia_semana'].value_counts()

    # Calcular el porcentaje de casos por día de la semana
    porcentaje_por_dia = casos_por_dia / casos_por_dia.sum() * 100

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = porcentaje_por_dia.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Distribución porcentual de casos por día de la semana')
    ax.set_xlabel('Día de la semana')
    ax.set_ylabel('Porcentaje de casos')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)

    # Anotar los valores de porcentaje en cada barra
    for i in range(len(porcentaje_por_dia)):
        plt.annotate(f'{porcentaje_por_dia.iloc[i]:.2f}%', 
                    xy=(i, porcentaje_por_dia.iloc[i]), 
                    ha='center', va='bottom')

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


with st.container():
    # Calcular el número de accidentes por franja horaria
    accidentes_por_franja = No_Fatales['HH'].value_counts()

    # Calcular el porcentaje de accidentes para cada franja horaria
    porcentaje_accidentes = accidentes_por_franja / len(Fatales) * 100

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(15, 10))
    porcentaje_accidentes.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Distribución porcentual de accidentes por franja horaria')
    ax.set_xlabel('Franja horaria')
    ax.set_ylabel('Porcentaje de accidentes (%)')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)

    # Anotar los valores exactos de cada barra
    for i in range(len(porcentaje_accidentes)):
        value = porcentaje_accidentes.iloc[i]
        plt.annotate(f"{value:.2f}%", 
                    xy=(i, value), 
                    xytext=(0, 3),  # Ajuste vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
        
        
        
        



st.page_link('pages/04_Analisis_por_Victima_Fatal.py',label='➡️ Siguiente')