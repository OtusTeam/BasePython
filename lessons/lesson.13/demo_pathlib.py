from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)


def demo_paths():
    # venv_path = Path(".venv").resolve()
    venv_path = BASE_DIR / ".venv"
    print(venv_path)
    print("is file?", venv_path.is_file())
    print("is directory?", venv_path.is_dir())

    print(Path.home())
    print(Path.cwd())
    # home_path = Path.home()
    # cache_dir = home_path / ".cache" / "myapp.json"
    # cache_dir = home_path / ".cache" / "myapp.json"

    # for path in BASE_DIR.glob("**/*.py"):
    for path in BASE_DIR.iterdir():
        print(path, "is dir?", path.is_dir(), "is file?", path.is_file())


def demo_paths_two():
    # cats_dir = Path.cwd()
    cats_dir = BASE_DIR / "pics" / "cats"
    print(cats_dir)
    print("is directory?", cats_dir.is_dir())
    cats_dir.mkdir(parents=True, exist_ok=True)
    cats_dir_readme = cats_dir / "README.txt"
    cats_dir_readme.write_text("Cats pics directory\n")

    print()
    print(cats_dir_readme.read_text())
    with cats_dir_readme.open("r") as f:
        for line in f:
            print(repr(line))


def main():
    # demo_paths()
    demo_paths_two()


if __name__ == "__main__":
    main()
