import asyncio
import logging
from pathlib import Path

from common import configure_logging


NAME = Path(__file__).stem

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # имитируем отправку настоящего запроса и ожидание ответа
    await asyncio.sleep(1.001)
    data = {"weather": {"rain-chance": 70}}
    log.info("Got weather")
    return data


async def get_currencies():
    log.info("Start getting currencies")
    # имитируем отправку настоящего запроса и ожидание ответа
    await asyncio.sleep(1)
    data = {"currencies": {"exchange-rate": 1.5}}
    log.info("Got currencies")
    return data


async def main() -> None:
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
