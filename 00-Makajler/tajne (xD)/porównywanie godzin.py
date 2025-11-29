from datetime import datetime

def f(time1, time2):
    # funkcja pomocnicza, żeby nie pisać tego samego dwa razy
    def parse_time(t):
        # sprawdzanie czy w tekście jest "m" (od am/pm)
        if 'm' in t.lower():
            # format 12godzinny (np. "02:30pm")
            # %I - godzina 1-12
            # %M - minuty
            # %p - AM/PM
            # .upper() po to żeby było duże AM/PM
            return datetime.strptime(t.upper(), "%I:%M%p")
        else:
            # format 24godzinny (np. "14:30")
            # %H - godzina 0-23
            # %M - minuty
            return datetime.strptime(t, "%H:%M")
    
    # zamiana napisu na obiekt czasu
    t1_obj = parse_time(time1)
    t2_obj = parse_time(time2)

    if t1_obj < t2_obj:
        return time1
    else:
        return time2
    
if __name__ == "__main__":
    print(f("11:00am", "02:30pm"))
    print(f("10:00pm", "22:05"))
    print(f("14:00", "01:00pm"))