from models import Base

from models.db import engine


def main():
    print(Base.metadata.tables)
    Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
