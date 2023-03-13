SAY_HI = False


def say_hello(user_name: str, greeting='', start_word='hello') -> None:
    print(start_word, user_name, greeting)


# say_hello(12)
# args = ('a.andreeev',)
# args = ('a.andreeev', 'have a very good day!')
args = ['a.andreeev', 'have a very good day!', 'hi']
# 'a.andreeev', 'have a very good day!', 'hi'
say_hello(*args)

# say_hello('a.andreeev', 'have a very good day!')
# say_hello('a.andreeev', 'have a very good day!', 'hi')
# say_hello('a.andreeev', 'hi', 'have a very good day!')
# # kwargs keyword arguments
# say_hello('a.andreeev', start_word='hi', greeting='have a very good day!')
kwargs = {'user_name': 'a.andreeev',
          # 'start_word': 'hi',
          'greeting': 'have a very good day!'}
if SAY_HI:
    kwargs['start_word'] = 'hi'

# say_hello(user_name='a.andreeev', start_word='hi', greeting='have a very good day!')
say_hello(**kwargs)
