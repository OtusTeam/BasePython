from pathlib import Path


cur_dir  = Path.cwd()
print(cur_dir)

for item in cur_dir.iterdir():
    print(item.name)
