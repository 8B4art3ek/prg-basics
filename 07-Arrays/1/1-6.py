# Write a program that prints the name of the day of the week for a given day number. Then, using the defined function, print the name of the day of the week for the following day numbers: 1, 4, 7.

###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    return f"{n}-{weekdays[n-1]}"

if __name__ == "__main__":
    print(weekday(1))
    print(weekday(4))
    print(weekday(7))