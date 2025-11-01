###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

temp_in_c = float(input("Wprowadź temperature w st. C: "))
temp_in_f = temp_in_c * 9 / 5 + 32
temp_in_k = temp_in_c + 273.15
print(f"Temperatura {temp_in_c} stopni celsjusza to {temp_in_f} stopni fahrenfeita i {temp_in_k} stopni kelvina")