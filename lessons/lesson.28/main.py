# from models import Base
from models import Base

# import models


def main() -> None:
    print(Base.metadata.tables.keys())
    # print(models.Base.metadata.tables.keys())
    # print(Base.metadata.create_all(engine))


if __name__ == "__main__":
    main()
