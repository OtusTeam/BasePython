my_file =  open("data/otus.txt", "rt", encoding="utf-8")
data = my_file.read()
my_file.close()
print(data)
