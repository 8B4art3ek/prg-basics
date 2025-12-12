# Tablica zawiera wartości:
# [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

# Stwórz program, który modyfikuje wartości tablicy, aby stworzyć tabliczkę mnożenia jak poniżej. Użyj instrukcji pętli. Wypisz tablicę.
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
] 

for i in range(5):
    for j in range(5):
        arr[i][j] = (i+1) * (j+1)

for row in arr:
    for col in row:
        print(str(col).rjust(2), end=" ")
    print()