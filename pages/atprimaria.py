import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
import codecs

def app():

    # at_title = pd.read_csv('output/yearcie10.csv')
    # fig = px.line(at_title, x="Año", y="Casos",color = 'cei10')
    # fig.update_layout(width=1000,height=500)
    # st.plotly_chart(fig, use_container_width=True)
    
           
    prima=codecs.open("output/fig_atprim.html", 'r')
    prima_tras = prima.read()
    components.html(prima_tras,height=550, width=900,scrolling=True)
    
    st.write("""
    ### Renta media por hogar / problemas de salud mental en atención primaria:
    """)
    f=codecs.open("output/dual_renta_at_prim.html", 'r')
    mapa = f.read()
    components.html(mapa,height=550,width=900,scrolling=True)
    

    