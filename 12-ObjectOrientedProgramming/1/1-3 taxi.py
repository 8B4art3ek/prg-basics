# Plik taxi.py zawiera definicję klasy opisującej przejazdy taksówką. Uzupełnij klasę, dodając metodę print_receipt(self), która drukuje paragon. Powinna ona zawierać wszystkie informacje o przejeździe: dystans, stawkę i opłatę. Następnie napisz program, w którym stworzysz dwa obiekty reprezentujące dwa różne przejazdy taksówką. Oblicz opłaty za oba przejazdy i wydrukuj paragony.

class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print("---PARAGON---")
        print(f"Dystans: {self.distance}")
        print(f"Stawka: {self.rate_per_km}")
        print(f"Opłata: {self.fare:.2f}")
        print("--------------------")

def main():
    przejazd1 = TaxiRide(2.0)
    przejazd1.calculate_fare(5)
    print("Klient 1: ")
    przejazd1.print_receipt()

    przejazd2 = TaxiRide(3.5)
    przejazd2.calculate_fare(12.5)
    print("Klient 2: ")
    przejazd2.print_receipt()


if __name__ == "__main__":
    main()
