class C:
    def __init__(self, start_val):
        self.licznik = start_val
    
    def m1(self):
        return self.licznik
    
    def m2(self):
        self.licznik += 10

    def m3(self):
        self.licznik -= 10

    def m4(self, ile):
        self.licznik += ile

    def __str__(self):
        return str(self.licznik)