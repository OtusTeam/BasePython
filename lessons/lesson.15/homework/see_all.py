from pathlib import Path
from textwrap import indent
import json
def see_all_list():
    contacts_path = Path("contacts.json")
    if contacts_path.exists():
        with open("contacts.json", "r", encoding="UTF-8") as contacts_file:
            data_cont = contacts_file.readlines()
            #print(data_cont)
            for line in data_cont:
                contact = json.loads(line)
                print(json.dumps(contact, indent=4))
                #print(id(contacts_file))
    else:
        print("файл не существует")
