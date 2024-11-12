import asyncio
import logging
from dataclasses import dataclass
from random import random

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class UserData:
    id: int
    slept: float


async def get_user(user_id: int) -> UserData:
    sleep_time = random()
    log.info(
        "get user %02d, sleep %0.4f",
        user_id,
        sleep_time,
    )
    await asyncio.sleep(sleep_time)

    if random() < 0.3:
        log.warning("could not get user %02d, raise error", user_id)
        raise ValueError(user_id)

    log.info("got user %02d", user_id)
    return UserData(id=user_id, slept=sleep_time)


async def get_n_users(n_users: int) -> list[UserData]:
    log.info("Request %d users", n_users)
    tasks = {
        asyncio.create_task(
            # create coro to get user
            get_user(user_id=user_id),
            name=f"user-{user_id:02d}",
        )
        # create n tasks for n users
        for user_id in range(1, n_users + 1)
    }

    # res = await asyncio.gather(*tasks)
    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()
        log.info("Task %r cancelled", task.get_name())

    users_result: list[UserData] = []

    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed, error: %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        user_data: UserData = task.result()
        users_result.append(user_data)

    log.info("%d users result %s", n_users, users_result)
    return users_result


async def async_main() -> None:
    log.info("Start main 08 wait for many tasks")
    await get_n_users(n_users=100)
    log.info("Finished main 08 wait for many tasks")


def main() -> None:
    configure_logging()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
