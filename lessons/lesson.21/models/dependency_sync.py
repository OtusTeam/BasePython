from . import Session


def get_session():
    session = Session()
    yield session
    try:
        session.close()
    except:
        pass
