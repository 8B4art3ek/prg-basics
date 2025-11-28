# The following program prints a list of countries from 'countries.txt' file. Modify the program to print a list of countries sorted alphabetically.

# Tip. Before printing the contents of the array, sort it alphabetically using the built-in function sorted()

###
# Reads the entire contents of a file
#

def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = sorted(file_content.splitlines())

# prints the array
for line in file_lines:
    print(line)