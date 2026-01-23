import re

def f(vname):
    return bool(re.match(r"^[a-zA-Z_][a-zA-Z0-9_]{0,4}$", vname))

if __name__ == "__main__":
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB8_"))