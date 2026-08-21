import logging

from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather() -> dict:
    log.info("Getting weather data")
    # response = requests.get("https://www.openweathermap.org/query=Moscow")
    # data = response.json()
    sleep(1)
    log.info("got weather data")
    return {"weather": {"temperature": 18}}


def get_exchange() -> dict:
    log.info("Getting exchange data")
    # response = requests.get("https://www.openexchangemap.org/query=Moscow")
    # data = response.json()
    sleep(1)
    log.info("got exchange data")
    return {"exchange": {"rate": 2}}


def main() -> None:
    configure_logging()

    log.info("start")
    get_weather()
    get_exchange()
    log.info("end")


if __name__ == "__main__":
    main()
