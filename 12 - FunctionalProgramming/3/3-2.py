# Dla następującego tekstu:

# I completely agree with you
# napisz program, który oblicza i wyświetla liczbę liter w każdym słowie. Użyj funkcji map() oraz funkcji anonimowych do obliczenia liczby liter.

# Wskazówka: aby podzielić tekst na słowa, użyj funkcji split().

# Przykładowy wynik:

# Text: I completely agree with you
# No. of letters in words: [1,10,5,4,3]

sentence = 'I completely agree with you'
result = list(map(lambda x:len(x), sentence.split()))
print(result)

