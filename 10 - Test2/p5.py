def f(shopping_cart, price_list, customer_wallet):
    total = 0
    for key, value in shopping_cart.items():
        if key in price_list:
            total += (price_list[key])*value
    if customer_wallet > total:
        return True
    else:
        return False

if __name__ == "__main__":
    cart = {'juice': 3, 'bread': 1, 'milk': 2}
    prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

    print(f(cart, prices, 10))
    print(f(cart, prices, 8))