import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np
import seaborn as sns
import calendar

#Importo el dataset 
Fatales = pd.DataFrame(pd.read_csv('src/fatales.csv'))
# Convertir la columna 'fecha' de str a datetime
Fatales['Fecha'] = pd.to_datetime(Fatales['Fecha'])


st.page_link('Home.py',label='🏠 Inicio')

st.page_link('pages/04_Analisis_Temporal_No_Fatal.py',label='⬅️ Volver')

st.title('Análisis por Víctima Fatal')

# GRAFICO DISTRIBUCIÓN ETARIA

distribucion_por_edad = Fatales['Edad'].value_counts()

# Agrupar las edades en rangos específicos
bins = [0, 18, 50, 65, float('inf')]
labels = ['0-18', '19-50', '51-65', '65+']
Fatales['Rango de Edades'] = pd.cut(Fatales['Edad'], bins=bins, labels=labels, right=False)

# Contar el número de casos en cada rango de edades
distribucion_por_rango = Fatales['Rango de Edades'].value_counts().sort_index()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(8, 4))
distribucion_por_rango.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución por rango de edades de los casos fatales')
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
total_casos = len(Fatales)

# Contar el número de casos para cada sexo
distribucion_por_sexo = Fatales['Sexo'].value_counts()

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
Sexo = st.selectbox('Seleccione una opción:',['MASCULINO','FEMENINO'])

bins = [0, 18, 50, 65, float('inf')]
labels = ['0-18', '19-50', '51-65', '65+']
Fatales['Rango de Edades'] = pd.cut(Fatales['Edad'], bins=bins, labels=labels, right=False)

#Filtramos por sexo
Filtro_Sexo = Fatales[Fatales['Sexo']==Sexo]

# Contar el número de casos en cada rango de edades
distribucion_por_rango_y_sexo = Filtro_Sexo['Rango de Edades'].value_counts().sort_index()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(8, 4))
distribucion_por_rango_y_sexo.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución etaria y por sexo de los casos fatales')
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
Vehiculo_Victima = Fatales['Vehiculo Victima'].value_counts()
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


#DISTRIBUCION DE ROLES SEGUN EL VEHICULO

Vehiculo = st.selectbox('Seleccione un vehiculo:',Fatales['Vehiculo Victima'].unique())

#Filtramos el dataframe 
Vehiculo_Filtrado = Fatales[Fatales['Vehiculo Victima']==Vehiculo]
total_casos_vehiculo = len(Vehiculo_Filtrado)
Roles_Filtrado = Vehiculo_Filtrado['ROL'].value_counts()
Porcentaje_Roles = (Roles_Filtrado/total_casos_vehiculo) * 100
#Graficamos 
fig, ax = plt.subplots(figsize=(8,4))
Porcentaje_Roles.plot(kind='bar',color='skyblue',ax=ax)
ax.set_title('Roles dentro del Vehiculo')
ax.set_xlabel('Roles')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y',linestyle='--',alpha=1)
for i in range(len(Porcentaje_Roles)):
    plt.annotate(str(f"{Porcentaje_Roles.iloc[i]:.1f}%"),
                 xy = (i,Porcentaje_Roles.iloc[i]),
                 ha = 'center', va = 'bottom')
st.pyplot(fig)
    

# VICTIMARIOS POR VEHICULO VICTIMA

Vehiculo_Victima = Vehiculo_Filtrado
Vehiculo_Victimario = Vehiculo_Victima['Vehiculo Acusado'].value_counts()
Porcentaje_Vehiculos_Victimarios = (Vehiculo_Victimario/total_casos_vehiculo) * 100
#Graficamos 
fig, ax = plt.subplots(figsize=(8,4))
Porcentaje_Vehiculos_Victimarios.plot(kind='bar',color='skyblue',ax=ax)
ax.set_title('Porcentaje de Victimarios según el vehículo de la víctima')
ax.set_xlabel('Victimarios')
ax.set_ylabel('Porcentaje')
ax.grid(axis='y',linestyle='--',alpha=1)
for i in range (len(Porcentaje_Vehiculos_Victimarios)):
    plt.annotate(str(f"{Porcentaje_Vehiculos_Victimarios.iloc[i]:.1f}%"),
                 xy = (i,Porcentaje_Vehiculos_Victimarios.iloc[i]),
                 ha = 'center', va = 'bottom')
st.pyplot(fig)






st.page_link('pages/06_Analisis_por_Victima_No_Fatal.py',label='➡️ Siguiente')