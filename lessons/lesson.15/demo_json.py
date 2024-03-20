import json
from datetime import datetime, timedelta, date, timezone
from pprint import pprint

DEMO_JSON_FILE = "demo_json.json"


def custom_json_encoder(obj):
    if isinstance(obj, date):
        return obj.isoformat()
        # return obj.strftime("%d.%m.%Y")
        # return obj.strftime("%H:%M:%S")

    message = f"Type {type(obj)} not serializable"
    raise TypeError(message)


def dump_json_demo():
    data = {
        "data": {
            "users": [
                {
                    "id": 1,
                    "name": "Иван",
                    "email": "john@localhost.com",
                },
                {
                    "id": 2,
                    "name": "Арсений",
                    "email": None,
                },
            ],
            "posts": [
                {
                    "id": 1,
                    "title": "P1",
                    "published": True,
                    "created_at": datetime.now(tz=timezone.utc),
                },
                {
                    "id": 2,
                    "title": "P2",
                    "published": False,
                    "created_at": datetime.utcnow() - timedelta(days=1),
                },
                {
                    "id": 3,
                    "title": "P3",
                    "published": True,
                    "created_at": datetime.now(tz=timezone(timedelta(hours=3))),
                },
            ],
        },
        "meta": {
            "page": 1,
            "per_page": 10,
        },
    }
    print(data)
    json_string = json.dumps(
        data,
        default=custom_json_encoder,
        indent=2,
        ensure_ascii=False,
    )
    # with open(DEMO_JSON_FILE, "w") as f:
    #     f.write(json_string)

    print(json_string)

    with open(DEMO_JSON_FILE, "w") as f:
        json.dump(
            data,
            f,
            default=custom_json_encoder,
            indent=2,
            ensure_ascii=False,
        )


def load_json_demo():
    with open(DEMO_JSON_FILE) as f:
        data = json.load(f)

    pprint(data)
    for user in data["data"]["users"]:
        print("User info:", user)


def main():
    dump_json_demo()
    load_json_demo()
    assert json.loads("null") is None
    assert json.dumps(None) == "null"
    assert json.dumps("qwerty") == '"qwerty"'


if __name__ == "__main__":
    main()
