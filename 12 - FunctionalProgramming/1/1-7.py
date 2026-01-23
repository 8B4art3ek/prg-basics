# Zdefiniuj funkcję anonimową is_even(number), która sprawdza, czy liczba jest parzysta. Następnie przetestuj ją, pisząc program.

is_even = lambda number: True if number % 2 == 0 else False

print(is_even(5))
print(is_even(4))
print(is_even(10))
print(is_even(11))