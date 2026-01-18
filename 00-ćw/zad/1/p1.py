# (p1.py) Urządzenie rejestruje ludzi wchodzących i wychodzących z pokoju. Znak + (plus) wskazuje osobę, która weszła do pokoju, podczas gdy znak - (minus) wskazuje osobę, która opuściła pokój. Stwórz funkcję f(d), która, na podstawie informacji d zarejestrowanej przez urządzenie, zwraca liczbę osób pozostałych w pokoju. Przykład:

# f("") returns 0
# f("+-++-") returns 1
# f("+-+++-+---") returns 0
# f("+-+++++-") returns 4

def f(d):
    counter = 0
    for sign in d:
        if sign == "+":
            counter += 1
        elif sign == "-":
            counter -= 1
    return counter

if __name__ == "__main__":
    print(f(""))
    print(f("+-++-"))
    print(f("+-+++-+---"))
    print(f("+-+++++-"))