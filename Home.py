import streamlit as st

st.title('Portada')
st.write('El presente trabajo es un análisis profundo de los siniestros viales ocurridos en la Ciudad Autonoma de Buenos Aires (CABA)')
st.page_link("pages/01_Contexto.py",label="▶️  Comenzar")
st.markdown('#### Haga click en los diferentes items para ir a las secciones del análisis.')

st.page_link("pages/01_Contexto.py", label=" -> Ir a Contexto")
st.page_link("pages/02_Objetivos.py",label=" -> Ir a Objetivos")
st.page_link("pages/03_Analisis_Temporal_Fatal.py",label=" -> Ir a Análisis Temporal Fatal")
st.page_link("pages/04_Analisis_Temporal_No_Fatal.py",label=" -> Ir a Análisis Temporal No Fatal")
st.page_link("pages/05_Analisis_por_Victima_Fatal.py",label=" -> Ir a Análisis por víctima fatal")
st.page_link("pages/06_Analisis_por_Victima_No_Fatal.py",label=" -> Ir a Análisis por víctima no fatal")
st.page_link("pages/07_Analisis_Geografico_Fatal.py", label=" -> Ir a Mapa de Hechos Fatales")
st.page_link("pages/08_Analisis_Geografico_No_Fatal.py",label=" -> Ir a Análisis Geográfico de Hechos No Fatales")
st.page_link("pages/09_KPIs.py",label=" -> Ir a KPIs")
st.page_link("pages/10_Conclusiones.py",label=" -> Ir a Conclusiones")
st.page_link("")
st.divider()