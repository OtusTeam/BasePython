from switchable import Switchable


class Radio(Switchable):

    DESCRIPTION = "Radio player"

    def turn_on(self):
        print("playing radio")

    def turn_off(self):
        print("radio off")
