import asyncio
import logging
import random

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    # level=logging.WARNING,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


async def get_user(user_id):
    to_sleep = 0.5 + random.random()
    log.info("start get user %2d, wait %.3f", user_id, to_sleep)
    await asyncio.sleep(to_sleep)
    if random.random() > 0.5:
        log.warning("divide user %s", user_id)
        user_id / 0
    log.info("stop get user %2d", user_id)
    return {"user": {"id": user_id}}


async def get_users(n_users):
    log.info("fetch %s users", n_users)
    tasks = {
        asyncio.create_task(
            get_user(user_id),
            name=f"get-user-{user_id:02d}",
        )
        for user_id in range(1, n_users + 1)
    }

    # done = Tasks that are done
    # pending = Tasks that are pending

    done, pending = await asyncio.wait(tasks)

    log.info("process done tasks")
    for task in done:  # type: asyncio.Task
        error = task.exception()
        if error:
            # log.warning("task %s error %s", task.get_name(), error, exc_info=error)
            log.warning("task %s error %s", task.get_name(), error)
            continue
        result = task.result()
        log.info("task %s result %s", task.get_name(), result)

    for task in pending:  # type: asyncio.Task
        task.cancel()

    # await asyncio.gather(*tasks)

    log.info("done fetching users")


async def main():
    await get_users(10)


if __name__ == "__main__":
    asyncio.run(main())
