# Zdefiniuj funkcję, która zwraca true, jeśli nawiasy (), {}, [] są użyte poprawnie w podanym wyrażeniu. W przeciwnym razie funkcja zwraca false. Następnie napisz program, który sprawdza poprawność wyrażeń podanych poniżej.

# Użyj stosu. Czytaj kolejne znaki wyrażenia. Pomiń wszystko oprócz nawiasów. Jeśli jest to nawias otwierający, połóż go na stosie. Jeśli jest to nawias zamykający, pobierz element ze stosu i porównaj, czy jest to pasujący nawias otwierający.

import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:
        if char in '({[':
            stack.put(char)
        elif char in ')}]':
            if stack.empty():
                return False
            top = stack.get()
            if top != pairs[char]:
                return False
    return stack.empty()

# Sprawdzamy wyrażenie1
if brackets_ok(expression1):
    print("Expression 1 brackets are correct.")
else:
    print("Expression 1 brackets are NOT correct.")

# Sprawdzamy wyrażenie2
if brackets_ok(expression2):
    print("Expression 2 brackets are correct.")
else:
    print("Expression 2 brackets are NOT correct.")

# Sprawdzamy wyrażenie3
if brackets_ok(expression3):
    print("Expression 3 brackets are correct.")
else:
    print("Expression 3 brackets are NOT correct.")

print("------------------------------------------------")

def brackets_ok(expression):
    stack = []   # stos na nawiasy otwierające

    for char in expression:

        # jeśli nawias otwierający – wrzucamy na stos
        if char == '(' or char == '{' or char == '[':
            stack.append(char)

        # jeśli nawias zamykający
        elif char == ')' or char == '}' or char == ']':
            
            # nie ma czego zdejmować → błąd
            if len(stack) == 0:
                return False

            last = stack.pop()

            # sprawdzamy, czy typ nawiasu się zgadza
            if char == ')' and last != '(':
                return False
            if char == '}' and last != '{':
                return False
            if char == ']' and last != '[':
                return False

    # na końcu stos musi być pusty
    return len(stack) == 0


# Sprawdzamy wyrażenie1
if brackets_ok(expression1):
    print("Expression 1 brackets are correct.")
else:
    print("Expression 1 brackets are NOT correct.")

# Sprawdzamy wyrażenie2
if brackets_ok(expression2):
    print("Expression 2 brackets are correct.")
else:
    print("Expression 2 brackets are NOT correct.")

# Sprawdzamy wyrażenie3
if brackets_ok(expression3):
    print("Expression 3 brackets are correct.")
else:
    print("Expression 3 brackets are NOT correct.")