# Tablica zawiera liczby całkowite:
# [[-38, 19], [5,40],[-7,11],[29,16]]

# Stwórz program, który znajduje najmniejszą i największą wartość w tablicy oraz w którym wierszu i kolumnie się one znajdują.

arr = [
    [-38, 19], 
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_val = arr[0][0]
max_val = arr[0][0]
min_pos = (0, 0)
max_pos = (0, 0)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min_val:
            min_val = arr[i][j]
            min_pos = (i, j)
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_pos = (i, j)

print(f"Min: {min_val} na pozycji {min_pos}")
print(f"Max: {max_val} na pozycji {max_pos}")