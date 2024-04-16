import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd 
import locale

# Traigo los datasets para ser analizados
Fatales = pd.DataFrame(pd.read_csv('src/fatales.csv'))
No_Fatales = pd.DataFrame(pd.read_csv('src/No_fatales.csv'))





st.page_link('Home.py',label='🏠 Inicio')

st.page_link('pages/02_Objetivos.py',label='⬅️ Volver: Objetivos')

st.title('Análisis Temporal Fatal')

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# GRÁFICOS FATALIDADES POR AÑO

# Convertir la columna 'fecha' de str a datetime
Fatales['Fecha'] = pd.to_datetime(Fatales['Fecha'])

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


# Agregar una línea horizontal para mostrar el promedio
plt.axhline(y=promedio_casos_por_año, color='red', linestyle='--', label=f'Promedio: {promedio_casos_por_año:.2f}')
plt.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# GRÁFICO VARIACION PORCENTUAL FATALIDADES POR AÑO

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



# Mostrar el gráfico en Streamlit
st.pyplot(fig)
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#GRAFICO DE CASOS POR MESES
# Seleccionar el año
Año = st.selectbox('Seleccione un Año', Fatales['Fecha'].dt.year.unique())

# Filtrar el DataFrame por el año seleccionado
Fatales_Año_Filtrado = Fatales[Fatales['Fecha'].dt.year == Año]

# Contar los incidentes por mes en el año seleccionado
Fatales_Por_Mes_y_Año = Fatales_Año_Filtrado['Fecha'].dt.month.value_counts().sort_index()

# Crear el gráfico
fig, ax = plt.subplots()
Fatales_Por_Mes_y_Año.plot(kind='bar',color = 'skyblue', ax=ax)
ax.set_title(f'Número de incidentes fatales por mes en el año {Año}')
ax.set_xlabel('Mes')
ax.set_ylabel('Número de incidentes')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation = 0)

# Mostrar el valor exacto de cada barra
for i, value in enumerate(Fatales_Por_Mes_y_Año):
    plt.text(i, value, str(value), ha='center', va='bottom')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# GRÁFICO  FATALIDADES POR DIA
# Definir el orden de los días de la semana en español
orden_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

with st.container():
    # Crear una columna nueva con el día de la semana
    Fatales['Dia_semana'] = Fatales['Fecha'].dt.day_name(locale='es_ES')

    # Contar la cantidad de casos por día de la semana
    casos_por_dia = Fatales['Dia_semana'].value_counts()

    # Reordenar los valores de acuerdo al orden definido
    casos_por_dia = casos_por_dia.reindex(orden_dias)

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

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# GRÁFICO FATALIDADES POR HORA
# Calcular el número de accidentes por franja horaria
accidentes_por_franja = Fatales['HH'].value_counts().sort_index()

# Calcular el porcentaje de accidentes para cada franja horaria
porcentaje_accidentes = accidentes_por_franja / len(Fatales) * 100

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(12, 6))
porcentaje_accidentes.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución porcentual de accidentes por franja horaria')
ax.set_xlabel('Franja horaria')
ax.set_ylabel('Porcentaje de accidentes (%)')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)

# Anotar los valores exactos de cada barra
for i in range(len(porcentaje_accidentes)):
    value = porcentaje_accidentes.iloc[i]
    plt.annotate(f"{value:.1f}%", 
                xy=(i, value), 
                xytext=(0, 3),  # Ajuste vertical
                textcoords="offset points",
                ha='center', va='bottom')



# Mostrar el gráfico en Streamlit
st.pyplot(fig)


#-----------------------------------------------------------------------------------------------------------------------------------------------------

# GRAFICO + FILTRO DISTRIBUCIÓN HORARIA POR DIA FATALES

# Establecer el idioma local en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Obtener los nombres de los días de la semana en español
dias_espanol = pd.to_datetime(Fatales['Fecha']).dt.day_name(locale='Spanish')

# Obtener los nombres únicos de los días de la semana en español
dias_unicos = dias_espanol.unique()

# Crear el selectbox con los días de la semana en español
Dia = st.selectbox('Seleccione un día', dias_unicos)

# Filtrar el dataframe según el día seleccionado
Dia_Filtrado = Fatales[pd.to_datetime(Fatales['Fecha']).dt.day_name(locale='Spanish') == Dia]

# Contar la cantidad de casos fatales por franja horaria para el día seleccionado
accidentes_por_franja_y_dia = Dia_Filtrado['HH'].value_counts().sort_index()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(12, 6))
accidentes_por_franja_y_dia.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Casos Fatales por franja horaria para el día seleccionado')
ax.set_xlabel('Franja horaria')
ax.set_ylabel('Fatalidades')
ax.grid(axis='y', linestyle='--', alpha=1.0)
plt.xticks(rotation=0)

# Anotar los valores exactos de cada barra
for i in range(len(accidentes_por_franja_y_dia)):
    value = accidentes_por_franja_y_dia.iloc[i]
    plt.annotate(f"{value}", 
                xy=(i, value), 
                xytext=(0, 3),  # Ajuste vertical
                textcoords="offset points",
                ha='center', va='bottom')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
st.page_link('pages/04_Analisis_Temporal_No_Fatal.py',label='➡️ Siguiente: Análisis Temporal No Fatal')
st.divider()







