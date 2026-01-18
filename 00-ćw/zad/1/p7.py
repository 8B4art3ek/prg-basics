# (p7.py) Każdy plik w systemie komputerowym ma nazwę i rozszerzenie. Stwórz funkcję f(files), która, biorąc pod uwagę listę plików, zwraca listę uporządkowaną według rozszerzenia nazwy pliku. Przykład:

# files = ["a.txt", "bb.pdf", "ccc.py", "dddd.mpeg4"]
# f(files) returns ["dddd.mpeg4", "bb.pdf", "ccc.py", "a.txt"]

def f(files):
    return sorted(files, key=lambda x: x.split('.')[-1])

if __name__ == '__main__':
    files = ["a.txt", "bb.pdf", "ccc.py", "dddd.mpeg4"]
    print(f(files))