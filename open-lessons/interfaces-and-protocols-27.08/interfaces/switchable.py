from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def on(self):
        raise NotImplemented

    @abstractmethod
    def off(self):
        raise NotImplemented
