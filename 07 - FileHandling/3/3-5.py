# Many applications require that you create an account with a username and password to use them. Often, applications specify requirements for the username and password. Write a program that checks whether a username and password entered from the keyboard meet the requirements below. Use regular expressions.

# username is at least 6 characters long
# username contains only lowercase letters
# password is at least 8 characters long
# password contains only letters (lowercase and uppercase), numbers, and the underscore character
###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# pattern (criteria) for username and password
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[A-Za-z0-9_]{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
    print("Username and password are valid")
else:
    print("Username or password is invalid")