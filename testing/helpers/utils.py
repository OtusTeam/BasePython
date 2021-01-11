import sys
from pathlib import Path


def add_homework_path(file):
    current_file = Path(file).resolve()
    folder_test_homework_0X = current_file.parent
    homework_0X = folder_test_homework_0X.name.replace("test_", "")
    homework_0X_path = folder_test_homework_0X.parent.parent / homework_0X

    sys.path.insert(0, str(homework_0X_path))
    print("Added homework package to path:", homework_0X_path)
