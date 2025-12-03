# Napisz program, który wypisuje krotkę (10,20,30,40,50) w odwrotnej kolejności. Przykładowy wynik:

# Tuple: 10,20,30,40,50
# Reverse order: 50,40,30,20,10

tupl = (10, 20, 30, 40, 50)
reversed_tuple = reversed(tupl)

print(*tupl)
print(*reversed_tuple)