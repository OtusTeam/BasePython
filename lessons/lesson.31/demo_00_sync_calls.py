import logging
from pathlib import Path
from time import sleep

from common import configure_logging

NAME = Path(__file__).stem
log = logging.getLogger(NAME)


def get_weather():
    log.info("Start getting weather")
    # response = requests.get("https://openweathermap.org/current")
    # data = response.json()
    # реальный запрос во внешний мир
    # получаем примерно такие данные
    sleep(1)
    data = {
        "weather": {
            "sky": "sunny",
            "rain-chance": 10,
        },
    }
    log.info("Got weather")
    return data


def get_currencies():
    log.info("Start getting currencies")
    # response = requests.get("https://opencurrenciesmap.org/current")
    # data = response.json()
    # реальный запрос во внешний мир
    # получаем примерно такие данные
    sleep(1)
    data = {
        "currencies": {
            "exchange-rate": 1.5,
        },
    }
    log.info("Got currencies")
    return data


def main() -> None:
    configure_logging()
    log.info("Starting")

    weather = get_weather()
    log.info("Weather result: %s", weather)
    currencies = get_currencies()
    log.info("Currencies result: %s", currencies)

    log.info("Finishing")


if __name__ == "__main__":
    main()
