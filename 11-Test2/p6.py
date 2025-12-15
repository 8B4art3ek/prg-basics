def f(addr):
    if addr[0].isdigit():
        return False
    if len(addr) > 2:
        if addr[2].islower() or addr[2].isupper():
            return False
    cnt_digit = 0
    cnt_letter = 0
    for char in addr:
        if char.isdigit():
            cnt_digit += 1
        elif char.isupper() or char.islower():
            cnt_letter += 1
    if cnt_digit > 4:
        return False
    if cnt_letter > 2:
        return False
    return True

if __name__ == "__main__":
    print(f("A4"))
    print(f("a4"))
    print(f("4a"))
    print(f("bC123"))
    print(f("bcd555"))
    print(f("g80915"))

