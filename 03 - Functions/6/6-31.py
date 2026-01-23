# Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 53.
# Tip: xn = x * xn-1

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

if __name__ == "__main__":
    print(power(5, 3))