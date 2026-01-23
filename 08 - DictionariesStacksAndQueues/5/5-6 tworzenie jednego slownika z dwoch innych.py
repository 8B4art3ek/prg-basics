# Program zawiera dwa słowniki z danymi osobowymi:
# Napisz program, który tworzy słownik o nazwie person zawierający dane z dwóch pozostałych słowników (pięć par klucz-wartość). Wypisz zawartość słownika ‘person’.

basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading","swimming"]
}

person = basic_data | advanced_data
print(person)