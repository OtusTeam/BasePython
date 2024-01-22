def create(name):
    print(f'created user: {name}')


def update(name, **kwargs):
    print(f'updated user {name}: {kwargs}')


def delete(name):
    print(f'deleted user: {name}')


if __name__ == '__main__':
    create('Ivan')
    update('Ivan', age=28)
    delete('Ivan')
