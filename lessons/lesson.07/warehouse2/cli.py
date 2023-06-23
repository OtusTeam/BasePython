import sys

from models import Item, Storage

# from models.item import Item
# from models.storage import Storage

ROOT = '/home/jo/teach/python-basic/2023-05/230623'
sys.path.append(ROOT)
print(sys.path)


def main():
    # print('started cli')
    # if len(sys.argv) > 1:
    #     print('let`s do it')
    item_1 = Item('iphone 14')
    storage_1 = Storage()
    storage_1.add(item_1)


# print(__name__)
if __name__ == '__main__':
    main()
