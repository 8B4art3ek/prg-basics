# Zdefiniuj funkcję f(number), która sprawdza, czy podana liczba należy do ciągu Fibonacciego. Funkcja zwraca True, jeśli liczba jest elementem ciągu, lub False w przeciwnym wypadku. 
# Przykładowy wynik: 
# f(5) zwraca True 
# f(7) zwraca False

def f(number):
    if number < 0:
        return False
    if number == 0 or number == 1:
        return True
    
    first, second = 0, 1

    while second < number:
        first, second = second, first+second

    return second == number

if __name__ == "__main__":
    print(f(5))
    print(f(7))