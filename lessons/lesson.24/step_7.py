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
    d = {}
    for i in range(7_000):
        d[i] = i**i
        if i % 100 == 0:
            await asyncio.sleep(0)
    log.info("For real get currencies")
    await asyncio.sleep(0.5)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()
    log.info("Start step 7")

    coro_currencies = get_currencies()

    async with asyncio.TaskGroup() as tg:
        tg.create_task(coro_currencies)
        tg.create_task(get_weather())

    log.info("End step 7")


if __name__ == "__main__":
    asyncio.run(main())
