# tv_show.py file
# main program
import tv

def main():
    tv1 = tv.TV()
    tv1.show_status()
    tv1.turn_on()
    tv1.show_status()
    tv1.set_channel(5)
    tv1.show_status()
    tv1.turn_off()
    tv1.show_status()    

if __name__ == "__main__":
    main() 