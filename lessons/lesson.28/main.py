from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pet_router import router as pet_router
from record_router import router as record_router

from database import Session, engine
from models import Base, Owner as ModelOwner, Pet as ModelPet, MedicalRecord as ModelMedicalRecord
from schemas import OwnerCreate, Owner, PetCreate, Pet, MedicalRecordCreate, MedicalRecord
from database import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pet_router, prefix='/pet', tags=['pet'])
app.include_router(record_router, prefix='/router', tags=['records'])

@app.post("/owners/", response_model=Owner)
def create_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    db_owner = ModelOwner(name=owner.name)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

@app.get("/owners/", response_model=List[Owner])
def read_owners(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    owners = db.query(ModelOwner).offset(skip).limit(limit).all()
    return owners

@app.get("/owners/{owner_id}", response_model=Owner)
def read_owner(owner_id: int, db: Session = Depends(get_db)):
    owner = db.query(ModelOwner).filter(ModelOwner.id == owner_id).first()
    if owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner

@app.put("/owners/{owner_id}", response_model=Owner)
def update_owner(owner_id: int, owner: OwnerCreate, db: Session = Depends(get_db)):
    db_owner = db.query(ModelOwner).filter(ModelOwner.id == owner_id).first()
    if db_owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    db_owner.name = owner.name
    db.commit()
    db.refresh(db_owner)
    return db_owner

@app.delete("/owners/{owner_id}", response_model=Owner)
def delete_owner(owner_id: int, db: Session = Depends(get_db)):
    db_owner = db.query(ModelOwner).filter(ModelOwner.id == owner_id).first()
    if db_owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    db.delete(db_owner)
    db.commit()
    return db_owner

#
