from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .switchable import Switchable


class PowerSwitch:
    def __init__(self, client: "Switchable"):
        self.client = client
        self.on = False
        self.client.off()

    def toggle(self):
        if self.on:
            self.client.off()
            self.on = False
        else:
            self.client.on()
            self.on = True
