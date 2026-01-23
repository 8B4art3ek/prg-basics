# (p1.py) Karty do gry mają następujące wartości: As (A), Król (K), Dama (Q), Walet (J) i 10 (T) mają wartość 10 każdy. Pozostałe karty mają wartość wskazaną przez numer karty. Zdefiniuj funkcję f(player1, player2), która zwraca true, jeśli pierwszy gracz ma karty o tej samej lub wyższej wartości, a false w przeciwnym razie. 
# Przykład: 
# f("AJ972", "AQT72") → False 
# f("9532", "K8") → True

def f(player1, player2):
    values = {
        "A": 10,
        "K": 10,
        "Q": 10,
        "J": 10,
        "T": 10,
    }

    def score(hand):
        total = 0
        for card in hand:
            if card in values:
                total += values[card]
            else:
                total += int(card)
        return total
    return score(player1) >= score(player2)   # zwraca true/false


print(f("AJ972", "AQT72"))
print(f("9532", "K8"))