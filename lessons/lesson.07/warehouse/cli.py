import sys
# from models import *
from models import Item, Storage


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
