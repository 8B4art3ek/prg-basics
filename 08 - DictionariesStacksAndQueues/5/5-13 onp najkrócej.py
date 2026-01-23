stack = []

for token in input("Wprowadź wyrażenie RPN: ").split():
    if token == '=':
        continue
    if token in "+-*/":
        b, a = stack.pop(), stack.pop()
        stack.append(eval(f"{a}{token}{b}"))
    else:
        stack.append(int(token))

print("Wynik:", int(stack[0]))