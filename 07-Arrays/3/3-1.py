# Tablica zawiera liczby całkowite: 34,7,19,4,21,8. Stwórz program, który oblicza i wypisuje liczbę parzystych wartości w tablicy. Użyj instrukcji pętli ‘while’.

arr = [34,7,19,4,21,8]
counter = 0
i = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        counter += 1
    i += 1
print(counter)