my_file =  open("data/otus.txt", "r", encoding="utf-8")
data = my_file.readline()
data1 = my_file.readline()
data2 = my_file.readline()

my_file.close()
print(data)
print(data1)
print(data2)
