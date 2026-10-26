
from pathlib import Path
contacts_path = Path("contacts.json")
import json
def edit_contacts():
    data_search = []

    with open(contacts_path, "r", encoding="UTF-8") as contacts_file:
        for line in contacts_file:
            data_search.append(json.loads(line))

    key = input("Введите теелфон для поиска: ")

    found = False
    for contact in data_search:
        if key in str(contact["phone"]):
            #print(contact)
            new_name = input("Введите новое имя: ")
            new_phone = input("Введите новый телефон: ")
            new_comment = input("Введите новый комментарий: ")
            contact["name"] = new_name
            contact["phone"] = int(new_phone)
            contact["comment"] = new_comment
            found = True
            break
    if not found:
        print("такого номера не существует")
    if found:
        with open(contacts_path, "w", encoding="UTF-8") as contacts_file:
            for contact in data_search:
                json.dump(contact, contacts_file, ensure_ascii=False)
                contacts_file.write("\n")
        print("контакт сохранен")