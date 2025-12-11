# Napisz program, który rysuje wykres funkcji f(x)=x^2-3.

import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
   x.append(n)

# create y values
for n in x:
   y.append(n**2 - 3)

# print chart
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) = x^2 - 3")
plt.grid(True)
plt.show()