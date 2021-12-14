import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import sqlalchemy as alch
import os
import dotenv
import pandas as pd
import base64

def app():
    """### gif from local file"""
    file_ = open("images/giphy.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
        )   