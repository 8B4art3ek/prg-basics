# Stwórz funkcję transpose_matrix(m), która zwraca transponowaną macierz m:
# https://en.wikipedia.org/wiki/Transpose

# Następnie stwórz program, który wypisuje transponowane macierze, w wierszach i kolumnach, dla następujących macierzy.
# 1 2 3
# 4 5 6
# 7 8 9

# 1 2 3 4 5
# 6 7 8 9 0

# 5 6 7 8

def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])

    t = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(m[i][j])
        t.append(new_row)
    return t

matrices = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0]
    ],
    [
        [5, 6, 7, 8]
    ]
]

for m in matrices:
    tm = transpose_matrix(m)
    for row in tm:
        print(*row)
    print()