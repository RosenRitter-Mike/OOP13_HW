from facade_hw import *


class SmartHomeFacade:
    def __init__(self, pop_corn=PopcornMachine(),
                 ac=AirConditioner(),
                 lights=Lights(),
                 screen=TV()):
        self.lights = lights
        self.screen = screen
        self.ac = ac
        self.pop_corn = pop_corn

    def say_good_morning(self):
        print("\nGood morning sir!⏰\nYour personal butler Alfred is happy to see you, as always\n")
        self.lights.turn_on()
        self.screen.turn_on()
        self.screen.set_channel("🎶Music Channel🎸")
        self.ac.set_temperature(22)
        print("\nHave a nice day sir!🌄\n")

    def say_watch_movie(self):
        print("\nSetting up the TV for Netflix and chill, sir🛋\n")
        self.lights.turn_off()
        self.screen.turn_on()
        self.screen.set_channel("Netflix📺")
        self.ac.set_temperature(18)
        self.pop_corn.turn_on()
        self.pop_corn.pop_corn()
        self.pop_corn.turn_off()
        print("\nEnjoy your film sir!🎬\n")

    def say_good_night(self):
        print("\nGood night sir!🌃\nYour bed is ready for you, sleep well🛏\n")
        self.lights.turn_off()
        self.screen.turn_off()
        self.ac.set_temperature(28)
        print("\nHave pleasant dreams sir!😴💤\n")

