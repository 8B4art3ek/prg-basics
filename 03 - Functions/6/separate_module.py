def month(n):
    match n:
        case 1:
            return f"The name of month {n} is January"
        case 2:
            return f"The name of month {n} is February"
        case 3:
            return f"The name of month {n} is March"
        case 4:
            return f"The name of month {n} is April"
        case 5:
            return f"The name of month {n} is May"
        case 6:
            return f"The name of month {n} is June"
        case 7:
            return f"The name of month {n} is July"
        case 8:
            return f"The name of month {n} is August"
        case 9:
            return f"The name of month {n} is September"
        case 10:
            return f"The name of month {n} is October"
        case 11:
            return f"The name of month {n} is November"
        case 12:
            return f"The name of month {n} is December"
        case _:
            return "Invalid number"
        

def letter_calculation(letter, text):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    return counter


def check_number(number, x, y):
    return x <= number <= y


# f("5290312400019022") returns "52**********9022"   16 digits
def hide(card_number):
    result = ""
    for i in range(len(card_number)):
        if 2 <= i < 12:
            result += "*"
        else:
            result += card_number[i]
    return result