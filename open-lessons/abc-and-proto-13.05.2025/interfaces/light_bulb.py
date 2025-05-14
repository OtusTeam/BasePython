from interfaces.switchable import Switchable


class LightBulb(Switchable):
    def on(self) -> None:
        print("turned on light bulb", self)

    def off(self) -> None:
        print("turned off light bulb", self)
