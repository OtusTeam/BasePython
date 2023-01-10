import pathlib

ROOT = pathlib.Path(__file__).parent
DATA_ROOT = ROOT / 'users' / 'files'
# print(type(ROOT))
# print(dir(ROOT))
print(ROOT)
print(DATA_ROOT)
# print(ROOT)
# print(DATA_ROOT)

# for el in DATA_ROOT.iterdir():
#     print(el)
f_1 = DATA_ROOT / 'gamers.txt'
# f_1.write_text('Bon Jovi\nElton John')
f_content = f_1.read_text()
print(f_content)
# print(pathlib.Path.home())
