import internal.api as api
import sys
import time
import os


while True:
    
    user_input_address = input("Введите адрес: \n")

    if user_input_address == 'q' or user_input_address == 'й':
        sys.exit()

    possible_addresses = api.get_possible_addresses(user_input_address)
    print("Возможные адреса:".center(os.get_terminal_size().columns))
    k = 0
    for address in possible_addresses:
        k += 1
        print(f"{k} - {address['value']}")
    
    chosen_address_index = int(input("\n Выберите номер адреса: ")) - 1
    chosen_address = possible_addresses[chosen_address_index]
    
    coordinates = api.get_coords(chosen_address['value'])
    print("Введите q что бы выйти из программы.".center(os.get_terminal_size().columns))
    print("Программа будет автоматически перезапущена через 3 секунды.".center(os.get_terminal_size().columns))
    time.sleep(3)
