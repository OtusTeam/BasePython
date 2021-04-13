from datetime import datetime
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

print(client.list_database_names())

DB_SHOP = "shop"

db = client[DB_SHOP]

print(db)
print(db.list_collection_names())


COLLECTION_USERS = "users"
# res = db[COLLECTION_USERS].insert_one({"username": "john", "fullName": "John Smith"})
# print(res, res.inserted_id)

users_collection = db[COLLECTION_USERS]


def user_factory(username, full_name):
    return {
        "username": username,
        "fullName": full_name,
        "createdAt": datetime.now(),
    }


admin_user = user_factory("admin", "Admin")
admin_user["is_staff"] = True

users_collection.insert_one(admin_user)

users = [
    user_factory("sam", "Sam White"),
    user_factory("ann", "Ann Black"),
]
results = users_collection.insert_many(users)

print(results, results.inserted_ids)


res = users_collection.find({
    "$or": [
        {"username": "sam"},
        {"username": "john"},
    ],
})

for doc in res:
    print(doc)
