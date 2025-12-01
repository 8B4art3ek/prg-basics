def f(wysokosc_startowa, wspolczynnik_odbicia, wysokosc_docelowa):
    counter = 0
    wysokosc_po_odbiciu = wysokosc_startowa
    while wysokosc_po_odbiciu > wysokosc_docelowa:
        counter += 1
        wysokosc_po_odbiciu = wspolczynnik_odbicia * wysokosc_po_odbiciu
        
    return counter

if __name__ == "__main__":
    print(f(12,0.9,10))
    print(f(10,0.6,1))
    print(f(25,0.85,7))