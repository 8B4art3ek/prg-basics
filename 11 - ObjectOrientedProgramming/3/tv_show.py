# tv_show.py file
# main program
import tv

def main():
    my_tv = tv.TV()

    # Włączamy TV
    my_tv.turn_on()
    
    # Ustawiamy kanały (żeby status ładnie wyglądał)
    my_tv.set_channels(["TVP1", "Polsat", "TVN", "HBO"])
    my_tv.set_channel(4) # Przełączamy na HBO

    # 1. Pokaż status (głośność powinna być 0)
    print("\n--- Status początkowy głośności ---")
    my_tv.show_status()

    # 2. Zwiększ głośność kilka razy
    print("\n--- Zwiększanie głośności ---")
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.show_status()

    # 3. Zmniejsz głośność (testujemy działanie w dół)
    print("\n--- Zmniejszanie głośności ---")
    my_tv.decrease_volume()
    my_tv.show_status()
    
    # 4. Próba zejścia poniżej zera (test zabezpieczenia)
    print("\n--- Próba wyciszenia poniżej 0 ---")
    # Zjeżdżamy do zera
    my_tv.decrease_volume() # na 1
    my_tv.decrease_volume() # na 0
    my_tv.decrease_volume() # próba na -1 (powinien być komunikat lub brak reakcji w statusie)
    my_tv.show_status()

    my_tv.turn_off()

if __name__ == "__main__":
    main()