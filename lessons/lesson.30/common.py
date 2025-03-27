__all__ = (
    "DEFAULT_LOG_FORMAT",
    "configure_logging",
)

import logging

DEFAULT_LOG_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


def configure_logging(
    level: int = logging.INFO,
) -> None:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format=DEFAULT_LOG_FORMAT,
    )
