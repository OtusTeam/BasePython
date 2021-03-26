class A:
    def __init__(self):
        self.item = 666

    def __getattribute__(self, item):
        print("an attempt to access item0 attribute has been made")
        return super().__getattribute__(item)

    def __getattr__(self, sample):
        print(f"getattr method has been called with a param={sample}")
        return 555


a0 = A()

# a0.item0
# print(a0.item)
print(a0.item0)
