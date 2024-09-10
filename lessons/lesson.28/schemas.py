from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class PetBase(BaseModel):
    name: str
    species: str

class PetCreate(PetBase):
    owner_id: Optional[int] = None  # Питомец может создаваться без владельца

class Pet(PetBase):
    id: int
    owner_id: Optional[int]

    class Config:
        orm_mode = True

#


class OwnerBase(BaseModel):
    name: str

class OwnerCreate(OwnerBase):
    pass

class Owner(OwnerBase):
    id: Optional[int] = None
    pets: List[Pet] = []

    class Config:
        orm_mode = True


#


class MedicalRecordBase(BaseModel):
    notes: str
    last_visit: date

class MedicalRecordCreate(MedicalRecordBase):
    pet_id: int  # ID питомца для которого создается медицинская запись

class MedicalRecord(MedicalRecordBase):
    id: int
    pet_id: int

    class Config:
        orm_mode = True
