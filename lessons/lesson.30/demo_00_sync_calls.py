import logging
from time import sleep

from common import configure_logging


log = logging.getLogger(__name__)


def get_weather() -> dict:
    log.info("Getting weather data")
    # url = "https://openweathermap.org/?city=Moscow"
    # response = requests.get(url)
    # data = response.json()
    # return data
    sleep(1)
    log.info("fetched weather data")
    return {"weather": {"temperature": 23}}


def get_currencies() -> dict:
    log.info("Getting currencies data")
    # url = "https://exchange-rate.org/?from=FOO&to=BAR"
    # response = requests.get(url)
    # data = response.json()
    # return data
    sleep(1)
    log.info("fetched currencies data")
    return {"currencies": {"rate": 42}}


def main() -> None:
    configure_logging()
    log.warning("starting")
    weather = get_weather()
    log.info("weather result %s", weather)
    currencies = get_currencies()
    log.info("currencies result %s", currencies)
    log.warning("finishing")


if __name__ == "__main__":
    main()
