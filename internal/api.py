from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from dadata import Dadata
import os


def get_coords(address):
    dadata = Dadata(os.getenv('API_KEY'), os.getenv('SECRET_KEY'))
    coords = dadata.clean("address", address)
    coordsx = coords['geo_lat']
    coordsy = coords['geo_lon']
    if coordsx == None and coordsy == None:
        print('Не получилось определить координаты :(')
    else:
        print(f'Широта {coordsx}, Долгота {coordsy}')

def get_possible_addresses(query, preferred_language):
    dadata_client = Dadata(os.getenv('API_KEY'), os.getenv('SECRET_KEY'))
    addresses = dadata_client.suggest(name="address", query=query, language='en')
    return addresses