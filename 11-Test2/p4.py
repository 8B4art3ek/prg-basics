def f(subjects):
    srednia = 0
    nazwa = ""
    for key, value in subjects.items():
        sr = sum(value) / len(value)
        if sr > srednia:
            srednia = sr
            nazwa = key
    return nazwa

if __name__ == "__main__":
    subjects = {"math":[3,4,4], "geo":[5,4,4,4], "comp":[5,4]}
    print(f(subjects))