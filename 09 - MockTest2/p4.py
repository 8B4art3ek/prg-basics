# (p4.py) Słownik zawiera nazwy przedmiotów i uzyskane oceny. Zdefiniuj funkcję f(subjects), która dla podanych przedmiotów i ich ocen zwraca nazwę przedmiotu, dla którego średnia ocen jest najwyższa. 
# Przykład: 
# f({"math": [3,4,4], "geo": [5,4,4,4], "comp": [5,4]}) → "comp"

def f(subjects):
    best_subject = None
    best_avg = -1

    for subject, grades in subjects.items():
        avg = sum(grades) / len(grades)

        if avg > best_avg:
            best_avg = avg
            best_subject = subject
    return best_subject

print(f({"math": [3,4,4], "geo": [5,4,4,4], "comp": [5,4]}))