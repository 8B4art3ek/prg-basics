# Napisz program, który pobiera z klawiatury dane o zakupionym produkcie:

# nazwa
# cena (liczba rzeczywista z dwoma miejscami po przecinku)
# czy zapłacono (tak/nie)
# Następnie program zapisuje dane produktu w pliku product.json. Zwróć uwagę na poprawne typy danych opisujące produkt (string, float, bool).

import json

product = {}

# read product data from keyboard
product['name'] = input("Podaj nazwę produktu: ")
product['price'] = float(input("Podaj cenę: "))
paid_input = input("Czy zapłacono? (tak/nie): ").strip().lower()
product['paid'] = True if paid_input == "tak" else False

# save product data to json file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, ensure_ascii=False, indent=4)

print("Zapisano dane produktu do pliku product.json")