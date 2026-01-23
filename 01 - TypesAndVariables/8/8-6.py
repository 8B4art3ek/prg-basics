###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))
total_fuel_consumption = distance * fuel_consumption / 100
total_cost = total_fuel_consumption * fuel_price
print(f"Dystans: {distance}")
print(f"Cena paliwa: {fuel_price:.2f}")                                #:.2f wyświetlanie dwóch zer po przecinku
print(f"Spalanie: {fuel_consumption}/100 km")
print(f"Zużycie paliwa po przejechaniu {distance} km: {total_fuel_consumption}")
print(f"Koszt paliwa po przejechaniu {distance} km: {total_cost:.2f}")                         #:.2f wyświetlanie dwóch zer po przecinku