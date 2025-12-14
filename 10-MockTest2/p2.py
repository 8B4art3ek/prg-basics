# (p2.py) Tablica zawiera co najmniej 3 liczby całkowite. Wszystkie liczby w tablicy są równe z wyjątkiem jednej. Zdefiniuj funkcję f(arr), która zwraca liczbę w tablicy arr, która różni się od pozostałych liczb. 
# Przykład: 
# f([7,7,7,7,7,5,7,7]) → 5

def f(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
        
print(f([7,7,7,7,7,5,7,7]))