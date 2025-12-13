# Napisz program, który oblicza średnią prędkość pojazdu. Wprowadź z klawiatury: dystans w km, liczbę godzin podróży i liczbę minut podróży. Zdefiniuj i użyj funkcji anonimowej avg_speed(distance,hours,minutes) do obliczenia wyniku. Przykładowy wynik:

# Enter distance in km: 70
# Enter number of travel hours: 1
# Enter number of travel minutes: 23
# Average speed: 50.6 km/h 

avg_speed = lambda distance, hours, minutes: f"{distance/(hours + minutes/60):.2f}"

def main():
    distance = int(input("Enter distance in km: "))
    hours = int(input("Enter number of travel hours: "))
    minutes = int(input("Enter number of travel minutes: "))
    print(avg_speed(distance, hours, minutes))

main()