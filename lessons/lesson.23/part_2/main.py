from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship, sessionmaker, scoped_session, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import date  # Импортируем модуль для работы с датами

# Создаем движок для работы с SQLite
engine = create_engine('sqlite:///vet_clinic.db', echo=True)

# Создаем базовый класс для наших моделей
Base = declarative_base()

# Создаем фабрику сессий для работы с базой данных
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Модель для владельца питомца
class Owner(Base):
    __tablename__ = 'owners'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    pets: Mapped[list['Pet']] = relationship('Pet', back_populates='owner')  # Связь One-to-Many с моделью Pet

# Модель для питомца
class Pet(Base):
    __tablename__ = 'pets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[str] = mapped_column(String, nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))
    
    owner: Mapped['Owner'] = relationship('Owner', back_populates='pets')  # Обратная связь к владельцу (One-to-Many)
    visits: Mapped[list['Visit']] = relationship('Visit', back_populates='pet')  # Связь One-to-Many с моделью Visit
    medical_record: Mapped['MedicalRecord'] = relationship("MedicalRecord", back_populates="pet", uselist=False)  # Связь One-to-One с моделью MedicalRecord

# Модель для визитов в клинику
class Visit(Base):
    __tablename__ = 'visits'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    reason: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=False)
    
    pet: Mapped['Pet'] = relationship('Pet', back_populates='visits')  # Обратная связь к питомцу (One-to-Many)

# Модель для медицинской карты питомца
class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    notes: Mapped[str] = mapped_column(Text, nullable=False)
    last_visit: Mapped[date] = mapped_column(Date, nullable=False)  # Используем тип Date для хранения дат
    
    pet: Mapped['Pet'] = relationship("Pet", back_populates="medical_record", uselist=False)  # Связь One-to-One с моделью Pet

# Создаем все таблицы, которые описаны в моделях
Base.metadata.create_all(engine)

# Пример использования
def create_example_data_with_medical_record():
    session = Session()  # Открываем сессию для работы с базой данных

    # Создаем владельца
    owner = Owner(name="Jane Smith")
    session.add(owner)

    # Создаем питомца, который принадлежит этому владельцу
    pet = Pet(name="Whiskers", species="Cat", owner=owner)
    session.add(pet)

    # Создаем медицинскую карту для питомца
    medical_record = MedicalRecord(pet=pet, notes="Healthy, but needs a dental check-up.", last_visit=date(2024, 8, 1))
    session.add(medical_record)

    # Создаем еще одного питомца для этого владельца
    pet2 = Pet(name="Fido", species="Dog", owner=owner)
    session.add(pet2)

    # Создаем медицинскую карту для второго питомца
    medical_record2 = MedicalRecord(pet=pet2, notes="Needs regular exercise.", last_visit=date(2024, 7, 21))
    session.add(medical_record2)

    # Сохраняем все изменения в базе данных
    session.commit()  # Подтверждаем изменения и сохраняем их в базе данных
    session.close()  # Закрываем сессию

if __name__ == "__main__":
    create_example_data_with_medical_record()
