# Tablica prods zawiera nazwy produktów w magazynie. Stwórz funkcję f(fnc, prods), która mapuje nazwy produktów na ich ID, zgodnie z definicją w funkcji fnc. Funkcja f zwraca oddzielony przecinkami ciąg tekstowy ID produktów, bez spacji.

# prods = ["water","cheese","tomato"]  
# fnc1 = lambda x: "id:"+x[:2]  
# f(fnc1,prods) returns "id:wa,id:ch,id:to" 
# fnc2 = lambda x: (x[0]+x[-1]).upper()  
# f(fnc2,prods) returns "WR,CE,TO" 

def f(fnc, prods):
    ids = [fnc(x) for x in prods]
    return ",".join(ids)

if __name__ == "__main__":
    prods = ["water", "cheese", "tomato"]

    fnc1 = lambda x: "id:" + x[:2]
    print(f(fnc1, prods))

    fnc2 = lambda x: (x[0] + x[-1]).upper()
    print(f(fnc2, prods))