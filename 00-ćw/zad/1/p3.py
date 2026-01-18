# (p3.py) Załóż, że poprawna nazwa zmiennej w programie komputerowym składa się z jednego do pięciu znaków. Pierwszy znak nazwy zmiennej musi być małą lub dużą literą lub podkreślnikiem. Pozostałe znaki w nazwie zmiennej mogą być dużymi lub małymi literami, cyframi lub podkreślnikiem. Stwórz funkcję f(vname), która zwraca true, jeśli nazwa zmiennej vname jest poprawna. W przeciwnym razie funkcja zwraca false. Przykład:

# f("abc") returns True
# f("_ab_c") returns True
# f("abcdef") returns False
# f("8abc") returns False
# f("_aB8_") returns True

import re

def f(vname):
    return True if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]{0,4}$", vname) else False

if __name__ == "__main__":
    print(f("abc"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB8_"))