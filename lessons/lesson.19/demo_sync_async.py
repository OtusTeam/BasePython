import asyncio
import logging
from time import sleep

DEFAULT_FORMAT = "%(asctime)s %(levelname)-8s [%(name)-8s] (%(filename)s:%(funcName)s:%(lineno)d) %(message)s"

logging.basicConfig(format=DEFAULT_FORMAT, level=logging.DEBUG)

log = logging.getLogger(__name__)


def do_some_db_query_sync():
    sleep(.1)


async def do_some_db_query_async(to_sleep=0.1):
    await asyncio.sleep(to_sleep)
    # sleep(.1)


def foo_sync():
    log.info("foo_sync start")
    do_some_db_query_sync()
    log.info("foo_sync finish")


def bar_sync():
    log.info("bar_sync start")
    do_some_db_query_sync()
    log.info("bar_sync finish")


async def foo():
    log.info("foo start")
    await do_some_db_query_async()
    log.info("foo finish")


async def bar():
    log.info("bar start")
    # await do_some_db_query_async(0.101)
    await do_some_db_query_async(0.11)
    log.info("bar finish")


def run_main_sync():
    log.info("starting sync calls")
    foo_sync()
    bar_sync()
    log.info("finishing sync calls")


async def run_main():
    log.info("starting async calls")
    await foo()
    await bar()
    log.info("finishing async calls")


async def run_main_concurrent():
    log.info("starting conc async calls")
    # await asyncio.gather(foo(), bar(), foo(), bar())
    await asyncio.gather(bar(), bar(), foo(), foo(), bar())
    log.info("finishing conc async calls")


async def get_users_profile_pic(user_id):
    log.info("start fetching users_profile_pic")
    await asyncio.sleep(.1)
    log.info("finish fetching users_profile_pic")
    return b"abc"


async def get_users_close_friends(user_id):
    log.info("start fetching users_close_friends")
    await asyncio.sleep(.2)
    log.info("finish fetching users_close_friends")
    return {"user_id": user_id, "friends": [{"id": 1, "name": "Sam"}, {"id": 2, "name": "Ann"}]}


async def load_users_data():
    log.info("starting user data async calls")
    user_id = 123
    coro = get_users_profile_pic(user_id)
    log.info("coro %s", coro)
    # profile_pic = await coro
    # close_friends = await get_users_close_friends()

    foo_res, profile_pic, close_friends = await asyncio.gather(foo(), coro, get_users_close_friends(user_id))
    log.info("finishing user data async calls")
    log.info("profile_pic %s", profile_pic)
    log.info("close_friends %s", close_friends)


def main():
    # run_main_sync()
    # asyncio.run(run_main())
    # asyncio.run(run_main_concurrent())
    asyncio.run(load_users_data())


if __name__ == '__main__':
    main()

