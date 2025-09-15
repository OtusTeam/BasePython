import logging
from pathlib import Path
from time import sleep

from common import configure_logging


NAME = Path(__file__).stem

log = logging.getLogger(__name__)


def get_weather():
    log.info("Start getting weather")
    # response = requests.get("https://openweathermap.org/current")
    # data = response.json()
    # вместо реального запроса во внешний мир мы делаем синтетическое ожидание
    # в реальном коде никогда не должно быть никаких time.sleep()
    sleep(1)
    data = {"weather": {"rain-chance": 70}}
    log.info("Got weather")
    return data


def get_currencies():
    log.info("Start getting currencies")
    # вместо реального запроса во внешний мир мы делаем синтетическое ожидание
    # в реальном коде никогда не должно быть никаких time.sleep()
    sleep(1)
    data = {"currencies": {"exchange-rate": 1.5}}
    log.info("Got currencies")
    return data


def main() -> None:
    configure_logging()
    log.info("Starting %s", NAME)

    weather = get_weather()
    log.info("Weather result: %s", weather)
    currencies = get_currencies()
    log.info("Currencies result: %s", currencies)

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    main()
