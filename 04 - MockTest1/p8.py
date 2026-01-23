def f(palindrom):
    return palindrom == palindrom[::-1]

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))