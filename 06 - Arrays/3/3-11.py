# Stwórz program, który sortuje elementy tablicy zawierającej liczby całkowite. Zastosuj algorytm sortowania bąbelkowego (Bubble Sort). Zdefiniuj funkcję bubblesort(array), która zwraca posortowaną tablicę. Spróbuj posortować i wypisać dowolne trzy tablice.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
print(bubble_sort(arr1))
print(bubble_sort(arr2))