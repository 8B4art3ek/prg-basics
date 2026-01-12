# Licznik pozwala na zliczanie dowolnych elementów. Zdefiniuj klasę C, która pozwala tworzyć liczniki. Początkowa wartość licznika jest przypisywana podczas tworzenia obiektu. Klasa zawiera następujące metody: m1() (zwraca wartość licznika), m2() (zwiększa wartość licznika o 1), m3() (zmniejsza wartość licznika o 1), m4(n) (zwiększa lub zmniejsza wartość licznika o n), __str__() (zwraca wartość licznika jako ciąg znaków).

# c=C(5) 
# c.m1() returns 5 
# c.m2() 
# c.m1() returns 6 
# c.m4(-8) 
# c.m1() returns -2 
# c.m3() 
# c.m1() returns -3 
# c.m4(10) 
# c.m1() returns 7 
# c.__str__() returns "7" 

class C:
    def __init__(self, value):
        self.value = value

    def m1(self):
        return self.value

    def m2(self):
        self.value += 1

    def m3(self):
        self.value -= 1

    def m4(self, n):
        self.value += n

    def __str__(self):
        return str(self.value)

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