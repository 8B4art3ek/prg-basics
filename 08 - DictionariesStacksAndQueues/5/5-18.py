# Plik dogs.json zawiera dane o psach. Napisz program, który wypisuje informacje o psach młodszych niż 5 lat.

import json

with open("dogs.json", "r", encoding="utf-8") as file:
    dogs = json.load(file)

for dog in dogs:
    if dog.get('age', 0) < 5:
        print(f"Imię: {dog.get('name')}, Wiek: {dog.get('age')}, Rasa: {dog.get('breed')}")