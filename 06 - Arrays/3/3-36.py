# Stwórz funkcję, która konwertuje tablicę dwuwymiarową (2D) na jednowymiarową (1D). Następnie stwórz program, który wypisuje tablicę 1D dla następujących tablic 2D.
# 2 3
# 1 5

# 5 0 3 7 5
# 9 0 9 1 2

# 2 1
# 3 5
# 7 4
# 2 6

def flatten_2d(arr):
    result = []
    for row in arr:
        for col in row:
            result.append(col)
    return result

matrices = [
    [
        [2, 3],
        [1, 5]
    ],
    [
        [5, 0, 3, 7, 5],
        [9, 0, 9, 1, 2]
    ],
    [
        [2, 1],
        [3, 5],
        [7, 4],
        [2, 6]
    ]
]

for m in matrices:
    flat = flatten_2d(m)
    print(flat)
