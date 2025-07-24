import asyncio

import logging
from pathlib import Path

from common import configure_logging

NAME = Path(__file__).stem

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # имитация получения погоды
    # response = requests.get("https://openwerathermap.org/api?key=")
    # просто имитируем. точное ожидание: примерно 1с
    await asyncio.sleep(1.01)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


async def get_currencies():
    log.info("Start getting currencies")
    # просто имитируем. точное ожидание: примерно 1с
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 1.7}}


async def main():
    configure_logging()
    log.info("Starting %s", NAME)

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    weather, currencies = await asyncio.gather(
        get_weather(),
        currencies_coro,
    )

    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
