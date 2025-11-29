# The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:

# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice):
    longest_digit = dice[0]
    longest_count = 1

    current_digit = dice[0]
    current_count = 1

    for d in dice[1:]:
        if d == current_digit:
            current_count += 1
        else:
            current_digit = d
            current_count = 1

        if current_count > longest_count:
            longest_count = current_count
            longest_digit = current_digit
    
    return int(longest_digit)
    
if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))