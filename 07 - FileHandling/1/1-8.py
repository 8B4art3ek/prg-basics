# The file pets.txt contains humorous text about animals. Write a program that prints the text and counts the number of words in the text.

# To calculate the number of words in a line, use the split() method, which splits a string into a list where each word is a list item. Then read the length of this list. Use the len() function. Finally, sum the number of words in each line.
# https://www.w3schools.com/python/ref_string_split.asp


with open ('pets.txt', "r") as file:
    content = file.read()
    words = content.split()
    text = ""
    for word in words:
        text += word + " "
    text = text.strip()
    num = len(words)
    print(f"{text},\nNumber of words: {num}")