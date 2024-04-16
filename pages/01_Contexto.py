import streamlit as st 
import matplotlib.pyplot as plt
import streamlit_folium
import pandas as pd 
import numpy as np
import seaborn as sns
import calendar

st.page_link('Home.py',label='🏠 Inicio')
st.page_link('Home.py',label='⬅️ Anterior: Home ')

st.title('Contexto')
st.write('* En el período comprendido entre 2016 y 2021, la Ciudad Autónoma de Buenos Aires (CABA) ha experimentado un total de 707 incidentes de tránsito que resultaron en fatalidades. Estos incidentes han dejado un impacto significativo en la seguridad vial y la comunidad en general.')
st.write('* El análisis de datos se centra en una abanico de variables, incluyendo la comuna donde ocurrieron los incidentes, el tipo de vehículo involucrado, el rol de las personas afectadas, entre otros. Estos datos han sido recopilados y analizados con el fin de identificar patrones, tendencias y posibles áreas de intervención para mejorar la seguridad vial en la ciudad.')

st.page_link('pages/02_Objetivos.py', label='➡️ Siguiente: Objetivos')
st.divider()