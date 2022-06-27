from switchable import Switchable


class MusicPlayer(Switchable):

    def turn_on(self):
        print("music player turned on")

    def turn_off(self):
        print("music player turned off")
