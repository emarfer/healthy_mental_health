import streamlit as st
import src.managedata as dat

def app():

    st.write('Selecciona un género de trastorno mental')
    tras = st.selectbox("selecciona un tipo de trastorno", dat.list_tras())
    if tras == 'Explora los tipos de trastornos':
        st.stop()
    grafito = dat.grafico_tit(tras)
    diag = st.selectbox("seleciona un subtipo de trastorno",dat.list_sub(tras))
    if diag == 'Explora los tipos de trastornos':
        st.stop()
    grafi = dat.grafico(diag)