# Napisz program, który dla danej tablicy liczb rzeczywistych wypisuje liczbę elementów, które są większe od podanej wartości wprowadzonej z klawiatury.

numbers = [2.5, 7.1, 3.0, 9.4, 1.2, 6.8]
value = float(input("Podaj wartość: "))

counter = 0
for number in numbers:
    if number > value:
        counter += 1

print("Tablica:", numbers)
print("Liczba elementów większych od", value, ":", counter)