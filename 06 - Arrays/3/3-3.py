# Stwórz program, który oblicza drugą potęgę każdego elementu tablicy. Przykładowy wynik:
# Array: 8 2 5 1 9
# 2nd power: 64 4 25 1 81

arr = [8, 2, 5, 1, 9]
power_arr = []

for i in range(len(arr)):
    power_arr.append(arr[i] ** 2)

print(*arr)
print(*power_arr)