import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import codecs

def app():
    st.write("""
             Número de suicidios por mes del año y sexo
             """  )
    
    sui=codecs.open("output/fig_sui.html", 'r')
    sui_sex = sui.read()
    components.html(sui_sex,height=550,width=900,scrolling=True)
    
    st.write("""
            Muertes por trastornos mentales por sexo, evolución anual
             """  )
    
    muer=codecs.open("output/fig_muer.html", 'r')
    muer_sex = muer.read()
    components.html(muer_sex,height=550,width=900,scrolling=True)