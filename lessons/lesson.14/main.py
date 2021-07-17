USERS = {
}


def add_user(key, value):
    USERS[key] = value


if __name__ == '__main__':
    add_user("user_2", "Sam")
    print(USERS)
