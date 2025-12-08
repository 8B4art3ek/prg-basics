# Następujące osoby są zatrudnione w jednym z działów firmy:
# SMITH Lucy
# JONES Janet
# LEE Jerry
# JACKSON Peter
# JOHNSON Rick
# LEWIS Terry
# CLARKE Robin
# Zapisz listę pracowników w tablicy (liście) ciągów znaków. Następnie napisz program, który wyświetla osoby, których nazwiska zaczynają się na literę 'J'. Użyj funkcji anonimowych oraz filter(). 

# Przykładowy wynik:
# JONES Janet
# JACKSON Peter
# JOHNSON Rick

employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]

emp_J = list(filter(lambda e:e[0]=="J", employees))

print(emp_J)