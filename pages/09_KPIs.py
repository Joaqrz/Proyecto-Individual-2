import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.graph_objects as go

st.page_link('Home.py',label='🏠 Inicio')
st.page_link('pages/08_Analisis_Geografico_No_Fatal.py',label='⬅️ Anterior: Análisis Geográfico No Fatal')

#Importo Los DataSets que voy a trabajar
Fatales = pd.DataFrame(pd.read_csv('src/fatales.csv'))

No_fatales = pd.DataFrame(pd.read_csv('src/No_fatales.csv'))

Poblacion = pd.DataFrame(pd.read_csv('src/Poblacion.csv'))

st.title('KPIs')




# Convertir la columna de fechas a tipo datetime

#KPI HOMICIDIOS---------------------------------------------------------------------------------------------------------------------

Fatales['Fecha'] = pd.to_datetime(Fatales['Fecha'])

#Widget para obtener el año deseado

opciones_año = Fatales['Fecha'].dt.year.unique()
año = st.sidebar.selectbox('Seleccione un año para KPI Fatales',opciones_año)

#Traer el dato de población total
Poblacion_total = Poblacion['POBLACION'].sum()

# Filtrar solo los datos del año seleccionado
fatales_anual = Fatales[Fatales['Fecha'].dt.year == año]

# Dividir el año 2021 en dos semestres
primer_semestre = fatales_anual[(fatales_anual['Fecha'].dt.month >= 1) & (fatales_anual['Fecha'].dt.month <= 6)]
segundo_semestre = fatales_anual[(fatales_anual['Fecha'].dt.month >= 7) & (fatales_anual['Fecha'].dt.month <= 12)]

# Contar la cantidad de casos (filas) en cada semestre
cantidad_primer_semestre = len(primer_semestre)
cantidad_segundo_semestre = len(segundo_semestre)

#Aplicar Fórmula de tasa de homicidios
Tasa_primer_semestre = (cantidad_primer_semestre/Poblacion_total)*100000
Tasa_segundo_semestre = (cantidad_segundo_semestre/Poblacion_total)*100000
# Calcular la diferencia porcentual
diferencia_porcentual = ((Tasa_segundo_semestre - Tasa_primer_semestre)/Tasa_primer_semestre) * 100

st.header(f'Diferencia porcentual del segundo semestre con el primero del año {año}')


Objetivo1 = -10
# Crear un gráfico de velocímetro con Plotly
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = diferencia_porcentual,
    title_text = f"Objetivo: -10%",
    number={'suffix': "%"},
    delta={'reference': Objetivo1, 'relative': False, 'valueformat': '.2f', 'increasing':{'color':'red'}, 'decreasing':{'color':'green'}},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [-70, 70]},
        'bar': {'color': "rgba(0, 0, 0, 0)"},
        'steps' : [
            {'range': [-70, -10], 'color': "green"},
            {'range': [-10, 70], 'color': "red"}],
        'threshold' : {

            'line': {'color': "white", 'width': 6},
            'thickness': 0.80,
            'value': diferencia_porcentual},

    }
))


st.plotly_chart(fig)

#KPI MOTOCICLISTAS---------------------------------------------------------------------------------------------------------------------

# Filtro los accidentes en moto en el DataFrame Fatales
Motos_Mortales = Fatales[Fatales['Vehiculo Victima']=='MOTO']


# Filtrar las filas correspondientes a motos mortales en 2020 y 2021
Motos_Mortales_2020 = Motos_Mortales[Motos_Mortales['Fecha'].dt.year == 2020]
Motos_Mortales_2021 = Motos_Mortales[Motos_Mortales['Fecha'].dt.year == 2021]

# Calcular el número total de accidentes mortales en moto para cada año
total_accidentes_2020 = Motos_Mortales_2020.shape[0]
total_accidentes_2021 = Motos_Mortales_2021.shape[0]

# Calcular la diferencia porcentual entre los dos años
evolucion_porcentual = ((total_accidentes_2020 - total_accidentes_2021) / total_accidentes_2020) * 100
st.header('Evolución de Acidentes En Moto en 2021 con respecto a 2020')
Objetivo2 = -7
# Crear un gráfico de velocímetro con Plotly
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = evolucion_porcentual,
    title_text = f"Objetivo: -7%",
    number={'suffix': "%"},
    delta={'reference': Objetivo2, 'relative': False, 'valueformat': '.2f', 'increasing':{'color':'red'}, 'decreasing':{'color':'green'}},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [-70, 70]},
        'bar': {'color': "rgba(0, 0, 0, 0)"},
        'steps' : [
            {'range': [-70, -7], 'color': "green"},
            {'range': [-7, 70], 'color': "red"}],
        'threshold' : {

            'line': {'color': "white", 'width': 6},
            'thickness': 0.80,
            'value': evolucion_porcentual},

    }
))
st.plotly_chart(fig)


#KPI PEATONES---------------------------------------------------------------------------------------------------------------------

No_fatales['Fecha'] = pd.to_datetime(No_fatales['Fecha'])

#Creo un widget para seleccionar los años
#st.write(No_fatales)
#st.write('año lesiones:',año_lesiones)
#Traigo los casos de lesiones por año  

Lesiones_por_año = No_fatales[No_fatales['Fecha'].dt.year== año]
#st.write('Lesiones por año:',Lesiones_por_año)

#Divido el año en dos semestres
primer_semestre_lesiones = Lesiones_por_año[(Lesiones_por_año['Fecha'].dt.month >= 1) & (Lesiones_por_año['Fecha'].dt.month <= 6)]
segundo_semestre_lesiones = Lesiones_por_año[(Lesiones_por_año['Fecha'].dt.month >= 7) & (Lesiones_por_año['Fecha'].dt.month <= 12)]
#st.write('Lesiones Semestres:',primer_semestre_lesiones,segundo_semestre_lesiones)

#Calculo el total de cada semestre
Cantidad_primer_semestre_lesiones = len(primer_semestre_lesiones)
Cantidad_segundo_semestre_lesiones = len(segundo_semestre_lesiones)
#st.write('Lesiones Semestres 2:',Cantidad_primer_semestre_lesiones,Cantidad_segundo_semestre_lesiones)

#Aplicar Fórmula de tasa de homicidios
Tasa_primer_semestre_lesiones = (Cantidad_primer_semestre_lesiones/Poblacion_total)*100000
Tasa_segundo_semestre_lesiones = (Cantidad_segundo_semestre_lesiones/Poblacion_total)*100000
#st.write('Tasas:',Tasa_primer_semestre_lesiones,Tasa_segundo_semestre_lesiones)

# Calcular la diferencia porcentual
diferencia_porcentual_lesiones = ((Tasa_segundo_semestre_lesiones - Tasa_primer_semestre_lesiones)/Tasa_primer_semestre_lesiones) * 100
#st.write('Delta:',diferencia_porcentual_lesiones)

st.header(f'Variacion De Cantidad de Lesiones Del segundo semestre con respecto al primero del año {año}')
Objetivo3 = -5
# Crear un gráfico de velocímetro con Plotly
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = diferencia_porcentual_lesiones,
    title_text = f"Objetivo: -5%",
    number={'suffix': "%"},
    delta={'reference': Objetivo3, 'relative': False, 'valueformat': '.1f', 'increasing':{'color':'red'}, 'decreasing':{'color':'green'}},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [-70, 70]},
        'bar': {'color': "rgba(0, 0, 0, 0)"},
        'steps' : [
            {'range': [-70, -7], 'color': "green"},
            {'range': [-7, 70], 'color': "red"}],
        'threshold' : {

            'line': {'color': "white", 'width': 6},
            'thickness': 0.80,
            'value': diferencia_porcentual_lesiones},

    }
))
st.plotly_chart(fig)
st.page_link('pages/10_Conclusiones.py',label='➡️ Siguiente: Conclusiones')
st.divider()