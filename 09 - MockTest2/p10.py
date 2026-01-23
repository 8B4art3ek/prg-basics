# (p10.py) Tablica dwuwymiarowa zawiera różne liczby całkowite. Zdefiniuj funkcję f(array), która zwraca True, jeśli numery wiersza i kolumny dla najmniejszej wartości w tablicy są równe, a w przeciwnym razie False. 
# Przykład: 
# f([[7,8],[5,3], [9,4]]) → True, wiersz 1, kol 1 
# f([[7,8,5,3], [9,4,2,6]]) → False, wiersz 1, kol 2

def f(array):
    min_val = min(min(row) for row in array)

    for i, row in enumerate(array):
        for j, val in enumerate(row):
            if val == min_val:
                return i == j
            
print(f([[7,8],[5,3],[9,4]]))       # True
print(f([[7,8,5,3],[9,4,2,6]]))     # False