# (p9.py) Użycie samochodów firmowych jest dostępne w formie listy (struktura danych: tablica słowników) zawierającej numer rejestracyjny pojazdu i liczbę przejechanych kilometrów. Stwórz funkcję f(car,order), która zwraca listę samochodów posortowaną alfabetycznie (gdy order = 1) lub listę samochodów, które przejechały co najmniej 200 km, posortowaną według liczby przejechanych kilometrów, w kolejności malejącej (gdy order = 2). Przykład:

# cars = [{"KR333":138}, {"WL555":497}, {"DB444":341}, {"MC222":412}]
# f(cars, 1) returns [{"DB444":341}, {"KR333":138}, {"MC222":412}, {"WL555":497}]
# f(cars, 2) returns [{"WL555":497}, {"MC222":412}, {"DB444":341}]

def f(car,order):
    filtered_cars = [x for x in car if list(x.values())[0] > 200]

    if order == 1:
        return sorted(car, key=lambda x: list(x.keys())[0])
    elif order == 2:
        return sorted(filtered_cars, key=lambda x: list(x.values())[0], reverse = True)

if __name__ == "__main__":
    cars = [{"KR333":138}, {"WL555":497}, {"DB444":341}, {"MC222":412}]
    print(f(cars, 1))
    print(f(cars, 2))