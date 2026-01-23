# Strona internetowa https://api.nbp.pl/en.html zawiera dane o kursach walut publikowane przez Narodowy Bank Polski. Serwis udostępnia dane zarówno w formacie json, jak i xml. Wyświetl ostatnie dziesięć kursów Euro w formacie json w przeglądarce internetowej. Następnie zapisz dane do pliku euro.json. Na koniec napisz program, który wyświetla dane z pliku euro.json w następującym formacie:

# Date             Buying Rate      Selling Rate
# ============================================
# 2019-10-25       3.8150           3.9820
# ...
# ...
# ...
# Wskazówka: Jeśli interesują Cię zagadnienia API i Rest API, przeczytaj poniższy artykuł: https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/

import json

with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

rates = data['rates']

print("Date          Buying Rate      Selling Rate")
print("============================================")

for item in rates:
    date = item['effectiveDate']
    mid = item['mid']
    print(f"{date}        {mid:.4f}              {mid:.4f}")