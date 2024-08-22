from datetime import datetime

from sqlalchemy.orm import Session

from database import session_factory

from models import Owner, Pet, Visit, MedicalRecord


def create_owner(
    session: Session,
    name: str,
    username: str,
) -> Owner:
    owner = Owner(
        name=name,
        username=username,
    )
    session.add(owner)
    session.commit()
    return owner


def create_pet(
    session: Session,
    owner_id: int,
    name: str,
    species: str,
) -> Pet:
    pet = Pet(
        name=name,
        species=species,
        owner_id=owner_id,
    )
    session.add(pet)
    session.commit()
    return pet


def create_visit(
    session: Session,
    pet_id: int,
    reason: str,
) -> Visit:
    visit = Visit(
        pet_id=pet_id,
        reason=reason,
        visit_date=datetime.today(),
    )
    session.add(visit)
    session.commit()
    return visit


def create_medical_record(
    session: Session,
    pet_id: int,
    notes: str,
) -> MedicalRecord:
    medical_record = MedicalRecord(
        pet_id=pet_id,
        notes=notes,
        last_visit=datetime.today(),
    )
    session.add(medical_record)
    session.commit()
    return medical_record


def main():
    with session_factory() as session:
        bob = create_owner(session, "Bob", username="bob")
        spot = create_pet(session, owner_id=bob.id, name="Spot", species="dog")
        alice = create_pet(session, owner_id=bob.id, name="Alice", species="cat")

        first_visit = create_visit(
            session,
            pet_id=alice.id,
            reason="First visit",
        )
        second_visit = create_visit(
            session,
            pet_id=spot.id,
            reason="Second visit",
        )
        create_medical_record(
            session,
            pet_id=spot.id,
            notes="Good boy!",
        )


if __name__ == "__main__":
    main()
