from sqlalchemy import (
    select,
    create_engine,
    MetaData,
)

import config

engine = create_engine(
    "sqlite:///blog-app.db",
    echo=config.SQLA_DB_ECHO,
)

metadata = MetaData()


def main() -> None:
    print(metadata.tables)
    metadata.reflect(bind=engine)
    print(metadata.tables)
    users_table = metadata.tables["users"]
    print({"table info": users_table})

    statement = select(users_table).order_by(users_table.c.id)
    with engine.connect() as conn:
        result = conn.execute(statement)

    for row in result:
        print(row)
        print(row.id, row.username, row.email, row.full_name)
        # print(row[0], row[1], row[2], row[3])


if __name__ == "__main__":
    main()
