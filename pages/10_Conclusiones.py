import streamlit as st 

st.page_link('Home.py',label='🏠 Inicio')

st.page_link('pages/09_KPIs.py',label='⬅️ Anterior: KPIs')
    
st.title('Conclusiones')

st.write('Luego del análisis estadístico podemos sacar algunas conclusiones:')
st.write(' -> Análisis Temporal:')
st.write('* La tendencia de casos tanto fatales como no, es a la baja.')
st.write('* Durante el año 2020 se han reducido, con diferencia, los casos debido a la menor circulación de personas en la vía pública.')
st.write('* No existe una tendencia clara de aumentos de casos a medida que transcurre el año. Sin embargo Mayo es el mes más consistente en cantidad de casos, salvo algunas excepciones.')

st.write(' -> Análisis por Victima:')
st.write('* El rango etario predominante es de 19-35.')
st.write('* Hay más víctimas masculinas que femeninas.')
st.write('* El principal vehículo afectado es la Moto, generalmente por autos.')

st.write(' -> Análisis Geográfico:')
st.write('* La comuna más accidentada es la 1.')
st.write('* Los horarios coinciden con las horas de entrada y salida de los trabajos.')
st.write('* La calzada más común son las avenidas.')

st.divider()