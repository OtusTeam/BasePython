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
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


async def get_currencies():
    log.info("Start getting currencies")
    # просто имитируем. точное ожидание: примерно 1с
    # await asyncio.sleep(2)
    d = {}
    for n in range(9_000):
        d[n] = n**n
        if not n % 10:
            await asyncio.sleep(0)

    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 1.7}}


async def get_weather_and_currencies():
    log.info("Start getting weather and currencies")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    async with asyncio.timeout(1.1):
        weather, currencies = await asyncio.gather(
            get_weather(),
            currencies_coro,
        )

    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    return weather, currencies


async def main():
    configure_logging()
    log.info("Starting %s", NAME)

    try:
        weather, currencies = await get_weather_and_currencies()
    except TimeoutError:
        log.error("Timeout error getting weather and currencies")
    else:
        log.info(
            "The result: weather=%s, currencies=%s",
            weather,
            currencies,
        )

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
