import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
import codecs

def app():
    
    st.header(
        '''
        Análisis de los datos en Atención Primaria
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
    st.write('Estudiamos una si existe una correlación entre factores socieconómicos, a nivel macro, con la cantidad de casos relacionados con la salud mental en atención primaria')
    st.write('''
             - Observamos en País Vasco con datos altos de nivel de renta hay menos casos de salud mental
             - Mientras en Andalucía y Extremadura con muy poco nivel de renta por hogar hay también muy pocos casos en atención primaria
             '''
             )
    st.write('Concluimos que a nivel macro no observamos inferencia del nivel socioecómico en salud mental')
    st.subheader('Comparativa por comunidades autónmas')
    f=codecs.open("output/dual_renta_at_prim.html", 'r')
    mapa = f.read()
    components.html(mapa,height=550,width=900,scrolling=True)
    

    