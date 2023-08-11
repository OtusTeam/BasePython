import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("get weather")
    # wait for weather
    # TODO: real API call
    await asyncio.sleep(1)
    log.info("done get weather")
    return {"weather": {"moscow": {}}}


async def get_currencies():
    log.info("get currencies")
    # wait for currencies
    # TODO: real API call
    await asyncio.sleep(1)
    log.info("done get currencies")
    return {"currencies": [3, 4, 5]}


async def get_calendar():
    await asyncio.sleep(0)
    return {"calendar": [1, 2, 3]}


async def main():
    log.info("start main")
    # cal = await get_calendar()
    # log.info("calendar %s", cal)
    coro = get_weather()

    async with asyncio.TaskGroup() as tg:
        task_weather = tg.create_task(coro)
        task_currencies = tg.create_task(get_currencies())
        # log.info("one line in tg")
        # await asyncio.sleep(0)
        log.info("last line in tg")
    log.info("first line after tg")
    # loop = asyncio.get_running_loop()
    # loop.call_soon()
    # loop.call_at()
    # loop.call_later()
    weather = task_weather.result()
    log.info("weather %s", weather)
    currencies = task_currencies.result()
    log.info("currencies %s", currencies)

    log.info("finish main")


def run_main():
    configure_logging()
    coro_main = main()
    log.info("main coro: %s", coro_main)
    asyncio.run(coro_main)


if __name__ == '__main__':
    run_main()
