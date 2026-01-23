# Plik cities.json zawiera dane o wybranych miastach w Polsce. Otwórz plik json w edytorze i przejrzyj jego zawartość. Zauważ, że plik zawiera tablicę słowników.

# Następnie napisz program, który wypisuje informacje o miastach.

# Uwaga: użycie parametru encoding='utf-8' podczas otwierania pliku jest konieczne, ponieważ plik json zawiera również polskie znaki w nazwach miast, które muszą być poprawnie przetworzone. Pamiętaj, aby zawsze używać tego parametru przy otwieraniu plików zawierających znaki inne niż te z alfabetu łacińskiego.

import json

# Open the JSON file in read mode
with open('cities.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    data = json.load(file)

# Print the JSON data
for city in data:
    for key, value in city.items():
        print(key,':',value)
    print()