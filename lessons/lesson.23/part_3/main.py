from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, create_engine, func
from sqlalchemy.orm import relationship, sessionmaker, scoped_session, Mapped, mapped_column, joinedload
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

# Создаем движок для работы с SQLite
engine = create_engine('sqlite:///vet_clinic.db', echo=False)

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

# Пример использования для создания данных
def create_example_data_with_medical_record():
    session = Session()

    # Создаем владельца и питомцев
    owner1 = Owner(name="Alice Johnson")
    owner2 = Owner(name="Bob Smith")
    owner3 = Owner(name="Catherine Lee")
    session.add_all([owner1, owner2, owner3])

    pet1 = Pet(name="Bella", species="Dog", owner=owner1)
    pet2 = Pet(name="Milo", species="Cat", owner=owner1)
    pet3 = Pet(name="Max", species="Dog", owner=owner2)
    pet4 = Pet(name="Luna", species="Cat", owner=owner2)
    pet5 = Pet(name="Charlie", species="Dog", owner=owner3)
    session.add_all([pet1, pet2, pet3, pet4, pet5])

    # Создаем визиты для питомцев
    visit1 = Visit(pet=pet1, reason="Annual Check-up", date="2024-01-15")
    visit2 = Visit(pet=pet2, reason="Vaccination", date="2024-02-20")
    visit3 = Visit(pet=pet3, reason="Injury", date="2024-03-12")
    visit4 = Visit(pet=pet4, reason="Dental Cleaning", date="2024-04-25")
    visit5 = Visit(pet=pet5, reason="Skin Allergy", date="2024-05-30")
    session.add_all([visit1, visit2, visit3, visit4, visit5])

    # Создаем медицинские карты для питомцев
    medical_record1 = MedicalRecord(pet=pet1, notes="Healthy", last_visit=date(2024, 1, 15))
    medical_record2 = MedicalRecord(pet=pet2, notes="Needs regular vaccination", last_visit=date(2024, 2, 20))
    session.add_all([medical_record1, medical_record2])

    session.commit()
    session.close()

# Функции для выполнения joined запросов
def get_pets_with_owners():
    session = Session()
    results = session.query(Pet).join(Pet.owner).all()
    for pet in results:
        print(f"Pet: {pet.name}, Species: {pet.species}, Owner: {pet.owner.name}")
    session.close()

def get_visits_with_pets():
    session = Session()
    results = session.query(Visit).join(Visit.pet).all()
    for visit in results:
        print(f"Visit ID: {visit.id}, Pet: {visit.pet.name}, Reason: {visit.reason}, Date: {visit.date}")
    session.close()

def get_visits_with_pets_optimized():
    session = Session()
    results = session.query(Visit).options(joinedload(Visit.pet)).all()
    for visit in results:
        print(f"Visit ID: {visit.id}, Pet: {visit.pet.name}, Reason: {visit.reason}, Date: {visit.date}")
    session.close()

# Примеры сортировки и выборки данных
def sort_pets_by_name():
    session = Session()
    results = session.query(Pet).order_by(Pet.name).all()
    for pet in results:
        print(f"Pet: {pet.name}, Species: {pet.species}")
    session.close()

def sort_owners_by_name():
    session = Session()
    results = session.query(Owner).order_by(Owner.name).all()
    for owner in results:
        print(f"Owner: {owner.name}")
    session.close()

def sort_visits_by_date():
    session = Session()
    results = session.query(Visit).order_by(Visit.date).all()
    for visit in results:
        print(f"Visit Date: {visit.date}, Pet: {visit.pet.name}, Reason: {visit.reason}")
    session.close()

def filter_pets_by_species(species: str):
    session = Session()
    results = session.query(Pet).filter(Pet.species == species).all()
    for pet in results:
        print(f"Pet: {pet.name}, Species: {pet.species}")
    session.close()

def filter_visits_by_reason(reason: str):
    session = Session()
    results = session.query(Visit).filter(Visit.reason == reason).all()
    for visit in results:
        print(f"Visit Date: {visit.date}, Pet: {visit.pet.name}, Reason: {visit.reason}")
    session.close()

def sort_pets_by_owner_name():
    session = Session()
    results = session.query(Pet).join(Pet.owner).order_by(Owner.name).all()
    for pet in results:
        print(f"Owner: {pet.owner.name}, Pet: {pet.name}, Species: {pet.species}")
    session.close()

def sort_visits_by_pet_name():
    session = Session()
    results = session.query(Visit).join(Visit.pet).order_by(Pet.name).all()
    for visit in results:
        print(f"Pet: {visit.pet.name}, Visit Date: {visit.date}, Reason: {visit.reason}")
    session.close()

def get_pets_with_visit_count():
    session = Session()
    results = session.query(Pet, func.count(Visit.id).label('visit_count')).\
        join(Pet.visits).\
        group_by(Pet.id).\
        order_by(func.count(Visit.id).desc()).all()
    for pet, visit_count in results:
        print(f"Pet: {pet.name}, Visits: {visit_count}")
    session.close()

def get_owners_with_pet_count():
    session = Session()
    results = session.query(Owner, func.count(Pet.id).label('pet_count')).\
        join(Owner.pets).\
        group_by(Owner.id).\
        order_by(func.count(Pet.id).desc()).all()
    for owner, pet_count in results:
        print(f"Owner: {owner.name}, Pets: {pet_count}")
    session.close()

def sort_visits_by_date_and_pet_name():
    session = Session()
    results = session.query(Visit).join(Visit.pet).order_by(Visit.date, Pet.name).all()
    for visit in results:
        print(f"Visit Date: {visit.date}, Pet: {visit.pet.name}, Reason: {visit.reason}")
    session.close()

if __name__ == "__main__":
    # Создаем и заполняем базу данных
    create_example_data_with_medical_record()

    # Выполняем различные запросы и сортировки
    print("\nPets with Owners:")
    get_pets_with_owners()

    print("\nVisits with Pets:")
    get_visits_with_pets()

    print("\nVisits with Pets (Optimized):")
    get_visits_with_pets_optimized()

    print("\nSort Pets by Name:")
    sort_pets_by_name()

    print("\nSort Owners by Name:")
    sort_owners_by_name()

    print("\nSort Visits by Date:")
    sort_visits_by_date()

    print("\nFilter Pets by Species (Dog):")
    filter_pets_by_species("Dog")

    print("\nFilter Visits by Reason (Vaccination):")
    filter_visits_by_reason("Vaccination")

    print("\nSort Pets by Owner Name:")
    sort_pets_by_owner_name()

    print("\nSort Visits by Pet Name:")
    sort_visits_by_pet_name()

    print("\nPets with Visit Count:")
    get_pets_with_visit_count()

    print("\nOwners with Pet Count:")
    get_owners_with_pet_count()

    print("\nSort Visits by Date and Pet Name:")
    sort_visits_by_date_and_pet_name()
