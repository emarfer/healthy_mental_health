
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def cargadataframe():
    data = pd.read_csv("output/streamlitmor.csv")
    return data


def list_tras():
    data = cargadataframe()
    lista = list(data.title.unique())
    lista.insert(0, "Explora los tipos de trastornos")
    return lista

def list_sub(tras):
    data = cargadataframe()
    data = data[data['title']==tras]
    lista = list(data.diag.unique())
    lista.insert(0, "Explora los tipos de trastornos")
    return lista

def grafico(diag):
    data = cargadataframe()
    data = data[(data["diag"]==f"{diag}")].groupby(['year','month','SexNom']).agg({'day':'count','fecha_ing':'min'}).reset_index()
    fig = px.line(data, x="fecha_ing", y="day",color = 'SexNom')
    
    return st.plotly_chart(fig, use_container_width=True)


def grafico_tit(tras):
    data = cargadataframe()
    data = data[(data["title"]==f"{tras}")].groupby(['year','month','SexNom']).agg({'day':'count','fecha_ing':'min'}).reset_index()
    fig = px.line(data, x="fecha_ing", y="day",color = 'SexNom')
    
    return st.plotly_chart(fig, use_container_width=True)


#streamlitmor[streamlitmor['diag']=='Episodio maníaco'].groupby(['year','month','SexNom']).agg({'day':'count','fecha_ing':'min'}).reset_index()


