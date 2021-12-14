import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    trastornos = pd.read_csv('output/trastornos.csv')
    trastornos = trastornos.set_index('cap')
    st.dataframe(trastornos) 
    at_title = pd.read_csv('output/yearcie10.csv')
    fig = px.line(at_title, x="Año", y="Casos",color = 'cei10')
    st.plotly_chart(fig, use_container_width=True)
    