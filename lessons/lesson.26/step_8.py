import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather data")
    await asyncio.sleep(1)
    log.info("Done, got weather")


async def main():
    configure_logging()
    log.info("Starting step 8 - await future")

    # never! fire and forget is discouraged!
    asyncio.create_task(get_weather())

    await asyncio.Future()

    log.info("Finished main")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Bye bye!")
