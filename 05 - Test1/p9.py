def f(sizes):
    counter_S = 0
    counter_M = 0
    counter_L = 0

    lista = sizes.split(",")
    for item in lista:
        match item:
            case "S":
                counter_S += 1
            case "M":
                counter_M += 1
            case "L":
                counter_L += 1

    if counter_S == 0:
        return "S"
    if counter_M == 0:
        return "M"
    if counter_L == 0:
        return "L"
    
    if counter_S == counter_M and counter_S < counter_L and counter_M < counter_L:
        return "S"
    if counter_S == counter_L and counter_S < counter_M and counter_L < counter_M:
        return "S"
    if counter_M == counter_L and counter_M < counter_S and counter_L < counter_S:
        return "M"
    
    if counter_S < counter_M and counter_S < counter_L:
        return "S"
    if counter_M < counter_S and counter_M < counter_L:
        return "M"
    if counter_L < counter_S and counter_L < counter_M:
        return "L"

    
if __name__ == "__main__":
    print(f("L,S,L,M,L,S,S,L"))
    print(f("M,L,L,L,M"))
    print(f("M,L,M,L,S,S,S"))