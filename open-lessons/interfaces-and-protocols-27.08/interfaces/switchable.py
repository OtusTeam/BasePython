from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def on(self):
        raise NotImplementedError

    @abstractmethod
    def off(self):
        raise NotImplementedError
