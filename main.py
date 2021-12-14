from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import hello

app = MultiPage()

app.add_page("Index", hello.app)









app.run()