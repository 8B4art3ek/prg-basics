# An expression contains operators for adding and subtracting single-digit numbers. Define a function f(expression) that returns the value of the expression. Sample result:

# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6

def f(expression):
    return eval(expression)

if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))