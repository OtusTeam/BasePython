import asyncio
import logging
import threading

from common import configure_logging

log = logging.getLogger(__name__)


async def request_api():
    """
    Делаем запрос на какой-то настоящий API по сети
    """
    await asyncio.sleep(1)


async def get_weather():
    log.info(
        "Getting weather... thread %s",
        threading.current_thread().ident,
    )
    # await request_api()
    await asyncio.sleep(1.00005)
    # await asyncio.sleep(1.001)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


async def get_currencies():
    log.info(
        "Getting currencies... thread %s",
        threading.current_thread().ident,
    )
    await request_api()
    #     await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rates": [42, 13]}}


async def main():
    configure_logging()

    log.warning(
        "Starting 03 thread %s, event loop %s",
        threading.current_thread().ident,
        asyncio.get_running_loop(),
    )

    coro = get_currencies()
    log.info("created coro for currencies %s", coro)

    log.info("Get values")
    weather_result, currencies_result, _ = await asyncio.gather(
        get_weather(),
        coro,
        get_currencies(),
    )
    log.info("weather result: %s", weather_result)
    log.info("currencies result: %s", currencies_result)

    log.warning("Finished 03")


if __name__ == "__main__":
    asyncio.run(main())
