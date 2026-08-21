import logging

import asyncio

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather(city: str) -> dict:
    log.info("Getting weather data for %s", city)
    # response = await httpx.get("https://www.openweathermap.org/query=Moscow")
    await asyncio.sleep(1)
    log.info("got weather data for %s", city)
    return {"weather": {"temperature": 18}, "city": city}


async def get_exchange() -> dict:
    log.info("Getting exchange data")
    # response = await httpx.get("https://www.openexchangemap.org/query=Moscow")
    await asyncio.sleep(1.0001)
    log.info("got exchange data")
    return {"exchange": {"rate": 2}}


async def fetch_user_city(user_id: int) -> str:
    log.info("fetching user's city for %r", user_id)
    await asyncio.sleep(0.5)
    log.info("got user's city for %r", user_id)
    return "Moscow"


async def main() -> None:
    configure_logging()

    log.info("start")

    async with asyncio.TaskGroup() as tg:
        log.info("tg start")
        exchange_task = tg.create_task(get_exchange())
        log.info("tg exchange task: %s", exchange_task)
        city = await fetch_user_city(123)
        weather_task = tg.create_task(get_weather(city))
        log.info("tg weather task: %s", weather_task)
        # await asyncio.sleep(0.5)
    # log.info("exchange task: %s", exchange_task)
    # log.info("weather task: %s", weather_task)
    log.info("tg done")

    exchange = exchange_task.result()
    weather = weather_task.result()

    log.info("weather: %s", weather)
    log.info("exchange: %s", exchange)
    log.info("end")


if __name__ == "__main__":
    asyncio.run(main())
