import streamlit as st
import src.managedata as dat

def app():


    tras = st.selectbox("selecciona un tipo de trastorno", dat.list_tras())
    diag = st.selectbox("seleciona un subtipo de trastorno",dat.list_sub(tras))
    grafi = dat.grafico(diag)