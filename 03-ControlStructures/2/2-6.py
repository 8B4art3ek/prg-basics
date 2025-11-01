# Write a program that checks what number was entered from the keyboard and prints one of the messages below. Then run the program and check the following numbers:
# 7, 1, 0, -1, -4
# Number ... is positive
# Number ... is negative
# Number is 0

liczba = int(input("Podaj liczbe: "))
if liczba == 0:
    print("Podana liczba jest zerem")
elif liczba < 0:
    print(f"Liczba {liczba} jest ujemna")
elif liczba > 0:
    print(f"Liczba {liczba} jest dodatnia")