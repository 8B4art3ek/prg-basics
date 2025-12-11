# Zapoznaj się z metodami wizualizacji danych:
# https://www.w3schools.com/python/matplotlib_intro.asp

# Następnie, używając ‘matplotlib’, narysuj na wykresie linię od pozycji (1, 3) do pozycji (8, 10).
# Wskazówka: aby używać 'matplotlib' w swoich programach, musisz najpierw zainstalować moduł używając polecenia 'pip' (menedżer pakietów python).
# https://pythonguides.com/how-to-install-matplotlib-python/

import matplotlib.pyplot as plt
xpoints = [1, 8]
ypoints = [3, 10]
plt.plot(xpoints, ypoints)
plt.show()