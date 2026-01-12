# Poprawna liczba na planecie Metis składa się z cyfr od 1 do 7 oraz małych lub wielkich liter od a do d. Na początku liczby może również wystąpić znak plus (+) lub minus (-). Stwórz funkcję f(mnumbers), która zwraca, ile liczb w tablicy mnumbers jest poprawnych na planecie Metis.

# f(["A15","-31","7abC","+D1","-g4"]) returns 4 
# f(["A05","-3+1","7ab8C","+Bb7","-22c55"]) returns 2

import re

def f(mnumbers):
    pattern = r"^[+-]?[1-7a-dA-D]+$"
    # ^           -> początek napisu
    # [+-]?       -> opcjonalny znak plus lub minus (0 lub 1 raz)
    # [1-7a-dA-D]+ -> jeden lub więcej znaków z zakresu 1-7 lub a-d (duże i małe)
    # $           -> koniec napisu (żeby nie dopasowało np. "-3+1" jako "-3")
    count = 0
    for num in mnumbers:
        if re.match(pattern, num):
            count += 1
            
    return count

if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-g4"])) 
    print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))  