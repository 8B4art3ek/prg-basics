# Zdefiniuj funkcję anonimową initials(name,surname), która zwraca pierwsze litery imienia i nazwiska.

initials = lambda name, surname: f"{name[0]}.{surname[0]}"

print(initials("Jan", "Kowalski"))
print(initials("Donald", "Tusk"))