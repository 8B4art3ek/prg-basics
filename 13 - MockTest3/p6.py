# Zdefiniuj klasę C, która pozwala tworzyć obiekty reprezentujące osoby. Konstruktor klasy ma 3 parametry: imię, nazwisko i wiek. Reprezentacja tekstowa obiektu zawiera inicjał imienia i nazwiska oraz wiek osoby. Jeśli wiek osoby jest mniejszy niż 18 lat, ich inicjały składają się z małych liter, a jeśli są dorosłymi, składają się z wielkich liter.

# C("John","May",21) returns "JM21" 
# C("Anna","Brown",17) returns "ab17"

class C:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        initials = self.fname[0] + self.lname[0]
        
        if self.age < 18:
            result = initials.lower()
        else:
            result = initials.upper()

        return f"{result}{self.age}"

if __name__ == "__main__":
    print(C("John", "May", 21))  
    print(C("Anna", "Brown", 17)) 