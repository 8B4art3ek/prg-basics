# program liczacy wartosc vatu 23% na podstawie podanej kwoty 
kwota = float(input("Podaj kwote z której chcesz obliczyć VAT 23%: "))
vat = round(kwota*0.23, 2)
print(f"Vat kwoty {kwota} wynosi {vat}")