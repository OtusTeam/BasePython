# import utils


def say_world():
    print('world')


def say_hello():
    import utils

    utils.say_hello()


say_hello()
say_world()
