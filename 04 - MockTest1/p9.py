def f(sentence):
    samogloski = "aeiouy"
    counter = 0
    if sentence.islower():
        for char in sentence:
            if char in samogloski:
                counter += 1
        return counter
    else:
        return "tylko male litery"
    
if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))
