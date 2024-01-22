# import sys
# from datetime import datetime
# import datetime
# print(sys.path)
# sys.path.append('...')


import products
import users
from users.api import requests as users_requests
# import utils
# from users import *

# from users.create import create as user_create
# from users.update import update
# import products, users


def main():
    # user_create('Ivan')
    # update('Ivan', age=28)
    users.create("'Ivan'")
    # users.create('\'Ivan\'')
    users.update('Ivan', age=28)

    products.create('iphone')
    products.update('iphone', price=1000)


main()
