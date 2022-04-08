import json


def main():
    json_string = """
    {
        "spam": "eggs1",
        "spam": "eggs2",
        "Spam": "eggs3"
    }
    """
    print(type(json_string), repr(json_string))

    data = json.loads(json_string)
    print(type(data), repr(data))
    print(data["spam"])
    data["foo"] = "bar"
    print(data)


if __name__ == '__main__':
    main()
