# Define the function f(n), which returns the n-th value of the Fibonacci sequence. The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. Each subsequent value is the sum of the previous two. Sample result:

# f(5) returns 3
# f(9) returns 21

def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    first = 0
    second = 1
    for i in range(3, n+1):
        next_num = first + second
        first, second = second, next_num
    return second

if __name__ == "__main__":
    print(f(5))
    print(f(9))
    print(f(400))

