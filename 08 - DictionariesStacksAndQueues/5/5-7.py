# Program zawiera dwie funkcje:
# hotel_list(hotels) która zwraca listę nazw hoteli, oddzielonych przecinkiem
# avg_price(hotels) która zwraca średnią cenę pokoju dla podanej listy hoteli, zaokrągloną do liczby całkowitej
# Napisz program, który oblicza i wyświetla średnią cenę za pokój w hotelach w Krakowie i Sopocie oraz wskazuje, w których miastach hotele są tańsze. 

# Przykładowy wynik:
# Hotels in Krakow: …,…,…,…
# Average hotel price in Krakow: …
# Hotels in Sopot: …,…,…,…
# Average hotel price in Sopot: …
# Cheaper hotels in: …

def hotel_list(hotels):
    names = []
    for hotel in hotels:
        names.append(hotel['name'])
    return ", ".join(names)

def avg_prices(hotels):
    total = 0
    for hotel in hotels:
        total += hotel['price']
    return round(total / len(hotels))

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {avg_prices(hotels_in_Krakow)}")
print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {avg_prices(hotels_in_Sopot)}")
if avg_prices(hotels_in_Krakow) > avg_prices(hotels_in_Sopot):
    print("Cheaper hotels in Sopot")
else:
    print("Cheaper hotels in Kraków")