from pathlib import Path
import json

from homework.config import CONTACTS_FILE_NAME


def new_reg():
    contacts_path = Path(CONTACTS_FILE_NAME)
    data_cont = []
    known_phones = set[int]()
    if contacts_path.exists():
        with contacts_path.open("r", encoding="UTF-8") as contacts_file:
            for line in contacts_file:
                loaded_contact = json.loads(line)
                data_cont.append(loaded_contact)
                known_phones.add(loaded_contact["phone"])
    name = input("напишите имя ")

    while True:
        try:
            phone = int(input("Введите номер телефона: "))
            break
        except ValueError:
            print("Ошибка! Введите только цифры.")

    if phone in known_phones:
        print("Ошибка! Такой номер уже существует.")
        return

    comment = input("Напишите комментарий ")
    phone_list = {"name": name, "phone": phone, "comment": comment}

    with contacts_path.open("a", encoding="UTF-8") as contacts_file:
        json.dump(phone_list, contacts_file, ensure_ascii=False)
        contacts_file.write("\n")
