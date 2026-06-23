import asyncio
import logging

from common import configure_logging


log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Getting weather data")
    await asyncio.sleep(1.001)
    log.info("fetched weather data")
    return {"weather": {"temperature": 23}}


async def get_currencies() -> dict:
    log.info("Getting currencies data")
    await asyncio.sleep(1)
    log.info("fetched currencies data")
    return {"currencies": {"rate": 42}}


async def main() -> None:
    configure_logging()
    log.warning("starting")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    weather, currencies = await asyncio.gather(
        get_weather(),
        currencies_coro,
    )
    log.info("weather result %s", weather)
    log.info("currencies result %s", currencies)

    log.warning("finishing")


if __name__ == "__main__":
    asyncio.run(main())
