# Napisz program, który oblicza, wypisuje i zapisuje do pliku tekstowego liczby całkowite od 1 do 100 oraz ich drugie i trzecie potęgi. Przykładowy wynik:
# 1,1,1
# 2,4,8
# 3,9,27
# ...
# ...

with open("powers.txt", "w") as file:
    for i in range(1, 101):
        line = f"{i}, {i**2}, {i**3}"
        print(line)
        file.write(line + "\n")