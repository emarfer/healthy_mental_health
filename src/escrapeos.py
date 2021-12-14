import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime

def capitulos(url,elemento):
    """
    recibe una url y el elemento que vamos a buscar dentro de su html
    escrapea por la web recogiendo lso elementos que queremos(capítulos)
    hace un selección de estos datos y sus strings
    devuleve un dataframe con los capítulos principales
    
    """
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")
    head_line = soup.find_all(elemento)
    cap = {}
    for h in head_line[1:-2]:
        cap[h.getText()[:-8].split(' ',1)[0][1:-1]] = h.getText()[:-8].split(' ',1)[1]
    return pd.DataFrame([[key,cap[key]] for key in cap.keys()], columns = ["cap","title"])

def diagnostics(url,elemento):
    """
    recibe una url y el elemento que vamos a buscar dentro de su html
    escrapea por la web recogiendo lso elementos que queremos(subcapítulos)
    hace un selección de estos datos y sus strings
    devuleve un dataframe con los capítulos principales
    
    """
    
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")
    tags = soup.find_all(elemento)
    
    dia = {}
    for t in tags[12:-65]:
        dia[t.getText()[:110].split(' ',1)[0]] = t.getText()[:110].split(' ',1)[1]
    return pd.DataFrame([[key,dia[key]] for key in dia.keys()], columns = ["code","diag"])
    
def calendariolunar(url_,range1,range2):
    """
    recibe una url y el rango de años de los que queremos datos
    (range2 = año después del año que queremos los datos)
    escrapea por la web recogiendo los datos de fechas de las fases de las lunas
    devuelve un dataframe con fecha y fase luna    
    """
    
    
    callunar = []
    for i in range(range1,range2):
        
        url = f'{url_}{i}'
        html = requests.get(url,verify=False)
        soup = BeautifulSoup(html.content,"html.parser")
        lunar_tab = soup.findAll('table')[0]
        
        for l in lunar_tab.findAll('tr'):
            callunar.append(l.getText().strip())
            
    lunas = {}
    for luna in callunar:
        lunas[luna[-10:].strip()] = luna[:-10].strip()
    
    lunas_df = pd.DataFrame([[key, lunas[key]] for key in lunas.keys()],columns = ['fecha','moon'])
    lunas_df["fecha_Date"] =pd.to_datetime(lunas_df.fecha,dayfirst=True)
    return lunas_df
    
    