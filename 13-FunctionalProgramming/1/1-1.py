# Zdefiniuj funkcję, która oblicza średnią arytmetyczną dwóch liczb. Następnie napisz program, który pobiera dwie liczby całkowite z klawiatury i oblicza ich średnią arytmetyczną.

###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   return (x+y)/2

# takes two numbers from keyboard
n1 = int(input("Podaj liczbe: "))
n2 = int(input("Podaj liczbe: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')