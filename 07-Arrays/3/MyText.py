# Stwórz moduł MyText, zawierający:

# Funkcję, która zwraca liczbę słów w tekście
# Funkcję, która zwraca uporządkowaną tablicę słów, od najdłuższego do najkrótszego
# Funkcję, która zwraca tablicę słów uporządkowaną alfabetycznie

def liczba_slow(sentence):
    return len(sentence.split())

def slowa_od_najdluzszego(sentence):
    words = sentence.split()
    return sorted(words, key=len, reverse=True)

def alfabetycznie(sentence):
    words = sentence.split()
    return sorted(words, key=str.lower)