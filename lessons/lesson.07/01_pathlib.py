from pathlib import Path

filepath = Path("some-file.txt")

print(filepath)
print(repr(filepath))

print(Path.cwd())
print(filepath.resolve())

filepath.unlink(missing_ok=True)
print("file exists?", filepath.exists())
print("file is file?", filepath.is_file())

with filepath.open("w") as file:
    file.write("Hello World from Pathlib\n")
    file.write("Thanks!\n")

with filepath.open("r") as file:
    for line in file:
        print(f"line: {line!r}")
print("file exists?", filepath.exists())

with filepath.open("a") as file:
    file.write("Bye-Bye!\n")

print("file is file?", filepath.is_file())


hello_file = Path("hello.txt")

new_text = """Hi,
it's a new example for text writing.
Pathlib is the best!
"""

hello_file.write_text(new_text)

print("file contents:")
print(hello_file.read_text())
