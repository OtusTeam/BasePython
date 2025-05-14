from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def on(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def off(self) -> None:
        raise NotImplementedError
