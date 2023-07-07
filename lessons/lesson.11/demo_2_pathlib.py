from pathlib import Path

# print(__builtins__)
# print(vars(__builtins__))

BASE_DIR = Path(__file__).parent

print(BASE_DIR)
print(repr(BASE_DIR))


def demo_cwd():
    cwd = Path.cwd()
    print(cwd)
    print(repr(cwd))
    home = Path.home()
    print(home)


def demo_dirs():
    users_path = Path("/Users")
    print(users_path)
    print(list(users_path.iterdir()))
    # cats_dir = Path(str(BASE_DIR) + "/") / "cats"
    cats_dir = BASE_DIR / "cats"
    print(cats_dir)
    print("exists", cats_dir.exists())
    print("is_dir", cats_dir.is_dir())
    cats_dir.mkdir(exist_ok=True)
    pic = "kitty.jpg"
    kittens = BASE_DIR / "cats" / "kittens" / pic
    print(kittens)


def show_dir():
    for path in BASE_DIR.iterdir():
        print(
            path.name,
            "is file?",
            path.is_file(),
            "is dir?",
            path.is_dir(),
        )


def main():
    # demo_cwd()
    # demo_dirs()
    show_dir()


if __name__ == '__main__':
    main()
