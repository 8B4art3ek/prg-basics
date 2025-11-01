###
# Calculation of circle area and circumference 
# r = 1 --> circumference = 6.28, area = 3.14
# r = 3 --> circumference = 18.84, area = 28.26

import math
r = float(input("Wprowadż wartość r: "))
area = round(math.pi * r **2, 2)
circumference = round(2 * math.pi * r, 2)
print(f"r = {r} --> circumference = {circumference}, area = {area}")
