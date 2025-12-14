# Napisz program obsługujący klientów w urzędzie. Użyj kolejki. Każdy nowy klient otrzymuje bilet z automatycznie przydzielonym kolejnym numerem i jest dodawany na koniec kolejki. Następny klient do obsługi jest pobierany z początku kolejki.

import queue

q = queue.Queue()
numer = 1

for _ in range(3):
    print(f"Wydano bilet: {numer}")
    q.put(numer)
    numer += 1

print("---")

while not q.empty():
    klient = q.get()
    print(f"Obługiwany klient z biletem: {klient}")