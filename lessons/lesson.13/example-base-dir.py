from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

PYPROJECT =  BASE_DIR / "pyproject.toml"
print(PYPROJECT)
