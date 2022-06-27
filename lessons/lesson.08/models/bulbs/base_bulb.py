__all__ = ("LightBulb",)

from switchable import Switchable


class LightBulb(Switchable):

    def get_description(self):
        return "just a bulb"

    def turn_on(self):
        print("turned bulb on")

    def turn_off(self):
        print("turned bulb off")


def helper():
    ...


print("__name__ for base_bulb", __name__)
