from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Boolean

engine = create_engine("sqlite:///example.db")
metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False),
)

if __name__ == "__main__":
    metadata.create_all(engine)
