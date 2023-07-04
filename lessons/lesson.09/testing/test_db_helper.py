from pytest import fixture

from db_helper import (
    get_engine,
    get_connection,
    Engine,
    Connection,
)


# @fixture(scope="module")
@fixture(scope="function")
def url_default():
    # print("create url default")
    return object()


@fixture()
def url_custom():
    return object()


@fixture()
def engine_default(url_default) -> Engine:
    return get_engine(url=url_default)


@fixture()
def conn_default(engine_default) -> Connection:
    # return get_connection(engine=engine_default)
    conn = get_connection(engine=engine_default)
    yield conn
    conn.close()


def test_another_bound(url_default, conn_default):
    # print("test_another_bound", url_default)

    assert isinstance(conn_default, Connection)
    assert conn_default.engine.url is url_default


def test_fixtures_bound(
    url_default,
    url_custom,
    engine_default,
    conn_default,
):
    # print("test_fixtures_bound", url_default)
    assert url_custom is not url_default
    assert isinstance(conn_default, Connection)
    assert conn_default.engine.url is url_default
    assert isinstance(engine_default, Engine)
    assert engine_default.url is url_default
    assert conn_default.engine is engine_default
