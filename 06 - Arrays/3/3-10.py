# Dwie tablice zawierają następujące liczby całkowite [4,36,12,28,9,44,5] oraz [5,1,36]. Stwórz program, który wypisuje liczby z pierwszej tablicy, które nie występują w drugiej tablicy.

arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

wynik = [x for x in arr1 if x not in arr2]
print(wynik)