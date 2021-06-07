import pytest

# import homework package and skip the whole test if not available
homework = pytest.importorskip("homework_04")

import requests
from faker import Faker

from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

fake = Faker()

module_models = homework.models
module_main = homework.main
module_jsonplaceholder_requests = homework.jsonplaceholder_requests

pytestmark = pytest.mark.asyncio


def get_data(url):
    response = requests.get(url)
    return response.json()


@pytest.fixture(scope="module")
def users_data():
    return get_data(module_jsonplaceholder_requests.USERS_DATA_URL)


@pytest.fixture(scope="module")
def posts_data():
    return get_data(module_jsonplaceholder_requests.POSTS_DATA_URL)


def check_data_match(items_from_db, items_from_remote, args_mapping: dict):
    assert len(items_from_db) == len(items_from_remote)
    db_data = {
        item.id: [
            getattr(item, k)
            for k in args_mapping.keys()
        ]
        for item in items_from_db
    }
    remote_data = {
        item["id"]: [
            item[k]
            for k in args_mapping.values()
        ]
        for item in items_from_remote
    }
    assert db_data == remote_data


async def test_main(users_data, posts_data):
    await module_main.async_main()

    stmt_query_users = select(module_models.User).options(selectinload(module_models.User.posts))
    stmt_query_posts = select(module_models.Post).options(joinedload(module_models.Post.user))

    users = []
    posts = []

    async with module_models.Session() as session:
        # there're problems with asyncio.gather in pytest :/
        # res_users, res_posts = await asyncio.gather(
        #     session.execute(stmt_query_users),
        #     session.execute(stmt_query_posts),
        # )
        res_users = await session.execute(stmt_query_users)
        res_posts = await session.execute(stmt_query_posts)

        users.extend(res_users.scalars())
        posts.extend(res_posts.scalars())

    assert len(posts) == len(posts_data)

    check_data_match(users, users_data, args_mapping=dict(
        name="name",
        username="username",
        email="email",
    ))
    check_data_match(posts, posts_data, args_mapping=dict(
        user_id="userId",
        title="title",
        body="body",
    ))

    for post in posts:
        # check relationships
        assert post.user in users
        assert post in post.user.posts
