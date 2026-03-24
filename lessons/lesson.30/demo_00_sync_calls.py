import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather():
    log.info("Start getting weather")
    # response = requests.get("https://api.openweathermap.org/data/2.5/weather?")
    # data = response.json()
    # нам нужен синтетический пример.
    # Мы не хотим зависеть от внешнего API,
    # мы хотим предсказуемое время ожидания.
    sleep(1)
    data = {
        "weather": {
            "sky": "cloudy",
            "temp": "5",
        },
    }
    log.info("Got weather")
    return data


def get_currencies():
    log.info("Start getting currencies")
    # response = requests.get("https://api.opencurrencies.org/data/2.5/currencies?")
    # data = response.json()
    # нам нужен синтетический пример.
    # Мы не хотим зависеть от внешнего API,
    # мы хотим предсказуемое время ожидания.
    sleep(1)
    data = {
        "currencies": {
            "exchange-rate": 2,
        },
    }
    log.info("Got currencies")
    return data


def main():
    configure_logging()
    log.info("Starting")
    weather = get_weather()
    log.info("weather result: %s", weather)
    currencies = get_currencies()
    log.info("currencies result: %s", currencies)
    log.info("Finishing")


if __name__ == "__main__":
    main()
