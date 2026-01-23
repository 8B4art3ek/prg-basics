# The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:
# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

godziny_parkingu = int(input("Ile chcesz godzin spędzić na parkingu: "))
if godziny_parkingu >= 1 and godziny_parkingu <= 2:
    cena = godziny_parkingu * 5
    print(f"Płacisz {cena} zł")
elif godziny_parkingu >= 3 and godziny_parkingu <= 6:
    cena = godziny_parkingu * 15
    print(f"Płacisz {cena} zł")
elif godziny_parkingu > 6:
    cena = godziny_parkingu * 20
    print(f"Płacisz {cena} zł")