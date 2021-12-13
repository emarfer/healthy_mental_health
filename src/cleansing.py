import json


def provinciasjson():
    """
    no recibe parámetros
    crea y devuelve un diccionario de cod_prov : nombre_prov para hacer correspondencia con geojson
    
    """
    geo_json = r"../data/socioecon/spain_provinces.geojson"
    with open (geo_json) as geo_file:
        provincias = json.load(geo_file)

    cod_prov = {}
    for i in range(52):    
        cod_prov[provincias['features'][i]['properties']['cod_prov']] = provincias['features'][i]['properties']['name']
    
    return cod_prov


def comunidadesjson():
    """
    no recibe parámetros
    crea y devuelve un diccionario de cod_comunidad : nombre_com para hacer correspondencia con geojson
    
    """
    geo_json = r"../data/socioecon/comunidades.geojson"
    with open (geo_json) as geo_file:
        comunidades = json.load(geo_file)
    
    cod_com = {}
    for i in range(19):    
        cod_com[comunidades['features'][i]['properties']['cod_ccaa']] = comunidades['features'][i]['properties']['name']
    
    return cod_com

def reverseprovinciasjson():
    """
    no recibe parámetros
    crea y devuelve un diccionario de cod_prov : nombre_prov para hacer correspondencia con geojson
    
    """
    geo_json = r"../data/socioecon/spain_provinces.geojson"
    with open (geo_json) as geo_file:
        provincias = json.load(geo_file)

    cod_prov = {}
    for i in range(52):    
        cod_prov[provincias['features'][i]['properties']['name']] = provincias['features'][i]['properties']['cod_prov']
    
    return cod_prov