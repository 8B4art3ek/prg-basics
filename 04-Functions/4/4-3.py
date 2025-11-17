# Define a function triangle_area that calculates and returns the area of ​​a triangle with sides a, b, and c. Use Heron's formula: https://en.wikipedia.org/wiki/Heron's_formula

# Write a program that calculates the area of ​​a triangle based on the lengths of the triangle's sides read from the keyboard. Use the defined function. Then calculate the area of ​​the triangle for the following dimensions of sides a, b, and c:
# 3, 4, 5 (result is 6)
# 5, 12, 13 (result is 30)
# 7, 24, 25 (result is 84)
###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#

import math

def triangle_area(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

print(f'The area of a triangle with sides {a,b,c} is {triangle_area(a,b,c)}')
print(f'The area of a triangle with sides {a,b,c} is {triangle_area(a,b,c)}')
print(f'The area of a triangle with sides {a,b,c} is {triangle_area(a,b,c)}')