import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np
import seaborn as sns
import calendar




st.page_link('Home.py',label='🏠 Inicio')
st.page_link('pages/05_Analisis_por_Victima_Fatal.py',label='⬅️ Volver')
    
st.title('Análisis por Víctima No Fatal')
#Importo el dataset 
No_Fatales = pd.DataFrame(pd.read_csv('src/No_fatales.csv'))
# Convertir la columna 'fecha' de str a datetime
No_Fatales['Fecha'] = pd.to_datetime(No_Fatales['Fecha'])




# GRAFICO DISTRIBUCIÓN ETARIA

distribucion_por_edad = No_Fatales['Edad'].value_counts()

# Agrupar las edades en rangos específicos
bins = [0, 18, 50, 65, float('inf')]
labels = ['0-18', '19-50', '51-65', '65+']
No_Fatales['Rango de Edades'] = pd.cut(No_Fatales['Edad'], bins=bins, labels=labels, right=False)

# Contar el número de casos en cada rango de edades
distribucion_por_rango = No_Fatales['Rango de Edades'].value_counts().sort_index()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(8, 4))
distribucion_por_rango.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución por rango de edades de lesiones')
ax.set_xlabel('Rango de Edades')
ax.set_ylabel('Número de casos')
ax.grid(axis='y', linestyle='--', alpha=0.7)
# Anotar los valores exactos de cada barra
for i in range(len(distribucion_por_rango)):
    plt.annotate(str(distribucion_por_rango.iloc[i]), 
                xy=(i, distribucion_por_rango.iloc[i]), 
                ha='center', va='bottom')
plt.xticks(rotation=0)
st.pyplot(fig)


#DISTRIBUCION POR SEXO
# Contar el número total de casos
total_casos = len(No_Fatales)

# Contar el número de casos para cada sexo
distribucion_por_sexo = No_Fatales['Sexo'].value_counts()

# Calcular el porcentaje de cada sexo
porcentaje_por_sexo = (distribucion_por_sexo / total_casos) * 100

# Crear el gráfico de torta
fig, ax = plt.subplots(figsize=(3, 3))
porcentaje_por_sexo.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'pink','gray'], ax=ax)
ax.set_title('Distribución de casos por sexo')
ax.set_ylabel('')  # Eliminar la etiqueta del eje y

# Ajustar el diseño para que la torta se vea circular
plt.axis('equal')

# Mostrar el gráfico
st.pyplot(fig)

#DISTRIBUCION ETARIA POR SEXO
Sexo = st.selectbox('Seleccione una opción:',['Varon','Mujer'])

bins = [0, 18, 50, 65, float('inf')]
labels = ['0-18', '19-50', '51-65', '65+']
No_Fatales['Rango de Edades'] = pd.cut(No_Fatales['Edad'], bins=bins, labels=labels, right=False)

#Filtramos por sexo
Filtro_Sexo = No_Fatales[No_Fatales['Sexo']==Sexo]

# Contar el número de casos en cada rango de edades
distribucion_por_rango_y_sexo = Filtro_Sexo['Rango de Edades'].value_counts().sort_index()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(8, 4))
distribucion_por_rango_y_sexo.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución etaria y por sexo de lesiones')
ax.set_xlabel('Rango de Edades')
ax.set_ylabel('Número de casos')
ax.grid(axis='y', linestyle='--', alpha=0.7)
# Anotar los valores exactos de cada barra
for i in range(len(distribucion_por_rango_y_sexo)):
    plt.annotate(str(distribucion_por_rango_y_sexo.iloc[i]), 
                xy=(i, distribucion_por_rango_y_sexo.iloc[i]), 
                ha='center', va='bottom')
plt.xticks(rotation=0)
st.pyplot(fig)


#DISTRIBUCION DE TIPOS DE VEHICULOS DE LAS VICTIMAS
Vehiculo_Victima = No_Fatales['Vehiculo Victima'].value_counts()
Porcentaje_Vehiculo_Victima = (Vehiculo_Victima/ total_casos) * 100

fig, ax = plt.subplots(figsize=(8,4))
Porcentaje_Vehiculo_Victima.plot(kind='bar',color='skyblue',ax=ax)
ax.set_title('Distribucion porcentual de tipos de vehiculos de las víctimas')
ax.set_xlabel('Vehiculos')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y',linestyle='--',alpha=1)
for i in range(len(Porcentaje_Vehiculo_Victima)):
    plt.annotate(str(f"{Porcentaje_Vehiculo_Victima.iloc[i]:.1f}%"),
                 xy = (i, Porcentaje_Vehiculo_Victima.iloc[i]),
                 ha = 'center',va='bottom')
plt.xticks(rotation=0)
st.pyplot(fig)

# GRAFICO DE GRAVEDAD DE LESIONES

Gravedad = No_Fatales['Gravedad'].value_counts()
Porcentaje_Gravedad = (Gravedad / total_casos) * 100
#Grafico 
fig,ax = plt.subplots(figsize=(8,4))
Porcentaje_Gravedad.plot(kind='bar',color='skyblue',ax=ax)
ax.set_title('Porcentaje de Gravedad de lesiones')
ax.set_xlabel('Gravedad')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y',linestyle='--',alpha=1)
for i in range(len(Porcentaje_Gravedad)):
    plt.annotate(str(f"{Porcentaje_Gravedad.iloc[i]:.1f}%"),
                 xy = (i,Porcentaje_Gravedad.iloc[i]),
                 ha = 'center', va= 'bottom')

# GRAFICO DE GRAVEDAD DE LESIONES POR VEHICULO 
Gravedad_Lesiones_Vehiculo = st.selectbox('Seleccione tipo de vehiculo', No_Fatales['Vehiculo Victima'].unique())

# Filtramos
Gravedad_Filtrado = No_Fatales[No_Fatales['Vehiculo Victima'] == Gravedad_Lesiones_Vehiculo]['Gravedad'].value_counts()
Total_Gravedad_Filtrado = len(No_Fatales[No_Fatales['Vehiculo Victima'] == Gravedad_Lesiones_Vehiculo])
Porcentaje_Gravedad_Filtrado = (Gravedad_Filtrado / Total_Gravedad_Filtrado) * 100

# Gráfico
fig, ax = plt.subplots(figsize=(8, 4))
Porcentaje_Gravedad_Filtrado.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Porcentaje de Gravedad de lesiones por vehículo')
ax.set_xlabel('Gravedad')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y', linestyle='--', alpha=0.7)

for i in range(len(Porcentaje_Gravedad_Filtrado)):
    plt.annotate(f"{Porcentaje_Gravedad_Filtrado.iloc[i]:.1f}%",
                 xy=(i, Porcentaje_Gravedad_Filtrado.iloc[i]),
                 ha='center', va='bottom')
st.pyplot(fig)


st.page_link('pages/07_Analisis_Geografico_Fatal.py',label='➡️ Siguiente')