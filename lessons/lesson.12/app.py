from pprint import pprint

# from models import *
# from models import PostsTagsAssociation
import models

from one.two.three import value
from one.two.four import another_value
from one.two.five import value as new_value
from one.two import five

# print(User)
# print(Post)
# print(dataclass)
# print(sha256)
# print(uuid4)
pprint(locals())
print(models.User)

# print(posts_tags_association.PostsTagsAssociation)
print(models.PostsTagsAssociation)

print("value:", value)
print("new_value:", new_value)
print("another_value:", another_value)

print("five.value:", five.value)
print("five.hello:", five.hello)
