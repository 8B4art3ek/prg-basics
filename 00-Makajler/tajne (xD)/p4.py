class C:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    
    def __str__(self):
        initial = self.imie[0]
        if self.wiek < 18:
            initial = initial.lower()
        else:
            initial = initial.upper()
        return f"{initial}-{self.wiek}"