# Napisz program, aby rozdzielić liczby parzyste i nieparzyste z danej tablicy liczb całkowitych. Umieść wszystkie liczby parzyste na początku, a następnie liczby nieparzyste. Przykładowy wynik: 
# arr = [7,9,2,4,5,6] 
# ... ... 
# arr = [2,4,6,7,9,5]


arr = [7, 9, 2, 4, 5, 6]
even = []
odd = []

for x in arr:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

arr = even + odd
print(arr)