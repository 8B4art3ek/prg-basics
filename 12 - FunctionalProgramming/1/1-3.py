# Napisz program, który przelicza prędkość w metrach na sekundę na prędkość w kilometrach na godzinę. Zdefiniuj funkcję ms_to_kmh(ms), która zwraca obliczoną prędkość w km/h. Przykładowy wynik:

# 10 m/s = 36 km/h
# 35 m/s = 126 km/h

def ms_to_kmh(ms):
    return int(ms*3.6)

print(ms_to_kmh(10))
print(ms_to_kmh(35))