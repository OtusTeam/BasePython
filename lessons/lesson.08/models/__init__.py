__all__ = (
    "LightBulb",
    "MusicPlayer",
    "PowerSwitch",
    "Radio",
)

# from models.bulbs import LightBulb

from .bulbs import LightBulb
from .player import MusicPlayer
from .power_switch import PowerSwitch
from .radio import Radio

# missing = object()
# default = object()
#
# CONST = 42
#
# value = "random"
#
# if value == CONST:
#     ...
