from pathlib import Path

BASE_DIR = Path(__file__).parent

print(BASE_DIR)
print(repr(BASE_DIR))


def demo_paths():
    venv_path = BASE_DIR / ".venv"
    print(venv_path)
    cats_pic_path = BASE_DIR / "images" / "cats"
    print(cats_pic_path)
    print("cats_pic_path exists?", cats_pic_path.exists())
    print("is dir?", cats_pic_path.is_dir())
    print("venv_path exists?", venv_path.exists())
    print("is dir?", venv_path.is_dir())
    print("is file?", venv_path.is_file())
    # cats_pic_path = BASE_DIR / "images/cats"

    cats_pic_path.mkdir(exist_ok=True, parents=True)

    print("cats_pic_path exists?", cats_pic_path.exists())
    print("is dir?", cats_pic_path.is_dir())

    filepath = BASE_DIR / "file.txt"
    print(filepath)
    print(filepath.read_text())

    # filepath.write_text("hello\n")
    print(filepath.read_text())

    # filepath.unlink(missing_ok=True)
    with filepath.open("r") as f:
        for line in f:
            print(repr(line))

    promocode_file = BASE_DIR / "promocode.txt"
    promocode_file.write_text("promo!\n")
    with promocode_file.open("a") as f:
        f.write("another-promo\n")


def main():
    demo_paths()

    print(Path.home())
    print(Path.cwd())


if __name__ == "__main__":
    main()
