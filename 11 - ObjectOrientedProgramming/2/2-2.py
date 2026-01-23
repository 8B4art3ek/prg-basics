# Stwórz klasę reprezentującą utwory muzyczne. Zdefiniuj konstruktor klasy, który pozwala ustawić początkowe wartości utworu (wykonawca, tytuł utworu, album, rok) podczas tworzenia obiektu. Uzupełnij klasę o metodę __str__ zwracającą dane utworu jako ciąg znaków, w formacie jak poniżej (4 linie). Następnie stwórz dwa obiekty reprezentujące dwa utwory muzyczne i wypisz ich dane. Przykładowy wynik:

# Performer: Ed Sheeran
# Title:     Hearts Don't Break Around Here
# Album:     Divide
# Year:      2017

# Performer: Queen
# Title:     Bohemian Rhapsody
# Album:     A Night at the Opera
# Year:      1975

# class definition
class Song:
    def __init__(self, performer, title, album, year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f"Performer: {self.performer} \nTitle: {self.title} \nAlbum: {self.album} \nYear: {self.year}"

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

## object usage
print(song1)
print()
print(song2)