# Tablica zawiera liczby całkowite: 2, 6, 4, 9, 7. Stwórz program, który wypisuje wartości tablicy graficznie, jak poniżej. Zdefiniuj funkcję star(n), która zwraca zadaną liczbę gwiazdek jako ciąg znaków (string). Użyj zdefiniowanej funkcji w programie.

# 2: **
# 6: ******
# 4: ****
# 9: *********
# 7: *******

def star(n):
    return n*"*"

arr = [2, 6, 4, 9, 7]
for i in range(len(arr)):
    print(f'{arr[i]}: {star(arr[i])}')