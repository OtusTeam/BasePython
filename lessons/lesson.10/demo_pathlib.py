from pathlib import Path

cwd = Path.cwd()
print("cwd", cwd)
print("cwd repr", repr(cwd))

p = Path("/Users")
print(p, "exists?", p.exists())

current_file = Path(__file__)
print(current_file)
base_dir = current_file.parent
print(base_dir)

print(current_file.parent.parent)


file_path = base_dir / "file.txt"

print(file_path, "exists file", file_path.exists())
file_path.unlink(missing_ok=True)
print(file_path, "exists file", file_path.exists())
file_path.write_text("Hello world\n")
print("file text:", file_path.read_text())


root = Path("/").resolve()
print(root)
print(root.parent)
print(root.parent.parent)


dir_path = base_dir.joinpath("abc", "qwe")
print("dir path", dir_path)
dir_path.mkdir(exist_ok=True, parents=True)

file_name = "fileqweqwe.txt"

fp = Path(file_name)
print(fp)
full_fp = fp.resolve()
print(full_fp)

print("suffix", full_fp.suffix)
print("name", full_fp.name)
print("stem", full_fp.stem)
print("anchor", full_fp.anchor)

print()

for p in cwd.iterdir():
    print(p)
