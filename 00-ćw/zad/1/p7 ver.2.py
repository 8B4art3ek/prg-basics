# (p7.py) Nazwy plików zawierają część literalną, która jest taka sama dla wszystkich plików, i liczbę. Stwórz funkcję f(files), która, biorąc pod uwagę nazwy plików, zwraca listę plików uporządkowaną według numeru. Przykład:

# files = ["copy179", "copy15", "copy3", "copy123", "copy9"]
# f(files) returns ["copy3", "copy9", "copy15", "copy123", "copy179"]

import re

def f(files):
    return sorted(files, key=lambda x: int(re.findall(r"\d+", x)[0]))

if __name__ == "__main__":
    files = ["copy179", "copy15", "copy3", "copy123", "copy9"]
    print(f(files))