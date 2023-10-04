# import os.path
from pathlib import Path

BASE_DIR = Path(__file__).parent


# print(BASE_DIR)
# print(repr(BASE_DIR))


def demo_cwd():
    cwd = Path.cwd()
    print(cwd)

    print(Path.home())


def demo_dirs():
    users_path = Path("/User")
    print(users_path)
    print(users_path.is_dir())
    print(users_path.is_file())
    print(users_path.exists())

    print()
    users_path = Path("/Users")
    print(users_path.is_dir())
    print(users_path.is_file())
    print(users_path.exists())

    for path in users_path.iterdir():
        print(path, "dir?", path.is_dir(), "file?", path.is_file())

    pics_folder_name = "pics"
    cats_pics_dir = BASE_DIR / pics_folder_name / "cats"
    DB_NAME = "db.sqlite3"
    DB_PATH = BASE_DIR / DB_NAME
    # database_path = f"sqlite://{BASE_DIR}/{DB_NAME}"
    # database_path = f"sqlite://{BASE_DIR}{os.path.sep}{DB_NAME}"
    database_path = f"sqlite://{DB_PATH}"
    print(database_path)
    print(cats_pics_dir)
    print(cats_pics_dir.is_dir())
    print(cats_pics_dir.exists())
    cats_pics_dir.mkdir(parents=True, exist_ok=True)
    print(cats_pics_dir.is_dir())
    print(cats_pics_dir.exists())


def demo_files():
    filepath = BASE_DIR / "file.txt"
    # filepath.exists()
    filepath.write_text("hello world\n")
    # print(filepath.read_text())
    print(repr(filepath.read_text()))


if __name__ == "__main__":
    # demo_cwd()
    # demo_dirs()
    demo_files()
