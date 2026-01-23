# Stwórz funkcję f(word), która dla danego słowa word zwraca ciąg znaków, w którym kolejne litery słowa tworzą tzw. meksykańską falę. Początkowo pierwsza litera słowa jest wielka, a pozostałe są małe. Następnie druga litera słowa jest wielka, a pozostałe są małe itd. Oddziel słowa znakiem myślnika (-).

# f("water") returns "Water-wAter-waTer-watEr-wateR" 
# f("a") returns "A" 
# f("") returns ""

def f(word):
    if not word:
        return ""
    
    word = word.lower()
    wynik = []

    for i in range(len(word)):
        fala = word[:i] + word[i].upper() + word[i+1:]
        wynik.append(fala)

    return "-".join(wynik)

if __name__ == "__main__":
    print(f("water")) 
    print(f("a"))  
    print(f("")) 