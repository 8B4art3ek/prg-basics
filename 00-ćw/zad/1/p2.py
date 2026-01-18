# (p2.py) Odwrotna Notacja Polska (RPN) to notacja matematyczna, w której operatory następują po swoich operandach, np. 2 3 + 4 *. Zdefiniuj funkcję f(expression), która, biorąc pod uwagę wyrażenie RPN, zwraca wartość tego wyrażenia. Wyrażenie zawiera tylko nieujemne liczby całkowite oraz operatory + i -. Przykład:

# f("2 3 4 5 + - +") returns -4
# f("11 7 + 15 - 14 +") returns 17

def f(expression):
    stack = []
    for token in expression.split():
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        else:
            stack.append(int(token))
    return stack[0]

if __name__ == "__main__":
    print(f("2 3 4 5 + - +"))
    print(f("11 7 + 15 - 14 +"))