#def menu():
from new_contact import new_reg
from see_all import see_all_list
from find_contact import search_all
from edit_contact import edit_contacts
from delete_contct import delete

while True:
    print("1 - чтобы добавить контакт")
    print("2 - чтобы посмотреть все контакты")
    print("3 - чтобы найти контакт")
    print("4 - чтобы изменить контакт")
    print("5 - чтобы удалить контакт")

    action_menu = input("Выберите действие: ")

    if action_menu == "1":
        new_reg()
    elif action_menu == "2":
        see_all_list()
    elif action_menu == "3":
        search_all()
    elif action_menu == "4":
        edit_contacts()
    elif action_menu == "5":
        delete()
    else:
        print("неверная команда")
#menu()
