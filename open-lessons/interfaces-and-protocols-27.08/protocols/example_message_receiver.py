from typing import Protocol


class CallbackProtocol(Protocol):
    __name__: str

    def __call__(
        self,
        message: str,
        size: int,
    ) -> None: ...


class Callback:

    @property
    def __name__(self):
        return self.__class__.__name__

    def __call__(self, message: str, size: int) -> None:
        print("(cls) received message:", message, "of size", size)


def process_incoming_message(
    data: bytes,
    callback: CallbackProtocol,
) -> None:
    message = data.decode("utf-8")
    message_size = len(message)
    print("notify callback", callback.__name__)
    callback(
        message=message,
        size=message_size,
    )
    callback(
        message,
        size=message_size,
    )
    callback(
        message,
        message_size,
    )


def my_callback(message: str, size: int) -> None:
    print("received message:", message, "of size", size)


def main() -> None:
    data = b"Hello World!"
    process_incoming_message(
        data=data,
        callback=my_callback,
    )
    callback = Callback()

    process_incoming_message(
        data=data,
        # беда
        callback=callback,
    )


if __name__ == "__main__":
    main()
