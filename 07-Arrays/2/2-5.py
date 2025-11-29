# The data below represents a cinema's seating arrangement. Write a program that:

# calculates how many seats are available
# calculates how many seats are booked
# informs what the status of a seat is in a given row and given place (available or booked)

# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    total = 0
    for row in seats:
        total += len(row)
    return total

def seats_available(seats):
    available = 0
    for row in seats:
        for column in row:
            if column == "A":
                available += 1
    return available

def seats_booked(seats):
    booked = 0
    for row in seats:
        for column in row:
            if column == "B":
                booked += 1
    return booked

def seat_status(seats, row, place):
    value = seats[row-1][place-1]
    if value == "A":
        return "Available"
    else:
        return "Booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))