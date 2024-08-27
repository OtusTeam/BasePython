from .switchable import Switchable


class WirelessMouse(Switchable):
    def on(self):
        print("mouse on")

    def off(self):
        print("mouse off")

    def track(self):
        print("mouse tracking")

    def click(self):
        print("mouse clicking")
