# Tablica zawiera liczby naturalne: 15, 8, 31, 47, 2, 19. Stwórz program, który wypisuje zawartość tablicy w odwrotnej kolejności. Użyj dowolnej pętli. Przykładowy wynik:
# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

arr = [15, 8, 31, 47, 2, 19]
for i in range(len(arr)):
    print(arr[i], end=" ")

print()

for i in reversed(range(len(arr))):
    print(arr[i], end=" ")
