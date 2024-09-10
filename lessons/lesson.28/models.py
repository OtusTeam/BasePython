from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Промежуточная таблица для связи Owner и Stock
owner_stock_association = Table(
    "owner_stock",
    Base.metadata,
    Column("owner_id", Integer, ForeignKey("owners.id"), primary_key=True),
    Column("stock_id", Integer, ForeignKey("stocks.id"), primary_key=True),
)

# Промежуточная таблица для связи Pet и Vaccine
pet_vaccine_association = Table(
    "pet_vaccine",
    Base.metadata,
    Column("pet_id", Integer, ForeignKey("pets.id"), primary_key=True),
    Column("vaccine_id", Integer, ForeignKey("vaccines.id"), primary_key=True),
)


class Owner(Base):
    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    pets: Mapped[list["Pet"]] = relationship("Pet", back_populates="owner")
    stocks: Mapped[list["Stock"]] = relationship(
        "Stock", secondary=owner_stock_association, back_populates="owners"
    )


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[str] = mapped_column(String, nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("owners.id"))

    owner: Mapped["Owner"] = relationship("Owner", back_populates="pets")
    visits: Mapped[list["Visit"]] = relationship("Visit", back_populates="pet")
    medical_record: Mapped["MedicalRecord"] = relationship(
        "MedicalRecord", back_populates="pet", uselist=False
    )
    vaccines: Mapped[list["Vaccine"]] = relationship(
        "Vaccine", secondary=pet_vaccine_association, back_populates="pets"
    )


class Stock(Base):
    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Integer, nullable=False)

    owners: Mapped[list["Owner"]] = relationship(
        "Owner", secondary=owner_stock_association, back_populates="stocks"
    )


class Vaccine(Base):
    __tablename__ = "vaccines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    pets: Mapped[list["Pet"]] = relationship(
        "Pet", secondary=pet_vaccine_association, back_populates="vaccines"
    )


class Visit(Base):
    __tablename__ = "visits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey("pets.id"))
    reason: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=False)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="visits")


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey("pets.id"))
    notes: Mapped[str] = mapped_column(Text, nullable=False)
    last_visit: Mapped[Date] = mapped_column(Date, nullable=False)

    pet: Mapped["Pet"] = relationship(
        "Pet", back_populates="medical_record", uselist=False
    )
