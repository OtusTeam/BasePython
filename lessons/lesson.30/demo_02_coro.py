import asyncio
import logging
from pathlib import Path

from common import configure_logging

NAME = Path(__file__).stem
log = logging.getLogger(NAME)


async def get_weather():
    log.info("Start getting weather")
    # response = async ... get("https://openweathermap.org/current")
    # data = async get ... response.json()
    # реальный асинхронный запрос во внешний мир
    # получаем примерно такие данные
    await asyncio.sleep(1)
    data = {
        "weather": {
            "sky": "sunny",
            "rain-chance": 10,
        },
    }
    log.info("Got weather")
    return data


async def get_currencies():
    log.info("Start getting currencies")
    # response = requests.get("https://opencurrenciesmap.org/current")
    # data = response.json()
    # реальный запрос во внешний мир
    # получаем примерно такие данные
    await asyncio.sleep(1)
    data = {
        "currencies": {
            "exchange-rate": 1.5,
        },
    }
    log.info("Got currencies")
    return data


async def main() -> None:
    configure_logging()
    log.info("Starting")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    weather = await get_weather()
    log.info("Weather result: %s", weather)
    currencies = await currencies_coro
    log.info("Currencies result: %s", currencies)

    log.info("Finishing")


if __name__ == "__main__":
    asyncio.run(main())
