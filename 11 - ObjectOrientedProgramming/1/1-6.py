# Zidentyfikuj co najmniej 3 stany i 3 zachowania dla swojego smartfona. Następnie, dla wymienionych stanów i zachowań, stwórz klasę z atrybutami i metodami. Postaraj się używać czasowników w nazwach metod, ponieważ opisują one czynności. Na koniec stwórz obiekt smartfona, wywołaj jego metody i wyświetl właściwości obiektu.

class Phone():
    def __init__(self, brand, battery_level):
        self.brand = brand
        self.is_on = False
        self.is_locked = True
        self.battery_level = battery_level

    def wlacz(self):
        if self.battery_level > 0:
            self.is_on = True
            print("Telefon włączony")
        else:
            print("Telefon rozładowany")

    def wylacz(self):
        self.is_on = False
        print("Telefon wyłączony")

    def odblokuj(self):
        if self.is_on:
            self.is_locked = False
            print("Telefon odblokowany")
        else:
            print("Najpierw go włącz")

    def zablokuj(self):
        self.is_locked = True
        print("Telefon zablokowany")

    def laduj(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Bateria: {self.battery_level}%")

    def rozladuj(self, amount):
        self.battery_level = max(0, self.battery_level - amount)
        print(f"Bateria: {self.battery_level}%")


phone = Phone("Samsung", 20)

phone.wlacz()
phone.odblokuj()
phone.rozladuj(10)
phone.laduj(50)
phone.zablokuj()

print("Marka:", phone.brand)
print("Włączony:", phone.is_on)
print("Zablokowany:", phone.is_locked)
print("Bateria:", phone.battery_level, "%")
