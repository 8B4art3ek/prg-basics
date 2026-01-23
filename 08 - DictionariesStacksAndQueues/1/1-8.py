# Poniższe dane zawierają cennik artykułów ze sklepu odzieżowego wraz z ich cenami. Z powodu sezonowej wyprzedaży sklep obniża cenę każdego artykułu o 10%. Napisz program, który:
# wypisuje listę produktów i ich ceny przed obniżką
# wypisuje całkowitą wartość produktów przed obniżką
# modyfikuje cennik zgodnie z rabatem (zaokrąglij ceny do dwóch miejsc po przecinku)
# wypisuje listę produktów i ich ceny po 10% zniżce
# wypisuje całkowitą wartość produktów po zniżce

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Ceny przed obniżką: ")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

total_before = sum(price_list.values())
print(f"Całkowita wartość przed obniżką: ${total_before:.2f}")

for product in price_list:
    discounted_price = price_list[product] * 0.9       # 10% rabatu
    price_list[product] = round(discounted_price, 2)

print()
print("Ceny po 10% zniżce: ")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

total_after = sum(price_list.values())
print(f"Całkowita wartość po obniżce: ${total_after:.2f}")