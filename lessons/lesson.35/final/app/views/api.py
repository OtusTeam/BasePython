from flask import Blueprint, jsonify
from models.models import Owner, Pet

api = Blueprint("api", __name__)


@api.route("/api/owners", methods=["GET"])
def get_owners():
    owners = Owner.query.all()
    return jsonify(
        [
            {
                "id": owner.id,
                "name": owner.name,
                "age": owner.age,
                "phone": owner.phone,
                "pets": [
                    {"id": pet.id, "name": pet.name, "breed": pet.breed, "age": pet.age}
                    for pet in owner.pets
                ],
            }
            for owner in owners
        ]
    )


@api.route("/api/pets", methods=["GET"])
def get_pets():
    pets = Pet.query.all()
    return jsonify(
        [
            {
                "id": pet.id,
                "name": pet.name,
                "breed": pet.breed,
                "age": pet.age,
                "owner": (
                    {"id": pet.owner.id, "name": pet.owner.name} if pet.owner else None
                ),
            }
            for pet in pets
        ]
    )


@api.route("/api/owners_without_pets", methods=["GET"])
def get_owners_without_pets():
    owners = Owner.query.outerjoin(Pet).filter(Pet.id == None).all()
    return jsonify(
        [
            {"id": owner.id, "name": owner.name, "age": owner.age, "phone": owner.phone}
            for owner in owners
        ]
    )


@api.route("/api/pets_without_owners", methods=["GET"])
def get_pets_without_owners():
    pets = Pet.query.filter(Pet.owner_id == None).all()
    return jsonify(
        [
            {"id": pet.id, "name": pet.name, "breed": pet.breed, "age": pet.age}
            for pet in pets
        ]
    )
