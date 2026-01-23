# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.hair_color = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.hair_color = "blond"
    student2.name = "Olivia"
    student2.age = 21
    student2.hair_color = "red"
    student3.name = "Norbert"
    student3.age = 25
    student3.hair_color = "dark"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, hair color: {student1.hair_color}')
    print(f'{student2.name}, {student2.age} years old, hair color: {student2.hair_color}')
    print(f'{student3.name}, {student3.age} years old, hair color: {student3.hair_color}')

if __name__ == "__main__":
    main()