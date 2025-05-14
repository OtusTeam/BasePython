from interfaces.switchable import Switchable


class Fan(Switchable):
    def on(self) -> None:
        print("turned on fan", self)

    def off(self) -> None:
        print("turned off fan", self)
