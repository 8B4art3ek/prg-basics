def f(n):
    result = ""
    for i in range(n):
        result += '*/'
    return result[:-1]

if __name__ == "__main__":
    print(f(4))
    print(f(1))
    print(f(0))
    print(f(10))