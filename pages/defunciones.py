import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import codecs
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
    
    st.sidebar.write(':copyright: Powered by [Ester Sinaxe](http://estersinatxe.blogspot.com/2015/12/su-mente-rota.html/)')
 
    st.title('Análisis de suicidos y muertes por trastornos mentales')
    st.write('''
                fuente: [INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176780&menu=ultiDatos&idp=1254735573175)
                
                Lo que más me ha llamado la atención de este análisis es ver las grandes diferencias por sexo que existen
                 ''')
    st.subheader("""
             Número de suicidios por mes del año y sexo
             """  )
    st.write('''
             - Reseñar que el número de suicidos de hombres es muy superior al de mujeres
             - Además en los meses de juliio y marzo son los meses en los que más suicidios de hombres y mujeres hay respectivamente.
             ''')
    
    sui=codecs.open("output/fig_sui.html", 'r')
    sui_sex = sui.read()
    components.html(sui_sex,height=550,width=900,scrolling=True)
    
    st.subheader("""
            Evolución anual por género del número de muertes por trastornos mentales            
             """  )
    st.subheader("""            
            (no suicidios)            
             """  )
    st.write('Entre estas causas encontramos las debidas al consumo de psicotrópicos o trastornos alimenticios')
    st.write('''
             - Hay un claro aumento a lo largo de los años
             - También observamos que en estos casos, hay más número de muertes de mujeres que de hombres
             ''')
    
    muer=codecs.open("output/fig_muer.html", 'r')
    muer_sex = muer.read()
    components.html(muer_sex,height=550,width=900,scrolling=True)