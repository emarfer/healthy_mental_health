# La salud mental importa

# ¿Por qué este estudio?:

![](https://c.tenor.com/DCNj0NL-kvMAAAAC/mental-health-matters-your-mind-matters.gif)

#### Creo que necesitamos hablar abiertamente de salud mental. Es urgente desarrollar campañas sobre prevención y conciención para manternos informados ya que es un problema que nos afecta a todos.
#### Según la Confederación de salud mental [1 de cada 4 españoles tendrá un trastorno mental a lo largo de su vida](https://comunicalasaludmental.org/guiadeestilo/la-salud-mental-en-cifras/)
#### En este estudio observaré cómo dirigir las campañas en función de trastorno, época del año, edad y género  

## Presentación de resultados con [Streamlit](https://streamlit.io/)


## Método:
- Estudio de diferentes archivos con datos sobre salud mental en España (fuentes)
    - Atención primaria: [Base de Datos Clínicos de Atención Primaria (BDCAP) del Sistema Nacional de Salud](https://pestadistico.inteligenciadegestion.mscbs.es/publicoSNS/S/base-de-datos-de-clinicos-de-atencion-primaria-bdcap)

    - Morbilidad hospitalaria: [INE - Encuesta de morbilidad hospitalaria](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176778&menu=resultados&secc=1254736195291&idp=1254735573175#!tabs-1254736195291)

    - Causas de muerte [INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176780&menu=ultiDatos&idp=1254735573175)

    - Datos socioeconómicos [INE](https://www.ine.es/dynt3/inebase/index.htm?padre=1928&capsel=1928)

- Recogida de información sobre los diagnósticos de salud mental según la Organización Mundial de la Salud, fechas de las fases de la luna y horas de luz en ESpaña



## Estructura:
- **Data (y subcarpetas)**: archivos csv/excel con la información a estudiar
-  **Images**: archivos de imagen para cargar en streamlit
- **Notebooks**: archivos de jupyter notebook con limpieza, estudio y visualización de datos
- **output**: arhivos con datos estuidiados + gráficos html para streamlit
- **pages**: archivos .py de la configuración de páginas de streamlit
- **src**: archivos .py con funciones para la limpieza y estudio de de datos + streamlit
- **main.py + multipage.py**: estructura y llamada streamlit



## Librerías:

* [sys](https://docs.python.org/3/library/sys.html)
* [pandas](https://pandas.pydata.org/)
* [os](https://docs.python.org/3/library/os.html)
* [dotenv](https://pypi.org/project/python-dotenv/)
* [seaborn](https://seaborn.pydata.org/)
* [matplotlib](https://matplotlib.org/)
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [json](https://www.json.org/json-en.html)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [matplotlib.pyplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
* [plotly.express](https://plotly.com/python-api-reference/plotly.express.html)
* [folium](http://python-visualization.github.io/folium/)
* [numpy](https://numpy.org/)
* [codecs](https://docs.python.org/3/library/codecs.html)