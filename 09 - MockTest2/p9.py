# (p9.py) Plik data.csv zawiera listę pracowników firmy ABC-Data. Zdefiniuj funkcję f(value), która zwraca liczbę pracowników, których wynagrodzenie jest większe lub równe podanej wartości. 
# Przykład: 
# f(9200) porównaj swój wynik z innymi studentami
# f(11640) porównaj swój wynik z innymi studentami

import csv

def f(value):
    count = 0
    with open("data.csv", "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = float(row["salary"])
            if salary >= value:
                count += 1
    return count

print(f(9200))   # liczba pracowników z pensją >= 9200
print(f(11640))  # liczba pracowników z pensją >= 11640