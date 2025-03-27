import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def request_api():
    """
    Делаем запрос на какой-то настоящий API по сети
    """
    log.info("requesting api...")
    await asyncio.sleep(1)


async def get_weather():
    log.info("Getting weather...")
    await asyncio.sleep(0.5)
    await request_api()
    # await asyncio.sleep(1.001)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


async def get_currencies():
    log.info("Getting currencies...")
    await request_api()
    #     await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rates": [42, 13]}}


async def main():
    configure_logging()

    log.warning("Starting 04")

    coro = get_currencies()
    log.info("created coro for currencies %s", coro)

    log.info("Get values")
    async with asyncio.TaskGroup() as tg:
        weather_task = tg.create_task(get_weather())
        currencies_task = tg.create_task(coro)
        log.info(
            "weather_task done? %s, %s",
            weather_task.done(),
            weather_task,
        )
        log.info(
            "currencies_task done? %s, %s",
            currencies_task.done(),
            currencies_task,
        )
        await asyncio.sleep(0.5)
        log.info("after sleep 0.5")
        await asyncio.sleep(0.51)

        log.info(
            "weather_task done? %s, %s",
            weather_task.done(),
            weather_task,
        )
        log.info(
            "currencies_task done? %s, %s",
            currencies_task.done(),
            currencies_task,
        )

    log.info("just after tg")

    weather_result = weather_task.result()
    currencies_result = currencies_task.result()
    log.info("weather result: %s", weather_result)
    log.info("currencies result: %s", currencies_result)

    log.warning("Finished 04")


if __name__ == "__main__":
    asyncio.run(main())
