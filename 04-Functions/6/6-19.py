# Define a function f(number) that returns the sum of repeated digits in a number. Sample result:

# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number):
    number = str(number)
    result = 0

    for digit in number:
        if number.count(digit) > 1: #czy duplikat?
            if str(result).count(digit) == 0: #żeby nie dodawać 2 razy
                result += int(digit)
    return result

print(f(1027))
print(f(230335))
print(f(513553007))