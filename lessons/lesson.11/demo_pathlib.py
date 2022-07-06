from pathlib import Path

# import pathlib

# pathlib.Path
# pathlib.PosixPath
# pathlib.WindowsPath


BASE_DIR = Path(__file__).parent
# print(BASE_DIR)


def demo_cwd():
    cwd = Path.cwd()
    print(cwd)
    print(repr(cwd))

    print(cwd.iterdir())

    for path in cwd.iterdir():
        print(path.name, path.is_dir(), path.is_file())


def demo_home():
    home = Path.home()
    print("home:", home)


def demo_files():
    users = Path("/Users")
    print(users)
    print("users exists?", users.exists())

    cats = Path("/Cats")
    print(cats)
    print("cats exists?", cats.exists())
    # for files..
    cats.unlink(missing_ok=True)


def demo_file_paths():
    current_path = Path(__file__)
    base_dir = current_path.parent
    print("base_dir", base_dir)

    print("base_dir.parent", base_dir.parent)

    print("file parents:", list(current_path.parents))


def demo_build_path():
    current_path = Path(__file__)
    base_dir = current_path.parent

    folder_name = "pictures"
    filename = "cats.jpg"

    # 1 + 2
    # "a" + "b"
    # "a" * 2
    # 2 * "a"
    # 1 / 2
    # print(object() / 2)
    cats_filepath = base_dir / folder_name / filename
    h = "hello" / Path(filename)
    print(h)
    # 1 / Path(filename)
    print(10 / 4)
    cats_path = base_dir.joinpath(folder_name, filename)
    print(cats_filepath)
    print("cats_filepath exists?", cats_filepath.exists())
    print("eq?", cats_path == cats_filepath)

    print(Path("cat.js.jpg").suffixes)
    print(Path("cat.empty").suffixes)
    print("cats_path.name", cats_path.name)
    print("cats_path.suffix", cats_path.suffix)
    print("cats_path.stem", cats_path.stem)
    print("cats_path.anchor", cats_path.anchor)


def demo_file_create():
    filename = "file.txt"

    file = Path(filename).resolve()
    # print(file)
    # print(repr(file))
    # print(file.resolve())

    # remove file
    file.unlink(missing_ok=True)

    file.write_text("hello\n")

    print(file.read_text())


def main():
    demo_cwd()
    demo_home()
    demo_files()
    demo_file_paths()
    demo_build_path()
    demo_file_create()


if __name__ == '__main__':
    main()

