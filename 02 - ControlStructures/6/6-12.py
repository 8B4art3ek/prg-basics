# In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:

# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

number_of_products = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))

if number_of_products > 2:
    amount_to_pay = 2 * product_price + (number_of_products - 2) * product_price * 0.75

print(f"Amount to pay: {amount_to_pay}")