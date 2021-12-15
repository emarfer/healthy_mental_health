
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
# def renombra_id(x):
#     x = f"Frase {x}"
#     return x


# def grafico(trastorno):
#     data = cargadataframe()
#     data = data[(data["character_name"]==f"{personaje}")]
#     data = data[["frase","polarity"]].reset_index(drop=True)
#     data["frase"] = data.index+1
#     data["frase"] = data.frase.apply(renombra_id)
#     return data


# def bar_1():
#     data = cargadataframe()
#     data = data.groupby("character_name").agg({"character_name":'count'}).rename(columns={"character_name":"character_name", "character_name":"número de frases"}).reset_index().set_index("character_name", drop=True)
#     return data


