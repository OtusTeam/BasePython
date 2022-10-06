from pathlib import Path

BASE_DIR = Path(__file__).parent


def demo_cwd():
    print("base dir", BASE_DIR)

    cwd = Path.cwd()
    print(cwd)

    print(list(cwd.iterdir()))

    for path in cwd.iterdir():
        print("path", path.name, path.is_dir(), path.is_file())


def demo_home():
    home = Path.home()
    print("home:", home)


def demo_dirs():
    users = Path("/Users")
    print("users", users, users.exists())

    cats = Path("/Cats")
    print("cats", cats, cats.exists())

    BASE_DIR.mkdir(exist_ok=True)


def demo_files():
    filepath = BASE_DIR / "file.txt"
    # print(filepath)
    # filepath = "dirname" / Path("pictures")
    print(filepath)

    filepath.unlink(missing_ok=True)
    filepath.write_text("Hello world!\n")

    text = filepath.read_text()
    # bytes_obj = filepath.read_bytes()
    print("text", text)

    print(filepath)
    print(filepath.suffixes)
    print(Path("cat.py.jpg").suffixes)
    print(Path("cat.py.jpg").suffix)
    print(Path("archive.tar.gz").suffixes)
    print(Path("archive.tar.gz").stem)
    print("filepath.name", filepath.name)
    print("filepath.suffix", filepath.suffix)
    print("filepath.stem", filepath.stem)
    print("filepath.parents", list(filepath.parents))
    print(filepath.stat())
    filepath.chmod(0o777)
    print(filepath.stat())


if __name__ == "__main__":
    demo_cwd()
    demo_home()
    demo_files()
