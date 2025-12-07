# Zdefiniuj funkcję rand_elem(array), która zwraca losowo wybrany element tablicy. Używając tej funkcji, wypisz kilka losowo wybranych elementów tablicy.

import random

def rand_elem(array):
    return random.choice(array)

# przykładowa tablica
arr = [10, 20, 30, 40, 50]

# wypisujemy kilka losowych elementów
for _ in range(5):
    print(rand_elem(arr))
