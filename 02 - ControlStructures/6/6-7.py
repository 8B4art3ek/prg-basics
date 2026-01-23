# Write a program that asks the user for their age and then checks which age group they belong to:
# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
# Senior: 65 or older

age = int(input("Ile masz lat?: "))

if age < 13:
    print("You are a child")
elif age <= 19:
    print("You are a teen")
elif age <= 64:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")