# Dwuwymiarowa tablica o rozmiarze 3 na 5 zawiera liczby całkowite. Stwórz program, który zamienia miejscami pierwszą i ostatnią kolumnę. Wypisz wartości tablicy w wierszach i kolumnach przed i po zmianach.

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Przed zmianą: ")
for row in arr:
    for col in row:
        print(str(col).rjust(2), end=" ")
    print()

for i in range(len(arr)):
    arr[i][0], arr[i][-1] = arr[i][-1], arr[i][0]

print()

print("Po zmianie: ")
for row in arr:
    for col in row:
        print(str(col).rjust(2), end=" ")
    print()