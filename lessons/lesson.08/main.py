import models.bulbs

# from models import LightBulb, MusicPlayer, PowerSwitch
# from models.bulbs import LightBulb
from models import LightBulb
from models import MusicPlayer
from models import PowerSwitch
from models import Radio

import main2
import main3

# from switchable import Switchable
# from models.bulbs.base_bulb import Switchable
# from models import *
# from switchable import Switchable

# from models import
# from models.player import MusicPlayer

# class LightBulb(object):
#     pass
print("__name__ for main.py", __name__)


def main():
    # import main3
    print("main3.MY_VAR:", main3.MY_VAR)
    print(models.bulbs.LightBulb)

    bulb = models.bulbs.LightBulb()

    bulb2 = LightBulb()

    print(bulb)
    print(bulb2)

    print("LightBulb is models.bulbs.LightBulb:", LightBulb is models.bulbs.LightBulb)

    bulb2.turn_off()
    bulb2.turn_on()

    player = MusicPlayer()

    player.turn_off()
    player.turn_on()

    switch = PowerSwitch(player)

    switch.toggle()
    switch.toggle()

    # print(CONST)
    # print(missing)
    # print(default)

    radio = Radio()

    s2 = PowerSwitch(radio)
    s2.toggle()
    s2.toggle()
    s2.toggle()

    print("radio:", radio.get_description())

    print("bulb:", bulb.get_description())


# app = App()
# app.run()  # NEVER!!

if __name__ == "__main__":
    main()
    print("main2 name:", main2, repr(main2.__name__))
    # app.run()
