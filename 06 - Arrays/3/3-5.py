# Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Stwórz program, który oblicza i wypisuje tablicę oraz średnią arytmetyczną wartości tablicy. Użyj instrukcji pętli „for”.

arr = [15, 8, 31, 47, 2, 19]
suma = 0

for value in arr:
    suma += value

srednia = suma/len(arr)
print(srednia)