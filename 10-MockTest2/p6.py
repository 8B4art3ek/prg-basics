# (p6.py) Zdefiniuj funkcję f(years, course, average_grade), która dla pliku data.json zwraca liczbę studentów, którzy mają co najmniej podaną liczbę lat i średnią ocen co najmniej average_grade z podanej nazwy kursu. 
# Przykład: f(21, "statistics", 4) porównaj swój wynik z innymi studentami

import json

def f(years, course_name, average_grade):
    count = 0
    with open('data.json', 'r', encoding='utf-8') as file:
        students = json.load(file)

    for student in students:
        if student.get("age", 0) < years:
            continue

        courses = student.get("studies", {}).get('courses', [])
        for course in courses:
            if course.get("name") == course_name:
                grades = course.get("grades", [])
                if grades and sum(grades)/len(grades) >= average_grade:
                    count += 1
                break
    return count

print(f(21, "statistics", 4))