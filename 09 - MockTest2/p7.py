# (p7.py) Poprawna nazwa użytkownika składa się z 4 do 12 znaków: małych liter, cyfr i znaku podkreślenia. Zdefiniuj funkcję f(array), która dla danej tablicy nazw użytkowników zwraca liczbę poprawnych nazw użytkowników w tablicy. 
# Przykład: f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]) → 2

import re

def f(array):
    pattern = re.compile(r'^[a-z0-9_]{4,12}$')
    return sum(1 for username in array if pattern.match(username))

print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))