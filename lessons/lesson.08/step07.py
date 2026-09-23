text = [
    "Hello World!!!\n",
    "1111. Python lang\n",
    "2222. Bob 23 age\n",
    "3333. James 23 age\n",
]
my_file =  open("data/file.txt", "w", encoding="utf-8")

my_file.writelines(text)

my_file.close()
