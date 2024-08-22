from models import Owner, Visit, Pet
from database import Session

def get_visits_by_owner(owner_name: str):
    session = Session()
    
    results = session.query(Visit).join(Visit.pet).join(Pet.owner).\
        filter(Owner.name == owner_name).all()
    
    for visit in results:
        print(f"Owner: {visit.pet.owner.name}, Pet: {visit.pet.name}, Visit Date: {visit.date}, Reason: {visit.reason}")
    
    session.close()

def filter_visits_by_date_range(start_date: str, end_date: str):
    session = Session()
    
    results = session.query(Visit).filter(Visit.date.between(start_date, end_date)).all()
    
    for visit in results:
        print(f"Visit Date: {visit.date}, Pet: {visit.pet.name}, Reason: {visit.reason}")
    
    session.close()
