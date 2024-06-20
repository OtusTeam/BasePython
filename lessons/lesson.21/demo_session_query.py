from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.orm import Session

from db import engine


def example_calc(session: Session):
    result = session.execute(select(1))

    # all: [(1,)]
    # print("all:", result.all())
    # one: (1,)
    # print("one:", result.one())
    # scalar: 1
    print("scalar:", result.scalar())

    # SELECT 1 + 2
    result = session.execute(select(text("1 + 2")))
    print(result.scalar())


SQL = """
SELECT now() AS "current-time";
SELECT gen_random_uuid() AS "random-uuid";
SELECT to_jsonb('foo'::VARCHAR) AS to_jsonb_1;
"""


def demo_func(session: Session):
    result = session.execute(select(func.now().label("current-time")))
    # now: 2024-06-20 18:10:14.650608+00:00
    print("now:", result.scalar())

    result = session.execute(select(func.gen_random_uuid().label("random-uuid")))
    # uuid: 810461b6-199e-4300-b9c5-ba0a1d1488eb
    print("uuid:", result.scalar())

    result = session.execute(select(func.to_jsonb("foo")))
    # jsonb foo: 'foo'
    print("jsonb foo:", repr(result.scalar()))


def demo_session():
    with Session(engine) as session:
        example_calc(session)
        demo_func(session)


if __name__ == "__main__":
    demo_session()
