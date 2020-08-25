import pathlib

cwd = pathlib.Path.cwd()
print(cwd)
print(str(cwd))
print(repr(cwd))

p = pathlib.Path("/var")
print(repr(p), "exists?", p.exists())

p = pathlib.Path("/qwerty")
print(repr(p), "exists?", p.exists())

home = pathlib.Path.home()
print(repr(home))

downloads = home / "Downloads"
print(repr(downloads))

print(downloads / "qwerty" / "subdir")

# print("value: %s" % "val")
# print("1" * 10)

print(home.joinpath("scripts", "python", "main.py"))

file_name = "file.txt"
file_path = cwd / file_name
print(file_path)
print("exitsts?", file_path.exists())

with file_path.open(mode="w") as f:
    res = f.write("Hello world!")
    print("res:", res)

print(file_path.read_text())

f_path = pathlib.Path(file_name)
print(f_path)

path = f_path.resolve()
print(path)

print(path.parent)
print(path.parent.parent)

print(path.name)
print(path.parent.name)

print(path.stem)
print(path.suffix)

print(path.anchor)

print(path.with_suffix(".py"))
print(path.with_name("main.py"))

print()
for p in cwd.iterdir():
    print(p)
