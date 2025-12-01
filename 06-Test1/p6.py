def f(student1, student2):
    s1 = student1.split(",")
    s2 = student2.split(",")

    positive = "345"
    negative = "2"
    counter1 = 0
    counter2 = 0



    for item in s1:
        if item in positive:
            counter1 += 1
        
    for item in s2:
        if item in positive:
            counter2 += 1

    if counter1 > counter2:
        return 1
    if counter2 > counter1:
        return 2
    if counter1 == counter2:
        return 0
    
if __name__ == "__main__":
    print(f("3,4,5", "4,3"))
    print(f("3,2,5", "5,5,2,5"))
    print(f("3,2,5,2,2", "4,4"))