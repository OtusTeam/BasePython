import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1.0001)
    log.info(f"Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info(f"Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()
    log.info("Start step 5")

    coro_currencies = get_currencies()
    log.info("Coro get currencies: %s", coro_currencies)

    async with asyncio.TaskGroup() as tg:
        task_get_weather = tg.create_task(get_weather())
        task_coro_currencies = tg.create_task(coro_currencies)

    res_weather = task_get_weather.result()
    res_currencies = task_coro_currencies.result()
    log.info("Res get weather: %s", res_weather)
    log.info("Res get currencies: %s", res_currencies)

    log.info("End step 5")


if __name__ == "__main__":
    asyncio.run(main())
