# Create a dictionary describing your mobile phone. Use 6 key-value pairs of data. Then, using for loop, display the contents of the dictionary. To read a key and value, use the items() method. Sample result:

mobile = {
    "OS":"Android",
    "Producent": "Samsung",
    "Model": "A56",
    "is5G": True,
    "Screen size in inch": 6.7,
    "My opinion": "Okay"
}
for key,value in mobile.items():
    print(f"{key}: {value}")