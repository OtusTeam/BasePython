from functools import partial


def say_hello(name, greeting='Hello'):
    msg = f'{greeting}, {name}!'
    print(msg)


say_hi = partial(say_hello, greeting='Hi')
# say_hi = lambda name: say_hello(name, 'Hi')
say_morning = partial(say_hello, greeting='Good morning')

# say_hello('Ivan', 'Hello')
# say_hello('Olga', 'Hello')
# say_hello('Dmitry', 'Hello')
# say_hello('Elena', 'Hello')

say_hi('Ivan')
say_hi('Olga')
say_hi('Dmitry')
say_hi('Elena')
say_morning('Elena')
