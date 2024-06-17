# Proyecto-Individual-2

Este proyecto trata de un análisis de datos para la realización de un dashboard sobre los accidentes fatales ocurridos en caba entre el 2016 y el 2021, ademas de los hechos no fatales con lesiones como resultados entre el 2019 y el 2021.

La tecnología utilizada para el desarrollo del dashboard es "Streamlit" para crear una aplicación web donde cualquiera con el link sea capaz de visualizarlo en cualquier dispositivo. Se usan componentes como pandas para trabajar los datasets, matplotlib y plotly para crear los gráficos; y Streamlit-Folium para crear un mapa interactivo de los hechos ocurridos.

El proyecto consta de: 
Dos archivos ipynb:
* EDA.ipynb: Es donde se realiza el análisis exploratorio de datos, se cuentan los nulos, se eliminan columnas redundantes y se crean los archivos que serán consumidos en el dashboard.
* ETL.ipynb: En este archivo se extraen los datos crudos de los archivos y se los transforma en formatos más tratables.

Un archivo .py:
* Home.py: Es la página de inicio que el cliente vé a la hora de ingresar al dashboard.

Dos archivos .txt:
* packages.txt: Indica a streamlit cloud qué paquetes se van a usar.
* requirements.txt: Indica a streamlit cloud qué librerías se van a usar.

Tres carpetas: 
* raw: Se alojan los datos crudos para ser transformados.
* src: Directorio donde se guardan  los datos ya extraidos y transformados para ser consumidos en el dashboard.
* pages: Aquí se encuentran todas y cada una de las páginas que se van a visualizar en el dashboard.

raw: 
* Barrios_por_comuna.csv: Indica qué barrios pertenecen a cada comuna.
* homicidios.csv: Trae información sobre los hechos que han terminado en fatalidades.
* lesiones_hechos.csv: Datos sobre los hechos no fatales.
* lesiones_victimas.csv: Datos sobre las victimas de los hechos no fatales.
* lesiones.csv: Es un merge entre lesiones_hechos y lesiones_victimas.
* pob_comunas_17.csv: Contiene el dato sobre la población total de CABA.
* victimas_fatales.csv: Información sobre las víctimas de hechos fatales.

src:
* Barrios.csv: Informa sobre que barrios pertenecen a cada comuna.
* fatales.csv: Datos sobre hechos y víctimas fatales.
* No_fatales.csv: Datos sobre hechos y víctimas no fatales
* Poblacion: Dato sobre la población de CABA.

pages: 
* 01_Contexto.py: Presenta una pequeña introducción al proyecto.
* 02_Objetivos.py: Presenta los objetivos elejidos para el proyecto.
* 03_Analisis_Temporal_Fatal.py: Realiza un análisis de casos fatales con respecto al tiempo.
* 04_Analisis_Temporal_No_Fatal.py: Realiza un análisis de casos no fatales con respecto al tiempo.
* 05_Analisis_por_Victima_Fatal.py: Realiza un análisis de casos fatales por las características de las víctimas.
* 06_Analisis_por_Victima_No_Fatal.py: Realiza un análisis de casos no fatales por las características de las víctimas.
* 07_Analisis_Geografico_Fatal.py: Realiza un análisis geográfico de los casos fatales.
* 08_Analisis_Geografico_No_Fatal.py: Realiza un análisis geográfico de los casos no fatales.
* 09_KPIs.py: Presenta un análisis de tipo KPI interactivo.
* 10_Conclusiones.py: Realiza un cierre al análisis.


# Reporte


* El año con más fatalidades es el año 2018 mientras que el año con más lesiones es 2019.
* La tendencia de casos fatales como no a lo largo del tiempo es a la baja.
* No existe una tendencia clara de aumentos de casos a lo largo del transcurso del año.
* El dia con mas casos fatales es el sábado, y con más lesiones es el viernes.
* Los picos de casos fatales como no fatales coinciden con las horas de los inicios y finalizaciones de las jornadas laborales. Cuando más gente hay en la calle.
* La amplia mayoria de casos son victimas hombre.
* Para ambos sexos el rango etario más afectado es entre 19 y 35 años.
* El vehículo más afectado es la moto, donde la mayoría de fallecidos y lesionados son los conductores.
* Los autos son los vehiculos más frecuentes en los victimarios.
* Las comunas con más casos fatales son la comuna 1, 4 y 9, mientras que las comunas con más lesiones son la 1, 15 y 4.
* Dos de los 3 kpis propuestos se cumplen: el de la diferencia porcentual del último semetre con respecto al anterior, y el de los accidentes en moto de 2021 con respecto a 2020. El kpi de reducir las lesiones un 5% del último semestre con relación al anterior no se cumple.

# Link:

El dashboard puede accederse a través del siguiente enlace:
https://proyecto-individual-2.streamlit.app

(Si la app se encuentra suspendida, hacer click en 'Yes, wake it up.')
