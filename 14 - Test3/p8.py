class C:
    def __init__(self, poczatkowa_wartosc):
        self.licznik = poczatkowa_wartosc
    def m1(self):
        return self.licznik
    def m2(self):
        self.licznik += 1
    def m3(self):
        self.licznik -= 1
    def m4(self, n):
        self.licznik += n
    def __str__(self):
        return f"#{self.licznik}#"
    
if __name__ == "__main__":
    c = C(5)
    print(c.m1())
    c.m2()
    print(c.m1())
    c.m4(-8)
    print(c.m1())
    c.m3()
    print(c.m1())
    c.m4(10)
    print(c.m1())
    print(c.__str__())