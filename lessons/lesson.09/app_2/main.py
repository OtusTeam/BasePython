import users
from users import check
# from users import create

# from users import *


def main():
    print("Hello main")
    print("users module (package)", users)
    print("magic variable:", users.USERS_MAGIC_VARIABLE)
    print(dir(users))
    print(users.create)
    print(users.update)

    # create("Bob")
    # update("Bob")
    print(users.check)
    users.check()
    check()


if __name__ == "__main__":
    main()
    # print(locals())
