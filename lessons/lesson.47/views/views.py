from flask import Blueprint, render_template
from models.models import Owner, Pet

views = Blueprint("views", __name__)


@views.route("/")
def index():
    owners_with_pets = Owner.query.join(Pet).all()
    owners_without_pets = Owner.query.outerjoin(Pet).filter(Pet.id == None).all()
    pets_without_owners = Pet.query.filter(Pet.owner_id == None).all()
    return render_template(
        "index.html",
        owners_with_pets=owners_with_pets,
        owners_without_pets=owners_without_pets,
        pets_without_owners=pets_without_owners,
    )