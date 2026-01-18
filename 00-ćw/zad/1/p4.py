# (p4.py) Zdefiniuj klasę C, która pozwala ci tworzyć obiekty reprezentujące ludzi. Konstruktor klasy ma 3 parametry: imię, nazwisko i wiek. Tekstowa reprezentacja obiektu zawiera inicjał imienia i nazwiska oraz wiek osoby. Jeśli wiek osoby jest mniejszy niż 18 lat, ich inicjały składają się z małych liter, a jeśli są dorośli, składają się z wielkich liter. Przykład:

# C("John", "May", 18) returns "JM18"
# C("Anna", "Brown", 17) returns "ab17"

class C:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def __str__(self):
        inicjal = self.imie[0] + self.nazwisko[0]
        if self.wiek < 18:
            return f"{inicjal.lower()}{self.wiek}"
        else:
            return f"{inicjal.upper()}{self.wiek}"

if __name__ == "__main__":
    print(C("John", "May", 18))
    print(C("Anna", "Brown", 17))