import logging
from time import sleep

import common

log = logging.getLogger(__name__)


def get_weather():
    log.info("Start getting weather")
    sleep(1)
    log.info("Done, got weather")


def get_currencies():
    log.info("Start getting currencies")
    sleep(1)
    log.info("Done, got currencies")


def main():
    common.configure_logging()
    log.info("Starting step 0")

    get_weather()
    get_currencies()


if __name__ == "__main__":
    main()
