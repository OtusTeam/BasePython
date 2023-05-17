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
    await asyncio.sleep(1)
    log.info("fetched users")
    return {"users": []}


async def get_weather():
    log.info("get weather")
    await asyncio.sleep(1)
    log.info("fetched weather")
    return {"weather": {}}


async def main():
    log.info("Start")
    users, weather = await asyncio.gather(
        get_users(),
        get_weather(),
    )
    log.info("users: %s", users)
    log.info("weather: %s", weather)
    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
