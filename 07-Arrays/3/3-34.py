# W matematyce macierz to prostokątna tablica liczb, symboli lub wyrażeń, ułożonych w wierszach i kolumnach, np.:
# -7  12 38
# 41 -19 11

# Stwórz funkcję identity_matrix(n), która zwraca macierz jednostkową (tablicę 2D) o rozmiarze n.
# https://en.wikipedia.org/wiki/Identity_matrix

# Następnie stwórz funkcję, która wypisuje tablicę 2D w wierszach i kolumnach. Na koniec stwórz program, który wypisuje trzy macierze jednostkowe o wymiarach 3, 5 i 8. Przykładowy wynik:
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1

def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        matrix.append(row)
    return matrix

for matrix in (identity_matrix(3), identity_matrix(5), identity_matrix(8)):
    for row in matrix:
        print(*row)
    print()