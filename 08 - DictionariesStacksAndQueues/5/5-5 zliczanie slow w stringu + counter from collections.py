# Napisz program, który zlicza, ile razy każde słowo występuje w akapicie.

# Wskazówka: Sprawdź w słowniku, czy kolejne słowo w nim występuje. Jeśli tak, zwiększ liczbę wystąpień słowa o 1. Możesz łatwo podzielić akapit na pojedyncze słowa używając metody split(). Poszukaj w Internecie, jak jej używać.

paragraph = "cat dog mouse cat rat cat mouse"
word_count = {}
words = paragraph.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word}: {count}")

print()
print()
print()

# WERSJA MAKAJLER

from collections import Counter

paragraph = "cat dog mouse cat rat cat mouse"

# Counter automatycznie zlicza wystąpienia słów
word_count = Counter(paragraph.split())

# wypisanie wyników
for word, count in word_count.items():
    print(f"{word}: {count}")