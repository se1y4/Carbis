import internal.api as api
import sys
import time

while True:
    user_input = input("Введите адрес: \n")
    if user_input == 'q':
        sys.exit()
    possible_addresses = api.get_possible_addresses(user_input)
    print("Возможные адреса:")
    k = 0
    for address in possible_addresses:
        k += 1
        print(f"{k} - {address['value']}")
    
    chosen_address_index = int(input("Выберите номер адреса: ")) - 1
    chosen_address = possible_addresses[chosen_address_index]
    
    coordinates = api.get_coords(chosen_address['value'])
    print("Введите q что бы выйти из программы.")
    time.sleep(2)
