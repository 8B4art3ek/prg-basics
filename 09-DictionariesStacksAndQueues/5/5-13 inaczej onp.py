def oblicz_onp(wyrazenie):
    stos = []
    tokens = wyrazenie.split()

    for token in tokens:
        if token == '=':
            continue
        if token.isdigit():
            stos.append(float(token))
        else:
            b = stos.pop()
            a = stos.pop()

            match token:
                case '+':
                    stos.append(a + b)
                case '-':
                    stos.append(a - b)
                case '*':
                    stos.append(a * b)
                case '/':
                    stos.append(a / b)
    return stos[0]

print(oblicz_onp("2 3 + ="))
print(oblicz_onp("2 4 1 + * ="))
print(oblicz_onp("2 3 + 4 5 + * ="))
print(oblicz_onp("8 3 1 + / 3 2 - 4 + * ="))