# Napisz program, który rysuje funkcję y = sin(x) dla wartości kąta w zakresie 0-360 stopni.

import matplotlib.pyplot as plt
import math

x = []
y = []

# generujemy wartości x w stopniach
for deg in range(0, 361):
    x.append(deg)
    y.append(math.sin(math.radians(deg)))  # zamiana stopni na radiany

plt.plot(x, y)
plt.xlabel("x (stopnie)")
plt.ylabel("sin(x)")
plt.title("Wykres funkcji y = sin(x)")
plt.grid(True)
plt.show()
