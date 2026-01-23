def f(n):
    if n == 1:
        return 0
    if n == 2: 
        return 1
    
    first = 0
    second = 1

    for _ in range(3, n+1):
        next_num = first + second
        first, second = second, next_num
    
    return second

if __name__ == "__main__":
    print(f(5))
    print(f(9))