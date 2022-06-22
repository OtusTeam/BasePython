class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class LightBulb(Switchable):
    # def __init__(self, watts: int):
    #     self.power = watts

    def turn_on(self):
        print("LightBulb turned on")

    def turn_off(self):
        print("LightBulb turned off")


class Computer(Switchable):
    ...


class PowerSwitch:
    def __init__(self, client: Switchable):
        if not isinstance(client, Switchable):
            raise TypeError("expected Switchable, got", client)

        self.client = client
        self.on = False

    def toggle(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


bulb = LightBulb()
switch = PowerSwitch(bulb)
switch.client.turn_on()
switch.client.turn_off()
print("switch toggle:")
switch.toggle()
switch.toggle()
switch.toggle()
switch.toggle()
