from datetime import datetime

import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)

print(client.list_database_names())

db = client["blog"]

COLLECTION_USERS = "users"


def create_user(username: str, **kwargs) -> dict:
    user = {
        "username": username,
        "created_at": datetime.utcnow(),
    }
    user.update(kwargs)
    return user


def create_admin():
    user_admin = create_user("admin")
    res = db[COLLECTION_USERS].insert_one(user_admin)

    print(res.inserted_id)

    admin = db[COLLECTION_USERS].find_one({"_id": res.inserted_id})
    print(admin)


def create_john():
    user_john = create_user("john", first_name="John", last_name="Smith")
    res = db[COLLECTION_USERS].insert_one(user_john)

    print(res.inserted_id)

    john = db[COLLECTION_USERS].find_one({"_id": res.inserted_id})
    print(john)


user_sam = create_user("sam2", first_name="Sam", last_name="Brown")
res = db[COLLECTION_USERS].insert_one(user_sam)

print(res.inserted_id)

sam = db[COLLECTION_USERS].find_one({"_id": res.inserted_id})
print(sam)
