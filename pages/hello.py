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
    
    file_ = open("images/anigifpeq.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.sidebar.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True
        )   
    
    st.sidebar.write(':copyright: Powered by [Ester Sinaxe](http://estersinatxe.blogspot.com/2015/12/su-mente-rota.html)')
 
    
    """### gif from local file"""
    st.title('Salud mental', anchor=None)
    st.subheader('''
             Para la Organización Mundial de la Salud (OMS), la [salud mental](https://feafesgalicia.org/ES/content/salud-mental) se define como “un estado de bienestar en el cual la persona es consciente de sus propias capacidades, puede afrontar las tensiones normales de la vida, puede trabajar de forma productiva y fructífera y es capaz de hacer una contribución a su comunidad”
             ''')
    
    
    

    
    st.title('¿Por qué este estudio?')
    st.subheader('''
             Creo que necesitamos hablar abiertamente de salud mental. Es urgente implementar campañas de concienciación para manternos informados ya que es un problema que nos afecta a todos, ya sea a nosotros mismos o alguien muy cercano.
             ''')
    st.subheader('''
             Según la Confederación de salud mental [1 de cada 4 españoles tendrá un trastorno mental a lo largo de su vida](https://comunicalasaludmental.org/guiadeestilo/la-salud-mental-en-cifras/)
             ''')
    st.subheader('''
             En este estudio observaremos algunos patrones que podrán ayudar a desarrollar estas campañas en función diversos parámetros, como sexo o época del año.          
             ''')
    
