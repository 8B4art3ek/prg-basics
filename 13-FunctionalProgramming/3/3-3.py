# Poniższe dane zawierają listę produktów dostępnych w magazynie oraz ich cenę jednostkową.

# stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
# Napisz program, który oblicza całkowitą wartość produktów w magazynie. Użyj funkcji map(), sum() oraz funkcji anonimowej. Przykładowy wynik:

# Products in stock: [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
# Total value: 423.35

stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
print(f"Products in stock: {stock}")
print(sum(list(map(lambda item: item[0]*item[1], stock))))