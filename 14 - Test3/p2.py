def f(expression):
    stack = []
    for token in expression.split():
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a-b)
        else:
            stack.append(int(token))
    return stack[0]

if __name__ == "__main__":
    print(f("2 3 4 5 + - +"))
    print(f("11 7 + 15 - 14 +"))