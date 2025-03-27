import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_currencies():
    log.info("Getting currencies...")
    await asyncio.sleep(0.5)
    log.info("Got currencies")
    return {"currencies": {"exchange-rates": [42, 13]}}


async def get_data(n):
    await asyncio.sleep(0)
    return range(n)


async def process_many_items(n_items: int):
    data = await get_data(n_items)
    d = {}
    log.info("Processing %d items...", n_items)
    for val in data:
        # if not val % 10:
        await asyncio.sleep(0)
        if not val % 1000:
            log.info("Processing item %s", val)
        d[val] = val**val
    log.info("done processing %d items...", n_items)
    return d


async def main():
    configure_logging()

    log.warning("Starting 05")

    async with asyncio.TaskGroup() as tg:
        tg.create_task(get_currencies())
        tg.create_task(process_many_items(6000))

    log.warning("Finished 05")


if __name__ == "__main__":
    asyncio.run(main())
