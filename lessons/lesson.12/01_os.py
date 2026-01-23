import os

print(os.name)
print("sep:", os.path.sep)

print(os.getcwd())
# print()
# os.system("ls -la")

print(os.listdir())

items = list(os.listdir()) + ["foobar"]
for f in items:
    print()
    print(f, "is file?", os.path.isfile(f))
    print(f, "is dir?", os.path.isdir(f))
    print(f, "exists?", os.path.exists(f))


pictures_dir = "pictures"
pictures_full_path = os.path.join(
    os.path.split(__file__)[0],
    pictures_dir,
)
print("pictures_full_path")
print(pictures_full_path)

if not os.path.exists(pictures_full_path):
    os.mkdir(pictures_full_path)

cats_pic_dir = os.path.join(pictures_dir, "cats")
if not os.path.exists(cats_pic_dir):
    os.mkdir(cats_pic_dir)


cats_readme = os.path.join(cats_pic_dir, "readme.txt")
if os.path.isfile(cats_readme):
    os.unlink(cats_readme)
with open(cats_readme, "w") as f:
    f.write("# Cats Pictures\n")
    print("## Cats Pictures here", file=f)


# walk

for base_dir, dirs, files in os.walk("."):
    print()
    print("#", base_dir)
    for d in dirs:
        print("D", os.path.join(base_dir, d))
    for f in files:
        print("F", os.path.join(base_dir, f))
