# KLASY I OBIEKTY (CLASSES AND OBJECTS)

1. Programowanie obiektowe (OOP - Object-Oriented Programming) to paradygmat programowania oparty na koncepcji "obiektów". W OOP oprogramowanie jest projektowane poprzez definiowanie obiektów, które reprezentują byty ze świata rzeczywistego. Obiekty te mogą zawierać zarówno dane (atrybuty lub właściwości), jak i metody (funkcje lub zachowania), które operują na tych danych. Głównym celem OOP jest uczynienie kodu programu bardziej modularnym, wielokrotnego użytku i łatwiejszym w utrzymaniu.

   Obejrzyj film (od początku do 3:42) wyjaśniający koncepcje obiektu, klasy i wirtualizacji.

   <https://youtu.be/m_MQYyJpIjg?feature=shared>

1. W Pythonie klasa to konstrukcja, która pozwala definiować własne typy danych. Jest to fundamentalna koncepcja programowania obiektowego, umożliwiająca tworzenie obiektów, które łączą dane (`atrybuty`) i zachowania (`metody`).

   **Cechy klasy:**

   * **Atrybuty**: Zmienne przechowujące dane związane z obiektem. Mogą reprezentować stan obiektu, taki jak nazwa, wiek, cena itp.
   * **Metody**: Funkcje zdefiniowane wewnątrz klasy, które operują na obiektach tej klasy. Metody mogą modyfikować stan obiektu, pobierać informacje lub wykonywać określone działania.

   **Definiowanie klasy:**

   Aby zdefiniować klasę w Pythonie, używamy słowa kluczowego `class`. Przykład:

   ```python
   class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Object attribute
        self.model = model  # Object attribute
        self.year = year    # Object attribute

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")
   ```

   **W powyższym przykładzie:**

   * **Car** to klasa opisująca samochody.
   * **Konstruktor** `__init__()` to specjalna metoda wywoływana przy tworzeniu nowego obiektu. Inicjalizuje ona obiekt i przypisuje wartości do atrybutów obiektu.
   * `display_info` to metoda, która wypisuje informacje o samochodzie.

   **Tworzenie obiektu:**

   Obiekt jest instancją klasy, co oznacza konkretny egzemplarz opisany przez klasę. Tworzymy obiekt, wywołując klasę tak, jakby była funkcją.

   ```python
   my_car = Car("Toyota", "Corolla", 2021)  # Creating an object of the Car class
   my_car.display_info()  # Calling a method on the object
   ```

1. Dowiedz się, jak używać klas i obiektów w Pythonie:

   <https://youtu.be/f0TrMH9s-VE?feature=shared>

## 1. Tworzenie Klas i Obiektów

1. Plik `student.py` zawiera definicję klasy, która posiada atrybuty opisujące studenta. Zmodyfikuj klasę, dodając trzeci atrybut. Następnie wprowadź zmiany w programie, dodając trzeciego studenta. Przypisz wartości wszystkich dostępnych atrybutów dla wszystkich studentów. Na koniec wypisz informacje o wszystkich studentach.

1. Klasa `Square` reprezentuje obiekty opisujące figurę geometryczną (kwadrat). Uzupełnij klasę, dodając metodę do obliczania obwodu kwadratu. Następnie napisz program, który tworzy dwa kwadraty o bokach odpowiednio 4 i 6. Oblicz pola i obwody tych kwadratów. Wypisz wyniki.

   ```python
   class Square:
      def __init__(self, a):
         self.a = a
      def area(self):
         return self.a * self.a

   square1 = Square(4)
   square2 = ...

   print('Square with side 4:')
   print('Area is ..., Perimeter is ....')
   print ('Square with side 6:')
   ...
   ...
   ```

1. Plik `taxi.py` zawiera definicję klasy opisującej przejazdy taksówką. Uzupełnij klasę, dodając metodę `print_receipt(self)`, która drukuje paragon. Powinna ona zawierać wszystkie informacje o przejeździe: dystans, stawkę i opłatę. Następnie napisz program, w którym stworzysz dwa obiekty reprezentujące dwa różne przejazdy taksówką. Oblicz opłaty za oba przejazdy i wydrukuj paragony.

1. Klasa zawarta w `socialmedia.py` modeluje profil w mediach społecznościowych, pozwalając użytkownikom dodawać posty i wyświetlać ich oś czasu. Dodaj do klasy metodę `display_timeline(self)`, która wypisuje imię użytkownika wraz z listą postów. Ponumeruj elementy listy. Następnie napisz program, który tworzy użytkownika 'johndoe'. Dodaj następujące posty. Wypisz imię użytkownika i posty.

   * Hello, world! 
   * Had a great day at the park!
   * What's up, Natalie? How are you?

1. Klasa `Book`, dostępna w pliku `book.py`, zawiera zbiór atrybutów i metod opisujących książkę. Wprowadź zmiany tak, aby klasa zawierała również informację o cenie książki, którą można podać przy jej tworzeniu (ustal cenę na `48`). Wypisz informację o cenie wraz z innymi drukowanymi danymi.

1. Zidentyfikuj co najmniej 3 stany i 3 zachowania dla swojego smartfona. Następnie, dla wymienionych stanów i zachowań, stwórz klasę z atrybutami i metodami. Postaraj się używać czasowników w nazwach metod, ponieważ opisują one czynności. Na koniec stwórz obiekt smartfona, wywołaj jego metody i wyświetl właściwości obiektu.

   ```python
      class Phone():
         ...
         ...
         ...
   ```

## 2. Reprezentacja Tekstowa Obiektu (String Representation)

1. W Pythonie `__str__()` to specjalna metoda używana do zdefiniowania, jak obiekt powinien być reprezentowany jako ciąg znaków (string). Ta metoda jest wywoływana, gdy używasz funkcji `str()` lub `print()` na instancji klasy. Pozwala to kontrolować czytelną dla człowieka reprezentację tekstową Twoich obiektów.

   Metoda `__str__()` powinna zwracać ciąg znaków, który jest czytelną lub znaczącą reprezentacją obiektu. Jest używana głównie do wyświetlania obiektu użytkownikom. Kiedy przekazujesz obiekt do `str()` lub `print()`, Python wewnętrznie wywołuje `__str__()`, aby uzyskać tekstową reprezentację obiektu. Spójrz na poniższy przykład. Następnie uruchom ten program.

   ```python
   class Car:
      def __init__(self, brand, model, year):
         self.brand = brand
         self.model = model
         self.year = year

      def __str__(self):
         return f"{self.year} {self.brand} {self.model}"

   # Creating an instance of the Car class
   my_car = Car("Toyota", "Corolla", 2021)

   # Print the object
   print(my_car)  # Output: 2021 Toyota Corolla
   ```

   Dodatkowe informacje na temat metody `__str__` możesz znaleźć w Internecie:

   <https://www.pythontutorial.net/python-oop/python-__str__/>

1. Stwórz klasę reprezentującą utwory muzyczne. Zdefiniuj konstruktor klasy, który pozwala ustawić początkowe wartości utworu (wykonawca, tytuł utworu, album, rok) podczas tworzenia obiektu. Uzupełnij klasę o metodę `__str__` zwracającą dane utworu jako ciąg znaków, w formacie jak poniżej (4 linie). Następnie stwórz dwa obiekty reprezentujące dwa utwory muzyczne i wypisz ich dane. Przykładowy wynik:

   ```
   Performer: Ed Sheeran
   Title:     Hearts Don't Break Around Here
   Album:     Divide
   Year:      2017

   Performer: Queen
   Title:     Bohemian Rhapsody
   Album:     A Night at the Opera
   Year:      1975
   ```

   ```python
   # class definition
   class Song:
      def __...___(self,...,...,...,...):
         ...
         ...
         ...
         ...
      def __str.............
         ...
         ...
         ...
   
   # object creation
   song1 = ...
   song2 = ...

   ## object usage
   print(song1)
   ...
   ```

## 3. Klasa z Wieloma Komponentami

1. W pliku `tv.py` stwórz klasę TV, która opisuje telewizor. Klasa powinna zawierać jeden atrybut logiczny (boolean) o nazwie `is_on`, który określa, czy telewizor jest włączony. Początkowo telewizor jest wyłączony. Dodaj do klasy metody `turn_on()` i `turn_off()`, aby odpowiednio włączać i wyłączać telewizor. Dodaj także metodę `show_status()`, aby wypisać, czy telewizor jest włączony, czy wyłączony. Następnie w pliku `tv_show.py` napisz program główny, w którym spróbujesz stworzyć i użyć telewizora. Przykładowy komunikat:

   ```
   TV is on
   ```

   Następnie spróbuj użyć telewizora w programie:

   1. Stwórz telewizor
   1. Pokaż status telewizora
   1. Włącz telewizor
   1. Pokaż status telewizora
   1. Wyłącz telewizor
   1. Pokaż status telewizora

   ```python
   # tv.py file
   # class definition
   class TV:
      def __init__(self):
         self.is_on = False
      def turn_off(self):
         ...
      def turn_on ...
         ...
      ... show_status ...
   ```

   ```python
   # tv_show.py file
   # main program
   import ...

   def main():
      # object creation
      ...

      # object usage
      ...
   
   if __name__ == "__main__":
      main() 
   ```

1. W klasie TV dodaj atrybut `channel_no` wskazujący numer aktualnego kanału wyświetlanego przez telewizor. Początkowo telewizor jest ustawiony na kanał 1. Zmodyfikuj metodę `show_status()` tak, aby wypisywała również numer kanału, ale tylko wtedy, gdy telewizor jest włączony:

   ```
   TV is on, channel 1
   TV is off
   ```

   Następnie spróbuj użyć telewizora. Wypisz status telewizora zarówno po włączeniu, jak i wyłączeniu. Sprawdź, czy numer kanału jest wypisywany tylko wtedy, gdy telewizor jest włączony.

1. Dodaj metodę `set_channel(new_channel_no)` w klasie TV, aby ustawić numer kanału telewizora. Następnie spróbuj użyć telewizora.

   1. Stwórz telewizor
   1. Pokaż status telewizora
   1. Włącz telewizor
   1. Pokaż status telewizora
   1. Zmień kanał na 5
   1. Pokaż status telewizora
   1. Wyłącz telewizor
   1. Pokaż status telewizora 

1. W klasie TV dodaj atrybut `channels` zawierający listę nazw dostępnych kanałów TV (użyj tablicy/listy). Początkowo tablica powinna być pusta (telewizor niezaprogramowany, brak dostępnych kanałów). Dodaj metody `set_channels(channels_list)` i `show_channels()` w klasie TV, które pozwalają ustawić kanały w telewizorze i wypisać listę dostępnych kanałów. Przykładowa lista dostępnych kanałów:

   ```
   Channel list:
   1. TVP1
   2. TVP2
   3. Polsat
   4. TVN
   5. Filmbox
   6. Discovery
   ```

   Następnie spróbuj użyć telewizora:

   1. Stwórz telewizor
   1. Pokaż status telewizora
   1. Włącz telewizor
   1. Pokaż status telewizora
   1. Wyświetl listę dostępnych kanałów
   1. Ustaw kanały TV: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
   1. Wyświetl listę dostępnych kanałów
   1. Pokaż status telewizora
   1. Wyłącz telewizor

1. W klasie TV wprowadź zmiany w metodzie `show_status()` tak, aby wypisywała nie tylko wybrany numer kanału, ale także jego nazwę. Gdy wybrany numer kanału przekracza listę dostępnych kanałów, nazwa kanału nie jest wyświetlana.

   ```
   TV is on, channel 4 (TVN)
   ```

   Następnie spróbuj użyć telewizora. Ustaw co najmniej 7 kanałów (siedem stacji TV), zmień numery kanałów kilka razy i za każdym razem wypisz status telewizora.

1. W klasie TV dodaj obsługę regulacji głośności w zakresie od 0 do 10. Początkowa wartość poziomu głośności wynosi 0. Dodaj dwie metody, aby zwiększyć i zmniejszyć poziom głośności telewizora o jeden. Zwróć uwagę, że nie można zwiększyć ani zmniejszyć głośności poza określony zakres. Wyświetl aktualny poziom głośności w metodzie `show_status()`. Następnie sprawdź działanie telewizora, regulując i wyświetlając jego poziom głośności.

## 4. Trening czyni mistrza (Practice Makes Perfect)

1. Przeczytaj rozdział w podręczniku kursu, który dotyczy Programowania Obiektowego (Object-Oriented Programming).

1. Obejrzyj film o tym, jak definiowane są klasy w Pythonie:

   <https://youtu.be/apACNr7DC_s?feature=shared>

1. Zapoznaj się z tutorialami dostępnymi na w3schools, które dotyczą tworzenia klas i ich komponentów (pól i metod).

   <https://www.w3schools.com/python/python_classes.asp>

1. E-book to cyfrowa książka, którą można czytać za pomocą komputera lub innych urządzeń elektronicznych (czytników e-booków). Napisz program, w którym zdefiniujesz klasę opisującą stany i zachowania e-booka. Każda książka ma tytuł, autora, liczbę stron i numer bieżącej strony, która jest aktualnie czytana. Możliwe jest otwarcie książki - wtedy możemy ją czytać. Jeśli książka jest otwarta, możliwe jest przejście do następnej lub poprzedniej strony.

   Umieść klasę opisującą e-booki w osobnym pliku/module. W głównym pliku programu spróbuj użyć e-booka:

   1. Stwórz książkę z tytułem, autorem, liczbą stron (sprawdź, jak ustawić początkowe wartości pól w momencie tworzenia obiektu używając metody `__init__` / konstruktora i przekazując początkowe wartości jako argumenty wywołania metody)
   1. Otwórz książkę
   1. Wyświetl status książki (tytuł, autor, liczba stron, numer bieżącej strony)
   1. Przeczytaj kilka stron
   1. Wyświetl status książki
   1. Zamknij książkę
   1. Przeczytaj kilka stron (wykonanie tej operacji nie powinno być możliwe - wyświetl komunikat, że książka jest zamknięta).

1. Termometr medyczny mierzy temperaturę pacjenta w zakresie od 34.0 do 42.0 stopni Celsjusza, z dokładnością do 0.1 stopnia. Napisz program, w którym zdefiniujesz klasę opisującą stany i zachowania termometru. Termometr powinien umożliwiać pomiar temperatury (zrób to, generując losową liczbę z zakresu 34.0 do 42.0) i wyświetlać zmierzoną wartość. Jeśli temperatura wynosi co najmniej 37 stopni Celsjusza, termometr powinien dodatkowo wyświetlić komunikat 'Gorączka' (Fever), np.

   ```
   Temperature: 37.2C (fever)
   ```

   Gdy temperatura wynosi co najmniej 41.0, termometr powinien dodatkowo wypisać komunikat 'TEMPERATURA KRYTYCZNA!!' (CRITICAL TEMPERATURE!!). Umieść definicję klasy i program główny w osobnych plikach. Następnie użyj programu i:

   1. Stwórz termometr
   1. Włącz termometr
   1. Zmierz temperaturę
   1. Wyświetl temperaturę
   1. Wyłącz termometr

1. Konto bankowe posiada 26-cyfrowy numer przypisany podczas tworzenia konta. Początkowe saldo konta wynosi 0 PLN. Możesz wpłacić dowolną kwotę na konto. Możesz również wypłacić dowolną kwotę z konta, pod warunkiem, że nie przekracza ona salda konta. Jeśli spróbujesz wypłacić większą kwotę, wyświetlony zostanie komunikat: "Niewystarczające środki na koncie". W dowolnym momencie możliwe jest wyświetlenie informacji o numerze i saldzie konta bankowego w następującym formacie:

   ```
   Bank Account No: 11 1111 1111 1111 1111 1111 1111
   Balance: PLN 25,38
   ```

   Stwórz program obsługujący konto bankowe.

   1. Zapoznaj się z problemem.
   1. Zidentyfikuj obiekt.
   1. Zdefiniuj stany i zachowania obiektu.
   1. Przekształć stany i zachowania obiektu w pola i metody klasy, która posłuży jako wzorzec do tworzenia obiektu.
   1. Stwórz szkic klasy bez tworzenia treści metod.
   1. Stwórz treść każdej metody.

   Następnie użyj programu i:

   1. Stwórz konto bankowe o numerze 12 3456 5555 9090 1111 0000 7722
   1. Wyświetl saldo konta
   1. Wpłać 25,30 PLN
   1. Wyświetl saldo konta
   1. Wypłać 31,70 PLN
   1. Wyświetl saldo konta
   1. Wypłać 14 PLN
   1. Wyświetl saldo konta

1. Napisz program zawierający klasę Statistics, która opisuje właściwości dowolnego zbioru liczb. Klasa powinna umożliwiać:

   1. Dodanie do zbioru liczb kolejnej liczby wczytanej z klawiatury (przechowuj liczby w tablicy)
   1. Wyświetlenie wszystkich liczb oddzielonych spacją
   1. Wyznaczenie największej liczby
   1. Wyznaczenie najmniejszej liczby
   1. Obliczenie średniej arytmetycznej liczb
   1. Obliczenie mediany
   1. Wypisanie obliczonych / wyznaczonych wielkości statystycznych (minimum, maksimum, średnia arytmetyczna, mediana)

   Następnie użyj programu dla poniższych liczb, aby obliczyć i wypisać podstawowe statystyki:

   ```
   12, 37, 6, 9, 17 
   ```

1. Klasa `Contact` zawiera pola `name`, `email` i `telephone` umożliwiające opis pojedynczego kontaktu w smartfonie. Klasa `Contact_List` pozwala przechowywać kontakty (przechowywać obiekty opisujące kontakty w tablicy) i wykonywać następujące operacje:

   1. Dodaj nowy kontakt
   1. Wyświetl listę kontaktów

   Napisz program składający się z 3 plików (`smartphone.py`, `contact.py`, `contact_list.py`). W programie głównym (`smartphone.py`) stwórz obiekt reprezentujący listę kontaktów i dodaj dane następujących osób:

   ```
   John Brown     brown@onet.pl       555234000
   Anna May       am@o2.pl            232000199
   George Small   smallg@google.pl    222999100
   Paola Big      bigpaola@poczta.pl  100200300
   ```

   Następnie wyświetl listę kontaktów dostępną w smartfonie.

1. Obiekt reprezentujący pracownika zawiera następujące dane: imię, nazwisko, wiek i staż pracy (liczba przepracowanych lat). Zdefiniuj klasę `C`, która pozwala stworzyć obiekt. Podaj dane pracownika w momencie tworzenia obiektu, w podanej kolejności. Zdefiniuj w klasie reprezentację tekstową obiektu, która zawiera ciąg składający się z nazwiska, pierwszej litery imienia i stażu pracy. Jeśli pracownik jest pełnoletni (ma co najmniej 18 lat), użyj wielkich liter, w przeciwnym razie małych. Przykładowy wynik:

   ```
   C("Anna","May",17,7) returns "maya7"
   C("George","Brown",21,4) returns "BROWNG4"
   ```

1. Obiekt zawiera listę współrzędnych punktów na płaszczyźnie, jako tablicę dwuwymiarową. Zdefiniuj klasę `C`, która pozwala stworzyć obiekt. Podaj listę współrzędnych punktów w momencie tworzenia obiektu. W klasie `C` zdefiniuj metodę `m(n)`, która zwraca true, gdy co najmniej `n` punktów znajduje się w pierwszej ćwiartce układu współrzędnych (obie współrzędne punktu są większe od 0), lub false w przeciwnym wypadku. Przykładowy wynik:

   ```
   C([[2,3],[1,8],[-6,4],[3,-7]])
   m(2) returns True
   m(3) returns False
   ```

1. Stadion jest podzielony na sektory, każdy oznaczony literą. W każdym sektorze znajduje się pewna liczba kibiców. Zdefiniuj klasę `C`, która pozwala stworzyć obiekt reprezentujący stadion z listą sektorów i liczbą kibiców w sektorach. Dane, jako słownik, powinny być przekazane do obiektu w momencie jego tworzenia. Zdefiniuj w klasie metodę `m1(s,n)`, która pozwala zmienić liczbę kibiców `n` w sektorze `s` lub dodać nowy sektor `s` z podaną liczbą kibiców `n`. Zdefiniuj w klasie metodę `m2(s)`, która zwraca sumę kibiców w sektorach wymienionych w ciągu znaków `s`. Przykładowy wynik:

   ```
   C({"A":120,"D":150,"G":90,"K":110})
   m1("G",130)
   m2("GD") returns 280
   m2("KEJ") returns 110
   ```