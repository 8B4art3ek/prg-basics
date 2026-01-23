# Zdefiniuj funkcję anonimową (lambda), która oblicza średnią arytmetyczną dwóch liczb. Szczegóły dotyczące definiowania funkcji anonimowej można znaleźć na stronie:
# https://www.w3schools.com/python/python_lambda.asp

# Następnie napisz program, który pobiera dwie liczby całkowite z klawiatury i oblicza ich średnią arytmetyczną.

# takes two numbers from keyboard
n1 = int(input("Podaj liczbe: "))
n2 = int(input("Podaj liczbe: "))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')
