import random


def add_f(friends_list, friend_name):
    """Добавляет друга в список."""
    if friend_name not in friends_list:
        friends_list.append(friend_name)
        friends_list.append(random.x)
        return f'{friend_name} добавлен в список'
    return f'{friend_name} уже есть в списке'
