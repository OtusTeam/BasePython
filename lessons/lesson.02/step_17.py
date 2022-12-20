# def user_greet(username, punct='!', greeting='Hi'):
def user_greet(username, greeting='Hi', punct='!', **kwargs):
    # if kwargs.get('render_style'):
    #     print('custom style')
    print(f'{greeting}, {username}{punct}')


# user_greet('Ivan')
# user_greet('Ivan', '!!!')
# user_greet('Ivan', 'Привет')
user_greet('Ivan', punct='!', greeting='Привет')
user_greet('Ivan', greeting='Привет', punct='!')
user_greet(username='Ivan', greeting='Привет', punct='!')
user_greet(username='Ivan', greeting='Привет', punct='!', render_style='right')
