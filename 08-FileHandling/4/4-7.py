# Napisz program, który oblicza liczbę samogłosek w tekście wprowadzonym z klawiatury. Użyj wyrażeń regularnych.

import re
text = input("Podaj text: ")

vowels = re.findall(r"[aeiouyąęóAEIOUYĄĘÓ]", text)

print("Liczba samogłosek:", len(vowels))

