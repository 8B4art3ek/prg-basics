# Napisz program do tłumaczenia słów z angielskiego na polski. Użytkownik wpisuje słowo po angielsku z klawiatury. Program wyświetla tłumaczenie słowa lub informację, że tłumaczenie jest niedostępne.

translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

slowo = input("Jakie słowo chcesz przetłumaczyć na polski?: ")

if slowo in translations:
    print(f"{slowo} to {translations[slowo]} po polsku")
else:
    print("Tłumaczenie niedostępne")