def f(name):
    words = name.split()
    result = ""
    for word in words:
        result += word[0]
    
    return result

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))