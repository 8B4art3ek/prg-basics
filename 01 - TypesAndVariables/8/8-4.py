###
# A program that prints your height both in cm and in feet and inches.
#
cm = 190
feet = round(cm / 30.48, 2)
inches = round(cm * 0.3937, 2)
# calculate the number of feet

print(f'I am {cm} cm tall, i.e. {feet} feet and {inches} inches')