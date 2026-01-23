# Stwórz program, który:
# Wyświetla imię (name)
# Wyświetla hobby
# Wyświetla całą zawartość słownika
# Zmienia nazwisko (surname) na 'Nowak'
# Zmienia stan cywilny osoby (married)
# Dodaje płeć (gender): 'male'
# Dodaje nowe hobby: 'bicycle'
# Dodaje telefon służbowy do istniejących telefonów: '313131444'
# Wyświetla całą zawartość słownika (iteruj po elementach słownika)

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{
        "landline":"123444321",
        "mobile":"777888999"
    }
}

print(person["name"])
print(person["hobby"])
print(person)

person["surname"] = "Nowak"
print(person["surname"])

person["married"] = False
print(person["married"])

person["gender"] = "male"
print(person["gender"])

person["hobby"].append("bicycle")
print(person["hobby"])

person["phone"]["office"] = 313131444
print(person["phone"])

for key, value in person.items():
    print(f"{key}: {value}")