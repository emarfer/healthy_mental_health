import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import codecs

def app():
    st.write("""
            ¿Somos unos lúnaticos?        
            
            """)
#     ing_lunas = pd.read_csv('output/total_lunas.csv')
#     lunismo = px.histogram(ing_lunas, x="luna",y='total',color = 'luna')
#     st.plotly_chart(lunismo, use_container_width=True)
    
    luna=codecs.open("output/luna.html", 'r')
    luna_ht = luna.read()
    components.html(luna_ht,height=550,width=900,scrolling=True)
    
    
    
    #fig_luz
    
    st.write('Pues parece que la luna no afeca tanto nuestros ingresos por salud mental...')
    
    
    st.write("""ingresos por mes y horas de luz
             
             """)
    
    luz=codecs.open("output/fig_luz.html", 'r')
    luz_ht = luz.read()
    components.html(luz_ht,height=550,width=900,scrolling=True)
    
#     ingresos_mes_luz = pd.read_csv('output/ingresos_mes_luz.csv')
#     fig_03 = go.Figure(data=[
#     go.Bar(name="ingresos",x=ingresos_mes_luz['mes_n'],y=ingresos_mes_luz['count'],
#            marker_color='skyblue'
          
#           ),
#     go.Line(name = 'horas luz',y=ingresos_mes_luz["horas_m"], x=ingresos_mes_luz["mes_n"],
#             marker_color='yellow'
#            )   
    
#     ])
#     st.plotly_chart(fig_03.update_layout(barmode='group'))




