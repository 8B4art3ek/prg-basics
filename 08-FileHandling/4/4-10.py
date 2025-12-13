# Plik clothing.csv zawiera listę ubrań w magazynie. Napisz program, który wypisuje te produkty, których cena jest niższa niż 60, a stan magazynowy jest mniejszy niż 40.

import csv

try:
    with open("clothing.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            price = float(row["Price"])
            stock = int(row["Stock_Quantity"])

            if price < 60 and stock < 40:
                print(f"{row["Product_Name"]} | price: {price} | stock: {stock}")

except FileNotFoundError:
    print("Nie ma takiego pliku.")