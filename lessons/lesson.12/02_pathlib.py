from pathlib import Path

print(Path.cwd())
print(repr(Path.cwd()))

BASE_DIR = Path(__file__).resolve().parent

pictures_path = BASE_DIR / "pictures"
print(repr(pictures_path))
print("exists?", pictures_path.exists())
print("is_file?", pictures_path.is_file())
print("is_dir?", pictures_path.is_dir())

cats_pics_path = pictures_path / "cats"
print(repr(cats_pics_path))
print("exists?", cats_pics_path.exists())
print("is_file?", cats_pics_path.is_file())
print("is_dir?", cats_pics_path.is_dir())

cats_pics_path.mkdir(parents=True, exist_ok=True)

# cats_pictures_path = BASE_DIR / "pictures" / "cats"
# cats_pictures_path.mkdir(parents=True, exist_ok=True)

cats_readme_path = cats_pics_path / "readme.txt"
cats_readme_path.unlink(missing_ok=True)
cats_readme_path.write_text("# Hello cats pics!\n")

with cats_readme_path.open("a") as f:
    f.write("## Hello again cats pics!\n")

print(cats_readme_path.read_text())
print(cats_readme_path.stem)
print(cats_readme_path.suffix)

arch = Path("files.tar.gz").resolve()
print(repr(arch))
print(arch.stem)
print(arch.name)
print(arch.suffix)
print(arch.suffixes)

a_zip = arch.with_name("new-arch.zip")
print(repr(a_zip))
