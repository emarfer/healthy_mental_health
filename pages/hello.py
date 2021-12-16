from typing import Sized
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import os
import dotenv
import pandas as pd
import base64

def app():
    """### gif from local file"""
    st.title('Salud mental', anchor=None)
    st.subheader('''
             Para la Organización Mundial de la Salud (OMS), la [salud mental](https://feafesgalicia.org/ES/content/salud-mental) se define como “un estado de bienestar en el cual la persona es consciente de sus propias capacidades, puede afrontar las tensiones normales de la vida, puede trabajar de forma productiva y fructífera y es capaz de hacer una contribución a su comunidad”
             ''')
    
    
    
    file_ = open("images/anigif.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True
        )   
    
    
    st.title('¿Por qué este estudio?')
    st.write('''
             Creo que necesitamos hablar abiertamente de salud mental. Es urgente desarrollar campañas sobre prevención y conciención para manternos informados ya que es un problema que nos afecta a todos.
             ''')
    st.write('''
             Según la Confederación de salud mental [1 de cada 4 españoles tendrá un trastorno mental a lo largo de su vida](https://comunicalasaludmental.org/guiadeestilo/la-salud-mental-en-cifras/)
             ''')
    st.write('''
             En este estudio observaré cómo dirigir las campañas en función de trastorno, época del año, edad y género             
             ''')