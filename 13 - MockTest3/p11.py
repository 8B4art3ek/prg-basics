# Wykorzystanie samochodów służbowych jest dostępne w formie listy (struktura danych: tablica słowników) zawierającej numer rejestracyjny pojazdu i liczbę przejechanych kilometrów. Stwórz funkcję f(car, order), która zwraca listę samochodów posortowaną alfabetycznie (gdy order = 1) lub listę samochodów posortowaną według liczby przejechanych kilometrów, w kolejności malejącej (gdy order = 2).

# cars = [{"KR333":138},{"WL555":497},{"DB444":341},{"MC222":412}] 
# f(cars,1) returns [{"DB444":341},{"KR333":138},{"MC222":412},{"WL555":497}] 
# f(cars,2) returns [{"WL555":497},{"MC222":412},{"DB444":341},{"KR333":138}] 

def f(car, order):
    if order == 1:
        return sorted(car, key=lambda x: list(x.keys())[0])
    elif order == 2:
        return sorted(car, key=lambda x: list(x.values())[0], reverse=True)
    return car

if __name__ == "__main__":
    cars = [{"KR333":138},{"WL555":497},{"DB444":341},{"MC222":412}]
    print(f(cars, 1))
    print(f(cars, 2))