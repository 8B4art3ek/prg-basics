# Write a program that creates the following pattern. Sample result:

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

number = int(input("Enter number: "))
i = 0
while i < number:
    i += 1
    print("*"*i)
while i > 0:
    i -= 1
    print("*"*i)