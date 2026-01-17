class C:
    def __init__(self, data):
        self.data = data

    def m1(self, sektor, liczba):
        self.data[sektor] = liczba

    def m2(self, sektory):
        total = 0
        for s in sektory:
            total += self.data[s]
        return total / len(sektory)