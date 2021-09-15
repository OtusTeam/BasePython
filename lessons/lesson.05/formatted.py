class Point:
    is_parent = True

    def __init__(self, x=0):
        # print('Point init called')
        self.x = x

    def who_am_i(self):
        print('I am a parent point')

    def __str__(self):
        point_name = "Geometric Point"
        "{name}".format(name=point_name)
        return f'Point name = {point_name}, x = {self.x}'
