import asyncio
from datetime import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base, Owner, Pet, Visit, MedicalRecord
from models.db_async import engine, async_session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_owner(
    session: AsyncSession,
    name: str,
    username: str,
) -> Owner:
    owner = Owner(
        name=name,
        username=username,
    )
    session.add(owner)
    await session.commit()
    # await session.refresh(owner)
    return owner


async def create_pet(
    session: AsyncSession,
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
    await session.commit()
    return pet


async def create_visit(
    session: AsyncSession,
    pet_id: int,
    reason: str,
) -> Visit:
    visit = Visit(
        pet_id=pet_id,
        reason=reason,
        visit_date=datetime.today(),
    )
    session.add(visit)
    await session.commit()
    return visit


async def create_medical_record(
    session: AsyncSession,
    pet_id: int,
    notes: str,
) -> MedicalRecord:
    medical_record = MedicalRecord(
        pet_id=pet_id,
        notes=notes,
        last_visit=datetime.today(),
    )
    session.add(medical_record)
    await session.commit()
    return medical_record


async def get_all_owners_with_pets(
    session: AsyncSession,
) -> Sequence[Owner]:
    stmt = (
        select(Owner)
        .options(
            selectinload(Owner.pets)
        )
        .order_by(Owner.id)
    )

    # res = await session.execute(stmt)
    # owners = res.scalars().all()
    # return owners
    result = await session.scalars(stmt)
    owners = result.all()
    for owner in owners:
        print(owner)
        for pet in owner.pets:
            print("+ pet:", pet)
    return owners


async def get_all_pets_with_owners(
    session: AsyncSession,
) -> Sequence[Pet]:
    stmt = (
        select(Pet)
        .options(
            # selectinload(Pet.owner)
            joinedload(Pet.owner)
        )
        .order_by(Pet.id)
    )

    result = await session.scalars(stmt)
    pets = result.all()
    for pet in pets:
        print("- pet:", pet, pet.owner)
    return pets


async def create_items(session: AsyncSession) -> None:
    bob = await create_owner(session, "Bob", username="bob")
    spot = await create_pet(session, owner_id=bob.id, name="Spot", species="dog")
    alice = await create_pet(session, owner_id=bob.id, name="Alice", species="cat")

    print("bob:", bob)
    print("spot:", spot)
    print("alice:", alice)
    first_visit: Visit = await create_visit(
        session,
        pet_id=alice.id,
        reason="First visit",
    )
    second_visit: Visit = await create_visit(
        session,
        pet_id=spot.id,
        reason="Second visit",
    )
    await create_medical_record(
        session,
        pet_id=spot.id,
        notes="Good boy!",
    )


async def main():
    async with async_session() as session:
        # await create_items(session)
        # john = await create_owner(session, "John", username="john")
        # jack = await create_pet(session, owner_id=john.id, name="Jack", species="dog")
        # bella = await create_pet(session, owner_id=john.id, name="Bella", species="cat")

        josh = await create_owner(session, "Josh", username="josh")
        print(josh)
        owners = await get_all_owners_with_pets(session)
        # pets = await get_all_pets_with_owners(session)

if __name__ == "__main__":
    asyncio.run(main())
