# Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise. Sample result:

# f(11,6,-4) returns True
# f(5,4,14) returns False

def f(n1,n2,n3):
    numbers = [n1, n2, n3]
    for i in numbers:
        if i < 0:
            return True
    return False

print(f(11,6,-4))
print(f(5,4,14))


def f2(n1,n2,n3):
    return any(x < 0 for x in (n1,n2,n3))     # any() zwraca true gdy chociaz jeden w (n1,n2,n3) jest < 0 (war. x < 0)
    
print(f2(11,6,-4))
print(f2(5,4,14))