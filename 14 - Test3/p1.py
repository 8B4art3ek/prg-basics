def f(d):
    counter = 0
    for sign in d:
        if sign == "+":
            counter += 1
        elif sign == "-":
            counter -= 1
    return counter

if __name__ == "__main__":
    print(f(""))
    print(f("+-+"))
    print(f("+-+++-+---"))
    print(f("+-+++++-"))