my_file =  open("data/otus.txt", "r", encoding="utf-8")
data = my_file.readlines()

my_file.close()
print(data)

