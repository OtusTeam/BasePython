import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather():
    log.info("Start getting weather data")
    sleep(1)
    log.info("Done, got weather")


def get_currencies():
    log.info("Start getting currencies data")
    sleep(1)
    log.info("Done, got currencies")


def main():
    configure_logging()
    log.info("Starting step 0")

    get_weather()
    get_currencies()

    log.info("Finished main")


if __name__ == "__main__":
    main()
