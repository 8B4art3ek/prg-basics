# Define a function that calculates and returns the sum of the digits in a number. Then write a program that reads a number from the keyboard and prints the sum of its digits.
# Kroki algorytmu sumowania cyfr liczby:
# Pobierz liczbę całkowitą od użytkownika. Liczba może być dodatnia, ujemna lub równa zero.
# Obsłuż liczby ujemne: zamień liczbę na jej wartość bezwzględną używając funkcji abs(). Dzięki temu ignorujemy znak minus.
# Zamień liczbę na napis (str()), żeby móc przechodzić po jej cyfrach.
# Iteruj po cyfrach:
# przechodź po każdym znaku (cyfrze) w napisie,
# zamień go z powrotem na liczbę całkowitą.
# Sumuj cyfry — dodawaj każdą cyfrę do zmiennej, która przechowuje wynik.
# Wyświetl wynik lub zwróć go z funkcji.

def sum_digits(number):
    wynik = 0
    for digit in number:
        digit = int(digit)
        wynik += digit
    return wynik

number = str(abs(int(input("Podaj liczbe: "))))
print(f'The sum of the digits in the number {number} is {sum_digits(number)}')
