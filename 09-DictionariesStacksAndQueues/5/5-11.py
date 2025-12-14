# Napisz program do rejestrowania głosowania. Wyniki głosowania są zapisywane w pliku voting.json o poniższej strukturze. Program pobiera imię osoby z klawiatury i zwiększa liczbę głosów dla tej osoby o 1. Jeśli jest to nowa osoba, jest dodawana do listy z liczbą głosów 1. Możesz uruchomić program wielokrotnie, aby dodać kolejne głosy do pliku json.
# {
#    person_name: number of votes,
#    person_name: number of votes,
#    ...
#    ...
# }

import json
filename = "voting.json" 

# Read the contents of the json file
try:
    with open(filename, "r", encoding="utf-8") as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}

# Vote for a person
person_name = input('Name of the person you are voting for: ').strip()
votes[person_name] = votes.get(person_name, 0) + 1

# Save voting data to json file
with open(filename, "w", encoding="utf-8") as file:
    json.dump(votes, file, indent=4)

print("Vote recorded")