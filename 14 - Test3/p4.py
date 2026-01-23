class C:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def __str__(self):
        if self.wiek < 18:
            return f"{self.imie[0:2].lower()}-{self.nazwisko[0:2].lower()}-{self.wiek}"
        else:
            return f"{self.imie[0:2].upper()}-{self.nazwisko[0:2].upper()}-{self.wiek}"
        
if __name__ == "__main__":
    print(C("John", "May", 18))
    print(C("Anna", "Brown", 17))