# Napisz program, który wyświetla pierwsze pięć linii z pliku it_company.csv, a następnie wypisuje 'Press Enter key...' w kolejnej linii i czeka na naciśnięcie klawisza Enter. Program ma powtarzać wyświetlanie kolejnych pięciu linii z pliku, czekając za każdym razem na wciśnięcie Entera.

chunk_size = 5

try:
    with open('it_company.csv', 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    current_line = 0

    while current_line < total_lines:
        for line in lines[current_line:current_line + chunk_size]:
            print(line.strip())
        
        current_line += chunk_size

        if current_line < total_lines:
            try:
                input("Wciśnij klawisz Enter...")
            except KeyboardInterrupt:
                print()
                print("Program został przerwany przez użytkownika")
                break

except FileNotFoundError:
    print("Plik 'it_company.csv' nie został znaleziony.")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")