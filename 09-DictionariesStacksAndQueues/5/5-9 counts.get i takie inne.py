# Kamera drogowa rejestruje przejeżdżające pojazdy. Kamera zapisuje ich numery rejestracyjne w pliku vehicle.txt. Napisz program, który oblicza i wypisuje, ile zarejestrowanych samochodów pochodzi z każdego województwa Polski. Lista województw i odpowiadające im pierwsze litery numerów rejestracyjnych pojazdów znajdują się w pliku province.csv.

# Wskazówka: użyj słownika zawierającego litery odpowiadające województwom oraz liczbę pojazdów, których pierwsze litery numeru rejestracyjnego pasują do liter województwa.

province_map = {}

with open("province.csv", "r", encoding="utf-8") as file:
    for line in file:
        letter, province = line.strip().split(",")
        province_map[letter] = province

counts = {}

with open("vehicle.txt", "r", encoding="utf-8") as file:
    for plate in file:
        first_letter = plate.strip()[0]

        if first_letter in province_map:
            province = province_map[first_letter]
            counts[province] = counts.get(province, 0) + 1

for province, amount in counts.items():
    print(f"{province}: {amount}")