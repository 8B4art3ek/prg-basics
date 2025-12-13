# W Pythonie funkcja sorted() służy do zwracania nowej posortowanej listy z elementów dowolnego obiektu iterowalnego (iterable), takiego jak lista, krotka czy słownik. Nie modyfikuje ona oryginalnego obiektu, lecz zwraca nową posortowaną listę.

# Jednym z opcjonalnych argumentów funkcji sorted() może być funkcja, która służy jako klucz do porównywania podczas sortowania. Na przykład możesz przekazać funkcję, która wyodrębnia konkretne pole z elementów.

# Znajdź składnię funkcji sorted() w Internecie. Następnie użyj tej funkcji, aby posortować listę imion według ich długości (liczby liter). Zdefiniuj funkcję anonimową, której użyjesz jako argumentu do funkcji sorted(). Przykładowy wynik:

# Unsorted list:
# names = [
#    'James',
#    'Emily',
#    'William',
#    'Olivia',
#    'Benjamin',
#    'Sophia',
#    'Henry']
# Sorted list:
# James
# Emily
# Henry
# Olivia
# Sophia
# William
# Benjamin


names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

sorted_names = sorted(names, key=lambda name: len(name))

print("Unsorted list:")
print(names)

print()

print("Sorted list:")
for name in sorted_names:
    print(name)