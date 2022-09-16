
foo = "foo"
spam = "spam"

f1 = f"foo={foo}, spam={spam}, bar={foo}"
print(f1)


format1 = "foo={foo}, spam={spam}, bar={foo}".format(foo=foo, spam=spam)
print(format1)
format2 = "foo={0}, spam={1}, bar={0}".format(foo, spam)
print(format2)
format3 = "foo={abc}, spam={qwe}, bar={qwe}".format(abc=foo, qwe=spam)
print(format3)
format4 = "foo={abc}, spam={qwe}, bar={abc}".format(abc="hello", qwe="world")
print(format4)
