import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    at_prim = pd.read_csv('data/psico_atprimaria.csv')
    at_title = at_prim.groupby(['Año','cei10']).agg({"Casos":"sum"}).reset_index()
    fig = px.line(at_title, x="Año", y="Casos",color = 'cei10')
    st.plotly_chart(fig, use_container_width=True)
    