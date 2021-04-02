from pathlib import Path

cwd = Path.cwd()
print("cwd:", cwd)
p = Path('/var')
print(p, 'exists?', p.exists())
p = Path("/hello")
print(p, 'exists?', p.exists())

home = Path.home()
print(home)

downloads = home / "Downloads"
print(downloads)

print(home.joinpath("Downloads", "Pictures", "Dogs"))
print(home.joinpath("Downloads", "Pictures", "Dogs").exists())

file_path = cwd / 'file.txt'

with file_path.open(mode='w') as f:
    data = f.write('Hello World!')
    print(data)

print("content: ", file_path.read_text())

print(cwd.name)
print(cwd.parent)
print(cwd.parts)
