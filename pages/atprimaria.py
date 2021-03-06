import streamlit as st
import pandas as pd
import plotly.express as px
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
    
    st.sidebar.write(':copyright: Powered by [Ester Sinaxe](http://estersinatxe.blogspot.com/2015/12/su-mente-rota.html/)')
 
    
    
    st.header(
        '''
        Análisis de los datos en Atención Primaria:
        '''
    )
    
    st.write('''
            
             fuente: [Base de Datos Clínicos de Atención Primaria (BDCAP) del Sistema Nacional de Salud](https://pestadistico.inteligenciadegestion.mscbs.es/publicoSNS/S/base-de-datos-de-clinicos-de-atencion-primaria-bdcap)
             
              ''')
    
    st.write('(La útlima comunidad en empezar a presentar sus datos fue La Rioja, por eso solo mostramos los datos totales desde esta fecha)')
    
    st.header('Número de casos por año y tipos de trastorno mental'
    )
    st.write('Apreciamos un ligero aumento de casos anualmente en casi todos los tipos de trastorno')
    
    st.subheader('Los trastornos más diagnosticados son:')
    st.write('''
             - Trastornos neuróticos, trastornos relacionados con el estrés y trastornos somatomorfos (ansiedad, TOC)
             - Trastornos del estado de animo, trastornos afectivos (depresión, trastorno bipolar)
             - Trastornos mentales y de comportamiento debidos al consumo de psicotrópicos
             ''')
  
    

           
    prima=codecs.open("output/fig_atprim.html", 'r')
    prima_tras = prima.read()
    components.html(prima_tras,height=600, width=1000,scrolling=True)
    
    
    
    st.title("""
     Mapa comparativo Renta media por hogar / problemas de salud mental:
    """)
    st.write('Estudiamos si existe una correlación entre factores socieconómicos, a nivel macro, con la cantidad de casos relacionados con la salud mental en atención primaria, por comunidad autónoma')
    st.write('''
             - En el País Vasco observamos que, con altos niveles de renta hay pocos casos de salud mental
             - Mientras en Andalucía y Extremadura con muy poco nivel de renta por hogar, también hay muy pocos casos en atención primaria
             '''
             )
    st.write('Concluimos que, a nivel autonómico, no observamos ningún tipo de inferencia del nivel socioecómico en los problemas de salud mental')
    st.subheader('Comparativa por comunidades autónmas')
    f=codecs.open("output/dual_renta_at_prim.html", 'r')
    mapa = f.read()
    components.html(mapa,height=550,width=900,scrolling=True)
    

    