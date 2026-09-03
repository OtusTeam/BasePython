from sqlalchemy import (
    create_engine,
    text,
    select,
    func,
)

engine = create_engine(
    "sqlite:///:memory:",
    echo=True,  # debug flag!
)

with engine.connect() as conn:
    res = conn.execute(text("select 1 + 2, 3 + 4;"))
    print(res.fetchall())

    username = "bob"
    res = conn.execute(
        select(text(":name")),
        {"name": username},
    )
    print(res.fetchall())

    some_text = "Hello THERE!"

    res = conn.execute(
        text("select lower(:text)"),
        {"text": some_text},
    )
    print(res.fetchall())

    res = conn.execute(
        select(
            func.lower(some_text).label("lower_text"),
            text("1 + 2 as total"),
        ),
    )
    # print(res.scalars().all())
    # print(res.scalar())
    result = res.one()
    print(result.lower_text)
    print(result.total)
