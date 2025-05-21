import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # await asyncio.sleep(5)
    d = {}
    for n in range(9_000):
        d[n] = n**n
        if not n % 10:
            await asyncio.sleep(0)

    log.info("Got weather")
    return {"weather": {"rain_chance": 20}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def get_weather_and_currencies():
    log.info("Start getting weather and currencies")

    currencies_coro = get_currencies()
    log.info("created currencies coro: %s", currencies_coro)

    async with asyncio.timeout(1.1):
        weather, currencies = await asyncio.gather(
            get_weather(),
            currencies_coro,
        )

    log.info("weather result: %s", weather)
    log.info("currencies result: %s", currencies)
    return weather, currencies


async def main() -> None:
    configure_logging()
    log.info("Starting 05")

    try:
        weather, currencies = await get_weather_and_currencies()
    except TimeoutError:
        log.error("Timeout error getting weather and currencies")
    else:
        log.info("got weather result: %s", weather)
        log.info("got currencies result: %s", currencies)

    log.info("Finished 05")


if __name__ == "__main__":
    asyncio.run(main())
