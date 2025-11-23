# Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:

# f(4) returns "*/*/*/*"
# f(1) returns "*"

def f(n):
    string = n*"*"
    result = ''
    for sign in string:
        result += sign + '/'
    return result[:-1]

if __name__ == "__main__":
    print(f(4))
    print(f(1))