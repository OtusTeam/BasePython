from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import func
from typing import List

from database import Session as SessionLocal, engine, get_db
from models import Base, Owner as ModelOwner, Pet as ModelPet, MedicalRecord as ModelMedicalRecord, Vaccine as ModelVaccine
from schemas import OwnerCreate, Owner, PetCreate, Pet, MedicalRecordCreate, MedicalRecord

router = APIRouter()


# 1. Показать животных без медицинских карт
@router.get("/pets/no_medical_record/", response_model=List[Pet])
def read_pets_without_medical_records(db: Session = Depends(get_db)):
    pets = db.query(ModelPet).filter(~ModelPet.medical_record.has()).all()
    return pets

# 2. Показать животных без медицинских записей
@router.get("/pets/no_medical_records/", response_model=List[Pet])
def read_pets_without_medical_records(db: Session = Depends(get_db)):
    pets = db.query(ModelPet).outerjoin(ModelMedicalRecord).filter(ModelMedicalRecord.id == None).all()
    return pets

# 3. Показать всех владельцев, их животных и записи по ним
@router.get("/owners/full_info/", response_model=List[Owner])
def read_owners_with_pets_and_records(db: Session = Depends(get_db)):
    owners = db.query(ModelOwner).options(joinedload(ModelOwner.pets).joinedload(ModelPet.medical_record)).all()
    return owners

# 4. Показать всех владельцев, у которых нет животных
@router.get("/owners/no_pets/", response_model=List[Owner])
def read_owners_without_pets(db: Session = Depends(get_db)):
    owners = db.query(ModelOwner).filter(~ModelOwner.pets.any()).all()
    return owners

# 5. Показать всех владельцев, у которых есть животные, но нет записей
@router.get("/owners/pets_no_records/", response_model=List[Owner])
def read_owners_with_pets_but_no_records(db: Session = Depends(get_db)):
    owners = db.query(ModelOwner).join(ModelPet).outerjoin(ModelMedicalRecord).filter(ModelMedicalRecord.id == None).all()
    return owners

# 6. Показать животных с их медицинскими картами и записями
@router.get("/pets/with_records/", response_model=List[Pet])
def read_pets_with_medical_records(db: Session = Depends(get_db)):
    pets = db.query(ModelPet).options(joinedload(ModelPet.medical_record)).all()
    return pets

# 7. Показать все медицинские записи для конкретного животного
@router.get("/pets/{pet_id}/medical_records/", response_model=List[MedicalRecord])
def read_medical_records_for_pet(pet_id: int, db: Session = Depends(get_db)):
    records = db.query(ModelMedicalRecord).filter(ModelMedicalRecord.pet_id == pet_id).all()
    if not records:
        raise HTTPException(status_code=404, detail="No medical records found for this pet")
    return records

# 8. Показать всех владельцев, у которых больше одного питомца
@router.get("/owners/multiple_pets/", response_model=List[Owner])
def read_owners_with_multiple_pets(db: Session = Depends(get_db)):
    owners = db.query(ModelOwner).join(ModelPet).group_by(ModelOwner.id).having(func.count(ModelPet.id) > 1).all()
    return owners

# 9. Показать всех владельцев и количество их животных
@router.get("/owners/pet_count/", response_model=List[dict])
def read_owners_and_pet_count(db: Session = Depends(get_db)):
    owners = db.query(ModelOwner, func.count(ModelPet.id).label("pet_count")).outerjoin(ModelPet).group_by(ModelOwner.id).all()
    return [{"owner": owner, "pet_count": pet_count} for owner, pet_count in owners]

# 10. Показать всех владельцев, у которых питомцы привиты
@router.get("/owners/vaccinated_pets/", response_model=List[Owner])
def read_owners_with_vaccinated_pets(db: Session = Depends(get_db)):
    owners = db.query(ModelOwner).join(ModelPet).join(ModelVaccine).filter(ModelVaccine.id != None).all()
    return owners
