# Funkcja create_2d_arr(x,y) tworzy i zwraca dwuwymiarową tablicę o wartościach 0. Stwórz program i tę funkcję. Następnie stwórz dwuwymiarową tablicę o wymiarach 3 na 5. Wypisz stworzoną tablicę.

def create_2d_arr(x,y):
    return [[0 for j in range(y)]for i in range(x)]
    
arr = create_2d_arr(3,5)
for row in arr:
    for col in row:
        print(col, end=" ")
    print()