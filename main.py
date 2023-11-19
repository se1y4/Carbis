import sys
import time
import os

import internal.api as api
import internal.db as db

user_api = str(input("Введите ваш API-ключ: \n"))
user_secret_key = str(input("Введите ваш секретный ключ: \n"))
user_lang = input("Выберите язык. Если поле оставить пустым, будет установлен русский язык.\n 1 - Русский \n 2 - Английский \n")
if user_lang == '2':
    user_lang = "en"
else:
    user_lang = "ru"
db.save_settings(user_api, user_lang)


while True:
    
    user_input_address = input("Введите адрес: \n")

    if user_input_address == 'q' or user_input_address == 'й':
        sys.exit()
    try:
        possible_addresses = api.get_possible_addresses(user_input_address, db.import_language(str(user_api)), user_api)
    except:
        print('Возможно вы ввели некорректный API-ключ, перезапустите программу и введите правильный ключ')
        break
    print("Возможные адреса:".center(os.get_terminal_size().columns))
    k = 0
    for address in possible_addresses:
        k += 1
        print(f"{k} - {address['value']}")
    
    chosen_address_index = int(input("\n Выберите номер адреса: ")) - 1
    chosen_address = possible_addresses[chosen_address_index]
    try:
        coordinates = api.get_coords(chosen_address['value'], user_api, user_secret_key)
    except:
        print('Возможно вы ввели некорректный секретный ключ, перезапустите программу и введите правильный ключ')
        break

    print("Введите q что бы выйти из программы.".center(os.get_terminal_size().columns))
    print("Программа будет автоматически перезапущена через 3 секунды.".center(os.get_terminal_size().columns))
    time.sleep(3)
