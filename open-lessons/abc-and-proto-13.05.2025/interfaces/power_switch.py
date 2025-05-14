from interfaces.switchable import Switchable


class PowerSwitch:
    def __init__(self, client: Switchable) -> None:
        self.client = client
        self.on = False
        self.client.off()

    def toggle(self) -> None:
        if self.on:
            self.client.off()
        else:
            self.client.on()

        self.on = not self.on
