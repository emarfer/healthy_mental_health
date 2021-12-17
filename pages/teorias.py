import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
 
    st.title("""
            ¿Somos unos lúnaticos?        
            
            """)
    
    st.write('He relacionado las fechs de ingreso con las fechas de las 4 fases de la luna para observar si es verdad que la luna llena nos afecta tanto como se comenta')
    st.write('En el gráfico podemos observar que no hay mucha diferencia entre el número de ingresos en función del estado de la luna')

    
    luna=codecs.open("output/luna.html", 'r')
    luna_ht = luna.read()
    components.html(luna_ht,height=550,width=900,scrolling=True)
    
    
    st.title("""
             ¿Y el Sol? ¿Las horas de luz en España nos influyen?
             """)
    st.write('Como pasa con la luna podemos ver que tampoco hay una correlación entre horas de luz por mes y el númro de ingresos')
    luz=codecs.open("output/fig_luz.html", 'r')
    luz_ht = luz.read()
    components.html(luz_ht,height=550,width=900,scrolling=True)
    



