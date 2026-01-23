def f(n1, n2, n3):
    if n1 == n2 or n1 == n3 or n2 == n3:
        return False
    else:
        return True
    
if __name__ == "__main__":
    print(f(4,8,5))
    print(f(2,9,2))