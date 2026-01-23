# tv.py file
# class definition

class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False
        print("Telewizor jest wyłączony")
        
    def turn_on(self):
        self.is_on = True
        print("Telewizor jest włączony")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print("Channel list:")
        if not self.channels:
            print("- Brak zaprogramowanych kanałów -")
        else:
            # enumerate(lista, 1) numeruje elementy zaczynając od 1
            for index, name in enumerate(self.channels, 1):
                print(f"{index}. {name}")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print("Maksymalna głośność (10) osiągnięta")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Wyciszony (0). Ciszej się nie da.")

    def show_status(self):
        if self.is_on:
            channel_name = ""
            if self.channels and 0 < self.channel_no <= len(self.channels):
                channel_name = f"({self.channels[self.channel_no - 1]})"
            print(f"TV status: ON, channel: {self.channel_no} {channel_name}, volume: {self.volume}")
        else:
            print("TV status: OFF")

