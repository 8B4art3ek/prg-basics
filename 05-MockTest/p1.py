def f(amount_to_pay):
    coins_5 = amount_to_pay // 5
    amount_to_pay = amount_to_pay % 5

    coins_2 = amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2

    coins_1 = amount_to_pay // 1
    amount_to_pay = amount_to_pay % 1

    return coins_5 + coins_2 + coins_1

if __name__ == "__main__":
    print(f(23))
    print(f(8))