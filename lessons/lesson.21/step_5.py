import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
)
log = logging.getLogger(__name__)


async def get_user(user_id: int):
    log.info("get user %s", user_id)
    await asyncio.sleep(1)
    log.info("fetched user %s", user_id)
    return {"data": {"id": user_id}}


async def get_n_users(n_users: int):
    log.info("get %s users", n_users)
    tasks = {
        asyncio.create_task(get_user(user_id), name=f"u{user_id}")
        for user_id in range(1, n_users + 1)
    }
    await asyncio.wait(tasks)
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
