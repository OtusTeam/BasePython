from pathlib import Path


BASE_DIR = Path(__file__).parent


def demo_cwd():
    cwd = Path.cwd()
    print(cwd)
    print(repr(cwd))

    print(Path.home())


def demo_dirs():
    users = Path("/Users")
    print(users)
    print(list(users.iterdir()))
    cats_dir = BASE_DIR / "cats"
    print(cats_dir)
    print(cats_dir.exists())
    cats_dir.mkdir(exist_ok=True)
    cats_dir.rmdir()

    for path in BASE_DIR.iterdir():
        print("path", path.name, path.is_dir(), path.is_file())


def main():
    # print(BASE_DIR)
    # print(repr(BASE_DIR))
    # demo_cwd()
    demo_dirs()


if __name__ == "__main__":
    main()


