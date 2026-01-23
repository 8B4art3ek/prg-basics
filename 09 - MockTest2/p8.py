# (p8.py) Odwrotna Notacja Polska (ONP) to notacja matematyczna, w której operatory następują po swoich operandach, np. 2 3 + 4 *. Zdefiniuj funkcję f(expression), która dla wyrażenia ONP zwraca wartość tego wyrażenia. Wyrażenie zawiera tylko nieujemne liczby całkowite oraz operatory + i -. 
# Przykład: f("2 3 +") -> 5 
# f("2 6 + 4 5 - +") -> 7
# f("11 7 + 15 - 14 +") -> 17

def f(expression):
    stack = []
    for token in expression.split():
        if token in "+-":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            else:
                stack.append(a - b)
        else:
            stack.append(int(token))
    return stack[0]

print(f("2 3 +"))
print(f("2 6 + 4 5 - +"))
print(f("11 7 + 15 - 14 +")) 