from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
)


DB_URL = "postgresql+pg8000://username:passwd!@localhost:5432/blog"
DB_ECHO = False
engine = create_engine(url=DB_URL, echo=DB_ECHO)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f'{self.id}, {self.username}'


def create_database():
    Base.metadata.create_all()


def create_user(session, username):
    user = User(username=username)
    session.add(user)
    session.commit()


def get_all_users(session):
    return session.query(User).all()

def get_one_user_by_username(session, username):
    # Берет всегда одного или ошибка
    #user = session.query(User).filter_by(username=username).one()
    # Берет одного или возвращает None, если больше 1-го то будет ошибка
    user = session.query(User).filter_by(username=username).one_or_none()
    # Берет первого или возвращает None
    # user = session.query(User).filter_by(username=username).first()
    return user

def get_user_by_id(session, id):
    # user = session.query(User).filter_by(id=id).one_or_none()
    user = session.get(User, id)
    return user


def update_user(session, user, new_username):
    user.username = new_username
    session.commit()


def delete_user(session, user):
    session.delete(user)
    session.commit()

def main():
    create_database()
    # сессия
    session = Session()

    # создание объекта

    create_user(session, 'leo')
    create_user(session, 'max')

    # выборка объектов
    users = get_all_users(session)
    print(type(users))
    for user in users:
        print(user)
        print(type(user))
    # выбор одного
    user = get_one_user_by_username(session, 'leo')
    print(user)
    # редактирование
    update_user(session, user, 'newleleel')
    user = get_one_user_by_username(session, 'newleleel')
    print(user)

    user = get_user_by_id(session, 2)
    print(user)
    # удаление
    delete_user(session, user)
    # выборка объектов

    # закрыть сессию
    session.close()

if __name__ == '__main__':
    main()