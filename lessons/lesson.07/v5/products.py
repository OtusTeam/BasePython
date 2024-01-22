def create(name):
    print(f'created product {name}')


def update(name, **kwargs):
    print(f'updated product {name}: {kwargs}')


if __name__ == '__main__':
    create('ipad')
    update('ipad', price=100)
