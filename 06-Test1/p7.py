def f(a, b):
    first = 0
    second = 1
    
    wynik = 0
    if a == 0:
        wynik += first
    if a == 1:
        wynik += second

    while second < b:
        next_num = first + second
        first, second = second, next_num
        if next_num >= a:
            wynik += next_num

    return wynik

if __name__ == "__main__":
    print(f(1,5))
    print(f(6,21))