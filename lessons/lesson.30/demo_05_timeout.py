import asyncio
import logging
import time
from pathlib import Path

from common import configure_logging


NAME = Path(__file__).stem

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # имитируем отправку настоящего запроса и ожидание ответа
    await asyncio.sleep(1)
    data = {"weather": {"rain-chance": 70}}
    log.info("Got weather")
    return data


async def get_currencies():
    log.info("Start getting currencies")
    # имитируем отправку настоящего запроса и ожидание ответа
    # await asyncio.sleep(1)
    # time.sleep(5)

    # нам из API вернулся большой массив данных
    # мы пытаемся этот массив обработать
    d = {}
    for n in range(10_000):
        d[n] = n**n
        if not n % 10:
            await asyncio.sleep(0)

    data = {"currencies": {"exchange-rate": 1.5}}
    log.info("Got currencies")
    return data


async def get_weather_and_currencies() -> tuple[dict, dict]:
    log.info("start getting weather and currencies")

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


async def main() -> None:
    configure_logging()
    log.info("Starting %s", NAME)

    try:
        weather, currencies = await get_weather_and_currencies()
    except TimeoutError:
        log.error("Timeout error when getting weather and currencies")
    else:
        log.info(
            "Results: weather=%s, currencies=%s",
            weather,
            currencies,
        )

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
