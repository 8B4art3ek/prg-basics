# Define a function f(text) that returns the given text with all characters separated by a dash sign. Example:

# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""

def f(text):
    if len(text) <= 1:
        return text
    new = ""
    for i in range(len(text)):
        new += text[i] + "-"
    return new[:-1]

if __name__ == "__main__":
    print(f("Univesity"))
    print(f("UE"))
    print(f("x"))
    print(f(""))