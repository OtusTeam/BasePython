import os
# import pathlib
from pathlib import Path

BASE_DIR = Path(__file__).parent


class PathString(str):
    # def __add__(self, other):
    #     pass
    #
    # def __sub__(self, other):
    #     pass
    #
    # def __mul__(self, other):
    #     pass
    #
    def __truediv__(self, other) -> "PathString":
        if not isinstance(other, str):
            raise TypeError("has to be str")
        return PathString(os.path.join(self, other))


def demo_paths_one():
    # venv_path = Path("venv").resolve()
    venv_path = Path("venv")
    print("is file:", venv_path.is_file())
    print("is dir:", venv_path.is_dir())
    print(venv_path)
    print(repr(venv_path))
    venv_path = venv_path.resolve()
    print(venv_path)
    print(repr(venv_path))

    home = Path.home()
    print(home)
    print(repr(home))

    cwd = Path.cwd()
    print(cwd)
    print(repr(cwd))


def demo_paths_two():
    pics_folder_name = "pics"
    home = Path.home()
    pic_filepath = home / pics_folder_name / "cat.jpg"
    print(pic_filepath)
    print(repr(pic_filepath))

    # print("all_pic_path" / Path(pics_folder_name))

    print()
    users_path = Path("/Users")
    print("Users exists", users_path.exists())
    # for path in users_path.iterdir():
    for path in users_path.iterdir():
        print("path", path, "is dir?", path.is_dir(), "is file", path.is_file())

    print()
    # for path in BASE_DIR.glob("*"):
    #     print(path)
    # print()

    cats_dir = Path.cwd() / "pics" / "cats"
    print(cats_dir)
    print("dir?", cats_dir.is_dir())
    print("exists?", cats_dir.exists())
    cats_dir.mkdir(parents=True, exist_ok=True)
    print("dir?", cats_dir.is_dir())
    print("exists?", cats_dir.exists())


def demo_files():
    filepath = BASE_DIR / "file.txt"
    # filepath.exists()
    filepath.write_text("Hello World!\n")
    print(repr(filepath.read_text()))


def demo_path_str():
    home = PathString(Path.home())
    print(home)
    print(repr(home))

    pics_folder = home / "pics"
    print(pics_folder)
    print(repr(pics_folder))

    cat_pic = pics_folder / "cat.jpg"
    print(cat_pic)
    print(repr(cat_pic))


def main():
    # demo_paths_one()
    demo_paths_two()
    # demo_files()
    # demo_path_str()


if __name__ == "__main__":
    main()
