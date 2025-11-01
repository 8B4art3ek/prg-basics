###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

if is_bonus:
    total_salary = basic_salary + bonus*basic_salary
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary:.2f}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary:.2f}')