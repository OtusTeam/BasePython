class Item:
    def __init__(self, name):
        self.name = name


class Storage:
    def __init__(self):
        self._items = {}

    def add(self, item):
        print('added')
        self._items[item.name] = item
