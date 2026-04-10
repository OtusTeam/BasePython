def del_f(friends_list, friend_name):
    """Добавляет друга в список."""
    if friend_name in friends_list:
        friends_list.remove(friend_name)
        return f'{friend_name} удален из списка'
    return f'{friend_name} не найден в списке'


def del_i(friends_list, friend_index):
    """Добавляет друга в список."""
    if friend_index >= 0 and friend_index < len(friends_list):
        name = friends_list.pop(friend_index)
        return f'{name} удален из списка'
    return f'такой индекс {friend_index} не найден в списке'