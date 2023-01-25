from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session

DB_URL = 'sqlite:///users.sqlite3'
# DB_URL = 'postgresql+pg8000://username:passwd@localhost:5432/users' #psycopg2
DB_ECHO = False

engine = create_engine(url=DB_URL, echo=DB_ECHO)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    is_staff = Column(Boolean, default=False, nullable=True)
    create_at = Column(DateTime, default=datetime.utcnow())

    def __str__(self):
        return f'{self.username} {self.is_staff}'


def create_database():
    Base.metadata.create_all(engine)


def create_user(session, username, is_staff=False):
    user = User(username=username, is_staff=is_staff)
    session.add(user)
    session.commit()


def get_all_users(session):
    users = session.query(User).all()
    return users

def get_one_user(session, username):
    # Всегда первый элемент если нету то вернет None
    # return session.query(User).filter_by(username=username).first()
    # Возвращает 1 элемент, если там нет или больше одного то ошибка
    # return session.query(User).filter_by(username=username).one()
    # Первый элемент или None но если там > 1, то будет ошибка
    return session.query(User).filter_by(username=username).one_or_none()


def get_one_user_by_id(session, id):
    return session.get(User, id)


def update_user_username(session, user, username):
    user.username = username
    session.commit()


def delete_user(session, user):
    session.delete(user)
    session.commit()


def main():
    # create_database()

    session = Session()

    users = get_all_users(session)
    for user in users:
        delete_user(session, user)

    # 1. Создание пользователя
    create_user(session, 'leo')
    create_user(session, 'max', True)
    # 2. Выбор всех пользователей
    users = get_all_users(session)
    for user in users:
        print(user)

    # 3. Выбор одного пользователя (варианты)
    user = get_one_user(session, 'leo')
    print(user)
    user = get_one_user_by_id(session, user.id)
    print(user)
    # 4. Изменение пользователя
    update_user_username(session, user, 'kate')
    user = get_one_user_by_id(session, user.id)
    print('update users')
    print(user)
    # 5. Удаление пользователя
    delete_user(session, user)

    users = get_all_users(session)
    for user in users:
        print(user)

    session.close()


if __name__ == '__main__':
    main()