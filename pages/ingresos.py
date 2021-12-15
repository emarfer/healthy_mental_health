import streamlit as st
import pandas as pd
import plotly.express as px
import pandas as pd
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
import plotly.graph_objects as go
import streamlit.components.v1 as components
import codecs

def app():
    st.write("""
            Edad - trastornos mentales
            
            """)
       
    edad=codecs.open("output/fig_edad.html", 'r')
    edad_tras = edad.read()
    components.html(edad_tras,height=550,width=900,scrolling=True)
    
    
    
    st.write('días ingreso - trastorno mental')
    dias =codecs.open("output/fig_dias.html", 'r')
    dias_tras = dias.read()
    components.html(dias_tras,height=550,width=900,scrolling=True)
    
