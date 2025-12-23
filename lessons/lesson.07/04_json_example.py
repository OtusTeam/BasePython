import json
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

json_file = CURRENT_DIR / "example.json"

print(json_file.read_text())

with json_file.open() as f:
    data = json.load(f)

print("data:", data)

data["address"]["extra"] = "Some address comment"

with json_file.open("w") as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=2,
        # sort_keys=True,
    )
