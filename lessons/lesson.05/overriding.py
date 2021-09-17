# overriding
class ParentPoint:
    is_parent = True

    def test(self):
        print("test")

    def print_stuff(self):
        print('I am a parent')


class ChildPoint(ParentPoint):
    is_parent = False

    def print_stuff(self):
        print('I am a child')


parent = ParentPoint()
parent.print_stuff()
parent.test()
print(parent.is_parent)

child = ChildPoint()
child.print_stuff()
child.test()
print(child.is_parent)
