# tv.py file
# class definition

class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1

    def turn_off(self):
        self.is_on = False
        print("Telewizor jest wyłączony")
        
    def turn_on(self):
        self.is_on = True
        print("Telewizor jest włączony")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def show_status(self):
        if self.is_on:
            print(f"TV status: ON, channel: {self.channel_no}")
        else:
            print("TV status: OFF")

