import streamlit as st

st.title('Dashboard')

st.page_link("pages/01_📊_Hechos_Fatales.py", label="📊 Ir a Análisis Hechos Fatales")
st.page_link("pages/02_🗺️_Mapa_Hechos_Fatales.py", label="🗺️ Ir al Mapa de Hechos Fatales")
st.page_link("pages/03_📊_Hechos_No_Fatales.py", label="📊 Ir a Análisis Hechos No Fatales")
st.page_link("pages/04_🗺️_Mapa_Hechos_No_Fatales.py", label="🗺️ Ir al Mapa de Hechos No Fatales")
st.page_link("pages/05_🤔_conclusiones.py", label="🤔 Conclusiones")