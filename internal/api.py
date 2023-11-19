import os

from dadata import Dadata


#ВЫВОД КООРДИНАТ ПО АДРЕСУ 
def get_coords(address, api_key, secret_key):
    dadata = Dadata(str(api_key), str(secret_key))
    coords = dadata.clean("address", address)
    coordsx = coords['geo_lat']
    coordsy = coords['geo_lon']

    if coordsx == None and coordsy == None:
        print('Не получилось определить координаты :( \n'.center(os.get_terminal_size().columns))
    else:
        print(f'Широта {coordsx}, Долгота {coordsy} \n'.center(os.get_terminal_size().columns))

#вЫВОД КОРРЕКТНОГО АДРЕСА (ПОДСКАЗКИ)
def get_possible_addresses(query, lang, api_key):
    dadata_client = Dadata(str(api_key))
    addresses = dadata_client.suggest(name="address", query=query, language=lang)
    return addresses
