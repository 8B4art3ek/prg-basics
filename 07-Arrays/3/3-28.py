# Dwuwymiarowa tablica zawiera następujące liczby:
# 7 3 7 9 0
# 2 9 0 1 5
# 3 8 6 4 7
# 8 7 1 1 5
# Stwórz program, który oblicza sumę wartości w ostatniej kolumnie.

arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

suma = 0
for row in arr:
    suma += row[-1]

print("Suma ostatniej kolumny:", suma)
