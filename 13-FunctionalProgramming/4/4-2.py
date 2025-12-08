# Fotoradar umieszczony w mieście mierzy prędkość przejeżdżających pojazdów. Maksymalna dozwolona prędkość pojazdów wynosi 50 km/h. W ostatniej minucie fotoradar zarejestrował następujące wartości:

# 48,47,54,50,42,68,39,46
# Napisz program, który wyświetla wartości prędkości wyższe niż dozwolona prędkość. Użyj funkcji anonimowych oraz filter(). Przykładowy wynik:

# Recorded values: 48,47,54,50,42,68,39,46
# Speed too high: 54,68

arr = [48,47,54,50,42,68,39,46]
print("Recorded values:", *arr)
print("Speed too high:", *(list(filter(lambda x: x>50, arr))))