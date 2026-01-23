# Dwuwymiarowa tablica o rozmiarze 2 na 4 zawiera liczby całkowite. Stwórz program, który wypisuje wartości tablicy w wierszach i kolumnach.

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

for row in arr: 
    for col in row:
        print(col, end=" ")
    print()