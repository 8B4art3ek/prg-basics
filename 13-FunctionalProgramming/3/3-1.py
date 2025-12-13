# Poniższy raport pokazuje ostatnie pięć płatności kartą kredytową w Euro:
# 15.90
# 38.47
# 4.07
# 132.70
# 9.15

# Napisz program, który oblicza i wyświetla kwoty transakcji w polskich złotych (1 EUR = 4.5 PLN). Użyj funkcji anonimowych oraz funkcji map(). Przykładowy wynik:
# 71.55
# 173.11
# 18.31
# 597.15
# 41.17


transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
transactions_in_pln = list(map(lambda x: round(x*4.5, 2), transactions_in_eur))

for amount in transactions_in_pln:
    print(amount)