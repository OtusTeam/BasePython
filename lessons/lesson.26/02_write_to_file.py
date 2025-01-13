from sqlalchemy import text

from common import engine


def main():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1 + 2"))
        print(result.scalar())

        conn.execute(text("CREATE TABLE users (user_id integer, name varchar);"))
        conn.execute(
            text("INSERT INTO users (user_id, name) VALUES (:user_id, :name)"),
            [
                {"user_id": 1, "name": "Bob"},
                {"user_id": 2, "name": "Alice"},
            ],
        )
        conn.commit()


if __name__ == "__main__":
    main()
