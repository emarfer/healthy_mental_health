import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.write("""
             Edad - trastornos mentales
             
             """)
    morbil = pd.read_csv('data/morbilidad_Fgen.csv')
    anteriores = morbil[morbil['fecha_ing'] < '2016'].index
    morbil.drop(anteriores,inplace = True)
    fig = px.box(morbil, x="cap", y="Edad", color = "cap")
    st.plotly_chart(fig, use_container_width=True)