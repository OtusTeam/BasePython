import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather():
    log.info("get weather")
    # wait for weather
    # TODO: real API call
    sleep(1)
    log.info("done get weather")


def get_currencies():
    log.info("get currencies")
    # wait for currencies
    # TODO: real API call
    sleep(1)
    log.info("done get currencies")


def main():
    configure_logging()
    log.info("start main")
    get_weather()
    get_currencies()
    log.info("finish main")


if __name__ == '__main__':
    main()
