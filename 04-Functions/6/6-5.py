# In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

# A number: 7
# Number 7 in the range <2,15>: yes

import separate_module

print(f"Number 7 in the range <2,15>: {separate_module.check_number(7, 2, 15)}")