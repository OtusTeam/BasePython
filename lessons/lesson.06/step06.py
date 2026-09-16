def greet(name="Гость", lang="Python"):
    print("Как тебя зовут?")
    # name = input("Введите имя: ")
    print("Привет", name, "Ты изучаешь", lang)
    # return None
    return


res = greet("Bob" )
print(res)

greet()

print()

my_lang = "Java"
greet(my_lang )