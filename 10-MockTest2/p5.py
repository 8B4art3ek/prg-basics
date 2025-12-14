# (p5.py) Zdefiniuj funkcję f(first_letter, last_letter), która dla pliku data.txt zwraca liczbę słów, które zaczynają się na first_letter i kończą na last_letter. 
# Przykład: f("w", "d") → porównaj swój wynik z innymi studentami

import re

def f(first_letter, last_letter):
    pattern = rf'\b{re.escape(first_letter)}\w*{re.escape(last_letter)}\b'
    with open('data.txt', 'r', encoding='utf-8') as file:
        text = file.read().lower()
    matches = re.findall(pattern, text)
    return len(matches)        

print(f("w", "d"))

