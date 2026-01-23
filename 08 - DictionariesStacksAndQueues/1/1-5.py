# Stwórz tablicę (listę) z 5 słownikami, z których każdy zawiera kraj i jego populację. Następnie wypisz zawartość tablicy. Przykładowy wynik:
# COUNTRY  POPULATION
# Poland   38000000
# …        …
# …        …
# …        …
# …        …

countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 65000000},
    {"name": "Italy", "population": 59000000},
    {"name": "Spain", "population": 48000000},
]

print("COUNTRY".ljust(10), "POPULATION")

for country in countries:
    print(country["name"].ljust(10), country["population"])