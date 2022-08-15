import asyncio

from loguru import logger


async def foo():
    logger.info("Start async foo")
    await asyncio.sleep(1)
    logger.info("Finish async foo")


async def bar():
    logger.info("Start async bar")
    await asyncio.sleep(1.0001)
    logger.info("Finish async bar")


def generate_sleep_time(task_id: int) -> float:
    # sleep(1)
    # requests.get(...)

    to_sleep = 1.0

    if task_id % 5 == 0:
        is_add = (task_id // 10) % 2 == 0
        to_sleep += (task_id / 1000) * (1 if is_add else -1)

    return to_sleep


async def some_func(task_id: int):
    # to_sleep = 1
    # to_sleep = 0.1234
    to_sleep = generate_sleep_time(task_id)
    logger.info("Start task #{:4d} and sleep {:.3f}", task_id, to_sleep)
    await asyncio.sleep(to_sleep)
    logger.info("Finish task #{:4d}", task_id)


async def run_many_tasks():
    tasks = {
        asyncio.create_task(
            some_func(task_id)
        )
        for task_id in range(1, 125)
    }
    coro = asyncio.wait(tasks)
    logger.info("wait for tasks")
    await coro
    logger.info("all tasks done")


async def run_by_one():
    # await foo()
    # await bar()
    coro = foo()
    await bar()
    await coro


async def error():
    1/0


async def main():
    logger.info("Starting main")
    # # await run_by_one()
    # await asyncio.gather(foo(), bar(), foo(), bar(), foo())
    # await run_many_tasks()
    # logger.info("Finishing main")

    task = asyncio.create_task(error())
    done, pending = await asyncio.wait({task})
    for task in done:
        exc = task.exception()
        logger.opt(exception=exc).info("There was an error!")

    logger.info("done")


if __name__ == '__main__':
    asyncio.run(main())
