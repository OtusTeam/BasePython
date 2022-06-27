from switchable import Switchable


class PowerSwitch:
    def __init__(self, client: Switchable):
        if not isinstance(client, Switchable):
            raise TypeError("Client must be switchable!")
        self.client = client
        self.on = False
        self.client.turn_off()

    def toggle(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
