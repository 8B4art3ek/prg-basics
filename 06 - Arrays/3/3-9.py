# Zdefiniuj funkcję compare(array1, array2), która zwraca True, jeśli obie tablice są takie same, lub False w przeciwnym wypadku. Dwie tablice są takie same, jeśli mają tę samą liczbę elementów, a wartości elementów w komórkach o tym samym indeksie są równe. Następnie stwórz program i spróbuj porównać następujące tablice:

# 1. ["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1]   [5,3,1]
# 1. [3,2,1]   [3,2]
# Wypisz obie tablice oraz wynik porównania. 

# Przykładowy wynik:
# Array1: water book sky
# Array2: water book sky
# Comparison: arrays are the same

def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

arrays_to_test = [
    (["water","book","sky"], ["water","book","sky"]),
    ([True,False], [True,False,True]),
    ([5,3,1], [5,3,1]),
    ([3,2,1], [3,2])
]

for arr1, arr2 in arrays_to_test:
    print("Array1:", *arr1)
    print("Array2:", *arr2)
    if compare(arr1, arr2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")