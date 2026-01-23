# Tablica uid zawiera przykładowe identyfikatory użytkowników popularnej strony internetowej. Identyfikatory muszą być unikalne. Stwórz funkcję f(uid), która zwraca true, jeśli wszystkie podane identyfikatory są unikalne. W przeciwnym razie funkcja zwraca false.

# f(["john5","ann123","JOHN5","xxx","abc333","a10"]) returns True 
# f(["abc123","ann","abc123","a10"]) returns False

def f(uid):
    return len(set(uid)) == len(uid)

if __name__ == "__main__":
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"])) 
    print(f(["abc123","ann","abc123","a10"]))    