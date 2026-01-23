# Write a program that allows you to create a shopping list. The program takes user input from the keyboard until the user enters 0. Each value taken is saved to a text file 'shopping_list.txt'.

# Hint: Open the file in append mode using the 'a' (append) parameter in the open() function.

###
# Creates a shopping list based on product names
# entered from the keyboard.
#

# shopping list file name
shopping_list = 'shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, product_name):
    with open(file_name,'a') as file:
        file.write(f"{product_name}\n")

# Takes next product name from the keyboard
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break
    else:
        add_product(shopping_list, product)