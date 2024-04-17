import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info(f"Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info(f"Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()
    log.info("Start step 2")

    coro_currencies = get_currencies()
    log.info("Coro get currencies: %s", coro_currencies)
    res_weather = await get_weather()
    log.info("Res get weather: %s", res_weather)
    res_currencies = await coro_currencies
    log.info("Res get currencies: %s", res_currencies)

    log.info("End step 2")


if __name__ == "__main__":
    asyncio.run(main())
