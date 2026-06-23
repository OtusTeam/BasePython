import asyncio
import logging

from common import configure_logging


log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Getting weather data")
    # await asyncio.sleep(1.001)
    # url = "https://openweathermap.org?city=Moscow"
    # async with httpx.AsyncClient() as client:
    #     await client.get(url)
    # response = requests.get(url)

    d = {}
    for n in range(9_000):
        d[n] = n**n
        # if not n % 10:
        await asyncio.sleep(0)

    log.info("len of d: %d", len(d))

    log.info("fetched weather data")
    return {"weather": {"temperature": 23}}


async def get_currencies(currency: str) -> dict:
    log.info("Getting currency %r data", currency)
    await asyncio.sleep(1)
    log.info("fetched currency %r data", currency)
    return {"currencies": {"rate": 42}, "currency": currency}


async def get_weather_and_currencies(
    timeout: float = 1.01,
) -> tuple[dict, dict]:

    async with asyncio.timeout(timeout):  # № 3
        weather, currencies, _ = await asyncio.gather(  # № 4
            get_weather(),  # № 5
            get_currencies("FOO"),  # № 6
            get_currencies("BAR"),  # № 7
        )

    return weather, currencies


async def main() -> None:
    configure_logging()
    log.warning("starting")

    try:
        weather, currencies = await get_weather_and_currencies()
    except TimeoutError:
        log.warning("too long waiting for results")
    else:
        log.info("weather result %s", weather)
        log.info("currencies result %s", currencies)

    log.warning("finishing")


if __name__ == "__main__":
    asyncio.run(main())
