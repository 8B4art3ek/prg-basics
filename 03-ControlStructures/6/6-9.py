# Most female names in Polish end with the letter "a". Write a program that prints the name entered from the keyboard, provided it is a female name. Sample result:
# Enter name: Anna
# Anna -- Polish female name

imie = input("Podaj imię: ")
if imie[-1] == "a":
    print("Polish female name")
else:
    print("Nie wiem")

