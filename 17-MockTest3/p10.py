# Stwórz funkcję f(value1), która zwraca funkcję z jednym parametrem value2 typu całkowitego. Zwrócona funkcja oblicza i zwraca iloczyn value1 * value2.

# times_five = f(5) 
# times_five(8) returns 40 
# times_three = f(3) 
# times_three(7) returns 21 

def f(value1):
    def inner(value2):
        return value1 * value2
    return inner

if __name__ == "__main__":
    times_five = f(5) 
    print(times_five(8)) 

    times_three = f(3) 
    print(times_three(7)) 