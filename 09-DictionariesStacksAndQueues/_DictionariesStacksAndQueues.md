<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# SŁOWNIKI, STOSY I KOLEJKI (DICTIONARIES, STACKS AND QUEUES)

## 1. Słownik (Dictionary)

1. Słownik to wbudowana struktura danych, która przechowuje dane w parach klucz-wartość. Każdy klucz jest unikalny i mapuje (wskazuje) na konkretną wartość, co pozwala na efektywne pobieranie, aktualizowanie i zarządzanie danymi. Słowniki są mutowalne (zmienne), co oznacza, że możesz modyfikować ich zawartość po utworzeniu.

   Spójrz na poniższy słownik. Zawiera on trzy elementy oddzielone przecinkami. Każdy element w słowniku składa się z klucza i wartości, gdzie klucz działa jak identyfikator do uzyskania dostępu do przypisanej mu wartości.

   ```python
   student = {'name':'John', 'age':25, 'major':'Computer Science'}
   ```

1. Zapoznaj się z podstawowymi operacjami, jakie możesz wykonywać na słowniku.

   **Podstawowe operacje na słowniku**

   ```python
   # Utworzenie słownika
   student = {
      'name': 'John',
      'age': 22,
      'major': 'Computer Science'
   }

   # Dostęp do wartości
   print(student['name'])

   # Dodanie nowej pary klucz-wartość
   student['grade'] = 'A'

   # Modyfikacja istniejącej wartości
   student['age'] = 23

   # Usunięcie pary klucz-wartość
   del student['major']
   print(student)
   ```

   **Iterowanie przez słownik**

   ```python
   # Utworzenie słownika
   fruits = {'apple': 3, 'banana': 5, 'orange': 2}

   # Iterowanie po kluczach
   for fruit in fruits:
      print(fruit)

   # Iterowanie po wartościach
   for count in fruits.values():
      print(count)

   # Iterowanie po parach klucz-wartość
   for fruit, count in fruits.items():
      print(f"The count of {fruit} is {count}")
   ```

   **Sprawdzanie, czy klucz istnieje**

   ```python
   # Utworzenie słownika
   person = {'name': 'Alice', 'age': 30}

   # Sprawdzenie czy klucz istnieje
   if 'name' in person:
      print("Name is present in the dictionary.")
   else:
      print("Name is not present.")
   ```

1. Stwórz słownik opisujący Twój telefon komórkowy. Użyj 6 par klucz-wartość. Następnie, używając pętli `for`, wyświetl zawartość słownika. Aby odczytać klucz i wartość, użyj metody `items()`. Przykładowy wynik:

   ```python
   mobile = {
   "OS":"Android",
      …
      …
      …
      …
      …
   }
   for key,value in mobile.items():
      print(f"{key} : {…}")
   ```

1. Stwórz słownik, jak w przykładzie poniżej. Czy wiesz, jaki typ wartości został użyty w każdej z sześciu par klucz-wartość?

   ```python
   person = {
      "name": "Marek",
      "surname": "Banach",
      "age": 25,
      "hobby": ["swimming","excursions"],
      "married": True,
      "phone":{"landline":"123444321","mobile":"777888999"}
   }
   ```

   Następnie stwórz program, który:

   1. Wyświetla imię (name)
   1. Wyświetla hobby
   1. Wyświetla całą zawartość słownika
   1. Zmienia nazwisko (surname) na 'Nowak'
   1. Zmienia stan cywilny osoby (married)
   1. Dodaje płeć (gender): 'male'
   1. Dodaje nowe hobby: 'bicycle'
   1. Dodaje telefon służbowy do istniejących telefonów: '313131444'
   1. Wyświetla całą zawartość słownika (iteruj po elementach słownika)

1. Stwórz tablicę (listę) z 5 słownikami, z których każdy zawiera kraj i jego populację. Następnie wypisz zawartość tablicy. Przykładowy wynik:

   ```
   COUNTRY  POPULATION
   Poland   38000000
   …        …
   …        …
   …        …
   …        …
   ```

   ```python
   countries = [
   {"name":"Poland", "population":38000000},
      …
      …
      …
      …
   ]
   ```

1. Napisz program, który wypisuje szczegóły osób z książki telefonicznej, których imiona zaczynają się na literę 'D'.

   ```python
   phone_book = {
      'John': '555-1234',
      'David': '555-5678',
      'Bob': '555-8765',
      'Charlie': '555-4321',
      'Diana': '555-9876',
      'Eve': '555-6543',
      'Frank': '555-3456',
      'Grace': '555-7890',
      'Hank': '555-1111',
      'Ivy': '555-2222',
      'Jack': '555-3333',
      'Daniel': '555-4444',
      'Liam': '555-5555',
      'Mia': '555-6666',
      'Nina': '555-7777',
      'Oscar': '555-8888',
      'Paul': '555-9999',
      'Dominic': '555-1010',
      'Rachel': '555-2020',
      'Sam': '555-3030'
   }

   ...
   ...
   ...
   ```

1. Poniższe dane zawierają informacje o liczbie produktów dostępnych w sklepie komputerowym. Napisz program, który wypisuje:

   * listę produktów i ich ilość
   * całkowitą liczbę produktów w sklepie

   ```python
   {
   'Laptop': 15,
   'Desktop PC': 10,
   'Monitor': 25,
   'Keyboard': 50,
   'Mouse': 60,
   'External Hard Drive': 30,
   'Printer': 12,
   'Router': 20,
   'USB Flash Drive': 100,
   'Graphics Card': 8
   }
   ```

1. Poniższe dane zawierają cennik artykułów ze sklepu odzieżowego wraz z ich cenami. Z powodu sezonowej wyprzedaży sklep obniża cenę każdego artykułu o 10%. Napisz program, który:

   * wypisuje listę produktów i ich ceny przed obniżką
   * wypisuje całkowitą wartość produktów przed obniżką
   * modyfikuje cennik zgodnie z rabatem (zaokrąglij ceny do dwóch miejsc po przecinku)
   * wypisuje listę produktów i ich ceny po 10% zniżce
   * wypisuje całkowitą wartość produktów po zniżce

   ```python
   price_list = {
      'T-shirt': 19.99,
      'Jeans': 49.99,
      'Jacket': 89.99,
      'Sneakers': 59.99,
      'Hat': 15.99
   }
   ```

## 2. Zbiór (Set)

1. Zbiór to nieuporządkowana kolekcja unikalnych elementów. Zbiory są przydatne, gdy chcesz przechowywać kolekcję przedmiotów i upewnić się, że nie ma duplikatów. W przeciwieństwie do list czy tablic, zbiory nie zachowują kolejności elementów i nie można uzyskać dostępu do elementów za pomocą indeksu. Obsługują szybkie testy przynależności, sumę, część wspólną, różnicę i inne operacje na zbiorach.

   Operacje na zbiorach:
   * `&` (Intersection - Część wspólna): Znajduje wspólne elementy pomiędzy zbiorami.
   * `|` (Union - Suma): Łączy wszystkie elementy z obu zbiorów (usuwa duplikaty).
   * `-` (Difference - Różnica): Znajduje elementy obecne w jednym zbiorze, ale nie w drugim.
   * `^` (Symmetric Difference - Różnica symetryczna): Znajduje elementy obecne w jednym lub drugim zbiorze, ale nie w obu jednocześnie.
   * `.issubset()`: Sprawdza, czy jeden zbiór jest podzbiorem drugiego.

1. Poniższy program usuwa zduplikowane adresy email. Uzupełnij i uruchom program.

   ```python
   emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
   unique_emails = set(...)  # Removes duplicates
   print(unique_emails)
   ```

1. Poniższy program identyfikuje studentów, którzy są nieobecni. Uzupełnij i uruchom program.

   ```python
   all_students = {"Alice", "John", "Sara", "Bob"}
   attended_students = {"Alice", "Bob"}

   absent_students = ... - ...  # Difference
   print(absent_students)
   ```

1. Poniższy program znajduje spam w otrzymanych wiadomościach email. Uzupełnij program, który wyświetla te otrzymane adresy email, które znajdują się na liście spamu.

   ```python
   emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
   spam_list = {"spam1@example.com", "spam2@example.com"}

   spam_emails = ... ... ...  # Intersection
   print("Spam emails:", spam_emails)
   ```

1. Dwie listy kontaktów pobrane z bazy danych zawierają adresy email. Napisz program, który łączy te listy i jednocześnie usuwa duplikaty.

   ```python
   contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
   contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

   merged_contacts = ... ... ...  # Union
   print("Merged contacts:", merged_contacts)
   ```

1. W systemie operacyjnym każdy użytkownik posiada pewne uprawnienia. Użytkownik chce wykonać pewną akcję, która wymaga określonych uprawnień. Napisz program, który sprawdza, czy użytkownik posiada wymagane uprawnienia.

   ```python
   required_permissions = {"read", "write", "execute"}
   user_permissions = {"read", "write"}

   has_permissions = ...   # subset
   print(has_permissions)  # Will return False because "execute" is missing.
   ```

## 3. Stos (Stack)

1. Stos to liniowa struktura danych, która działa zgodnie z zasadą Last In, First Out (LIFO - Ostatnie weszło, pierwsze wyszło). Oznacza to, że ostatni element dodany do stosu jest pierwszym, który zostanie usunięty. Pomyśl o stosie jak o stercie talerzy — ostatni talerz, który położysz na górze, jest pierwszym, który zdejmiesz.

   ![Stack Data Structure](https://media.geeksforgeeks.org/wp-content/uploads/20240606180325/What-is-Stack-(1).webp)

   W pliku `stack_example.py` możesz znaleźć prosty przykład, jak tworzyć i manipulować stosem. Przeanalizuj i uruchom program. Następnie zmodyfikuj program, w którym wykonasz następujące operacje:
   
      1. Połóż 2 na stosie
      1. Połóż 3 na stosie
      1. Połóż 7 na stosie
      1. Połóż 4 na stosie
      1. Połóż 1 na stosie
      1. Połóż 9 na stosie
      1. Połóż 8 na stosie
      1. Zsumuj dwie ostatnie liczby ze stosu i wypisz wynik
      1. Oblicz sumę pozostałych elementów stosu i wypisz wynik. Użyj pętli 'while'.
      
1. Program `back.py` symuluje przycisk Wstecz w przeglądarce internetowej (zapisywanie nazwy nowej strony internetowej lub wyświetlanie wcześniej odwiedzonej strony). Uzupełnij program.

1. Zdefiniuj funkcję, która zwraca true, jeśli nawiasy `()`, `{}`, `[]` są użyte poprawnie w podanym wyrażeniu. W przeciwnym razie funkcja zwraca false. Następnie napisz program, który sprawdza poprawność wyrażeń podanych poniżej.

   > Użyj stosu. Czytaj kolejne znaki wyrażenia. Pomiń wszystko oprócz nawiasów. Jeśli jest to nawias otwierający, połóż go na stosie. Jeśli jest to nawias zamykający, pobierz element ze stosu i porównaj, czy jest to pasujący nawias otwierający.

   ```python
   import queue

   expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
   expression2 = "[(2+3]/4)"                # brackets not correct
   expression3 = "(2-3*4+(5/6)"              # brackets not correct

   def brackets_ok(expression):
      ...
      ...
      ...
      return #True if brackets in expression are ok of False otherwise

   if brackets_ok(expression1):
      print(...)
   else
      ...

   if brackets_ok(expression2):
   ...
   ...
   ```

1. Napisz program, który konwertuje dowolną liczbę naturalną na liczbę binarną. Użyj stosu. Aby przekonwertować liczbę, dziel ją przez 2, za każdym razem biorąc resztę z dzielenia i odkładając resztę na stos. Powtarzaj dzielenie, aż liczba, którą dzielisz, wyniesie zero. Następnie zdejmij (pop) i wyświetl wszystkie wartości ze stosu. Przykładowy wynik dla liczby 18:

   |Division|Remainder|
   | :-: | :-: |
   |18 / 2 = 9|0|
   |9 / 2 = 4|1|
   |4 / 2 = 2|0|
   |2 / 2 = 1|0|
   |1  / 2 = 0|1|

   ```
   Natural number: 18
   Binary number: 10010 
   ```

## 4. Kolejka (Queue)

1. Kolejka to liniowa struktura danych, która działa zgodnie z zasadą First In, First Out (FIFO - Pierwsze weszło, pierwsze wyszło). Oznacza to, że pierwszy element dodany do kolejki będzie pierwszym, który zostanie usunięty. Kolejka działa podobnie jak kolejka w prawdziwym życiu, np. kolejka ludzi czekających na obsługę — osoba, która przyjdzie pierwsza, jest obsługiwana jako pierwsza.

   ![Queue Data Structure](https://media.geeksforgeeks.org/wp-content/uploads/20240606165428/Introduction-to-Queue-(2).webp)

   W pliku `queue_example.py` możesz znaleźć prosty przykład, jak tworzyć i manipulować kolejką. Przeanalizuj i uruchom program.

1. Używając kolejki, napisz program, który zarządza kolejką plików do wydrukowania.

   ```python
   import queue

   # creates a queue of files to print
   files_to_print = queue.Queue()

   while True:
      print('1. Add file to print')
      print('2. Print file')
      print('0. Quit')
      menu = input('Select an option: ')
      ...
      ...
      
      if menu == '1':
         file_name = input('Enter file name to print: ')
         # add new file to the end of the queue 
      ...

      elif ...:
         if # print queue not empty
            file_to_print = ...
            print(f'File {file_to_print} is currently being printed. Please wait!')
         else:
            print(...)

      elif menu == '0':
         break
   ```

## 5. Practice Makes Perfect

1. Przeczytaj rozdział w swoim podręczniku, który obejmuje tematy z tej sekcji.

1. Obejrzyj film o używaniu słowników w Pythonie:

   [https://youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-](https://youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-) 

1. Napisz program do tłumaczenia słów z angielskiego na polski. Użytkownik wpisuje słowo po angielsku z klawiatury. Program wyświetla tłumaczenie słowa lub informację, że tłumaczenie jest niedostępne.

   ```python
   translations = {
      'computer': 'komputer',
      'mouse': 'myszka',
      'keyboard': 'klawiatura',
      'printer': 'drukarka'
   }
   ...
   ...
   ...
   ```

1. Słownik zawiera nazwy przedmiotów wraz z liczbą godzin. Napisz program, który oblicza i wypisuje całkowitą liczbę godzin. Przykładowe wyniki:

   ```
   The total number of hours in the winter semester is …
   ```

   ```python
   winter_semester = {
      "math":60,
      "programming":30,
      "history":15
   }
   ```

1. Napisz program, który zlicza, ile razy każde słowo występuje w akapicie.

   > Wskazówka: Sprawdź w słowniku, czy kolejne słowo w nim występuje. Jeśli tak, zwiększ liczbę wystąpień słowa o 1. Możesz łatwo podzielić akapit na pojedyncze słowa używając metody `split()`. Poszukaj w Internecie, jak jej używać.

   ```python
   paragraph = "cat dog mouse cat rat cat mouse"
   ...
   ...
   ```

1. Program zawiera dwa słowniki z danymi osobowymi:

   ```python
   basic_data = {
      "name":"Barbara",
      "age":21
   }

   advanced_data = {
      "status":"student",
      "married":False,
      "interest":["reading","swimming"]
   }
   ```

   Napisz program, który tworzy słownik o nazwie `person` zawierający dane z dwóch pozostałych słowników (pięć par klucz-wartość). Wypisz zawartość słownika ‘person’.

1. Program zawiera dwie funkcje:
   1. `hotel_list(hotels)` która zwraca listę nazw hoteli, oddzielonych przecinkiem
   1. `avg_price(hotels)` która zwraca średnią cenę pokoju dla podanej listy hoteli, zaokrągloną do liczby całkowitej

   Napisz program, który oblicza i wyświetla średnią cenę za pokój w hotelach w Krakowie i Sopocie oraz wskazuje, w których miastach hotele są tańsze. Przykładowy wynik:

   ```
   Hotels in Krakow: …,…,…,…
   Average hotel price in Krakow: …
   Hotels in Sopot: …,…,…,…
   Average hotel price in Sopot: …
   Cheaper hotels in: …
   ```

   ```python
   hotels_in_Krakow = [
      {"name":"Sky","price":320.00},
      {"name":"Metropol","price":480.00},
      {"name":"New Port","price":420.00},
      {"name":"Aparthotel","price":390.00}
   ]

   hotels_in_Sopot = [
      {"name":"Focus","price":510.00},
      {"name":"Aqua","price":345.00},
      {"name":"La Boutique","price":390.00},
      {"name":"Marina","price":410.00}
   ]
   ```

1. Napisz program do obliczania całkowitego kosztu koszyka zakupowego przy użyciu cennika.

   ```python
   # Price list
   prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

   # Shopping cart with quantities
   cart = {'juice': 3, 'bread': 1, 'milk': 2}

   # Calculate total cost
   ...
   ...
   ```

1. Kamera drogowa rejestruje przejeżdżające pojazdy. Kamera zapisuje ich numery rejestracyjne w pliku `vehicle.txt`. Napisz program, który oblicza i wypisuje, ile zarejestrowanych samochodów pochodzi z każdego województwa Polski. Lista województw i odpowiadające im pierwsze litery numerów rejestracyjnych pojazdów znajdują się w pliku `province.csv`.

   > Wskazówka: użyj słownika zawierającego litery odpowiadające województwom oraz liczbę pojazdów, których pierwsze litery numeru rejestracyjnego pasują do liter województwa.

1. Obejrzyj film o tym, jak radzić sobie z plikami JSON w Pythonie:

   [https://youtu.be/pTT7HMqDnJw?feature=shared](https://youtu.be/pTT7HMqDnJw?feature=shared) 


1. Napisz program do rejestrowania głosowania. Wyniki głosowania są zapisywane w pliku `voting.json` o poniższej strukturze. Program pobiera imię osoby z klawiatury i zwiększa liczbę głosów dla tej osoby o 1. Jeśli jest to nowa osoba, jest dodawana do listy z liczbą głosów 1. Możesz uruchomić program wielokrotnie, aby dodać kolejne głosy do pliku json.

   ```python
   {
      person_name: number of votes,
      person_name: number of votes,
      ...
      ...
   }

   # Read the contents of the json file
   ...
   
   # Vote for a person
   person_name = input('Name of the person you are voting for:')
   ...
   
   # Save voting data to json file
   ...
   ```

1. Zdefiniuj funkcję, która przyjmuje ciąg znaków (string) jako wejście i używa stosu do jego odwrócenia. Następnie napisz program do odwracania dowolnego tekstu wprowadzonego z klawiatury.
   
   > Wskazówka: Połóż (push) każdy znak ciągu na stos, a następnie zdejmij (pop) znaki, aby utworzyć odwrócony ciąg.

1. Poszukaj w Internecie i zapoznaj się z Odwrotną Notacją Polską (RPN - Reverse Polish Notation). Następnie napisz program, który oblicza wyrażenia RPN. RPN można wygodnie obliczać przy użyciu struktury stosu. Użytkownik może wprowadzić z klawiatury dowolną liczbę, operator (+ - * / ) lub znak równości (=).

   1. Jeśli wprowadzona wartość jest liczbą, połóż liczbę na stos
   1. Jeśli wprowadzona wartość jest operatorem, zdejmij dwa elementy z góry stosu, wykonaj obliczenie i połóż wynik operacji na stos.
   1. Jeśli wprowadzona wartość jest znakiem równości, zdejmij ostateczny wynik ze stosu i wyświetl wynik obliczenia.

   Następnie, używając programu, oblicz wartość wyrażeń RPN:

   |Expression|RPN (Reverse Polish Notation)|
   | :- | :- |
   |2 + 3 =|2 3 + =|
   |2 * (4 + 1)|2 4 1 + * =|
   |(2 + 3) * ( 4 + 5) =|2 3 + 4 5 + * =|
   |8 / (3 + 1) * (3 - 2 + 4) = |8 3 1 + / 3 2 – 4 + * =|

1. Napisz program obsługujący klientów w urzędzie. Użyj kolejki. Każdy nowy klient otrzymuje bilet z automatycznie przydzielonym kolejnym numerem i jest dodawany na koniec kolejki. Następny klient do obsługi jest pobierany z początku kolejki.

1. JSON (JavaScript Object Notation) to lekki format wymiany danych, który jest łatwy do czytania i pisania dla ludzi oraz łatwy do parsowania i generowania dla maszyn. Jest często używany do przesyłania danych między serwerem a aplikacją internetową, a także do przechowywania ustrukturyzowanych danych.

   Zwróć uwagę na kluczowe cechy JSON:

   * Czytelność: JSON jest oparty na tekście, więc może być łatwo odczytywany przez ludzi.
   * Prostota: Jest zbudowany na parach klucz-wartość.
   * Niezależność od języka: Chociaż wywodzi się z JavaScript, JSON jest obsługiwany przez wiele języków programowania, takich jak Python, Java, PHP, C# i inne.

1. Plik `computer.json` zawiera przykładowe dane komputera. Otwórz plik json w edytorze i przejrzyj jego zawartość. Zauważ, że plik zawiera pojedynczy słownik danych.

   Następnie napisz program, który wypisuje informacje o komputerze.

   ```python
   import json

   # Open the JSON file in read mode
   with open('computer.json', 'r', encoding='utf-8') as file:
      # Load the data from the JSON file into a variable
      data = json.load(file)

   # Print the JSON data
   for ... , ... in data.items():
      print(...,':',value)
   ```

1. Plik `cities.json` zawiera dane o wybranych miastach w Polsce. Otwórz plik json w edytorze i przejrzyj jego zawartość. Zauważ, że plik zawiera tablicę słowników.

   Następnie napisz program, który wypisuje informacje o miastach.

   > Uwaga: użycie parametru `encoding='utf-8'` podczas otwierania pliku jest konieczne, ponieważ plik json zawiera również polskie znaki w nazwach miast, które muszą być poprawnie przetworzone. Pamiętaj, aby zawsze używać tego parametru przy otwieraniu plików zawierających znaki inne niż te z alfabetu łacińskiego.

   ```python
   import json

   # Open the JSON file in read mode
   with open('cities.json', 'r', encoding='utf-8') as file:
      # Load the data from the JSON file into a variable
      data = json.load(file)

   # Print the JSON data
   for city in data:
      for ... , ... in city. ...():
         print(key,':',value)
      print()
   ```

1. Plik `dogs.json` zawiera dane o psach. Napisz program, który wypisuje informacje o psach młodszych niż 5 lat.

1. System informatyczny hotelu zawiera listę zarezerwowanych pokoi. Dane znajdują się w pliku `reservations.json`. Napisz program, który wypisuje podsumowanie informacji, jak podano poniżej. Podziel swój program na mniejsze części, definiując funkcje.

   * liczba pokoi
   * liczba opłaconych rezerwacji
   * liczba nieopłaconych rezerwacji
   * całkowita wartość opłaconych rezerwacji
   * całkowita wartość nieopłaconych rezerwacji

1. Poniższy program zapisuje dane do pliku json. Przeanalizuj ten program. Następnie uruchom program i zobacz, czy plik json został utworzony. Wyświetl utworzony plik json w edytorze.

   ```python
   import json

   data = {
      "patient_record": {
         "patient_id": "P001234",
         "first_name": "John",
         "last_name": "Doe",
         "date_of_birth": "1985-05-15",
         "gender": "Male",
         "contact_info": {
               "phone_number": "+1-555-123-4567",
               "email": "johndoe@example.com",
               "address": {
                  "street": "123 Main St",
                  "city": "New York",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA"
               }
         },
         "medical_history": {
               "allergies": ["Penicillin", "Peanuts"],
               "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
               "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
               "surgeries": [
                  {
                     "surgery_type": "Appendectomy",
                     "date": "2015-08-20"
                  }
               ]
         }
      }
   }

   # Specify the file path and name
   file_name = "patient.json"

   # Open the file in write mode and use json.dump() to write the data to the file
   with open(file_name, 'w') as file:
      json.dump(data, file, indent=4)

   print("Data has been written to", file_name)
   ```

1. Stwórz słownik, który opisuje Twoją ulubioną książkę lub film za pomocą co najmniej pięciu par klucz-wartość. Następnie stwórz program, który zapisuje dane słownika do pliku `favourite.json`.

1. Napisz program, który pobiera z klawiatury dane o zakupionym produkcie:

   * nazwa
   * cena (liczba rzeczywista z dwoma miejscami po przecinku)
   * czy zapłacono (tak/nie)

   Następnie program zapisuje dane produktu w pliku `product.json`. Zwróć uwagę na poprawne typy danych opisujące produkt (string, float, bool).

   ```python
   product = {}
   
   # read product data from keyboard
   ...

   # save product data to json file
   ...
   ```

1. Strona internetowa [https://api.nbp.pl/en.html](https://api.nbp.pl/en.html) zawiera dane o kursach walut publikowane przez Narodowy Bank Polski. Serwis udostępnia dane zarówno w formacie json, jak i xml. Wyświetl ostatnie dziesięć kursów Euro w formacie json w przeglądarce internetowej. Następnie zapisz dane do pliku `euro.json`. Na koniec napisz program, który wyświetla dane z pliku `euro.json` w następującym formacie:

   ```
   Date             Buying Rate      Selling Rate
   ============================================
   2019-10-25       3.8150           3.9820
   ...
   ...
   ...
   ```

   > Wskazówka: Jeśli interesują Cię zagadnienia API i Rest API, przeczytaj poniższy artykuł:
   > [https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)