def f(h0, r, h):
    counter = 0
    while h0 > h:
        h0 *= r
        counter += 1
    return counter

if __name__ == "__main__":
    print(f(10, 0.8, 5))
    print(f(10, 0.95, 5))
    print(f(12, 0.7, 2))