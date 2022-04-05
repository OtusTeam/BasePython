from pathlib import Path


class User:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        # return f"{self.__class__.__name__}(name={self.name})"
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
        # return str(self)


def demo_user():
    user_john = User("john")
    print("user john:", user_john)
    print("user john repr:", repr(user_john))

    print(user_john)
    print([user_john])
    print({"user john": user_john})

    my_str = "foobar"
    print(my_str)
    print(repr(my_str))
    print([my_str])


def demo_cwd():
    cwd = Path.cwd()
    print(cwd)
    print(repr(cwd))


def demo_home():
    print(Path.home())
    print()


def demo_check_existence():
    users = Path("/Users")
    print(users)
    print("exists?", users.exists())

    cats = Path("/Cats")
    print(cats)
    print("exists?", cats.exists())
    # cats.unlink(missing_ok=True)


def demo_file_path():
    print("__file__:", __file__)
    current_file = Path(__file__)
    print(current_file)
    print(repr(current_file))
    base_dir: Path = current_file.parent
    print(base_dir)
    print(repr(base_dir))
    print(base_dir.parent)
    print(list(base_dir.parents))


def demo_build_path():
    current_file = Path(__file__)
    base_dir: Path = current_file.parent

    folder_name = "pictures"
    file_name = "cats.jpg"

    cats_pic = base_dir / folder_name / file_name
    print(cats_pic)
    cats_pic2 = base_dir.joinpath(folder_name, file_name)
    print(cats_pic2)
    print(cats_pic == cats_pic2)

    print("suffix", cats_pic.suffix)
    print("name", cats_pic.name)
    print("stem", cats_pic.stem)
    print("anchor", cats_pic.anchor)


def demo_files():
    filename = "file.txt"

    file = Path(filename).resolve()
    print(file)
    file.unlink(missing_ok=True)

    file.write_text("hello!\n")

    print(file.read_text())


def demo_folders():
    current_file = Path(__file__)
    base_dir: Path = current_file.parent

    some_folder = base_dir.joinpath("some", "folder")
    print(some_folder)
    some_folder.mkdir(parents=True, exist_ok=True)
    some_folder.chmod(0o644)
    print(0x1A)
    print(0b1111)
    # some_folder.chmod(420)

    print([Path("/Users").resolve()])
    print([Path("/Cats").resolve()])
    print([Path("file.html").resolve()])
    print([Path("web/file.html").resolve()])


def main():
    # demo_user()
    # demo_cwd()
    # demo_home()
    # demo_check_existence()
    # demo_file_path()
    # demo_build_path()
    # demo_files()
    demo_folders()


if __name__ == "__main__":
    main()
