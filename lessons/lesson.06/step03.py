def greet(lang, name):
    print("Как тебя зовут?")
    # name = input("Введите имя: ")
    print("Привет", name, "Ты изучаешь", lang)


greet("Python", "Bob")

print()

greet("С++", "Ivan")

print()

my_lang = "Java"
greet(my_lang, "Anna")