import re 

def f(filenames):
    def natural_key(text):
        return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]
    return sorted(filenames, key=natural_key)