def f(fun, arr):
    filtered = list(filter(fun, arr))
    return min(filtered) + max(filtered)