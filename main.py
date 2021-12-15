from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import hello
from pages import atprimaria
from pages import ingresos
from pages import teorias
from pages import datossociales
from pages import defunciones
from pages import grafiquillos

app = MultiPage()

app.add_page("Home", hello.app)
app.add_page('Atencion primaria', atprimaria.app)
app.add_page('Ingresos hospitalarios', ingresos.app)
app.add_page('¿Nos afecta la luna?', teorias.app)
app.add_page('socio económicos', datossociales.app)
app.add_page('Demasiadas muertes', defunciones.app)
app.add_page('comparativa', grafiquillos.app)








app.run()