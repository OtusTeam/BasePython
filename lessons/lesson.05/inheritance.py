class ParentPoint:
    is_parent = True

    def print_me(self):
        print('I am a parent')


class ChildPoint(ParentPoint):
    is_parent = False

    def print_me(self):
        print("I am a child")


parent = ParentPoint()
child = ChildPoint()

parent.print_me()
child.print_me()

print(parent.is_parent)
print(child.is_parent)

