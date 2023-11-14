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
        print('Не получилось определить координаты :( \n'.center(os.get_terminal_size().columns))
    else:
        print(f'Широта {coordsx}, Долгота {coordsy} \n'.center(os.get_terminal_size().columns))

def get_possible_addresses(query):
    dadata_client = Dadata(os.getenv('API_KEY'), os.getenv('SECRET_KEY'))
    addresses = dadata_client.suggest(name="address", query=query, language='ru')
    return addresses