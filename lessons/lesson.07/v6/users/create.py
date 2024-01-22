from .delete import delete


def create(name):
    delete(name)
    print(f'created user: {name}')
