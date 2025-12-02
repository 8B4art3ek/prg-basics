# Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Stwórz program, który oblicza i wypisuje tablicę oraz średnią arytmetyczną wartości tablicy. Użyj instrukcji pętli „while”.

arr = [15, 8, 31, 47, 2, 19]
suma = 0
i = 0

while i < len(arr):
    suma += arr[i]
    i += 1

srednia = suma/len(arr)
print(srednia)