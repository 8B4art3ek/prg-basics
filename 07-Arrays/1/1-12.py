# Monthly expenses and their corresponding expense categories are included in the arrays below. Write a program that calculates which expense category was the most expensive.

categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = expenses.index(max(expenses))

print("The most expensive category is:", categories[max_index])
print("Amount spent:", expenses[max_index])