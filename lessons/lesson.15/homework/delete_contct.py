from pathlib import Path
contacts_path = Path("contacts.json")
import json
def delete():
    data_search = []

    with open("contacts.json", "r", encoding="UTF-8") as contacts_file:
        for line in contacts_file:
            data_search.append(json.loads(line))

    key = input("Введите теелфон для поиска: ")

    found = False
    for contact in data_search:
        if key in str(contact["phone"]):
            print(contact)
            data_search.remove(contact)
            with open("contacts.json", "w", encoding="UTF-8") as contacts_file:
                for contact in data_search:
                    json.dump(contact, contacts_file, ensure_ascii=False)
                    contacts_file.write("\n")
            print(data_search)
            found = True
    if not found:
        print("такого номера не существует")