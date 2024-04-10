import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np
import seaborn as sns
import calendar





st.page_link('Home.py',label='🏠 Inicio')

st.page_link('pages/09_KPI.py',label='⬅️ Volver')
    
st.title('Conclusiones')

st.write('Luego del análisis estadístico podemos sacar algunas conclusiones:')
st.write(' -> Análisis Temporal:')
st.write('* La tendencia de casos tanto fatales como no, es a la baja.')
st.write('* Durante el año 2020 se han reducido, con diferencia, los casos debido a la menor circulación de personas en la vía pública.')
st.write('* No existe una tendencia clara de aumentos de casos a medida que transcurre el año. Sin embargo Mayo es el mes más consistente en cantidad de casos, salvo algunas excepciones')

st.page_link('pages/11_Cierre.py',label='➡️ Siguiente')