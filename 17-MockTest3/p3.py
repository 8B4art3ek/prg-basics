# Numery lotów wraz z liczbą pasażerów są przechowywane w słowniku d. Zdefiniuj funkcję f(d), która zwraca liczbę lotów, w których liczba pasażerów jest większa niż średnia liczba pasażerów we wszystkich lotach.

# f({"LO231":150,"BA787":120,"NZ15":30}) returns 2 
# f({"LO231":150,"BA787":20,"NZ15":30}) returns 1

def f(d):
    avg = sum(d.values()) / len(d)
    return sum(1 for passengers in d.values() if passengers > avg)

if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}))