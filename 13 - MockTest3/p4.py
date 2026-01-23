# Tablica res zawiera wyniki testów, tzn. liczbę punktów od 0 do 100. Stwórz funkcję f(fnc,res), która filtruje wyniki testów zgodnie z kryteriami zawartymi w funkcji fnc. Funkcja f zwraca różnicę między najwyższym a najniższym wynikiem testu.

# res = [95,90,20,50,70]  
# fnc1 = lambda x: x>50 
# f(fnc1,res) returns 25 
# fnc2 = lambda x: x>30 and x<90 
# f(fnc2,res) returns 20

def f(fnc, res):
    filtered = [x for x in res if fnc(x)]
    
    if not filtered:
        return 0
        
    return max(filtered) - min(filtered)

if __name__ == "__main__":
    res = [95, 90, 20, 50, 70]
    fnc1 = lambda x: x > 50
    print(f(fnc1, res)) 
    fnc2 = lambda x: x > 30 and x < 90
    print(f(fnc2, res)) 