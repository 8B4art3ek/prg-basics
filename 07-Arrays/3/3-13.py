# Zdefiniuj funkcję occurs(number, array), która zwraca True, jeśli podana liczba znajduje się w tablicy. Następnie stwórz program, który sprawdza, czy liczba wprowadzona z klawiatury jest obecna w tablicy [15, 38, 7, 23, 14]. Przykładowy wynik:

# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the 

def occurs(number, array):
    for item in array:
        if item == number:
            return True
    return False

def occurs2(number, array):
    return number in array
        
        
if __name__ == "__main__":
    arr = [15, 38, 7, 23, 14]
    print(occurs(23, arr))
    print(occurs2(23, arr))