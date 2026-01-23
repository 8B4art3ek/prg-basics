# A computer numeric keyboard has the arrangement of the keys as below. The included program code prints the computer keyboard. Analyse the program in terms of the printed results. Do you understand each program statement? Then make changes in your program code. Replace the 'for' with a 'while' statement.

# 7 8 9
# 4 5 6
# 1 2 3

for i in range(6,-1,-3):
    for j in range(1,4):
        print(f'{i+j}',end=' ')
    print()