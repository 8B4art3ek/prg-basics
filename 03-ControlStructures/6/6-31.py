# Write a program that prints 20 integer random numbers in the range of 5 to 10.

import random

n = 20
counter = 0 
while counter < n:
    num = random.randint(5, 10)
    print(num, end=" ")
    counter += 1