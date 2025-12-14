import json

favourite = {
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
    "genre": "science fiction",
    "rating": 9,
    "language": "English"
}

with open("favourite.json", "w", encoding="utf-8") as file:
    json.dump(favourite, file, ensure_ascii=False, indent=4)

print("Zapisano dane do pliku favourite.json")
