"""
Connection: <sqlalchemy.engine.base.Connection object at 0x1027855e0>
2024-10-25 20:42:50,229 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-25 20:42:50,229 INFO sqlalchemy.engine.Engine SELECT 1 + 2
2024-10-25 20:42:50,229 INFO sqlalchemy.engine.Engine [generated in 0.00017s] ()
Result: 3
2024-10-25 20:42:50,230 INFO sqlalchemy.engine.Engine ROLLBACK
"""

from sqlalchemy import text

from db import engine


def demo_engine():
    with engine.connect() as connection:
        print("Connection:", connection)
        res = connection.execute(text("SELECT 1 + 2"))
        print("Result:", res.scalar())
        # res = connection.execute(text("SELECT 1 where :val"), val=true())


def main():
    demo_engine()


if __name__ == "__main__":
    main()
