from .switchable import Switchable


class LightBulb(Switchable):
    def on(self):
        print("light bulb on")

    def off(self):
        print("light bulb off")
