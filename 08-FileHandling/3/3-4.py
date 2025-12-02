# A file report.txt contains an email with shopping report. Write a program that calculates the total value of money spent.
# Hint: To open and read a text file that contains special characters (like the Euro sign €), you need to ensure that the file is read using the correct character encoding. The most common encoding for such cases is UTF-8, which supports a wide range of characters, including special symbols. Here is an example use of the open() function:
# open("example.txt", "r", encoding="utf-8")

###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, "r") as file:
    email = file.read()

# regular expression pattern
# for amounts
pattern = r'\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
    total += int(amount)

# print result
print("Total spent:", total, "€")