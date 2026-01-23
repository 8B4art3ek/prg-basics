def f(number, even):
    result = 0
    match even:
        case True:
            for digit in str(number):
                if int(digit) % 2 == 0:
                    result += int(digit)
        case False:
            for digit in str(number):
                if int(digit) % 2 != 0:
                    result += int(digit)

    return result


if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))