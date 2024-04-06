import streamlit as st

st.title('Portada')
st.write('El presente trabajo es un análisis profundo de los siniestros viales ocurridos en la Ciudad Autonoma de Buenos Aires (CABA)')
st.page_link("pages/01_Contexto.py",label=" 🏁 Comenzar")
st.markdown('#### Haga click en los diferentes items para ir a las secciones del análsis.')









st.page_link("pages/01_Contexto.py", label=" -> Ir a Contexto")
st.page_link("pages/02_Objetivo.py",label=" -> Ir a Objetivos")
st.page_link("pages/03_Analisis_Temporal.py",label=" -> Ir al Análisis Temporal")
st.page_link("pages/04_Analisis_por_Victima_Fatal.py",label=" -> Ir al Análisis por victima fatal")
st.page_link("pages/05_Analisis_por_Victima_No_Fatal.py",label=" -> Ir al Análisis por victima no fatal")
st.page_link("pages/06_Analisis_Geografico_Fatal.py", label=" -> Ir al Mapa de Hechos Fatales")
st.page_link("pages/07_Analisis_Geografico_No_Fatal.py",label=" -> Ir al Análisis Geográfico de Hechos No Fatales")
st.page_link("pages/08_KPI.py",label=" -> Ir a los KPI")
st.page_link("pages/09_Conclusiones.py",label=" -> Ir a las Conclusiones")
st.page_link("pages/10_Cierre.py",label=" -> Ir al Cierre")
