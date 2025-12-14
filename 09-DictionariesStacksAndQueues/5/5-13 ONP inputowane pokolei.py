# Poszukaj w Internecie i zapoznaj się z Odwrotną Notacją Polską (RPN - Reverse Polish Notation). Następnie napisz program, który oblicza wyrażenia RPN. RPN można wygodnie obliczać przy użyciu struktury stosu. Użytkownik może wprowadzić z klawiatury dowolną liczbę, operator (+ - * / ) lub znak równości (=).

# Jeśli wprowadzona wartość jest liczbą, połóż liczbę na stos
# Jeśli wprowadzona wartość jest operatorem, zdejmij dwa elementy z góry stosu, wykonaj obliczenie i połóż wynik operacji na stos.
# Jeśli wprowadzona wartość jest znakiem równości, zdejmij ostateczny wynik ze stosu i wyświetl wynik obliczenia.
# Następnie, używając programu, oblicz wartość wyrażeń RPN:

# Expression	RPN (Reverse Polish Notation)
# 2 + 3 =	                    2 3 + =
# 2 * (4 + 1)	                2 4 1 + * =
# (2 + 3) * ( 4 + 5) =	        2 3 + 4 5 + * =
# 8 / (3 + 1) * (3 - 2 + 4) =	8 3 1 + / 3 2 – 4 + * =

stack = []

while True:
    token = input("Wprowadź liczbę, operator (+ - * /) lub '=' aby zakończyć: ")

    if token == '=':
        if stack:
            result = stack.pop()
            print("Wynik:", result)
        else:
            print("Stos pusty")
        break
    elif token in "+-*/":
        if len(stack) < 2:
            print("Za mało liczb na stosie")
            continue
        b = stack.pop()
        a = stack.pop()
        match token:
            case '+':
                stack.append(a + b)
            case '-':
                stack.append(a - b)
            case '*':
                stack.append(a * b)
            case '/':
                stack.append(a / b)
    else:
        try:
            num = float(token)
            stack.append(num)
        except ValueError:
            print("Nieprawidłowa wartość")