# Write a program that copies the contents of the file 'healthy_lifestyle.txt' to the file copy_healthy_lifestyle.txt'.
# Hint: Read the entire contents of the original file and write them to the target file (copy).

###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as file:
    content = file.read()

# write the content to the target file (copy)
with open(target_file, "w") as file:
    file.write(content)