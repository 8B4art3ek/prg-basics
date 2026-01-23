# Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user. Sample result:

# Enter number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60

number = int(input("Enter number: "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")