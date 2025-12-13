# Plik books.csv zawiera listę książek. Napisz program, który kopiuje dane książek z danego gatunku do odpowiadającego mu pliku. Użyj funkcji, aby podzielić program na logiczne części.

# Genre --> Filename
# Fantasy --> books_fantasy.txt
# Historical --> books_historical.txt
# Romance --> books_romance.txt
# Classic --> books_classic.txt  

import csv

GENRE_FILES = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt"
}

def read_books(filename):
    """Wczytuję książki z CSV do listy słowników"""
    with open(filename, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
    
def save_books_by_genre(books):
    """Zapisuje książki do plików według gatunku"""
    for genre, out_file in GENRE_FILES.items():
        with open(out_file, "w", encoding="utf-8") as file:
            for book in books:
                if book["Genre"] == genre:
                    file.write(f"{book['Title']},{book['Author']}\n")

def main():
    try:
        books = read_books("books.csv")
        save_books_by_genre(books)
        print("Gotowe. Książki zostały skopiowane do plików gatunków")
    except FileNotFoundError:
        print("Nie ma pliku books.csv")

if __name__ == "__main__":
    main()