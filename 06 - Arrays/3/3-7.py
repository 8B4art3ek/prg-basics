# Tablica zawiera listę polskich imion:

# Genowefa, Onufry, Celestyna, Alojzy, Pankracy
# Stwórz program, który wypisuje najdłuższe imię (składające się z największej liczby znaków). Przykładowy wynik:

# Names: Genowefa Onufry Celestyna Alojzy Pankracy
# Longest name: Celestyna

arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = arr[0]

for name in arr:
    if len(name) > len(longest):
        longest = name

print(longest)