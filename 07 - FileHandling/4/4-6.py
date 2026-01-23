# Napisz program, który oblicza liczbę linii, znaków i słów dla dowolnego pliku tekstowego. Użytkownik podaje nazwę pliku z klawiatury. Użyj bloku try-except, aby uniknąć przerwania programu, gdy użytkownik wpisze nazwę pliku, który nie istnieje. Wypisz wynik obliczeń. Aby sprawdzić, czy program działa poprawnie, znajdź w Internecie 3 pliki tekstowe i użyj ich do przetestowania programu. Przykładowy wynik:

# File name: books.txt
# Number of lines: 14
# Number of characters: 2540
# Number of words: 703

try:
    filename = input("Podaj nazwę pliku: ")
    with open(filename, "r") as file:
        lines = 0
        chars = 0
        words = 0

        for line in file:
            lines += 1
            chars += len(line)
            words += len(line.split())

    print(f"File name: {filename}")
    print(f"Number od lines: {lines}")
    print(f"Number of characters: {chars}")
    print(f"Number of words: {words}")

except FileNotFoundError:
    print("Nie ma takiego pliku.")