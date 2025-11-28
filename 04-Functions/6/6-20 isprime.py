# Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

# f(1) returns 2
# f(5) returns 11

import math 

def f(n):
    counter_is_prime = 0
    num = 2

    while counter_is_prime < n:
        is_prime = True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            counter_is_prime += 1
            if counter_is_prime == n:
                return num
        
        num += 1


if __name__ == "__main__":
    print(f(1))
    print(f(5))