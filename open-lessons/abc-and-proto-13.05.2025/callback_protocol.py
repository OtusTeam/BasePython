import logging
from typing import Any, Callable, Protocol


def configure_logging(
    level: int = logging.INFO,
) -> None:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
        # format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


log = logging.getLogger(__name__)


class MessageCallbackProtocol(Protocol):
    __name__: str

    def __call__(self, message: str, sender_id: int, **kwargs: str) -> None: ...


def process_message(
    message: str,
    sender_id: int,
    meta: dict[str, str],
    callback: MessageCallbackProtocol,
) -> None:
    log.info(
        "processing message: %s from sender #%d with meta %s",
        message,
        sender_id,
        meta,
    )
    ...
    log.info("Calling callback %s", callback.__name__)
    callback(message, sender_id, **meta)


def handle_message(
    message: str,
    sender_id: int,
    **kwargs: str,
) -> None:
    log.info("processing message: %s from sender #%d", message, sender_id)


def main() -> None:
    configure_logging()
    process_message(
        "some message",
        sender_id=1,
        meta={"foo": "bar"},
        callback=handle_message,
    )


if __name__ == "__main__":
    main()
