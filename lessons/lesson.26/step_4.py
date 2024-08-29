import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather data")
    await asyncio.sleep(1.2)
    log.info("Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start getting currencies data")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()
    log.info("Starting step 4")

    coro_currencies = get_currencies()
    log.info(
        "%r coro: %s",
        coro_currencies.__name__,
        coro_currencies,
    )
    res = await asyncio.gather(
        get_weather(),
        coro_currencies,
    )
    weather_result, currencies_result = res
    log.info("Weather result: %s", weather_result)
    log.info("Currencies result: %s", currencies_result)

    log.info("Finished main")


if __name__ == "__main__":
    asyncio.run(main())
