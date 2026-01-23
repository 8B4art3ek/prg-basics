# Format daty ISO to standard zapewniający unikalny sposób reprezentacji dat, niezależny od lokalnych konwencji. Data ISO jest reprezentowana w formie YYYY-MM-DD, gdzie YYYY to rok, MM to miesiąc, a DD to dzień, np. 2025-01-04 dla 4 stycznia 2025. Stwórz funkcję f(dates), która dla danego ciągu dat oddzielonych przecinkiem, zwraca tablicę dat zgodnych z formatem ISO.

# dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011" 
# f(dates) returns ["1998-12-11","2001-12-07"]

import re

def f(dates):
    return re.findall(r'\d{4}-\d{2}-\d{2}', dates)

if __name__ == "__main__":
    dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
    print(f(dates)) 