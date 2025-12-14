# (p3.py) Tablica dwuwymiarowa zawiera taką samą liczbę wierszy i kolumn. Zdefiniuj funkcję f(array2D), która dla danej tablicy dwuwymiarowej array2D zwraca True, gdy suma wartości w każdym wierszu tablicy jest równa sumie wartości w odpowiadającej kolumnie (np. suma wartości w wierszu 3 jest równa sumie wartości w kolumnie 3), a w przeciwnym razie False. 
# Przykład: 
# f([[3,7,2], [4,2,5], [5,2,1]]) → True 
# f([[3,7,2], [4,2,5], [9,2,1]]) → False

def f(array2D):
    n = len(array2D)

    for i in range(n):
        row_sum = sum(array2D[i])
        col_sum = 0
        for j in range(n):
            col_sum += array2D[j][i]

        if row_sum != col_sum:
            return False
    return True

print(f([[3,7,2], [4,2,5], [5,2,1]]))  # True
print(f([[3,7,2], [4,2,5], [9,2,1]]))  # False