import streamlit as st
import src.managedata as dat
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
    
    st.sidebar.write(':copyright: Powered by [Ester Sinaxe](http://estersinatxe.blogspot.com/)')
 

    st.title('Compartaiva ingresos por sexo y tipo de trastorno y subtipo')
    st.write('''
             Tras estudiar los datos de la morbilidad hospitalaria en España, he observado también las grandes diferencias que hay por géneros
             En estos gráficos podrmos observar la evolución anual de los ingresos de hombres y mujeres en España por tipo de trastorno y también por subtipo
             ''')
    
    tras = st.selectbox('Explora los tipos de trastornos:', dat.list_tras())
    if tras == 'Explora los tipos de trastornos':
        st.stop()
    grafito = dat.grafico_tit(tras)
    diag = st.selectbox('Explora los subtipos de trastornos:',dat.list_sub(tras))
    if diag == 'Explora los subtipos de trastornos':
        st.stop()
    grafi = dat.grafico(diag)