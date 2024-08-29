import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather data")
    await asyncio.sleep(1)
    log.info("Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start getting currencies data")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()
    log.info("Starting step 3")

    coro_currencies = get_currencies()
    log.info(
        "%r coro: %s",
        coro_currencies.__name__,
        coro_currencies,
    )
    log.info("Weather result: %s", await get_weather())
    currencies_result = await coro_currencies
    log.info("Currencies result: %s", currencies_result)

    log.info("Finished main")


if __name__ == "__main__":
    asyncio.run(main())
