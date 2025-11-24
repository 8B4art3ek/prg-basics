# Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. The available operators are +,-,*,%,**. Sample result:

# f(2,3, "+") returns 5
# f(2,3, "%") returns 2
# f(2,3, "**") returns 8
# f(2,3, "*") returns 6
# f(2,3, "-") returns -1

def f(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "%":
            if number2 == 0:
                return "Nie mozna dzielic przez 0"
            else: 
                return number1 % number2
        case "**":
            return number1 ** number2
        
if __name__ == "__main__":
    print(f(2,3, "+"))
    print(f(2,3, "%"))
    print(f(2,3, "**"))
    print(f(2,3, "*"))
    print(f(2,3, "-"))