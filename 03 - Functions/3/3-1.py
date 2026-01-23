# Using functions and constants available in the math module, write a program that calculates and prints:

# square root of 7
# natural logarithm of 5
# sine of 90 degrees

###
# To use the functions available in an external module,
# you must include that module in your program.
import math

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

natural_logarithm = math.log(5)
print("A natural logarithm of 5 is", natural_logarithm)

sin = math.sin(math.radians(90))
print("A sine of 90 degrees is", sin)