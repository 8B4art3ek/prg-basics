# Zdefiniuj funkcję, która przyjmuje ciąg znaków (string) jako wejście i używa stosu do jego odwrócenia. Następnie napisz program do odwracania dowolnego tekstu wprowadzonego z klawiatury.

# Wskazówka: Połóż (push) każdy znak ciągu na stos, a następnie zdejmij (pop) znaki, aby utworzyć odwrócony ciąg.

def reverse_string(text):
    stack = []

    for char in text:
        stack.append(char)

    reversed_text = ""

    while stack:
        reversed_text += stack.pop()
    
    return reversed_text

text = input("Podaj tekst: ")
print(reverse_string(text))


# lepsze jest to:
text = input("Podaj tekst: ")
reversed_text = text[::-1]
print(reversed_text)