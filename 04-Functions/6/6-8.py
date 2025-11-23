# The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:

# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

def f(amount_to_pay):
    coins_5 = 0
    coins_2 = 0
    coins_1 = 0
    coins = 0

    coins_5 = amount_to_pay // 5
    amount_to_pay %= 5

    coins_2 = amount_to_pay // 2
    amount_to_pay %= 2

    coins_1 = amount_to_pay // 1
    amount_to_pay %= 1

    coins = coins_1 + coins_2 + coins_5
    return coins

if __name__ == "__main__":
    print(f(23))