import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np
import seaborn as sns
import calendar


col1, col2 = st.columns(2)

with col1:
    st.page_link('Home.py',label='🏠 Inicio')
with col2: 
    st.page_link('pages/01_Contexto.py',label='⬅️ Volver')
st.title('Objetivos')
st.write('El presente informe busca proporcionar una visión detallada de los resultados obtenidos del análisis de datos, destacando hallazgos clave, tendencias significativas y recomendaciones para acciones futuras. Se espera que este análisis aporte a una mayor comprensión de los factores que contribuyen a los incidentes de tránsito mortales en CABA y sirva como base para implementar medidas efectivas de prevención y seguridad vial. Siendo así nuestra misión cumplir con los siguientes objetivos:')
st.write('* Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en comparación con el semestre anterior.')
st.write('* Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, respecto al año anterior.')


st.page_link('pages/03_Analisis_Temporal.py',label='➡️ Siguiente')
