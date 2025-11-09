# Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm

format_24h = input("Enter time (24-hour format): ")
format_12h = ""

if int(format_24h[0:2]) == 00:
    format_12h += str(int(format_24h[0:2]) + 12) + format_24h[2:5] + "am"
elif int(format_24h[0:2]) <= 11:
    format_12h += format_24h + "am"
elif int(format_24h[0:2]) == 12:
    format_12h += str(int(format_24h[0:2])) + format_24h[2:5] + "pm"
elif int(format_24h[0:2]) <= 23:
    format_12h += str(int(format_24h[0:2]) - 12) + format_24h[2:5] + "pm"
else:
    print("Wrong time")

print(f"Time in 12-hour format: {format_12h}")

