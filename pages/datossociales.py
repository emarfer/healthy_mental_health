#from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium
import streamlit as st


def app():
    
    # st.write("""
    # ### Mapa vacío:
    # """)
    # mapavacio = folium.Map(location=[37.39161,-5.97640], zoom_start=12, tiles='CartoDB positron')
    # folium_static(mapavacio)

    st.write("""
    ### Renta media por hoga / problemas de salud mental en atención primaria:
    """)
    f=codecs.open("output/dual_renta_at_prim.html", 'r')
    mapa = f.read()
    components.html(mapa,height=550,width=900,scrolling=True)
    
