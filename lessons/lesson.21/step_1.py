import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather():
    log.info("Start get weather")
    sleep(1)
    log.info("Done, got weather")


def get_currencies():
    log.info("Start get currencies")
    sleep(1)
    log.info("Done, got currencies")


def main():
    configure_logging()

    get_weather()
    get_currencies()


if __name__ == "__main__":
    main()
