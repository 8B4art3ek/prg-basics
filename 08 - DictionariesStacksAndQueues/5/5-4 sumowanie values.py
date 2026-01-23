# Słownik zawiera nazwy przedmiotów wraz z liczbą godzin. Napisz program, który oblicza i wypisuje całkowitą liczbę godzin. Przykładowe wyniki:

# The total number of hours in the winter semester is …

winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

total = sum(winter_semester.values())
print(f"The total number of hours in the winter semester is {total}")