# Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list or array, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until no more swaps are needed, which means the list is sorted.

# Here is the bubble sort algorithm expressed in pseudocode, a universal notation that is independent of the programming language:
"""
procedure bubbleSort(arr):
    n = length(arr)
    for i = 0 to n-1:
        for j = 0 to n-i-2:    # lub do n-i-1, zależnie od indeksowania
            if arr[j] > arr[j+1]:
                swap arr[j] and arr[j+1]
    return arr
"""