# Wygodne przetwarzanie dokumentów CSV jest możliwe dzięki modułowi CSV. Znajdź w Internecie informacje, jak używać tego modułu. Następnie napisz program, który na podstawie pliku it_company.csv wypisuje imię, nazwisko i email (w podanej kolejności, bez stanowiska pracy) osób zatrudnionych na stanowisku 'Graphic Designer'. Przykładowy wynik:

# GRAPHIC DESIGNERS
# =================
# Chris Martin,chris.martin@example.com
# Jane Taylor,jane.taylor@example.com
# ...
# ...

import csv

try:
    with open("it_company.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        print("GRAPHIC DESIGNERS")
        print("=================")

        for row in reader:
            if row["Job Title"] == "Graphic Designer":
                print(f"{row['First Name']} {row['Last Name']}, {row['Email']}")

except FileNotFoundError:
    print("Nie ma takiego pliku.")