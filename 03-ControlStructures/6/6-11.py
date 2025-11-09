# A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints a purchase recommendation:

# Buy the product!!
# Product price reduced by 17%

# Create such program. The current and previous price of the product are included in variables. Sample result:

# Current product price: 140.00
# Previous product price: 200.00
# Buy the product!!
# Product price reduced by 30%

current_price = 140.00
previous_price = 200.00

discount = 100 - (current_price * 100 / previous_price)

if discount >= 10:
    print(f"Current product price: {current_price}")
    print(f"Previous product price: {previous_price}")
    print(f"Buy this product!!")
    print(f"Product price reduced by {discount}%")
else:
    print("Don't buy this product!!")