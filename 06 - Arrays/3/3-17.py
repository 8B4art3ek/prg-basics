# Napisz program, który zlicza liczbę wystąpień dowolnej wartości z krotki. Przykładowy wynik:
# Tuple: 50,20,40,50,30,50
# Value: 50
# Number of occurrences: 3

tup = (50,20,40,50,30,50)

value = int(input("Value: "))

number = tup.count(value)

print(f"Number of occurrences: {number}")