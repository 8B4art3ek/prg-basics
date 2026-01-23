# Napisz program, który konwertuje dowolną liczbę naturalną na liczbę binarną. Użyj stosu. Aby przekonwertować liczbę, dziel ją przez 2, za każdym razem biorąc resztę z dzielenia i odkładając resztę na stos. Powtarzaj dzielenie, aż liczba, którą dzielisz, wyniesie zero. Następnie zdejmij (pop) i wyświetl wszystkie wartości ze stosu. Przykładowy wynik dla liczby 18:

# Division	Remainder
# 18 / 2 = 9	0
# 9 / 2 = 4	1
# 4 / 2 = 2	0
# 2 / 2 = 1	0
# 1 / 2 = 0	1
# Natural number: 18
# Binary number: 10010 

import queue

number = 18
stack = queue.LifoQueue()

n = number

while n > 0:
    stack.put(n % 2)
    n //= 2

binary = ""
while not stack.empty():
    binary += str(stack.get())

print("Natural number:", number)
print("Binary number:", binary)