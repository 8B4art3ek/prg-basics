# Napisz program do obliczania całkowitego kosztu koszyka zakupowego przy użyciu cennika.

# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total = 0

for product, quantity in cart.items():
    total += prices[product] * quantity

print(f"Total cost: {total:.2f}")