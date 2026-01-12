# # Klasa C opisuje punkt (x,y) na płaszczyźnie. Współrzędne punktu są podawane podczas tworzenia (inicjalizacji) obiektu. Klasa zawiera metodę m1(), która zwraca numer ćwiartki układu kartezjańskiego, w której znajduje się punkt (x,y). Metoda m1() zwraca 0, jeśli punkt (x,y) znajduje się na osi X lub osi Y. Klasa zawiera metodę m2(a,b), która zwraca true, gdy punkt (x,y) znajduje się w tej samej ćwiartce układu kartezjańskiego co punkt o współrzędnych a, b. W przeciwnym razie metoda zwraca false. Klasa zawiera metodę m3(a,b), która zwraca true, gdy odległość między punktami (x,y) i (a,b) jest większa niż 5. W przeciwnym razie metoda zwraca false.

# p = C(2,3) 
# p.m1() returns 1 
# p.m2(7,4) returns True 
# p.m2(-3,1) returns False 
# p.m3(8,5) returns True 
# p.m3(4,7) returns False 
# p1 = C(0,5) 
# p1.m1() returns 0 
# p1.m2(4,7) returns False 
# p1.m2(-7,0) returns True 

import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cwiartka(self, x, y):
        if x == 0 or y == 0: return 0
        if x > 0 and y > 0: return 1
        if x < 0 and y > 0: return 2
        if x < 0 and y < 0: return 3
        if x > 0 and y < 0: return 4

    def m1(self):
        return self.cwiartka(self.x, self.y)
    
    def m2(self, a, b):
        cwiartka = self.cwiartka(a, b)
        cwiartka2 = self.cwiartka(self.x, self.y)
        if cwiartka == cwiartka2:
            return True
        else:
            return False
        
    def m3(self, a, b):
        dist = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return dist > 5
    
if __name__ == "__main__":
    p = C(2,3)
    print(p.m1()) 
    print(p.m2(7,4)) 
    print(p.m2(-3,1)) 
    print(p.m3(8,5))
    print(p.m3(4,7)) 

    p1 = C(0,5)
    print(p1.m1()) 
    print(p1.m2(4,7)) 
    print(p1.m2(-7,0)) 