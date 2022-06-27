from abc import ABC, abstractmethod


# ABC = Abstract Base Class

class Switchable(ABC):
    DESCRIPTION = "base switchable"

    def get_description(self):
        return self.DESCRIPTION

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


print("__name__ for switchable", __name__)
