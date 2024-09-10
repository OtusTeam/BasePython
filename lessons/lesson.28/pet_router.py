from fastapi import APIRouter
from models import Base, Owner as ModelOwner, Pet as ModelPet, MedicalRecord as ModelMedicalRecord
from schemas import OwnerCreate, Owner, PetCreate, Pet, MedicalRecordCreate, MedicalRecord
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db


router = APIRouter()


@router.post("/pets/", response_model=Pet)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = ModelPet(name=pet.name, species=pet.species, owner_id=pet.owner_id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.get("/pets/", response_model=List[Pet])
def read_pets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pets = db.query(ModelPet).offset(skip).limit(limit).all()
    return pets

@router.get("/pets/{pet_id}", response_model=Pet)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(ModelPet).filter(ModelPet.id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.post("/pets/{pet_id}/medical_records/", response_model=MedicalRecord)
def create_medical_record_for_pet(pet_id: int, record: MedicalRecordCreate, db: Session = Depends(get_db)):
    db_pet = db.query(ModelPet).filter(ModelPet.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    db_record = ModelMedicalRecord(notes=record.notes, last_visit=record.last_visit, pet_id=pet_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.post("/pets/{pet_id}/associate_owner/", response_model=Pet)
def associate_pet_with_owner(pet_id: int, owner_id: int, db: Session = Depends(get_db)):
    db_pet = db.query(ModelPet).filter(ModelPet.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    db_owner = db.query(ModelOwner).filter(ModelOwner.id == owner_id).first()
    if db_owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    db_pet.owner_id = owner_id
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.get("/pets/no_owner/", response_model=List[Pet])
def read_pets_without_owners(db: Session = Depends(get_db)):
    pets = db.query(ModelPet).filter(ModelPet.owner_id == None).all()
    return pets
