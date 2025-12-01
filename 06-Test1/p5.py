def f(t):
    time = t.split(":")
    nowy = ""
    for ti in time:
        nowy += ti
    
    for char in nowy:
        if char.isupper() or char.islower():
            return False
        
    if len(nowy) > 6:
        return False
    
    if int(nowy[0:2]) > 59  or int(nowy[2:4]) > 59 or int(nowy[4:6]) > 59:
        return False

    return True

if __name__ == "__main__":
    print(f("17:38:25"))
    print(f("11:61:43"))
    print(f("23:05:19:46"))
    print(f("23:AB:10"))
