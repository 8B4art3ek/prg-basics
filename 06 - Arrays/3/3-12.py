# Stwórz program, który wypisuje wszystkie unikalne elementy w tablicy. Przykładowy wynik:

# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

arr = [2, 3, 2, 5, 8, 1, 9, 8]
print(*arr)

unique = [x for x in arr if arr.count(x) == 1]
print(*unique)