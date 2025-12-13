# Oceny końcowe uzyskane przez studentów z przedmiotu "Geografia Ekonomiczna" są zawarte w tablicy:

# [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2,0]
# Napisz program, który oblicza średnią arytmetyczną ocen, wykluczając oceny negatywne (2.0). Użyj filter() wraz z funkcją anonimową. Przykładowy wynik:

# Arithmetic mean for grades <> 2.0 is 3.85

arr = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2,0]
filtered_arr = list(filter(lambda x: x > 2.0, arr))
avg = sum(filtered_arr)/len(filtered_arr)
print(f"Arithmetic mean for grades <> 2.0 is {avg:.2f}")