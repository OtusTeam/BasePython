import pytest
import requests
from faker import Faker

fake = Faker()

homework = pytest.importorskip("homework_03")
module_models = homework.models
module_main = homework.main
module_jsonplaceholder_requests = homework.jsonplaceholder_requests


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


def test_main(users_data, posts_data):
    module_main.main()
    session = module_models.Session()
    users = session.query(module_models.User).all()
    posts = session.query(module_models.Post).all()

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
