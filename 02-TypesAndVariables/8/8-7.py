# The binary numeral system is a positional numeral system that requires only two digits to write numbers: 0 and 1. The hexadecimal numeral system is a positional numeral system that uses sixteen distinct symbols, most often the symbols "0" to "9" to represent values 0 to 9, and "A" to "F" (or alternatively "a" to "f") to represent values from ten to fifteen. Both are widely used in mathematics, computer science and digital electronics. Write a program that reads an integer number from the keyboard and prints that value as a binary and hexadecimal number. To convert a decimal number to binary or hexadecimal value, use the available Python functions. Sample result:
# Enter number: 125
# Binary number: 0b1111101
# Hexadecimal number: 0x7d
dec_number = int(input("Enter number: "))
print(f"Decimal number: {dec_number}")
print(f"Binary number: {bin(dec_number)}")
print(f"Hexadecinam number: {hex(dec_number)}")