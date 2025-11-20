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
    # await asyncio.sleep(1)
    # await asyncio.sleep(10)
    # await to get data from API / DB
    d = {}
    for n in range(10_000):
        d[n] = n**n
        if not n % 10:
            await asyncio.sleep(0)
    log.info("processed d size: %s", len(d))

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


async def get_weather_and_currencies() -> tuple[dict, dict]:
    log.info("Start getting weather and currencies")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    async with asyncio.timeout(1.01):
        weather, currencies = await asyncio.gather(
            get_weather(),
            currencies_coro,
        )

    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    return weather, currencies


async def main() -> None:
    configure_logging()
    log.info("Starting")

    try:
        weather, currencies = await get_weather_and_currencies()
    except TimeoutError:
        log.error("Timeout error while getting weather and currencies")
    else:
        log.info(
            "Results: weather=%s, currencies=%s",
            weather,
            currencies,
        )

    log.info("Finishing")


if __name__ == "__main__":
    asyncio.run(main())
