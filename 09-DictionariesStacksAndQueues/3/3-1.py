# Połóż 2 na stosie
# Połóż 3 na stosie
# Połóż 7 na stosie
# Połóż 4 na stosie
# Połóż 1 na stosie
# Połóż 9 na stosie
# Połóż 8 na stosie
# Zsumuj dwie ostatnie liczby ze stosu i wypisz wynik
# Oblicz sumę pozostałych elementów stosu i wypisz wynik. Użyj pętli 'while'.

import queue

stack = queue.LifoQueue()

stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

last = stack.get()
second_last = stack.get()
sum_last_two = last + second_last
print("Suma dwóch ostatnich liczb ze stosu:", sum_last_two)

sum_rest = 0
while not stack.empty():
    sum_rest += stack.get()

print("Suma pozostałych elementów stosu:", sum_rest)
