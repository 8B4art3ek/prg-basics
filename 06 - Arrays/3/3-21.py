# Napisz program, który sprawdza, czy pierwsza tablica jest podzbiorem drugiej (czy wszystkie elementy pierwszej tablicy występują w drugiej tablicy).

arr1 = [2, 4]
arr2 = [1, 2, 3, 4, 5]

is_subset = True

for x in arr1:
    if x not in arr2:
        is_subset = False
        break

print(is_subset)

