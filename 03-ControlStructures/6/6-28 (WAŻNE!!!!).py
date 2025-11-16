# Write a program that prints the first twenty words of the Fibonacci sequence. The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. Sample result:

# https://en.wikipedia.org/wiki/Fibonacci_number

# 0 1 1 2 3 5 8 13 21 34 ...

n = 40
first = 0
second = 1
print(first, second, end=' ')

for i in range (3, n+1):
    next_num = first + second
    print(next_num, end=" ")
    first, second = second, next_num