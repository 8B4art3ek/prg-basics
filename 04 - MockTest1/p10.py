def f(sentence):
    suma_kodow = 0
    for char in sentence:
        suma_kodow += ord(char)
    if suma_kodow % 3 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("hello world"))
    print(f("university"))
    print(f("student"))
