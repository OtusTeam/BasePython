from sqlalchemy import Column, Integer, String, ForeignKey  # Импортируем базовые типы данных и функции
from sqlalchemy.orm import relationship, sessionmaker, scoped_session, Mapped, mapped_column  # Импортируем функции для работы с отношениями и сессиями
from sqlalchemy.ext.declarative import declarative_base  # Импортируем базовый класс для декларативного стиля
from sqlalchemy import create_engine  # Импортируем функцию для создания движка базы данных

# Создаем движок для работы с SQLite
engine = create_engine('sqlite:///vet_clinic.db', echo=True)  # Создаем SQLite базу данных и включаем вывод SQL-запросов

# Создаем базовый класс для наших моделей
Base = declarative_base()  # Это наш базовый класс, от которого будут наследоваться все модели

# Создаем фабрику сессий для работы с базой данных
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Модель для владельца питомца
class Owner(Base):
    __tablename__ = 'owners'  # Имя таблицы в базе данных
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Первичный ключ для идентификации владельца
    name: Mapped[str] = mapped_column(String, nullable=False)  # Имя владельца, обязательное поле
    pets: Mapped[list['Pet']] = relationship('Pet', back_populates='owner')  # Связь One-to-Many с моделью Pet (один владелец - много питомцев)

# Модель для питомца
class Pet(Base):
    __tablename__ = 'pets'  # Имя таблицы в базе данных
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Первичный ключ для идентификации питомца
    name: Mapped[str] = mapped_column(String, nullable=False)  # Имя питомца, обязательное поле
    species: Mapped[str] = mapped_column(String, nullable=False)  # Вид питомца (собака, кошка и т.д.), обязательное поле
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))  # Внешний ключ, ссылающийся на владельца (Owner)
    owner: Mapped['Owner'] = relationship('Owner', back_populates='pets')  # Обратная связь к владельцу (One-to-Many)
    visits: Mapped[list['Visit']] = relationship('Visit', back_populates='pet')  # Связь One-to-Many с моделью Visit (один питомец - много визитов)

# Модель для визитов в клинику
class Visit(Base):
    __tablename__ = 'visits'  # Имя таблицы в базе данных
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Первичный ключ для идентификации визита
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))  # Внешний ключ, ссылающийся на питомца (Pet)
    reason: Mapped[str] = mapped_column(String, nullable=False)  # Причина визита, обязательное поле
    date: Mapped[str] = mapped_column(String, nullable=False)  # Дата визита, обязательное поле
    pet: Mapped['Pet'] = relationship('Pet', back_populates='visits')  # Обратная связь к питомцу (One-to-Many)

# Создаем все таблицы, которые описаны в моделях
Base.metadata.create_all(engine)  # Эта команда создает все таблицы, если они еще не существуют

def hello():
    print('Hello!')

# Пример использования
def create_example_data():
    session = Session()  # Открываем сессию для работы с базой данных

    # Создаем владельца
    owner = Owner(name="John Doe")
    session.add(owner)  # Добавляем владельца в сессию

    # Создаем питомца, который принадлежит этому владельцу
    pet = Pet(name="Rex", species="Dog", owner=owner)  # Связываем питомца с владельцем через owner
    session.add(pet)  # Добавляем питомца в сессию

    # Создаем визит питомца в клинику
    visit = Visit(pet=pet, reason="Check-up", date="2024-08-19")  # Связываем визит с питомцем через pet
    session.add(visit)  # Добавляем визит в сессию

    # Сохраняем все изменения в базе данных
    session.commit()  # Подтверждаем изменения и сохраняем их в базе данных
    session.close()  # Закрываем сессию

if __name__ == "__main__":
    create_example_data()  # Запускаем функцию для добавления данных в базу
