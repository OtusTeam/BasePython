import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
    # format="[{asctime}] {module:>15}:{lineno} {levelname:>8} - {message}",
    # style="{",
)
log = logging.getLogger(__name__)

stop = object()


async def producer(queue: asyncio.Queue, n_items: int):
    """
    produce new items

    :param queue:
    :param n_items:
    :return:
    """
    for i in range(1, n_items + 1):
        log.info("🔨 Start producing item %s", i)
        # call to database / api
        # ex: fetch data
        await asyncio.sleep(0.1)
        item = {"id": i}
        log.info("🛠️ Produced item %s", item)
        await queue.put(item)

    await queue.put(stop)
    log.info("✋ Done producing, stopped")


async def consumer(queue: asyncio.Queue):
    """
    Consume generated items

    :param queue:
    :return:
    """
    while True:
        item = await queue.get()
        if item is stop:
            break
        # call to database / api
        # ex: create data
        log.info("🍽️ Start consuming item %s", item)
        await asyncio.sleep(0.2)
        log.info("💤 Consumed item %s", item)

    log.info("✅ Done consuming")


async def main():
    log.warning("Start")
    queue = asyncio.Queue()

    await asyncio.gather(
        producer(queue, n_items=10),
        consumer(queue),
    )
    # await producer(queue, n_items=10)
    # await consumer(queue)
    log.warning("End")


if __name__ == "__main__":
    asyncio.run(main())
