def f(hours,minutes,seconds):
    return True if seconds==60*minutes and minutes==60*hours and seconds==3600*hours else False

if __name__ == "__main__":
    print(f(1,60,3600))
    print(f(2,120,7200))
    print(f(4,220,14400))
    print(f(3,180,10600))