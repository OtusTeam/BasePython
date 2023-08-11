import random
import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_user(user_id: int) -> dict[str, int]:
    to_sleep = random.random()
    log.info("get user %02d, sleep %0.3f", user_id, to_sleep)
    # await asyncio.sleep(1)
    await asyncio.sleep(to_sleep)
    if random.random() > 0.7:
        log.info("create error on user %02d", user_id)
        raise ValueError(user_id)

    log.info("ok user %s", user_id)
    return {"user_id": user_id}


async def get_n_users(n_users: int):
    tasks = {
        asyncio.create_task(get_user(user_id=i), name=f"get-user-{i:03d}")
        for i in range(1, n_users + 1)
    }
    # await asyncio.gather(*tasks)
    done, pending = await asyncio.wait(tasks)

    for task in pending:  # type: asyncio.Task
        task.cancel()

    for task in done:  # type: asyncio.Task
        # try:
        #     res = task.result()
        # except ValueError as e:
        #     log.info("fsdfsdf")

        error = task.exception()
        if error:
            log.warning(
                "task %s got error %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        res = task.result()
        log.info("Result for task %s: %s", task.get_name(), res)


async def main():
    log.info("start main")
    await get_n_users(10)
    log.info("finish main")


def run_main():
    configure_logging()
    coro_main = main()
    log.info("main coro: %s", coro_main)
    asyncio.run(coro_main)


if __name__ == '__main__':
    run_main()
