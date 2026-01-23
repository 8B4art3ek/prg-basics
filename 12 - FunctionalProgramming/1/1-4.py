# Napisz program, który przelicza prędkość w metrach na sekundę na prędkość w kilometrach na godzinę. Zdefiniuj i użyj funkcji anonimowej ms_to_kmh(ms). Przykładowy wynik:

# 10 m/s = 36 km/h
# 35 m/s = 126 km/h

ms_to_kmh = lambda ms: ms*3.6

print(ms_to_kmh(10))
print(ms_to_kmh(35))