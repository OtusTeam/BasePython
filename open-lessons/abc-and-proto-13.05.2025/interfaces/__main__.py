from interfaces.light_bulb import LightBulb
from interfaces.fan import Fan
from interfaces.power_switch import PowerSwitch


def main() -> None:
    fan_switch = PowerSwitch(Fan())
    fan_switch.toggle()
    light_switch = PowerSwitch(LightBulb())
    light_switch.toggle()
    light_switch.toggle()
    fan_switch.toggle()
    light_switch.toggle()


if __name__ == "__main__":
    main()
