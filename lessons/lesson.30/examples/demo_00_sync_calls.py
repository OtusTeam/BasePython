import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather() -> dict:
    log.info("Start getting weather")
    sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


def get_currencies() -> dict:
    log.info("Start getting currencies")
    sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


def main() -> None:
    configure_logging()
    log.info("Start main 00")
    weather = get_weather()
    log.info("Weather result: %s", weather)
    currencies = get_currencies()
    log.info("Currencies result: %s", currencies)
    log.info("Finished main 00")


if __name__ == "__main__":
    main()
