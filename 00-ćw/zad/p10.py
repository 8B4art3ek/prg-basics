import re

def f(dates):
    return re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}', dates)