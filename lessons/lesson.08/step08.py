text = [
    "Hello World!!!\n",
    "1. Python lang\n",
    "2. Bob 23 age\n",
    "3. James 23 age\n",
]
my_file =  open("data/file.txt", "a", encoding="utf-8")

my_file.writelines(text)

my_file.close()
