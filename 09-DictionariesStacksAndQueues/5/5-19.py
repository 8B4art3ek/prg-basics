# System informatyczny hotelu zawiera listę zarezerwowanych pokoi. Dane znajdują się w pliku reservations.json. Napisz program, który wypisuje podsumowanie informacji, jak podano poniżej. Podziel swój program na mniejsze części, definiując funkcje.

# liczba pokoi
# liczba opłaconych rezerwacji
# liczba nieopłaconych rezerwacji
# całkowita wartość opłaconych rezerwacji
# całkowita wartość nieopłaconych rezerwacji

import json

def load_reservations(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data['reservations']

def count_rooms(reservations):
    return len(reservations)

def count_paid(reservations):
    return sum(1 for r in reservations if r.get('paid', False))

def count_unpaid(reservations):
    return sum(1 for r in reservations if not r.get('paid', False))

def total_paid_value(reservations):
    return sum(r['nights'] * r['price_per_night'] for r in reservations if r.get('paid', False))

def total_unpaid_value(reservations):
    return sum(r['nights'] * r['price_per_night'] for r in reservations if not r.get('paid', False))

def print_summary(reservations):
    print("Podsumowanie rezerwacji:")
    print("Liczba pokoi:", count_rooms(reservations))
    print("Liczba opłaconych rezerwacji:", count_paid(reservations))
    print("Liczba nieopłaconych rezerwacji:", count_unpaid(reservations))
    print("Całkowita wartość opłaconych rezerwacji:", total_paid_value(reservations))
    print("Całkowita wartość nieopłaconych rezerwacji:", total_unpaid_value(reservations))

def main():
    reservations = load_reservations('reservations.json')
    print_summary(reservations)

if __name__ == "__main__":
    main()