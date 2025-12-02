<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# ARRAYS

## 1. One dimensional arrays

1. Watch the video on using lists:

   <https://youtu.be/ohCDWZgNIU0?feature=shared> 

1. Familiarise yourself with creating and manipulating Lists:

   <https://www.w3schools.com/python/python_lists.asp> 

1. Many programming languages ​​provide both arrays and lists to store and manage collections of data. Despite their many similarities, they have key differences in terms of functionality, flexibility, and performance.

   The main differences between an array and a list are presented in the table below. 

   | FEATURE           | LISTS                         | ARRAYS                         |
   |-------------------|-------------------------------|-------------------------------|
   | Data Types        | Mixed                        | Single, fixed data type       |
   | Flexibility       | Highly flexible              | Less flexible                |
   | Performance       | Slower for numerical ops     | Faster for numerical ops      |
   | Memory Efficiency | Less efficient               | More efficient               |
   | Built-in Support  | Yes                          | Needs `array` or `numpy`     |

   > **Notice that in subsequent tasks, a list will be used in place of an array for basic applications.**

1. An array contains values: 2, 3, 7, 5, 4. Write a program that prints:
   1. the array
   1. number of elements
   1. first value
   1. second value
   1. last value
   1. last but one value (do not use negative index values)
   1. sum of the first and last value
   1. middle value
   1. all array values separated by a single space (use a loop statement)

   ```python
   ###
   # Prints some array elements
   #
   arr = [2, 3, 7, 5, 4]

   print(arr)
   print('Number of elements', len(arr))
   print('First value', arr[...])
   print('Second value', arr[...])
   ...
   ...
   ```

   > Tip: to read the last value of an array use array[len(array)-1] or array[-1]

1. An array contains values: 1, 2, 3, 4, 5. Write a program that modifies the array values. Print the array after each change.

   1. subtract one from the first element of the array
   1. increase the last array element by 4
   1. multiple the middle array element by 2

   Sample result:

   ```python
   Array: [1,2,3,4,5]
   Array: [0,2,3,4,5]
   Array: [0,2,3,4,9]
   Array: [0,2,6,4,9]
   ```

1. Write a program that prints the name of the day of the week for a given day number. Then, using the defined function, print the name of the day of the week for the following day numbers: 1, 4, 7.

   ```python
   ###
   # Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
   #
   def weekday(n):
         weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
      return weekdays[...]

   ...
   ...   
   ```

1. Write a program that prints a shopping list, each product on a separate line.

   ```python
   ###
   # Prints shopping list
   #
   shopping_list = [
      "milk", "bread", "eggs", "butter", "cheese",
      "tomatoes", "potatoes", "carrots", "onions", "garlic"
   ]
   for item in shopping_list:
      print(...)
   ```

1. Write a program that prints a popular computer games, each game name on a separate line. Use the while statement. Additionally, number the list (print the next number before each list item) and sort the list alphabetically (use one of a Python built-in functions for sorting)

   ```python
   computer_games = [
      "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
      "League of Legends", "Valorant", "Grand Theft Auto V", 
      "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
   ]
   ```

1. The list contains vehicle registration numbers in Poland. Cars from Krakow have numbers starting with the letters 'KR' or 'KK'. Write a program that prints car registration numbers from Krakow. Number the list printed.

   ```python
   ###
   # Prints vehicle registration numbers from Krakow
   #
   polish_license_plates = [
      'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
      'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
      'KK54985', 'LU4864U'
   ]
   counter = 1
   for car_number in polish_license_plates:
      if car_number ...:
         print(counter, ...)
         counter += 1
   ```

1. The array contains the student's test results. A value of True indicates that the student answered the question correctly, while a value of False indicates an incorrect answer. Write a program that prints information about the test results:

   * Number of questions:
   * Number of correct answers:
   * Number of incorrect answers:
   * Percentage of correct answers:

   ```python
   ###
   # Prints test statistics
   #
   test_results = [
      False, True, False, True, True,
      True, True, False, True, True,
      False, True, True, True, False
   ]

   # calculates the number of test questions
   question number = len(...)

   # calculates the number of correct answers
   correct_answers = 0
   for answer in test_results:
      if ...:
         correct_answer = ...
   
   # calculates the number of incorrect answers
   ...

   # calculates the percentage of correct answers
   ...

   print('TEST STATISTICS')
   print('===============')
   print('Number of questions:', ...)
   print('Number of correct answers:', ...)
   ...
   ...
   ```

1. The weather station measures temperature once a day. The measurement results for each day in March are stored in an array. Write a program that analyzes the temperature based on the observations from March and prints the following report:

   ```
   TEMPERATURE REPORT
   Month: March
   Number of measurements:
   Average temperature in the month:
   Minimum temperature:
   Maximum temperature:
   Number of days with negative temperature:
   ```

   ```python
   ###
   # The weather station report
   #
   temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
   ]

   # number of mesaurements
   mesaurements = len(...)

   # calculates average temperature
   temp_total = 0
   for temp in temperatures:
      temp_total = ...
   avg_temp = temp_total ...

   # calculates min and max temperatures
   min_temp = min(...)
   max_temp = ...

   # calculates number of days with negative temp
   negative_temp = 0
   i = 0
   while i < ...:
      if temperatures[...] < ...:
         negative_temp ...
      i = ...

   # prints out month report
   ...
   ...
   ...
   ```

1. Monthly expenses and their corresponding expense categories are included in the arrays below. Write a program that calculates which expense category was the most expensive.

   ```python
   categories = ["Food", "Transport", "Rent","Entertainment"]
   expenses = [500, 150, 1000, 200]
   ```

1. The store has 10 types of goods in stock. The prices of the goods and the number of pieces of goods are given below. Write a program that calculates the value of all the goods available in the store.

   ```python
   # Prices of 10 products in the computer store (in currency units)
   product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

   # Number of units available for each product
   product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]
   ```

1. Very often, there is a need to organize the data contained in the array. Organized data allows for faster retrieval, analysis, and presentation of information. There are many sorting algorithms that organize data in the array. One of the simplest is bubble sort, which organizes data in ascending or descending order.

   Watch the video on bubble sort algorithm:

   <https://youtu.be/hahrx5WUeNI?feature=shared>

   Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list or array, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until no more swaps are needed, which means the list is sorted.

   Here is the bubble sort algorithm expressed in pseudocode, a universal notation that is independent of the programming language:

   ```python
   procedure bubbleSort(arr):
      n = length(arr)
      for i = 0 to n-1:
         for j = 0 to n-i-2:
            if arr[j] > arr[j+1]:
                  swap arr[j] and arr[j+1]
      return arr
   ```

1. Define a function that sorts an array of numbers using the bubble sort algorithm. Use the information in the pseudocode provided earlier. Then, write a program that sorts the following collections of data:

   ```python
   car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
   bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
   ```

   ```python
   ###
   # Bubble sort
   #
   def bubble_sort(arr):

      for i in n:
         for ...:
            if ...:

      return arr

   car_fuel_consumption = ...
   print(car_fuel_consumption)
   sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
   print(sorted_car_fuel_consumption)

   bank_transactions = ...
   ...
   ...
   ...
   ```

1. Programming languages ​​often provide built-in functions for sorting collections of data. Data can be sorted in ascending or descending order. Look at the list of built-in functions below and find the one that allows you to sort collections of data.

   <https://docs.python.org/3/library/functions.html>

   Then write a program that uses the built-in function to sort the data below:

   ```python
   # Sort the data from lowest to highest value
   distances_traveled = [120, 150, 180, 90, 200, 175, 160]
   # Sort the data in descending order, from highest to lowest value
   daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
   # Sort the data in ascending order
   file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
      "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
   ```

## 2. Two dimensional arrays

1. Watch the video on using two dimensional (2D) lists in Python:

   <https://youtu.be/z49F119uv6g> 

1. Tic-Tac-Toe is a simple yet fun game for two players. You play on a grid of nine squares arranged in three rows and three columns.

   The array below shows a Tic-Tac-Toe board. Write a program that prints a board on the screen.

   ```python
   # 3x3 Tic-Tac-Toe board
   tic_tac_toe_board = [
      ['X', 'O', 'X'],
      [' ', 'X', 'O'],
      ['O', ' ', 'X']
   ]

   for row in tic_tac_toe_board:
      for ... in ...:
         print(..., end=" ")
      print()
   ```

   > Hint: end=" " means that the cursor is not moved to the next line; a space is printed instead 

1. The data below represents monthly expenses divided into categories and weeks. Write a program that calculates and prints:

   * total expenses for each category
   * total expenses for each week
   * total expenses for a month

   ```python
   # Weekly expenses for different categories
   # [Food, Transport, Utilities]
   monthly_expenses = [
      [200, 50, 100],  # Week 1
      [180, 60, 110],  # Week 2
      [220, 55, 105],  # Week 3
      [210, 65, 95]    # Week 4
   ]

   # Calculates expenses
   # Use loop statements
   ...
   ...
   ...

   # Print expenses
   print('MONTHLY EXPENSES')
   print('----------------')
   print('Food:',...)
   print('Transport:',...)
   print('Utilities:',...)
   print('Week 1:',...)
   print('Week 2:',...)
   print('Week 3:',...)
   print('Week 4:',...)
   print('---------------')
   print('TOTAL:',...)
   ```

1. The data below contains weekly meal plan. Write a program that prints the weekly meal plan along with the day name as in the example below.

   ```
   WEEKLY MEAL PLAN
   (Breakfast, Lunch, Dinner)
   ==========================
   Monday: Oatmeal, Grilled Checken Salad, Spaghetti
   Tuesday: ...
   Wednesday: ...
   ...
   ...
   ...
   ...
   ```


   ```python
   # Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
   meal_plan = [
      ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
      ["Pancakes", "Sandwich", "Steak"],
      ["Smoothie", "Chicken Wrap", "Salmon"],
      ["Eggs", "Pasta", "Soup"],
      ["Toast", "Burrito", "Pizza"],
      ["Cereal", "Salad", "Fish Tacos"],
      ["Bagel", "Rice and Beans", "Stir-fry"]
   ]

   # Returns a week day name
   def weekday(n):
      weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
      return weekdays[n-1]

   # Returns a string with day meal names
   # separated by comma
   def day_meal_plan(meal_plan, day_number):
      ...
      return ...

   # Prints weekly meal plan
   ...
   ...
   ...
   ```

1. The data below represents a cinema's seating arrangement. Write a program that:

   * calculates how many seats are available
   * calculates how many seats are booked
   * informs what the status of a seat is in a given row and given place (available or booked)

   ```python
   # 5x5 cinema seating
   # A = Available, B = Booked
   cinema_seats = [
      ['A', 'A', 'B', 'A', 'A'],
      ['A', 'B', 'B', 'A', 'A'],
      ['A', 'A', 'A', 'A', 'B'],
      ['B', 'A', 'A', 'A', 'A'],
      ['A', 'B', 'A', 'A', 'A']
   ]

   def seats_total(seats):
      ...
      return ...

   def seats_available(seats):
      ...
      ...
      return ...

   def seats_booked(seats):
      ...
      ...
      return ...

   def seat_status(seats, row, place):
      ...
      ...
      return ...

   print('CINEMA INFORMATION TABLE')
   print('Total seats:',...)
   print('Seats available:',...)
   print('Seats booked:', ...)
   print('Seat in row 1, place 1:', ...)
   print('Seat in row 5, place 5:', ...)
   print('Seat in row 3, place 5:', ...)
   ```



1. The following array represents a square matrix and contains values:

   ```python
   [
      [0,0,0],
      [0,0,0],
      [0,0,0]
   ]
   ```

   Create a program that replaces the values of the main diagonal with 1. Use a loop statement. Print the modified array. Sample result:

   ```
   1 0 0
   0 1 0
   0 0 1
   ```

## 3. Practice Makes Perfect

0. Try to create the following arrays. Then, print the created array content.

   ```python
   arr1 = [3,7,1,0,4]
   arr2 = [[2,3],[7,1],[0,4]]
   arr3 = [7 for i in range(5)]
   arr4 = [i for i in range(1,10)]
   arr5 = [i*2 for i in range(1,10)]
   arr6 = [random.randint(1,20) for i in range(10)]
   arr7 = [[] for i in range(5)]
   arr8 = [[1 for i in range(2)] for j in range(4)]
   arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
   an array with values: 4,0,3
   15-element array filled with zeros
   an array with integer values in the range of <1,30>
   20-element array filled with 0 or 1 randomly
   two dimensional array with five rows and two columns filled with False
   ```
 > **Hint: Don't forget to import the random module before using random.randint**

1. Tablica zawiera liczby całkowite: 34,7,19,4,21,8. Stwórz program, który oblicza i wypisuje liczbę parzystych wartości w tablicy. Użyj instrukcji pętli ‘while’.

1. Tablica zawiera liczby naturalne: 15, 8, 31, 47, 2, 19. Stwórz program, który wypisuje zawartość tablicy w odwrotnej kolejności. Użyj dowolnej pętli. Przykładowy wynik:

   ```python
   existed array: 15 8 31 47 2 19 
   reverse array: 19 2 47 31 8 15
   ```

1. Stwórz program, który oblicza drugą potęgę każdego elementu tablicy. Przykładowy wynik:

   ```python
   Array: 8 2 5 1 9
   2nd power: 64 4 25 1 81
   ```

1. Tablica zawiera liczby: -15, 8, -31, 47, -2, 19. Stwórz program, który znajduje i wypisuje największą oraz najmniejszą liczbę. Nie używaj dostępnych (wbudowanych) funkcji.

1. Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Stwórz program, który oblicza i wypisuje tablicę oraz średnią arytmetyczną wartości tablicy. Użyj instrukcji pętli „for”.

1. Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Stwórz program, który oblicza i wypisuje tablicę oraz średnią arytmetyczną wartości tablicy. Użyj instrukcji pętli „while”.

1. Tablica zawiera listę polskich imion:

   ```
   Genowefa, Onufry, Celestyna, Alojzy, Pankracy
   ```

   Stwórz program, który wypisuje najdłuższe imię (składające się z największej liczby znaków). Przykładowy wynik:

   ```
   Names: Genowefa Onufry Celestyna Alojzy Pankracy
   Longest name: Celestyna
   ```

1. Tablica zawiera liczby całkowite: 2, 6, 4, 9, 7. Stwórz program, który wypisuje wartości tablicy graficznie, jak poniżej. Zdefiniuj funkcję star(n), która zwraca zadaną liczbę gwiazdek jako ciąg znaków (string). Użyj zdefiniowanej funkcji w programie.

   ```python
   2: **
   6: ******
   4: ****
   9: *********
   7: *******
   ```

1. Zdefiniuj funkcję compare(array1, array2), która zwraca True, jeśli obie tablice są takie same, lub False w przeciwnym wypadku. Dwie tablice są takie same, jeśli mają tę samą liczbę elementów, a wartości elementów w komórkach o tym samym indeksie są równe. Następnie stwórz program i spróbuj porównać następujące tablice: 

   ```python
   1. ["water","book","sky"]   ["water","book","sky"]
   1. [True,False]   [True,False,True]
   1. [5,3,1]   [5,3,1]
   1. [3,2,1]   [3,2]
   ```

   Wypisz obie tablice oraz wynik porównania. Przykładowy wynik:

   ```python
   Array1: water book sky
   Array2: water book sky
   Comparison: arrays are the same
   ```

1. Dwie tablice zawierają następujące liczby całkowite [4,36,12,28,9,44,5] oraz [5,1,36]. Stwórz program, który wypisuje liczby z pierwszej tablicy, które nie występują w drugiej tablicy.

1. Stwórz program, który sortuje elementy tablicy zawierającej liczby całkowite. Zastosuj algorytm sortowania bąbelkowego (Bubble Sort). Zdefiniuj funkcję bubblesort(array), która zwraca posortowaną tablicę. Spróbuj posortować i wypisać dowolne trzy tablice.

1. Stwórz program, który wypisuje wszystkie unikalne elementy w tablicy. Przykładowy wynik:

   ```python
   Array: 2 3 2 5 8 1 9 8
   Unique elements: 3 5 1 9
   ```

1. Zdefiniuj funkcję occurs(number, array), która zwraca True, jeśli podana liczba znajduje się w tablicy. Następnie stwórz program, który sprawdza, czy liczba wprowadzona z klawiatury jest obecna w tablicy [15, 38, 7, 23, 14]. Przykładowy wynik:

   ```python   
   Number: 23
   Array: 15 38 7 23 14
   Result: number 23 appears in the array
   ```

1. Krotka (tuple) w Pythonie to niezmienna, uporządkowana kolekcja elementów. Krotki są podobne do list, ale w przeciwieństwie do list, po utworzeniu krotki jej elementy nie mogą być modyfikowane, dodawane ani usuwane.

   Napisz program, który tworzy krotkę zawierającą pojedyncze słowo ‘computation’. Zapisz krotkę w zmiennej. Następnie wypisz typ zmiennej.

1. Napisz program, który wypisuje krotkę (10,20,30,40,50) w odwrotnej kolejności. Przykładowy wynik:

   ```python
   Tuple: 10,20,30,40,50
   Reverse order: 50,40,30,20,10
   ```

1. Napisz program, który dla krotki ("Seven", [10, 20, 30], (5, 15, 25)) wypisuje wartości:
   1. “Seven”
   1. 30

1. Napisz program, który zlicza liczbę wystąpień dowolnej wartości z krotki. Przykładowy wynik:

   ```python
   Tuple: 50,20,40,50,30,50
   Value: 50
   Number of occurrences: 3
   ```

1. Stwórz moduł MyArrays zawierający funkcje do operacji na tablicy liczb:

   1. Funkcję, która zwraca drugi co do wielkości element w tablicy
   1. Funkcję, która zwraca różnicę między największą a najmniejszą wartością w tablicy
   1. Funkcję, która zwraca medianę liczb w tablicy. 
   
   Nie używaj wbudowanych funkcji. Mediana to środkowa wartość w uporządkowanym ciągu liczb:

      <https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png> 

   1. Funkcję, która zwraca dwuelementową tablicę zawierającą najmniejszą i największą wartość w tablicy
   
   1. Funkcję, która zwraca elementy tablicy jako ciąg znaków (string), oddzielone znakiem minus

   Następnie napisz program, który dla ciągu liczb:

   ```python
   7,3,8,5,2
   ```

   oblicza i wypisuje wyniki. Przykładowy wynik:

   ```
   Numbers: 7,3,8,5,2
   Second largest number: 7 
   Median: 5
   Smallest and largest number: 2,8
   Numbers as a string: 7-3-8-5-2
   ```

1. Napisz program, który dla danej tablicy liczb rzeczywistych wypisuje liczbę elementów, które są większe od podanej wartości wprowadzonej z klawiatury.

1. Napisz program, aby rozdzielić liczby parzyste i nieparzyste z danej tablicy liczb całkowitych. Umieść wszystkie liczby parzyste na początku, a następnie liczby nieparzyste.

   Przykładowy wynik:

   ```python
   arr = [7,9,2,4,5,6]
   ...
   ...
   arr = [2,4,6,7,9,5]
   ```

1. Napisz program, który sprawdza, czy pierwsza tablica jest podzbiorem drugiej (czy wszystkie elementy pierwszej tablicy występują w drugiej tablicy).

1. Zdefiniuj funkcję rand_elem(array), która zwraca losowo wybrany element tablicy. Używając tej funkcji, wypisz kilka losowo wybranych elementów tablicy.

1. Zmienna zawiera tekst:

   An apple a day keeps the doctor away

   Stwórz moduł MyText, zawierający:

   1. Funkcję, która zwraca liczbę słów w tekście
   1. Funkcję, która zwraca uporządkowaną tablicę słów, od najdłuższego do najkrótszego
   1. Funkcję, która zwraca tablicę słów uporządkowaną alfabetycznie

   Następnie napisz program, wywołaj funkcje i wypisz wyniki. Przykładowy wynik:

   ```
   Text: An apple a day keeps the doctor away
   Number of words: 8
   Words from the longest: doctor,apple,…
   Words ordered alphabetically: a,An,apple,away,…
   ```

1. Zapoznaj się z metodami wizualizacji danych:

   <https://www.w3schools.com/python/matplotlib_intro.asp> 

   Następnie, używając ‘matplotlib’, narysuj na wykresie linię od pozycji (1, 3) do pozycji (8, 10). 

   > Wskazówka: aby używać 'matplotlib' w swoich programach, musisz najpierw zainstalować moduł używając polecenia 'pip' (menedżer pakietów python).

   <https://pythonguides.com/how-to-install-matplotlib-python/>

   ```python
   import matplotlib.pyplot as plt
   xpoints = [1, 8]
   ypoints = [3, 10]
   plt.plot(xpoints, ypoints)
   plt.show()
   ```
   

1. Napisz program, który rysuje wykres funkcji f(x)=x<sup>2</sup>-3. Przykładowy wynik:

   ```python
   import matplotlib.pyplot as plt

   x = []
   y = []

   # create x values
   for n in range(-100,101):
      x = x + [n]

   # create y values
   for n in x:
      y = ...

   # print chart
   ...
   ...
   ```

1. Napisz program, który rysuje funkcję y = sin(x) dla wartości kąta w zakresie 0-360 stopni.

1. Dwuwymiarowa tablica o rozmiarze 2 na 4 zawiera liczby całkowite. Stwórz program, który wypisuje wartości tablicy w wierszach i kolumnach.

1. Dwuwymiarowa tablica zawiera następujące liczby:

   ```
   7 3 7 9 0
   2 9 0 1 5
   3 8 6 4 7
   8 7 1 1 5
   ```

   Stwórz program, który oblicza sumę wartości w ostatniej kolumnie.

1. Funkcja create_2d_arr(x,y) tworzy i zwraca dwuwymiarową tablicę o wartościach 0. Stwórz program i tę funkcję. Następnie stwórz dwuwymiarową tablicę o wymiarach 3 na 5. Wypisz stworzoną tablicę.

1. Tablica zawiera wartości:

   ```
   [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
   ```
   
   Stwórz program, który modyfikuje wartości tablicy, aby stworzyć tabliczkę mnożenia jak poniżej. Użyj instrukcji pętli. Wypisz tablicę.

   ```
   1  2  3  4  5
   2  4  6  8 10
   3  6  9 12 15
   4  8 12 16 20
   5 10 15 20 25
   ```
   
1. Tablica zawiera liczby całkowite:

   ```
   [[-38, 19], [5,40],[-7,11],[29,16]]
   ```

   Stwórz program, który znajduje najmniejszą i największą wartość w tablicy oraz w którym wierszu i kolumnie się one znajdują. 

1. Dwuwymiarowa tablica o rozmiarze 3 na 5 zawiera liczby całkowite. Stwórz program, który zamienia miejscami pierwszy i ostatni wiersz. Wypisz wartości tablicy w wierszach i kolumnach przed i po zmianach.

1. Dwuwymiarowa tablica o rozmiarze 3 na 5 zawiera liczby całkowite. Stwórz program, który zamienia miejscami pierwszą i ostatnią kolumnę. Wypisz wartości tablicy w wierszach i kolumnach przed i po zmianach.

1. W matematyce macierz to prostokątna tablica liczb, symboli lub wyrażeń, ułożonych w wierszach i kolumnach, np.:

   ```
   -7  12 38
   41 -19 11
   ```

   Stwórz funkcję identity_matrix(n), która zwraca macierz jednostkową (tablicę 2D) o rozmiarze n.
   
   <https://en.wikipedia.org/wiki/Identity_matrix>
   
   Następnie stwórz funkcję, która wypisuje tablicę 2D w wierszach i kolumnach. Na koniec stwórz program, który wypisuje trzy macierze jednostkowe o wymiarach 3, 5 i 8. Przykładowy wynik:

   ```
   1 0 0 0 0
   0 1 0 0 0
   0 0 1 0 0
   0 0 0 1 0
   0 0 0 0 1
   ```

1. Stwórz funkcję transpose_matrix(m), która zwraca transponowaną macierz m:

   <https://en.wikipedia.org/wiki/Transpose> 

   Następnie stwórz program, który wypisuje transponowane macierze, w wierszach i kolumnach, dla następujących macierzy.
   1. 1 2 3\
      4 5 6\
      7 8 9
   1. 1 2 3 4 5\
      6 7 8 9 0
   1. 5 6 7 8
1. Stwórz funkcję, która konwertuje tablicę dwuwymiarową (2D) na jednowymiarową (1D). Następnie stwórz program, który wypisuje tablicę 1D dla następujących tablic 2D.

   1. 2 3\
      1 5 
   1. 5 0 3 7 5\
      9 0 9 1 2
   1. 2 1\
      3 5\
      7 4\
      2 6
