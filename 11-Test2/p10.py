def f(quiz_answers, student1, student2):
    counter = 0
    quiz_answers_list, student1_list, student2_list = quiz_answers.split(","), student1.split(","), student2.split(",")
    for answer in quiz_answers_list:
        if answer in student1_list and answer in student2_list:
            counter += 1
    return counter

if __name__ == "__main__":
    quiz_answers = "1a,2a,3c,4c,5b,6a,7d,8a,9b,10d,11a,12d"
    student1 = "2a,7d,11a,3b,4c"
    student2 = "9b,3b,7d"
    print(f(quiz_answers, student1, student2))

    quiz_answers = "1a,2a,3c,4c,5b,6a,7d,8a,9b,10d,11a,12d"
    student1 = "9b,5b,2a,1a,4b,12a,11a"
    student2 = "12a,3c,2a,1a,7d,8a,9b,5b,4b"
    print(f(quiz_answers, student1, student2))