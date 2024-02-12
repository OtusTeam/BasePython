# DEFAULT_TAGS = ["foo", "bar"]
# def populate_default_tags(item_type, tags=[]):
# def populate_default_tags(item_type, tags=("abc", "qwe")):
def populate_default_tags(item_type, tags=None):
    # tags = list(tags)
    if tags is None:
        tags = []
    # default_tags = TAGS_FOR_ITEMS[item_type]
    default_tags = ["spam", "eggs"]
    print("Add tags for", item_type)
    tags.extend(default_tags)
    return tags


print(populate_default_tags("foo", ["abc"]))
print(populate_default_tags("bar", ["qwe"]))
new_tags = []
print(populate_default_tags("abc", new_tags))

new_tags = populate_default_tags("fizz")
print(new_tags)

new_tags = populate_default_tags("buzz")
print(new_tags)
print(populate_default_tags("foobar", ["foo", "bar"]))

new_tags = populate_default_tags("qwe")
print(new_tags)
