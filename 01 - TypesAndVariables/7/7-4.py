# Napisz program, który na podstawie obwodu drzewa wprowadzonego z klawiatury oblicza i wyświetla wartość „Prawda”, jeśli drzewo można ściąć, lub wartość „Fałsz”, jeśli nie.

import math

obwod = int(input("Wprowadź obwód drzewa w cm: "))
srednica = obwod / math.pi
mozna_sciac = srednica >= 50
print(f"Drzewo można sciąć: {mozna_sciac}")