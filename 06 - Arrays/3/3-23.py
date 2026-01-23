# Zmienna zawiera tekst:
# An apple a day keeps the doctor away

# Następnie napisz program, wywołaj funkcje i wypisz wyniki. 
# Przykładowy wynik:
# Text: An apple a day keeps the doctor away
# Number of words: 8
# Words from the longest: doctor,apple,…
# Words ordered alphabetically: a,An,apple,away,…

import MyText

print("Text: An apple a day keeps the doctor away")
print("Number of words:", MyText.liczba_slow("An apple a day keeps the doctor away"))
print("Words from the longest:", MyText.slowa_od_najdluzszego("An apple a day keeps the doctor away"))
print("Words ordered alphabetically:", MyText.alfabetycznie("An apple a day keeps the doctor away"))