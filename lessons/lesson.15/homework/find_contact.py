from pathlib import Path
contacts_path = Path("contacts.json")
import json
def search_all():
    data_search = []

    with open("contacts.json", "r", encoding="UTF-8") as contacts_file:
        for line in contacts_file:
            data_search.append(json.loads(line))

    key = input("Введите теелфон для поиска: ").lower()

    found = False
    for contact in data_search:
        if key in str(contact["phone"]).lower():
            print(contact)
            found = True

    if not found:
        print("такого номера не существует")