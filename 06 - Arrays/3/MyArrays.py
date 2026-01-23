def second_largest(arr):
    if len(arr) < 2:
        return None
    unique = list(set(arr))
    unique.sort()
    return unique[-2]

def max_min_difference(arr):
    if len(arr) == 0:
        return None
    return max(arr) - min(arr)

def median(arr):
    if len(arr) == 0:
        return None
    temp = sorted(arr)
    n = len(temp)
    mid = n // 2

    if n % 2 == 1:
        return temp[mid]
    else:
        return (temp[mid -1] + temp[mid]) / 2 
    
def min_and_max(arr):
    if len(arr) == 0:
        return None
    return [min(arr), max(arr)]

def array_to_string(arr):
    return "-".join(str(x) for x in arr)