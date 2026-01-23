# Poniższe dane zawierają informacje o liczbie produktów dostępnych w sklepie komputerowym. Napisz program, który wypisuje:
# listę produktów i ich ilość
# całkowitą liczbę produktów w sklepie

items = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

print(items)

total = 0
for key, value in items.items():
    total += int(value)

print(f"Total: {total}")