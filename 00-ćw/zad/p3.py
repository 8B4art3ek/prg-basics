import re

def f(text):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{0-5}$'
    if re.match(pattern, text):
        return True
    else:
        return False