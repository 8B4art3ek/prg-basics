def f(thing_to_wash, extra_rinse, extra_spin):
    time = 0
    match thing_to_wash:
        case "J":
            time += 40
        case "U":
            time += 70
        case "S":
            time += 20

    if extra_rinse:
        time += 15
    if extra_spin:
        time += 9
    
    return time

if __name__ == "__main__":
    print(f("U", False, True))
    print(f("J", True, True))
    print(f("S", False, False))