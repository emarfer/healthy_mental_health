from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import hello
from pages import atprimaria
from pages import ingresos
from pages import teorias
from pages import defunciones
from pages import grafiquillos
from pages import helpin

app = MultiPage()

app.add_page("Home", hello.app)
app.add_page('Atencion primaria', atprimaria.app)
app.add_page('Ingresos hospitalarios', ingresos.app)
app.add_page('Luces y sombras', teorias.app)
app.add_page('Demasiadas muertes', defunciones.app)
app.add_page('Comparativa', grafiquillos.app)
app.add_page('Pide ayuda', helpin.app)








app.run()