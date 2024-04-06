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
    st.page_link('pages/04_Analisis_por_Victima_Fatal.py',label='⬅️ Volver')
    
st.title('Análisis por Víctima No Fatal')




st.page_link('pages/06_Analisis_Geografico_Fatal.py',label='➡️ Siguiente')