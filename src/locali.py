import requests
from urllib.parse import urlencode
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd

def latitu(lugar):
    geolocator = Nominatim(user_agent="sinatxe")
    location = geolocator.geocode(lugar)
    return location.latitude

def longi(lugar):
    geolocator = Nominatim(user_agent="sinatxe")
    location = geolocator.geocode(lugar)
    return location.longitude



def localizaciones(lugar,rad):
    lat = latitu(lugar)
    lng = longi(lugar)
    api_key = os.getenv("google")
    
    places = "https://maps.googleapis.com/maps/api/place/search/json"
    params = {
        "key": api_key,
        "location": f"{lat},{lng}",
        "radius": rad,
        "keyword": "Salud mental"
    }
    params_encoded = urlencode(params)
    places_url = f"{places}?{params_encoded}"

    facilites = requests.get(places_url)
    dispo = facilites.json()
    
    dic_ids = []
    for d in dispo['results']:
        dic_ids.append(d['place_id'])
    localidades = []
    for ids in dic_ids:
        details = requests.get(f"https://maps.googleapis.com/maps/api/place/details/json?place_id={ids}&key={api_key}").json()
        if 'formatted_phone_number' in details['result'].keys():
            localidades.append(f"{details['result']['name']}.\n DIRECCIÓN: Dirección: {details['result']['vicinity']}.\nTELÉFONO: {details['result']['formatted_phone_number']}")
    return localidades
        

    
