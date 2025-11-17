# Define a function that calculates the final grade for a test based on the number of points obtained, according to the rules:

# Less than 10 points, final grade: Fail
# At least 10 points, final grade: Satisfactory
# At least 14 points, final grade: Good
# At least 18 points, final grade: Excellent
###
# Calculates the final grade for a test based
# on the number of points obtained
#

def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    elif points < 10:
        grade = 'Fail'
    return grade

test_result = 9
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {pts_to_grade(test_result)}')