# Plik files.txt zawiera listę nazw plików. Napisz program, który wypisuje tylko te nazwy plików, których rozszerzenie składa się dokładnie z czterech znaków (np. .html).

import re

try:
    with open("files.txt", "r") as file:
        for line in file:
            name = line.strip()
            if re.search(r"\.[A-Za-z0-9]{4}$", name):
                print(name)

except FileNotFoundError:
    print("Plik files.txt nie istnieje")