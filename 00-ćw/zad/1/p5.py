# (p5.py) Stadion jest podzielony na sektory, każdy oznaczony literą. Każdy sektor ma określoną liczbę fanów. Zdefiniuj klasę C, która pozwala ci stworzyć obiekt reprezentujący stadion z listą sektorów i liczbą fanów w sektorach. Dane, w formie słownika, powinny być przekazane do obiektu, kiedy jest tworzony. Zdefiniuj metodę m1(s,n) w klasie, która pozwala ci zmienić liczbę fanów n w sektorze s lub dodać nowy sektor s z podaną liczbą fanów n. Zdefiniuj metodę m2(s) w klasie, która zwraca sumę fanów w sektorach wymienionych w ciągu znaków s. Przykład:

# stadium = C({"A":120, "D":150, "G":90, "K":110})
# stadium.m1("G", 130)
# stadium.m2("GD") returns 280
# stadium.m2("KEJ") returns 110

class C:
    def __init__(self, sectors):
        self.sectors = sectors
    def m1(self, s, n):
        self.sectors[s] = n
    def m2(self, s):
        total_fans = 0
        for sector in s:
            if sector in self.sectors:
                total_fans += self.sectors[sector]
        return total_fans
    
if __name__ == "__main__":
    stadium = C({"A":120, "D":150, "G":90, "K":110})
    stadium.m1("G", 130)            
    print(stadium.m2("GD"))         
    print(stadium.m2("KEJ"))