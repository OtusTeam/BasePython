import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather():
    log.info("Getting weather...")
    sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


def get_currencies():
    log.info("Getting currencies...")
    sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rates": [42, 13]}}


def main():
    configure_logging()

    log.warning("Starting 00")

    get_currencies()
    get_weather()

    log.warning("Finished 00")


if __name__ == "__main__":
    main()
