from contextlib import contextmanager


@contextmanager
def create_session():
    sess = object
    print("created session", sess)
    try:
        yield sess
    finally:
        print("close session", sess)


def main():
    with create_session() as sess:
        print("query session", sess)
        print("something else", sess)
        # 1 / 0
    print("done")
    # g = create_session()
    # session = next(g)
    # print(session)
    # print("query session", session)
    # next(g)
    # print("close session", session)
    # session.close()


if __name__ == "__main__":
    main()
