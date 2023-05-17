import asyncio
import logging
from random import random

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
)
log = logging.getLogger(__name__)


async def get_user(user_id: int):
    to_sleep = 0.5 + random()
    log.info("get user %s, sleep for %.4f", user_id, to_sleep)
    await asyncio.sleep(to_sleep)
    if random() > 0.5:
        log.warning("error user %s", user_id)
        user_id / 0
    log.info("fetched user %s", user_id)
    return {"data": {"id": user_id}}


async def get_n_users(n_users: int):
    log.info("get %s users", n_users)
    tasks = {
        asyncio.create_task(get_user(user_id), name=f"u{user_id}")
        for user_id in range(1, n_users + 1)
    }
    done, pending = await asyncio.wait(tasks)

    for task in pending:  # type: asyncio.Task
        # if task.get_name() == '...':
        #     task.cancel()
        task.cancel()

    for task in done:
        error = task.exception()
        if error:
            log.warning(
                "task %s error %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        result = task.result()
        log.info("task %s result %s", task.get_name(), result)

    # await asyncio.gather(*tasks)
    log.info("done %s users", n_users)


async def main():
    log.info("Start")
    # users = await asyncio.gather(
    #     get_user(1),
    #     get_user(2),
    # )
    # log.info("users: %s", users)

    # tasks = {
    #     asyncio.create_task(get_user(1), name="u1"),
    #     asyncio.create_task(get_user(2), name="u2"),
    # }
    # log.info("tasks prepared %s", tasks)
    # res = await asyncio.wait(tasks)
    # log.info("tasks done %s", tasks)
    # log.info("res: %s", res)

    await get_n_users(10)

    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
