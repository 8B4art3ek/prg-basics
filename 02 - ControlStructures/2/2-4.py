###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input("Wprowadź pierwszą liczbę: "))
number2 = float(input("Wprowadź drugą liczbę: "))
operator = input("Wprowadź operator działania które chcesz wykonać (+, -, *, /): ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 == 0:
        print("Nie można dzielić przez 0")
        exit()
    else:
        result = number1 / number2

print(f'{number1} {operator} {number2} = {result}')