# Write a program that writes a list of the Seven Wonders of the World to a text file, in alphabetical order, with each name on a separate line. Then, open the created file in the editor and check if its contents match the task.

###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders_sorted = sorted(seven_wonders)

# Write data to the file
with open(file_name, 'w') as file:
    for item in seven_wonders_sorted:
        file.write(f"{item}\n")