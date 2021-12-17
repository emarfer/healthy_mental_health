import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_keplergl import keplergl_static
import streamlit.components.v1 as components
import codecs
import base64

def app():
    
    file_ = open("images/anigifpeq.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.sidebar.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True
        )   
    
    st.sidebar.write(':copyright: Powered by [Ester Sinaxe](http://estersinatxe.blogspot.com/)')
 
    
    st.header(
        '''
        Análisis de los datos de morbilidad hospitalaria (2016 - 2019)
        '''
    )
    
    st.write('''
             
             fuente: [INE - Encuesta de morbilidad hospitalaria](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176778&menu=resultados&secc=1254736195291&idp=1254735573175#!tabs-1254736195291)
             
              ''')
    
    st.subheader('Correlación de la Edad de los pacientes y tipo de trastorno mental')
    st.write('Se puede apreciar claramente, sin necesidad de leyendas, entre qué grupo se encuentran las demencias y en qué grupo están los problemas relacionados con con el desarollo psicológico')
       
    edad=codecs.open("output/fig_edad.html", 'r')
    edad_tras = edad.read()
    components.html(edad_tras,height=550,width=900,scrolling=True)
    
    
    st.subheader('Correlación entre los días que el paciente ha estado ingresado y el tipo trastorno mental padecido')
    st.write('(Tras estudiar los datos y los "outlayers", se ha reducido el grupo de estudio a pacientes que han estado ingresados como mucho 50 días)')
    st.write('''
             - Los pacientes que pasan más tiempo ingresados de media son los que padecen alguno de los Síndromes del comportamiento asociados con alteraciones fisiológicas y factores físicos como los trastornos de la ingestión de alimentos
             - Seguidos de los trastornos esquizotípicos(esquizofreina, psicóticos agudos) y del ánimo/afectivos(trastorno bipolar, depresión)
             ''')
       
    
    dias =codecs.open("output/fig_dias.html", 'r')
    dias_tras = dias.read()
    components.html(dias_tras,height=550,width=900,scrolling=True)
    
