from pathlib import Path


cwd = Path.cwd()
print("cwd:", (cwd,))
print(str(cwd))

# p = Path("/var")
# print(p, "exists?", p.exists())
#
# p = Path("/spam")
# print(p, "exists?", p.exists())
#
# home = Path.home()
# print("home:", home)
#
# downloads = home / "Downloads"
# print(downloads)
# print("downloads exists?", downloads.exists())
# print(downloads / "foo" / "bar")
# sub_path = home.joinpath("Downloads", "foobar", "spameggs")
# print(sub_path, "( exists?", sub_path.exists(), ")")
#
# file_path = cwd / "file.txt"
#
# with file_path.open(mode="w") as f:
#     b = f.write("Hello world!")
#     print(b)
#
# print("contents:", file_path.read_text())
#
#
# print("file_path.name", file_path.name)
# print("file_path.parent", file_path.parent)
# print("file_path.parts", file_path.parts)
# print("file_path.suffix", file_path.suffix)
# print("cwd.parent.suffix", cwd.parent.suffix)
# print("cwd.parent.parent.suffix", cwd.parent.parent.suffix)
# print("is file?", file_path.is_file())
# print("is file (cwd)?", cwd.is_file())
#
# print("change suffix", file_path.with_suffix(".py"))
# print("change suffix", file_path.with_name("index.js"))
