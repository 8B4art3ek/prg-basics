# Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. Write a program that prints a survey consisting of three questions. Save the answers to logical type variables. Then view the survey result. Sample result:

# SURVEY 
# Are you interested in computer science? (y/n): y
# Do you like playing computer games? (y/n): n
# Do you have an Instagram account? (y/n): y

# SURVEY RESULTS 
# Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes

print("SURVEY")
science = input("Are you interested in computer science? (y/n): ")
games = input("Do you like playing computer games? (y/n): ")
instagram = input("Do you have an Instagram account? (y/n): ")

if science == "y":
    science = "Yes"
elif science == "n":
    science = "No"

if games == "y":
    games = "Yes"
elif games == "n":
    games = "No"

if instagram == "y":
    instagram = "Yes"
elif instagram == "n":
    instagram = "No"

print("SURVEY RESULTS")
print(f"Interested in computer science: {science}")
print(f"Playing computer games: {games}")
print(f"Has an Instagram account: {instagram}")