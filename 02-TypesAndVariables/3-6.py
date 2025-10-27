# program obliczajcy odległość horyzontu

import math
h = float(input("Give height: "))
d = 3.57 * math.sqrt(h)
d2 = 3.57 * math.sqrt(h+20)
print("Na plaży", d)
print("W hotelu", d)