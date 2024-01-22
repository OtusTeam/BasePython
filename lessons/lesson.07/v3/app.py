from products import (
    create,
    update,
)
# from users import create, update
# from products import *
# from users import *
# import settings


def main():
    create('iphone')
    update('iphone', price=1000)


main()
