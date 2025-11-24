def f(palindrom):
    return palindrom == palindrom[::-1]

print(f("radar"))
print(f("12-11-21"))
print(f("book"))