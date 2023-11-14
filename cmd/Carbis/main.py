import sys
sys.path.append('internal/api.py')
import internal.api as api

while True:
    user_input = input("Введите адрес: ")
    possible_addresses = api.get_possible_addresses(user_input)
    
    print("Возможные адреса:")
    for address in possible_addresses:
        print(address)
    
    chosen_address_index = int(input("Выберите номер адреса: ")) - 1
    chosen_address = possible_addresses[chosen_address_index]
    
    coordinates = api.get_coords(chosen_address['value'])