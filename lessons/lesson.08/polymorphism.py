# +
# len()

# 2 + 2
# 2.0 + 3.75
# "MY" + "NAME" + "IS" + "NIGAR"
# laptop + phone + calculator

sample_list = [1, 2, 3, 4]
name = "Nigar"
new_dict = {"13": "Adams", "15": "Smiths", "17": "Simpsons"}

print(len(sample_list))
print(len(name))
print(len(new_dict))

# __len__

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a {self.__class__.__name__}. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        print("Meow")


class Dog(Animal):

    def make_sound(self):
        print("Bark")


cat = Cat("Richard", 1.5)
dog = Dog("Boris", 2)

for animal in (cat, dog):
    animal.make_sound()
    animal.info()
    animal.make_sound()
