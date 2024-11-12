import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_currencies() -> dict:
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def async_main() -> None:
    log.info("Start main 02")

    currencies_coro = get_currencies()
    log.info("get currencies coro: %s", currencies_coro)

    weather = await get_weather()
    log.info("Weather result: %s", weather)

    currencies = await currencies_coro
    log.info("Currencies result: %s", currencies)

    log.info("Finished main 02")


def main() -> None:
    configure_logging()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
