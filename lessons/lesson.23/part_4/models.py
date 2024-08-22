from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    pets: Mapped[list['Pet']] = relationship('Pet', back_populates='owner')

class Pet(Base):
    __tablename__ = 'pets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[str] = mapped_column(String, nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))
    
    owner: Mapped['Owner'] = relationship('Owner', back_populates='pets')
    visits: Mapped[list['Visit']] = relationship('Visit', back_populates='pet')
    medical_record: Mapped['MedicalRecord'] = relationship("MedicalRecord", back_populates="pet", uselist=False)

class Visit(Base):
    __tablename__ = 'visits'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    reason: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=False)
    
    pet: Mapped['Pet'] = relationship('Pet', back_populates='visits')

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    notes: Mapped[str] = mapped_column(Text, nullable=False)
    last_visit: Mapped[Date] = mapped_column(Date, nullable=False)
    
    pet: Mapped['Pet'] = relationship("Pet", back_populates="medical_record", uselist=False)

