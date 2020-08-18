# class Foo:
#     """My Foo class"""
#     bar = True
#
#     # def echo_name(self):
#     #     print(self.__class__.__name__)
#
#     @classmethod
#     def echo_name(cls):
#         print(cls.__name__)


def print_class_demo(klass):
    f = klass()
    print(klass, klass.__class__, type(klass))
    print(f, f.__class__, type(f))

    print('class', klass.echo_name())
    print('inst', f.echo_bar())
    print(klass.bar, f.bar)

    f.bar = False
    print(klass.bar, f.bar)

    f.bar = True
    klass.bar = False
    f2 = klass()
    f2.echo_bar()
    print(klass.bar, f.bar, f2.bar)


@classmethod
def echo_name(cls):
    print(cls.__name__)


def echo_bar(self):
    print(self.bar)


# Foo = type('Foo', (), {'bar': True, 'echo_name': echo_name, 'echo_bar': echo_bar})
#
# NewFoo = type('NewFoo', (Foo, ), {'spam': 'eggs'})
#
# print(NewFoo)
# nf = NewFoo()
# print(nf)
# print(nf.spam)
# print(nf.bar)
# print(nf.echo_name())

# print_class_demo(Foo)


class MyMetaclass(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        # print('New class', name)
        # print('Bases:', bases)
        dct['SPAM'] = 'EGGS'
        # print('New attrs:', dct)
        for k in dct.keys():
            if k.startswith('_'):
                v = dct.pop(k)
                dct[k.upper()] = v

        new_cls = super().__new__(cls, name, bases, dct, *args, **kwargs)
        # class new_cls:
        #     bar = True

        # print('created new cls:', new_cls)
        return new_cls

#
# Foo = MyMetaclass('Foo', (), {})
#
# NewFoo = MyMetaclass('NewFoo', (Foo, ), {'spam': 'eggs'})


# print('creating new Foo class')
class Foo(metaclass=MyMetaclass):

    def __new__(cls, *args, **kwargs):
        print('__new__ FOO ', cls)

    bar = True
    _secret_attr = 'secret value'

    @classmethod
    def echo_name(cls):
        print(cls.__name__)

    def echo_bar(self):
        print(self.bar)
# print('CREATED new Foo class', Foo)
# print(Foo.__name__)
# print(Foo.bar)



class NewFoo(Foo):
    spam = 'egss'

    class SubNewCls:
        new = False

# print(NewFoo.SubNewCls.new)

class BaseUser:
    is_staff = False
    is_admin = False

class User(BaseUser):
    pass


class Admin(BaseUser):
    is_staff = True
    is_admin = True

# MyClass = MyMetaClass()
# my_instance = MyClass()

# print(Foo.SPAM)
# print(NewFoo.SPAM)
# f = Foo()
# Foo.echo_bar(f)
# f.echo_bar()
# nf = NewFoo()
# print(f, f.SPAM)
# print(nf, nf.SPAM)
# # print_class_demo(Foo)
#
# print(Foo._SECRET_ATTR)


from abc import ABCMeta, abstractmethod


class FileManagerABC(metaclass=ABCMeta):

    @abstractmethod
    def read_file(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def write_to_file(self, text: str) -> int:
        """
        Write to file
        :param text:
        :return:
        """
        raise NotImplementedError


class FileManager(FileManagerABC):
    def __init__(self, filename: str):
        self._filename = filename

    def read_file(self) -> str:
        with open(self._filename, 'r') as f:
            text = f.read()
            # f.seek(0)
            return text

    def write_to_file(self, text: str) -> int:
        with open(self._filename, 'a') as f:
            count = f.write(text)
            print('written text', text)
            return count


file_manager = FileManager('file.txt')
print(file_manager.read_file())
print(file_manager.write_to_file('\nhello again'))
