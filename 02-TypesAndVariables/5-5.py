# program obliczajacy roznice ceny miedzy cena na poczatku i cena na promocji

cena = float(input("Wprowadź cene: "))
znizka = (float(input("Wprowadź zniżke w %: ")))/100
cena_ze_znizka = round(cena-(cena*znizka),2)
roznica = round(cena-cena_ze_znizka, 2)
print(f"Cena ze znizka to {cena_ze_znizka} a roznica miedzy cena poczatkową a tej ze znizka to {roznica}")