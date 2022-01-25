import streamlit as st
import pandas as pd
import requests
from urllib.parse import urlencode
from geopy.geocoders import Nominatim
import src.locali as loca
from geopy.geocoders import Nominatim
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
 
    
    st.title('Busca ayuda')
    st.write('Inserta tu ubiación y luego la distancia en metros máximia que quieres recorrer y te mostrarermos una lista de dispositivos de salud mental, su direcciones y teléfonos')
    
    lugar = st.text_input('¿Dónde estás?')
    if lugar == '':
        st.stop()
    radio = st.number_input('Distancia máxima que quieres recorrer',value =0)
    if radio == 0:
        st.stop()
    lat = loca.latitu(lugar)
    lng = loca.longi(lugar)
    st.write(f'Buscando dispositivos de salud mental a {radio} metros de {lugar}')
    st.write(loca.localizaciones(lugar,radio))
   
    
    
    
    # st.write('The current movie title is', title)