import logging


# CRITICAL = 50
# ERROR    = 40
# WARNING  = 30
# INFO     = 20
# DEBUG    = 10


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    )
