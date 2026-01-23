# As you remember, the input() function allows you to read only a string from the keyboard. In the module keyboard.py, define your own functions that allow reading other types of data from the keyboard:

# input_string() that returns a string entered from the keyboard
# input_integer() that returns an integer number entered from the keyboard
# input_real() that returns a real number entered from the keyboard
# input_boolean() that returns a boolean value depending on the pressed y/n key

###
# Functions to read any data type from the keyboard
#
def input_string(message):
    return str(input(message))

def input_integer(message):
    return int(input(message))

def input_real(message):
    return float(input(message))

def input_boolean(message):
    user_input = input(message)
    match user_input:
        case "y" | "Y":
            return True
        case "n" | "N":
            return False
        case _:
            return "Invalid option"