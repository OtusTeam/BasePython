from interfaces.switchable import Switchable
from interfaces.light_bulb import LightBulb
from interfaces.wireless_mouse import WirelessMouse
from interfaces.power_switch import PowerSwitch


class Oven(Switchable):
    def off(self):
        print("oven off")

    def on(self):
        print("oven on")


def example_interfaces():
    # sw = Switchable()
    # print("SW:", sw)
    bulb = LightBulb()
    print("bulb:", bulb)
    bulb.on()
    bulb.off()

    mouse = WirelessMouse()
    print("mouse:", mouse)
    mouse.on()
    mouse.off()

    switch = PowerSwitch(client=bulb)
    switch.toggle()
    switch.toggle()
    switch.toggle()

    mouse_switch = PowerSwitch(client=mouse)
    mouse_switch.toggle()
    mouse_switch.toggle()
    mouse_switch.toggle()

    oven = Oven()
    oven_switch = PowerSwitch(client=oven)
    oven_switch.toggle()


def main():
    example_interfaces()


if __name__ == "__main__":
    main()
