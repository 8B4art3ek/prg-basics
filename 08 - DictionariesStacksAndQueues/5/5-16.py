# Plik computer.json zawiera przykładowe dane komputera. Otwórz plik json w edytorze i przejrzyj jego zawartość. Zauważ, że plik zawiera pojedynczy słownik danych.

# Następnie napisz program, który wypisuje informacje o komputerze.

import json

# Open the JSON file in read mode
with open('computer.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    data = json.load(file)

# Print the JSON data
for key, value in data.items():
    print(key,':',value)