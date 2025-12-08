# PROGRAMOWANIE FUNKCYJNE (FUNCTIONAL PROGRAMMING)

1. Programowanie funkcyjne (FP) to paradygmat programowania, który traktuje obliczenia jako ewaluację funkcji matematycznych i unika zmiany stanu oraz mutowalnych (zmiennych) danych. Kładzie nacisk na użycie czystych funkcji (pure functions), niemutowalność (immutability) i funkcje wyższego rzędu. Programowanie funkcyjne jest deklaratywne, a nie imperatywne, co oznacza, że skupia się na tym, *co* zrobić, a nie *jak* to zrobić.

   W programowaniu funkcyjnym funkcje są traktowane jako obywatele pierwszej kategorii (first-class citizens), co oznacza, że mogą być przypisywane do zmiennych, przekazywane jako argumenty i zwracane z innych funkcji. Ułatwia to tworzenie kodu modularnego, wielokrotnego użytku i łatwego do łączenia (kompozycji).

   **Kluczowe koncepcje programowania funkcyjnego:**

   * **Czyste Funkcje (Pure Functions)**: Czysta funkcja to taka, której wynik zależy wyłącznie od wartości wejściowych i nie posiada skutków ubocznych (nie modyfikuje żadnego zewnętrznego stanu ani zmiennych). Dla tych samych danych wejściowych czysta funkcja zawsze zwróci ten sam wynik.

   * **Niemutowalność (Immutability)**: Dane są uważane za niemutowalne, co oznacza, że nie można ich zmienić po utworzeniu. Zamiast modyfikować dane, tworzone są nowe struktury danych.

   * **Funkcje Wyższego Rzędu (Higher-Order Functions)**: Funkcja wyższego rzędu to funkcja, która przyjmuje jedną lub więcej funkcji jako argumenty, zwraca funkcję lub robi obie te rzeczy. Pozwala to na łączenie funkcji, ich ponowne wykorzystanie i przekazywanie jak każdych innych danych.

   * **Funkcje Pierwszej Kategorii (First-Class Functions)**: Funkcje są obywatelami pierwszej kategorii, co oznacza, że można je traktować jak zmienne. Mogą być przekazywane jako argumenty, zwracane z innych funkcji i przechowywane w strukturach danych.

   * **Rekurencja**: Zamiast używać pętli, programowanie funkcyjne często polega na rekurencji w celu iteracji. Rekurencja pozwala funkcji wywoływać samą siebie, dopóki nie zostanie spełniony warunek bazowy.

1. Python nie jest czysto funkcyjnym językiem programowania; jest językiem wieloparadygmatowym, co oznacza, że wspiera programowanie funkcyjne, obiektowe i proceduralne. Jednak Python oferuje kilka funkcji, które pozwalają na stosowanie technik programowania funkcyjnego, takich jak:

   * Funkcje pierwszej kategorii.
   * Funkcje wyższego rzędu, takie jak `map()`, `filter()` i `reduce()`.
   * Funkcje lambda (funkcje anonimowe).

   Obejrzyj film, aby dowiedzieć się, jak używać funkcji (`map`, `filter`, `reduce`), aby wspierać programowanie funkcyjne w Pythonie.

   [https://youtu.be/hUes6y2b--0?feature=shared](https://youtu.be/hUes6y2b--0?feature=shared)

## 1. Funkcja Anonimowa (Lambda)

1. Zdefiniuj funkcję, która oblicza średnią arytmetyczną dwóch liczb. Następnie napisz program, który pobiera dwie liczby całkowite z klawiatury i oblicza ich średnią arytmetyczną.

   ```python
   ###
   # Calculates arithmetic mean of two integer numbers
   #
   def mean(x,y):
      ...
      return ...
   
   # takes two numbers from keyboard
   n1 = input(...)
   n2 = ...

   # calculates arightmtic mean and print result
   result = mean(n1,n2)
   print(f'The arithmetic mean of the numbers ... and ... is ...')
   ```

1. Zdefiniuj funkcję anonimową (lambda), która oblicza średnią arytmetyczną dwóch liczb. Szczegóły dotyczące definiowania funkcji anonimowej można znaleźć na stronie:

   [https://www.w3schools.com/python/python_lambda.asp](https://www.w3schools.com/python/python_lambda.asp)

   Następnie napisz program, który pobiera dwie liczby całkowite z klawiatury i oblicza ich średnią arytmetyczną.

   ```python
   # takes two numbers from keyboard
   n1 = input(...)
   n2 = ...

   # define an anonymous function
   mean = lambda x,y: (x+y)/2


   # calculates arightmtic mean and print result
   result = mean(n1,n2)
   print(f"The arithmetic mean of ...............")
   ```

1. Napisz program, który przelicza prędkość w metrach na sekundę na prędkość w kilometrach na godzinę. Zdefiniuj funkcję `ms_to_kmh(ms)`, która zwraca obliczoną prędkość w km/h. Przykładowy wynik:

   ```
   10 m/s = 36 km/h
   35 m/s = 126 km/h
   ```

1. Napisz program, który przelicza prędkość w metrach na sekundę na prędkość w kilometrach na godzinę. Zdefiniuj i użyj funkcji anonimowej `ms_to_kmh(ms)`. Przykładowy wynik:

   ```
   10 m/s = 36 km/h
   35 m/s = 126 km/h
   ```

1. Napisz program, który oblicza średnią prędkość pojazdu. Wprowadź z klawiatury: dystans w km, liczbę godzin podróży i liczbę minut podróży. Zdefiniuj funkcję `avg_speed(distance,hours,minutes)`, która zwraca obliczoną średnią prędkość. Przykładowy wynik:

   ```
   Enter distance in km: 70
   Enter number of travel hours: 1
   Enter number of travel minutes: 23
   Average speed: 50.6 km/h 
   ```

1. Napisz program, który oblicza średnią prędkość pojazdu. Wprowadź z klawiatury: dystans w km, liczbę godzin podróży i liczbę minut podróży. Zdefiniuj i użyj funkcji anonimowej `avg_speed(distance,hours,minutes)` do obliczenia wyniku. Przykładowy wynik:

   ```
   Enter distance in km: 70
   Enter number of travel hours: 1
   Enter number of travel minutes: 23
   Average speed: 50.6 km/h 
   ```

1. Zdefiniuj funkcję anonimową `is_even(number)`, która sprawdza, czy liczba jest parzysta. Następnie przetestuj ją, pisząc program.

1. Zdefiniuj funkcję anonimową `initials(name,surname)`, która zwraca pierwsze litery imienia i nazwiska.

## 2. Funkcja Wyższego Rzędu (Higher-Order Function)

1. Kurs edukacyjny kończy się testem sprawdzającym wiedzę uczestników. Aby zaliczyć kurs, uczestnik musi uzyskać minimalną liczbę punktów. Poniższy program zawiera funkcję wyższego rzędu `min_pts`, która zwraca inną funkcję. Przeczytaj kod programu. Następnie uruchom program.

   ```python
   def min_pts(limit):
      def check(pts):
         if pts >= limit:
            return True
         return False
      return check

   print("=== MIN 50 PTS TO PASS ===")
   assess_test = min_pts(50)
   print(f"52 pts -> {assess_test(52)}")
   print(f"39 pts -> {assess_test(39)}")

   print("=== MIN 60 PTS TO PASS ===")
   assess_test = min_pts(60)
   print(f"52 pts -> {assess_test(52)}")
   print(f"39 pts -> {assess_test(39)}")
   ```

1. W Pythonie funkcja `sorted()` służy do zwracania nowej posortowanej listy z elementów dowolnego obiektu iterowalnego (iterable), takiego jak lista, krotka czy słownik. Nie modyfikuje ona oryginalnego obiektu, lecz zwraca nową posortowaną listę.

   Jednym z opcjonalnych argumentów funkcji `sorted()` może być funkcja, która służy jako klucz do porównywania podczas sortowania. Na przykład możesz przekazać funkcję, która wyodrębnia konkretne pole z elementów.

   Znajdź składnię funkcji `sorted()` w Internecie. Następnie użyj tej funkcji, aby posortować listę imion według ich długości (liczby liter). Zdefiniuj funkcję anonimową, której użyjesz jako argumentu do funkcji `sorted()`. Przykładowy wynik:

   ```
   Unsorted list:
   names = [
      'James',
      'Emily',
      'William',
      'Olivia',
      'Benjamin',
      'Sophia',
      'Henry']
   ```

   ```
   Sorted list:
   James
   Emily
   Henry
   Olivia
   Sophia
   William
   Benjamin
   ```


## 3. Mapowanie Danych (Data Mapping)

1. Poniższy raport pokazuje ostatnie pięć płatności kartą kredytową w Euro:

   ```
   15.90
   38.47
   4.07
   132.70
   9.15
   ```

   Napisz program, który oblicza i wyświetla kwoty transakcji w polskich złotych (1 EUR = 4.5 PLN). Użyj funkcji anonimowych oraz funkcji `map()`. Przykładowy wynik:

   ```
   71.55
   173.11
   18.31
   597.15
   41.17
   ```

   ```python
   transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
   transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))
   # print pln list ...
   ```

1. Dla następującego tekstu:

   ```
   I completely agree with you
   ```

   napisz program, który oblicza i wyświetla liczbę liter w każdym słowie. Użyj funkcji `map()` oraz funkcji anonimowych do obliczenia liczby liter.
   
   > Wskazówka: aby podzielić tekst na słowa, użyj funkcji `split()`.
   
   Przykładowy wynik:

   ```
   Text: I completely agree with you
   No. of letters in words: [1,10,5,4,3]
   ```

   ```python
   sentence = '...'
   result = list(map(lambda ... , sentence. ...))
   print(result)
   ```

1. Poniższe dane zawierają listę produktów dostępnych w magazynie oraz ich cenę jednostkową.

   ```python
   stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
   ```

   Napisz program, który oblicza całkowitą wartość produktów w magazynie. Użyj funkcji `map()`, `sum()` oraz funkcji anonimowej. Przykładowy wynik:

   ```python
   Products in stock: [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
   Total value: 423.35
   ```

## 4. Filtrowanie Danych (Data Filtering)

1. Następujące osoby są zatrudnione w jednym z działów firmy:

   ```
   SMITH Lucy
   JONES Janet
   LEE Jerry
   JACKSON Peter
   JOHNSON Rick
   LEWIS Terry
   CLARKE Robin
   ```

   Zapisz listę pracowników w tablicy (liście) ciągów znaków. Następnie napisz program, który wyświetla osoby, których nazwiska zaczynają się na literę 'J'. Użyj funkcji anonimowych oraz `filter()`. Przykładowy wynik:

   ```
   JONES Janet
   JACKSON Peter
   JOHNSON Rick
   ```

   ```python
   employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
                  "JACKSON Peter","JOHNSON Rick",
                  "LEWIS Terry","CLARKE Robin"]
   emp_J = list(filter(lambda e:...=="J", employees))
   # print a list …
   ``` 
   ...

1. Fotoradar umieszczony w mieście mierzy prędkość przejeżdżających pojazdów. Maksymalna dozwolona prędkość pojazdów wynosi 50 km/h. W ostatniej minucie fotoradar zarejestrował następujące wartości:

   ```
   48,47,54,50,42,68,39,46
   ```

   Napisz program, który wyświetla wartości prędkości wyższe niż dozwolona prędkość. Użyj funkcji anonimowych oraz `filter()`. Przykładowy wynik:

   ```
   Recorded values: 48,47,54,50,42,68,39,46
   Speed too high: 54,68
   ```

1. Oceny końcowe uzyskane przez studentów z przedmiotu "Geografia Ekonomiczna" są zawarte w tablicy:

   ```
   [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
   ```

   Napisz program, który oblicza średnią arytmetyczną ocen, wykluczając oceny negatywne (2.0). Użyj `filter()` wraz z funkcją anonimową. Przykładowy wynik:

   ```
   Arithmetic mean for grades <> 2.0 is 3.85
   ```

## 5. Redukcja Danych (Data Reducing)

1. Funkcja `reduce()` w Pythonie, która jest dostępna w module `functools`, służy do kumulatywnego stosowania funkcji do elementów obiektu iterowalnego, redukując go do pojedynczej wartości. Składnia:

   ```python
   from functools import reduce

   reduce(function, iterable[, initializer])
   ```

   Gdzie:

   * function: Funkcja, która przyjmuje dwa argumenty i wykonuje na nich operację.
   * iterable: Obiekt iterowalny (taki jak lista, krotka itp.), którego elementy są redukowane.
   * initializer (opcjonalny): Wartość początkowa rozpoczynająca proces redukcji.

   Jak działa reduce():

   * Pobiera funkcję, która akceptuje dwa argumenty.
   * Stosuje funkcję do pierwszych dwóch elementów obiektu iterowalnego.
   * Używa wyniku funkcji, aby połączyć go z następnym elementem.
   * Powtarza ten proces, aż wszystkie elementy zostaną przetworzone.
   * Zwraca pojedynczą, zredukowaną wartość jako wynik końcowy.

   Poniższy program oblicza sumę liczb. Zwróć uwagę na użycie funkcji `reduce()`. Następnie zmodyfikuj program: zastąp zwykłą funkcję `add(x,y)` funkcją anonimową.


   ```python
   from functools import reduce

   # Function to add two numbers
   def add(x, y):
      return x + y

   numbers = [1, 2, 3, 4, 5]

   # Using reduce to sum the numbers
   result = reduce(add, numbers)
   print(result)  # Output: 15
   ```

1. Napisz program, który oblicza sumę liczb parzystych. Użyj `filter()`, `reduce()` oraz funkcji anonimowych.

   > Wskazówka. Najpierw użyj filtrowania, aby wyodrębnić liczby parzyste. Następnie użyj `reduce()`, aby obliczyć sumę tych liczb.

   ```python
   numbers = [2,4,6,3,7,5]
   ```

## 6. Trening czyni mistrza (Practice Makes Perfect)

1. Zapoznaj się z podstawowymi koncepcjami programowania funkcyjnego:

   [https://www.geeksforgeeks.org/functional-programming-in-python/](https://www.geeksforgeeks.org/functional-programming-in-python/)

1. Przeczytaj tekst związany z programowaniem funkcyjnym w Pythonie:

   [https://www.codecademy.com/article/functional-programming-in-python](https://www.codecademy.com/article/functional-programming-in-python)

1. Obejrzyj film, aby dowiedzieć się o funkcjach wyższego rzędu:

   [https://youtu.be/xZtTIm3fpfA?feature=shared](https://youtu.be/xZtTIm3fpfA?feature=shared)

1. Tablica zawiera liczby od 1 do 20. Napisz program, który oblicza i wyświetla ich trzecią potęgę. Użyj `map()` i funkcji anonimowej.

1. Tablica zawiera liczby od 1 do 20. Napisz program, który wyświetla tylko liczby podzielne przez 2 i 3 bez reszty. Użyj `filter()` i funkcji anonimowej.

1. Poniższa tablica zawiera dane pracowników:

   ```python
   [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
      ("Jackson","Peter"),("Johnson","Rick"),
      ("Lewis","Terry"),("Clarke","Robin")]
   ```

   Napisz program, który wyznacza i wyświetla listę pracowników, których nazwiska są podane wielkimi literami, a po nich imiona, oddzielone przecinkami. Przykładowy wynik:

   ```
   SMITH, Lucy
   JONES, Janet
   …
   …
   ```

1. W zawodach w skokach narciarskich każdy zawodnik jest oceniany przez pięciu sędziów. Każdy sędzia może przyznać ocenę od 0 do 20 punktów. Najwyższa i najniższa ocena są odrzucane. Pozostałe trzy oceny są sumowane, tworząc wynik końcowy uzyskany przez zawodnika. Oceny czterech zawodników przedstawiono poniżej.

   ```
   [(17,15,16,17,15),
    (16,18,19,17,19),
    (19,15,15,19,18),
    (18,17,19,15,16)]
   ```

   Oblicz i wyświetl całkowitą liczbę punktów uzyskanych przez zawodników.
   
   > Wskazówka: użyj wbudowanych funkcji Pythona: `map()`, `sum()`, `min()`, `max()`.
   
   Przykładowy wynik:

   ```
   [48, 54, 52, 51]
   ```

1. Kurs edukacyjny zakończył się testem sprawdzającym wiedzę uczestników. Oto wyniki uzyskane przez studentów:

   ```
   [37,51,44,23,78,92,39,84,83,51]
   ```

   Napisz program, który oblicza i wyświetla wyniki studentów, które są równe lub wyższe niż następująca minimalna liczba punktów potrzebna do zaliczenia kursu:

   1. 70
   1. 40
   1. 30

   Użyj funkcji `filter()` i następującej funkcji wyższego rzędu:

   ```python
   def min_pts(limit):
      return lambda pts: pts>=limit
   ```

   Przykładowy wynik:

   ```
   Min 70 pts: [78, 92, 84, 83]
   Min 40 pts: [51, 44, 78, 92, 84, 83, 51]
   Min 30 pts: [37, 51, 44, 78, 92, 39, 84, 83, 51]
   ```

1. Stacje pomiarowe zarejestrowały następujące temperatury w stopniach Celsjusza:

   ```
   {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
   ```

   Napisz program, który wyświetla nazwy miast, w których zarejestrowano dodatnie temperatury. Użyj funkcji anonimowych i `filter()`. Przykładowy wynik:

   ```
   Cities with positive temperatures: Krakow Sopot Opole
   ```

1. Stacje pomiarowe zarejestrowały następujące temperatury w stopniach Celsjusza:

   ```
   {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
   ```

   Napisz program, który tworzy wykres słupkowy pokazujący temperatury zarejestrowane w miastach. Dodaj tytuł wykresu oraz opisy osi x i y.
   
   > Wskazówka: użyj funkcji `map()`, aby utworzyć dwie tablice danych dla wykresu.

1. Studenci uzyskali następujące wyniki testów (w punktach, od 0 do 100):

   ```python
   test_results = [
      {"name":"Peter","result":27},
      {"name":"Anna","result":63},
      {"name":"Robert","result":92},
      {"name":"Paul","result":46},
      {"name":"Barbara","result":52}]
   ```

   Napisz program, który wyświetla studentów, których wyniki mieszczą się w przedziale od 50 do 70 punktów. Użyj funkcji anonimowej i funkcji `filter()`.

1. Na jednych z Igrzysk Olimpijskich klasyfikacja medalowa wygląda następująco:

   ```
   {"country":"Denmark","gold":2,"silver":4,"bronze":6}
   {"country":"Finland","gold":5,"silver":0,"bronze":4}
   {"country":"USA","gold":12,"silver":5,"bronze":11}
   {"country":"Peru","gold":0,"silver":1,"bronze":7}
   ```

   Napisz program, który wyświetla dane krajów, które zdobyły co najmniej 10 medali. Użyj funkcji anonimowych i ```filter()```. Przykładowy wynik:

   ```
   COUNTRIES WITH AT LEAST 10 MEDALS
   Denmark: 2,4,6
   USA: 12,5,11
   ```

1. Na jednych z Igrzysk Olimpijskich klasyfikacja medalowa wygląda następująco:

   ```
   {"country":"Denmark","gold":2,"silver":4,"bronze":6}
   {"country":"Finland","gold":5,"silver":0,"bronze":4}
   {"country":"USA","gold":12,"silver":5,"bronze":11}
   {"country":"Peru","gold":0,"silver":1,"bronze":7}
   ```

   Napisz program, który tworzy wykres słupkowy pokazujący całkowitą liczbę medali zdobytych przez każdy kraj. Dodaj tytuł wykresu oraz opisy osi x i y.
   
   > Wskazówka: Użyj funkcji `map()`, aby utworzyć tablice danych dla swojego wykresu.

1. W fabryce napojów maszyna napełnia butelki o pojemności 500 ml. Komputer sprawdza, czy butelka została napełniona prawidłowo. Dla butelki 500 ml dopuszczalna tolerancja wynosi 2%. W ostatnich dziesięciu sprawdzonych butelkach napełnienie wynosiło:

   ```
   508,500,512,499,492,511,503,476,501,509
   ```

   Napisz program, który oblicza procent nieprawidłowo napełnionych butelek. Użyj `filter()` wraz z funkcją wyższego rzędu. Przykładowy wynik:

   ```
   Bottle capacity:    500ml
   Filling tolerance:  2%
   Filled bottles:     508,500,512,499,492,511,503,476,501,509
   Incorrectly filled: 30%
   ```