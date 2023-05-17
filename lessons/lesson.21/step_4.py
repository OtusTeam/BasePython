import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
)
log = logging.getLogger(__name__)


async def get_users():
    log.info("get users")
    # await asyncio.sleep(1)
    # sleep(0.001)
    for u in range(1, 5):
        log.info("u: %s *** %s = %s", u, u, u ** u ** u)
        # if u % 2 == 0:
        await asyncio.sleep(0.001)
    log.info("fetched users")
    return {"users": []}


async def get_weather():
    log.info("get weather")
    # await asyncio.sleep(1)
    for w in range(1, 50):
        log.info("w %s ** 2 = %s", w, w ** 2)
        await asyncio.sleep(0)
    log.info("fetched weather")
    return {"weather": {}}


async def main():
    log.info("Start")
    users, weather, u2 = await asyncio.gather(
        get_users(),
        get_weather(),
        get_users(),
    )
    log.info("users: %s", users)
    log.info("weather: %s", weather)
    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
