###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
click = int(input("Który chcesz kliknąć włącznik? (1 albo 2): "))
if click == 1:
    light_switch1 = True
    bulbs_on += 1
    print(f"Kliknieto {click} zatem light_switch1 = {light_switch1} i zapaliła się {bulbs_on} żarówka")
elif click == 2:
    light_switch2 - True
    bulbs_on += 2
    print(f"Kliknieto {click} zatem light_switch2 = {light_switch2} i zapaliły się {bulbs_on} żarówki")
else:
    print("Błąd")